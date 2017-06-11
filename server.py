from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined


app = Flask(__name__)
app.jinja_env.undefined = StrictUndefined
app.jinja_env.auto_reload = True

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# YOUR ROUTES GO HERE

@app.route("/")
def index():
    """Render index html """
    return render_template("/index.html")

@app.route("/application-form")
def application():
    """ Render application form"""

    jobs = {
            "se": "Software Engineer",
            "qa" : "QA Engineer",
            "pm": "Product Manager"
            }

    return render_template("/application-form.html", jobs=jobs)

@app.route("/application-success", methods=["POST"])
def success():
    """Render application success form"""

    response = request.form

    import locale
    locale.setlocale(locale.LC_ALL, '')
    salary = locale.currency(float(response.get("salary")), grouping=True)

    return render_template("application-response.html",
                           firstname = response.get("firstname").capitalize(),
                           lastname = response.get("lastname").capitalize(),
                           salary = salary,
                           job = response.get("job")
                           )

if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
