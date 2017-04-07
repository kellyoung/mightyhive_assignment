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


def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our PstgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///users'
    db.app = app
    db.init_app(app)


if __name__ == "__main__":

    from server import app
    connect_to_db(app)
    print "Connected to DB."