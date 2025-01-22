from config import db
from models.Detail_PesananModel import DetailPesanan  # Pastikan ini diimpor

class Pesanan(db.Model):
    __tablename__ = 'pesanan'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    kategori_id = db.Column(db.Integer, db.ForeignKey('kategori.id'), nullable=False)
    total_harga = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

    # Relasi ke User, ganti 'user' dengan 'pesanans' untuk menghindari konflik
    user = db.relationship('User', backref='pesanans')  # Ganti 'user' dengan 'pesanans' di backref
    kategori = db.relationship('Kategori', backref='pesanans')

    # Relasi dengan DetailPesanan
    details = db.relationship('DetailPesanan', backref='pesanan', lazy=True, cascade="all, delete-orphan")  # Menambahkan 'details'

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'kategori_id': self.kategori_id,
            'total_harga': self.total_harga,
            'created_at': self.created_at
        }
