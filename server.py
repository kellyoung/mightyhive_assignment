import os
from flask import Flask, render_template, redirect, request, session
import jinja2
from model import User, connect_to_db, db
import datetime

app = Flask(__name__)

secret_key = "5fkc1066myd11263gbpj066luz61064tuk"
app.config['SECRET_KEY'] = os.environ.get("FLASK_SECRET_KEY", secret_key)


@app.route("/", methods=["POST", "GET"])
def index():
    """Show homepage."""

    # get the info passed back in the AJAX request
    new_color = request.form.get('color')
    new_count = request.form.get('count')
    timestamp = datetime.datetime.now()

    if session.get('user') is None:
        # if there is not a user in session:
        print "no session"
        if new_count and new_color:

            # if there is a value for new_count and new_color create a new entry in db
            new_user = User(count=int(new_count), color=new_color, first_visit=timestamp)
            db.session.add(new_user)
            db.session.commit()

            # add this user's unique_id to the database
            session['user'] = new_user.unique_id
    else:
        print "session"
        # if there is a user in a session, get the user
        session_user = session.get('user')
        current_user = User.query.get(int(session_user))

        # update the count
        if new_count:
            current_user.count = int(new_count)
            db.session.commit()

    return render_template("index.html")


@app.route("/stats")
def show_stats():
    """Should show stats for all users"""

    # get all users in the database
    users = User.query.all()

    return render_template("stats.html", users=users)


if __name__ == "__main__":   
    connect_to_db(app, os.environ.get("DATABASE_URL"))
    DEBUG = "NO_DEBUG" not in os.environ
    PORT = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=PORT, debug=DEBUG)
