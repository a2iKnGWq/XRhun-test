from flask import Flask, flash, jsonify, redirect, render_template, request


# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response



@app.route("/", methods=["GET"])        #["GET", "POST"]
def index():
    """Show portfolio"""
    return render_template("home.html")

@app.route("/void", methods=["GET"])
def voidfunc():
    """Show portfolio"""
    return render_template("void.html")

@app.route("/cards", methods=["GET"])
def cards():
    """Show portfolio"""
    return render_template("cards.html")

@app.route("/FAQ", methods=["GET"])
def FAQ():
    """Show portfolio"""
    return render_template("FAQ.html")
