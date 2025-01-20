from config import db

class DetailPesanan(db.Model):
    __tablename__ = 'detail_pesanan'

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('pesanan.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('produk.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    subtotal = db.Column(db.Float, nullable=False)

    # Relasi
    order = db.relationship('Pesanan', back_populates='details')
    product = db.relationship('Produk', back_populates='order_details')

    def to_dict(self):
        return {
            'id': self.id,
            'order_id': self.order_id,
            'product_id': self.product_id,
            'quantity': self.quantity,
            'subtotal': self.subtotal
        }
