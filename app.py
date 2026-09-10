from flask import Flask, render_template, request
from connection import get_connection

app = Flask(__name__)

TABLE_CASEPAPER = "ka2627casepaper"
TABLE_FOLLOWUP = "ka2627followup"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/search")
def search_patient():

    name = request.args.get("name", "").strip()

    if not name:
        return render_template(
            "index.html",
            error="Please enter patient name"
        )

    conn = None

    try:
        conn = get_connection()

        with conn.cursor() as cursor:

            # ------------------------------------------------
            # Latest case paper
            # ------------------------------------------------
            sql = f"""
                SELECT *
                FROM `{TABLE_CASEPAPER}`
                WHERE case_paper_no LIKE %s
                ORDER BY id DESC
                LIMIT 1
            """

            cursor.execute(sql, (f"%{name}%",))
            patient = cursor.fetchone()

            if not patient:
                return render_template(
                    "index.html",
                    error="Patient not found"
                )

            # ------------------------------------------------
            # Follow-up records
            # ------------------------------------------------
            sql = f"""
                SELECT *
                FROM `{TABLE_FOLLOWUP}`
                WHERE name = %s
                ORDER BY id DESC
            """

            cursor.execute(
                sql,
                (patient.get("name"),)
            )

            followups = cursor.fetchall()

        return render_template(
            "patient.html",
            patient=patient,
            followups=followups
        )

    except Exception as e:

        return render_template(
            "index.html",
            error=f"Database error: {e}"
        )

    finally:

        if conn:
            conn.close()


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )