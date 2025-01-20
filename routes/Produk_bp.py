from flask import Blueprint
from controllers.ProdukControler import (
    get_produk,
    get_produk_by_id,
    add_produk,
    update_produk,
    delete_produk
)

# Membuat blueprint untuk produk
produk_bp = Blueprint('produk', __name__, url_prefix='/api')

# Mendefinisikan rute-rute yang berkaitan dengan produk
produk_bp.route('/produk', methods=['GET'])(get_produk)
produk_bp.route('/produk/<int:produk_id>', methods=['GET'])(get_produk_by_id)
produk_bp.route('/produk', methods=['POST'])(add_produk)
produk_bp.route('/produk/<int:produk_id>', methods=['PUT'])(update_produk)
produk_bp.route('/produk/<int:produk_id>', methods=['DELETE'])(delete_produk)
