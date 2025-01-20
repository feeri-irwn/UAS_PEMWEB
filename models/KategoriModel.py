from config import db

class Kategori(db.Model):
    __tablename__ = 'kategori'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    descrip = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'descrip': self.descrip,
            'created_at': self.created_at
        }
