from flask import Blueprint
from controllers.Detail_PesananControler import (
    get_detail_pesanan,
    get_detail_pesanan_by_id,
    add_detail_pesanan,
    update_detail_pesanan,
    delete_detail_pesanan
)

# Membuat blueprint untuk detail pesanan
detailpesanan_bp = Blueprint('detailpesanan', __name__, url_prefix='/api')

# Mendefinisikan rute-rute yang berkaitan dengan detail pesanan
detailpesanan_bp.route('/detail-pesanan', methods=['GET'])(get_detail_pesanan)
detailpesanan_bp.route('/detail-pesanan/<int:detail_id>', methods=['GET'])(get_detail_pesanan_by_id)
detailpesanan_bp.route('/detail-pesanan', methods=['POST'])(add_detail_pesanan)
detailpesanan_bp.route('/detail-pesanan/<int:detail_id>', methods=['PUT'])(update_detail_pesanan)
detailpesanan_bp.route('/detail-pesanan/<int:detail_id>', methods=['DELETE'])(delete_detail_pesanan)
