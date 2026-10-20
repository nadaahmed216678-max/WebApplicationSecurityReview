
from flask import Flask, render_template, request
from markupsafe import escape

app = Flask(__name__)

@app.after_request
def add_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["Content-Security-Policy"] = "default-src 'self'"
    return response

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username", "").strip()

    if not username:
        return "Error: Username is required.", 400

    if len(username) > 50:
        return "Error: Username is too long.", 400

    return f"<p>Login form received for: {escape(username)}</p>"

if __name__ == "__main__":
    app.run(debug=False)


