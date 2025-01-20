from flask import Blueprint
from controllers.UserControler import (
    login,
    get_users,
    get_user,
    update_user,
    patch_user,
    delete_user,
    add_user
)

# Membuat blueprint untuk user
user_bp = Blueprint('user', __name__, url_prefix='/api')

# Login
user_bp.route('/login', methods=['POST'])(login)

# Mendapatkan semua user
user_bp.route('/users', methods=['GET'])(get_users)

# Mendapatkan user berdasarkan ID
user_bp.route('/users/<int:user_id>', methods=['GET'])(get_user)

# Menambahkan user baru
user_bp.route('/users', methods=['POST'])(add_user)

# Memperbarui user berdasarkan ID
user_bp.route('/users/<int:user_id>', methods=['PUT'])(update_user)

# Memperbarui sebagian user (patch) berdasarkan ID
user_bp.route('/users/<int:user_id>', methods=['PATCH'])(patch_user)

# Menghapus user berdasarkan ID
user_bp.route('/users/<int:user_id>', methods=['DELETE'])(delete_user)
