import os
import logging
from flask import Flask, render_template


app = Flask(__name__)
app.secret_key = "no body no crime"
log = logging.getLogger()


@app.route("/")
def view_dashboard():
    """renders dashboard"""
    return render_template("homepage.html")


@app.route("/about", methods=["GET"])
def view_about():
    """View about me page."""
    return render_template("about.html")


@app.route("/homepage", methods=["GET"])
def view_homepage():
    """Homepage"""
    return render_template("homepage.html")

@app.route("/work", methods=["GET"])
def view_work():
    """View work page."""
    return render_template("work.html")

@app.route("/projects", methods=["GET"])
def view_projects():
    """View projects page."""
    return render_template("projects.html")

@app.route("/<project_id>", methods=["GET"])
def view_project(project_id):
    """View project page based on project ID."""
    try:
        return render_template(f"{project_id}.html")
    except TemplateNotFound:
        return "Project page not found", 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)

