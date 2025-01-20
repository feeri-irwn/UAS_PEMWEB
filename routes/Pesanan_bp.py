from flask import Blueprint
from controllers.PesananControler import (
    get_pesanan,
    get_pesanan_by_id,
    add_pesanan,
    update_pesanan,
    delete_pesanan
)

# Membuat blueprint untuk pesanan
pesanan_bp = Blueprint('pesanan', __name__, url_prefix='/api')

# Mendefinisikan rute-rute yang berkaitan dengan pesanan
pesanan_bp.route('/pesanan', methods=['GET'])(get_pesanan)
pesanan_bp.route('/pesanan/<int:pesanan_id>', methods=['GET'])(get_pesanan_by_id)
pesanan_bp.route('/pesanan', methods=['POST'])(add_pesanan)
pesanan_bp.route('/pesanan/<int:pesanan_id>', methods=['PUT'])(update_pesanan)
pesanan_bp.route('/pesanan/<int:pesanan_id>', methods=['DELETE'])(delete_pesanan)
