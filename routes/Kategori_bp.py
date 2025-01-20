from flask import Blueprint
from controllers.KategoriControler import (
    get_kategori,
    get_kategori_by_id,
    add_kategori,
    update_kategori,
    delete_kategori
)

# Membuat blueprint untuk kategori
kategori_bp = Blueprint('kategori', __name__, url_prefix='/api')

# Mendefinisikan rute-rute yang berkaitan dengan kategori
kategori_bp.route('/kategori', methods=['GET'])(get_kategori)
kategori_bp.route('/kategori/<int:kategori_id>', methods=['GET'])(get_kategori_by_id)
kategori_bp.route('/kategori', methods=['POST'])(add_kategori)
kategori_bp.route('/kategori/<int:kategori_id>', methods=['PUT'])(update_kategori)
kategori_bp.route('/kategori/<int:kategori_id>', methods=['DELETE'])(delete_kategori)
