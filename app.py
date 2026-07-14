"""
Project 1 (Web Server Edition): Password Strength Checker
DecodeLabs Cyber Security Industrial Training Kit - Batch 2026

A simple Flask web server that lets users check password strength
through a browser instead of the terminal.

Run with: python app.py
Then open: http://127.0.0.1:5000 in your browser
"""

from flask import Flask, render_template, request

app = Flask(__name__)

# A tiny sample list of common/leaked passwords (stretch goal)
COMMON_PASSWORDS = {
    "password", "password123", "123456", "12345678",
    "qwerty", "abc123", "letmein", "admin", "welcome"
}


def check_password_strength(password: str):
    """Return (strength_label, css_class) for the given password."""

    if not password:
        return None, None

    # Common/leaked password check
    if password.lower() in COMMON_PASSWORDS:
        return "Weak — this password appears on a common/leaked password list", "weak"

    # Length check (immediate fail)
    if len(password) < 8:
        return "Weak — must be at least 8 characters", "weak"

    # Character variety checks
    has_digit = any(char.isdigit() for char in password)
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_symbol = any(not char.isalnum() for char in password)

    score = sum([has_digit, has_upper, has_lower, has_symbol])

    if score == 4:
        return "Strong", "strong"
    elif score >= 2:
        return "Medium", "medium"
    else:
        return "Weak", "weak"


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    css_class = None
    password = ""

    if request.method == "POST":
        password = request.form.get("password", "")
        result, css_class = check_password_strength(password)

    return render_template("index.html", result=result, css_class=css_class, password=password)


if __name__ == "__main__":
    app.run(debug=True)
