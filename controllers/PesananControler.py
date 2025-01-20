from flask import jsonify, request
from models.PesananModel import Pesanan
from config import db
from flask_jwt_extended import jwt_required

@jwt_required()
def get_pesanan():
    pesanans = Pesanan.query.all()
    pesanan_data = []
    for pesanan in pesanans:
        pesanan_data.append({
            'id': pesanan.id,
            'buyer_id': pesanan.buyer_id,
            'order_date': pesanan.order_date,
            'status': pesanan.status,
            'total_price': pesanan.total_price
        })

    response = {
        'status': 'success',
        'data': {
            'pesanans': pesanan_data
        },
        'message': 'Pesanan retrieved successfully!'
    }
    return jsonify(response), 200

@jwt_required()
def get_pesanan_by_id(pesanan_id):
    pesanan = Pesanan.query.get(pesanan_id)
    if not pesanan:
        return jsonify({'error': 'Pesanan not found'}), 404

    pesanan_data = {
        'id': pesanan.id,
        'buyer_id': pesanan.buyer_id,
        'order_date': pesanan.order_date,
        'status': pesanan.status,
        'total_price': pesanan.total_price
    }

    response = {
        'status': 'success',
        'data': {
            'pesanan': pesanan_data
        },
        'message': 'Pesanan retrieved successfully!'
    }
    return jsonify(response), 200

@jwt_required()
def add_pesanan():
    new_pesanan_data = request.get_json()
    new_pesanan = Pesanan(
        buyer_id=new_pesanan_data['buyer_id'],
        order_date=new_pesanan_data['order_date'],
        status=new_pesanan_data['status'],
        total_price=new_pesanan_data['total_price']
    )
    db.session.add(new_pesanan)
    db.session.commit()
    return jsonify({'message': 'Pesanan added successfully!', 'pesanan': {
        'id': new_pesanan.id,
        'buyer_id': new_pesanan.buyer_id,
        'order_date': new_pesanan.order_date,
        'status': new_pesanan.status,
        'total_price': new_pesanan.total_price
    }}), 201

@jwt_required()
def update_pesanan(pesanan_id):
    pesanan = Pesanan.query.get(pesanan_id)
    if not pesanan:
        return jsonify({'error': 'Pesanan not found'}), 404

    update_data = request.get_json()
    pesanan.buyer_id = update_data.get('buyer_id', pesanan.buyer_id)
    pesanan.order_date = update_data.get('order_date', pesanan.order_date)
    pesanan.status = update_data.get('status', pesanan.status)
    pesanan.total_price = update_data.get('total_price', pesanan.total_price)

    db.session.commit()
    return jsonify({'message': 'Pesanan updated successfully!', 'pesanan': {
        'id': pesanan.id,
        'buyer_id': pesanan.buyer_id,
        'order_date': pesanan.order_date,
        'status': pesanan.status,
        'total_price': pesanan.total_price
    }}), 200

@jwt_required()
def delete_pesanan(pesanan_id):
    pesanan = Pesanan.query.get(pesanan_id)
    if not pesanan:
        return jsonify({'error': 'Pesanan not found'}), 404

    db.session.delete(pesanan)
    db.session.commit()
    return jsonify({'message': 'Pesanan deleted successfully!'}), 200
