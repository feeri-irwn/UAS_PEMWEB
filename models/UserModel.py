from config import db

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    fullname = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'fullname': self.fullname,
            'status': self.status,
            'role': self.role,
            'created_at': self.created_at
        }
