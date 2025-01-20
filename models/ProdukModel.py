from config import db

class Produk(db.Model):
    __tablename__ = 'produk'

    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100), nullable=False)
    deskripsi = db.Column(db.Text, nullable=True)
    harga = db.Column(db.Float, nullable=False)
    stok = db.Column(db.Integer, nullable=False)
    kategori_id = db.Column(db.Integer, db.ForeignKey('kategori.id'), nullable=False)  # Foreign key ke kategori
    created_at = db.Column(db.DateTime, nullable=False)

    # Relasi dengan Kategori
    kategori = db.relationship('Kategori', backref='produks', lazy=True)

    # Relasi dengan DetailPesanan
    order_details = db.relationship('DetailPesanan', back_populates='product', lazy=True)  # Menambahkan relasi ke DetailPesanan

    def to_dict(self):
        return {
            'id': self.id,
            'nama': self.nama,
            'deskripsi': self.deskripsi,
            'harga': self.harga,
            'stok': self.stok,
            'kategori_id': self.kategori_id,
            'created_at': self.created_at
        }
