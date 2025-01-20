from flask import jsonify, request
from models.Detail_PesananModel import DetailPesanan
from config import db
from flask_jwt_extended import jwt_required

@jwt_required()
def get_detail_pesanan():
    details = DetailPesanan.query.all()
    detail_data = []
    for detail in details:
        detail_data.append({
            'id': detail.id,
            'order_id': detail.order_id,
            'product_id': detail.product_id,
            'quantity': detail.quantity,
            'subtotal': detail.subtotal
        })

    response = {
        'status': 'success',
        'data': {
            'details': detail_data
        },
        'message': 'Detail pesanan retrieved successfully!'
    }
    return jsonify(response), 200

@jwt_required()
def get_detail_pesanan_by_id(detail_id):
    detail = DetailPesanan.query.get(detail_id)
    if not detail:
        return jsonify({'error': 'Detail pesanan not found'}), 404

    detail_data = {
        'id': detail.id,
        'order_id': detail.order_id,
        'product_id': detail.product_id,
        'quantity': detail.quantity,
        'subtotal': detail.subtotal
    }

    response = {
        'status': 'success',
        'data': {
            'detail': detail_data
        },
        'message': 'Detail pesanan retrieved successfully!'
    }
    return jsonify(response), 200

@jwt_required()
def add_detail_pesanan():
    new_detail_data = request.get_json()
    new_detail = DetailPesanan(
        order_id=new_detail_data['order_id'],
        product_id=new_detail_data['product_id'],
        quantity=new_detail_data['quantity'],
        subtotal=new_detail_data['subtotal']
    )
    db.session.add(new_detail)
    db.session.commit()
    return jsonify({'message': 'Detail pesanan added successfully!', 'detail': {
        'id': new_detail.id,
        'order_id': new_detail.order_id,
        'product_id': new_detail.product_id,
        'quantity': new_detail.quantity,
        'subtotal': new_detail.subtotal
    }}), 201

@jwt_required()
def update_detail_pesanan(detail_id):
    detail = DetailPesanan.query.get(detail_id)
    if not detail:
        return jsonify({'error': 'Detail pesanan not found'}), 404

    update_data = request.get_json()
    detail.order_id = update_data.get('order_id', detail.order_id)
    detail.product_id = update_data.get('product_id', detail.product_id)
    detail.quantity = update_data.get('quantity', detail.quantity)
    detail.subtotal = update_data.get('subtotal', detail.subtotal)

    db.session.commit()
    return jsonify({'message': 'Detail pesanan updated successfully!', 'detail': {
        'id': detail.id,
        'order_id': detail.order_id,
        'product_id': detail.product_id,
        'quantity': detail.quantity,
        'subtotal': detail.subtotal
    }}), 200

@jwt_required()
def delete_detail_pesanan(detail_id):
    detail = DetailPesanan.query.get(detail_id)
    if not detail:
        return jsonify({'error': 'Detail pesanan not found'}), 404

    db.session.delete(detail)
    db.session.commit()
    return jsonify({'message': 'Detail pesanan deleted successfully!'}), 200
