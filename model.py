from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """User of ratings website."""

    __tablename__ = "users"

    unique_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    color = db.Column(db.String(36), nullable=False)
    count = db.Column(db.Integer, nullable=False)
    first_visit = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<User unique_id=%s color=%s count=%s>" % (self.unique_id,
                                                          self.color,
                                                          self.count)


def connect_to_db(app, db_uri=None):
    """Connect the database to our Flask app."""

    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri or 'postgres:///users'
    db.app = app
    db.init_app(app)
    print "Connected to DB."


if __name__ == "__main__":

    from server import app
    connect_to_db(app)
    