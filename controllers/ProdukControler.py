from flask import jsonify, request
from models.ProdukModel import Produk
from config import db
from flask_jwt_extended import jwt_required

@jwt_required()
def get_produk():
    produks = Produk.query.all()
    produk_data = []
    for produk in produks:
        produk_data.append({
            'id': produk.id,
            'seller_id': produk.seller_id,
            'name': produk.name,
            'descrip': produk.descrip,
            'price': produk.price,
            'stock': produk.stock,
            'created_at': produk.created_at
        })

    response = {
        'status': 'success',
        'data': {
            'produks': produk_data
        },
        'message': 'Produk retrieved successfully!'
    }
    return jsonify(response), 200

@jwt_required()
def get_produk_by_id(produk_id):
    produk = Produk.query.get(produk_id)
    if not produk:
        return jsonify({'error': 'Produk not found'}), 404

    produk_data = {
        'id': produk.id,
        'seller_id': produk.seller_id,
        'name': produk.name,
        'descrip': produk.descrip,
        'price': produk.price,
        'stock': produk.stock,
        'created_at': produk.created_at
    }

    response = {
        'status': 'success',
        'data': {
            'produk': produk_data
        },
        'message': 'Produk retrieved successfully!'
    }
    return jsonify(response), 200

@jwt_required()
def add_produk():
    new_produk_data = request.get_json()
    new_produk = Produk(
        seller_id=new_produk_data['seller_id'],
        name=new_produk_data['name'],
        descrip=new_produk_data['descrip'],
        price=new_produk_data['price'],
        stock=new_produk_data['stock'],
        created_at=new_produk_data.get('created_at')
    )
    db.session.add(new_produk)
    db.session.commit()
    return jsonify({'message': 'Produk added successfully!', 'produk': {
        'id': new_produk.id,
        'seller_id': new_produk.seller_id,
        'name': new_produk.name,
        'descrip': new_produk.descrip,
        'price': new_produk.price,
        'stock': new_produk.stock,
        'created_at': new_produk.created_at
    }}), 201

@jwt_required()
def update_produk(produk_id):
    produk = Produk.query.get(produk_id)
    if not produk:
        return jsonify({'error': 'Produk not found'}), 404

    update_data = request.get_json()
    produk.seller_id = update_data.get('seller_id', produk.seller_id)
    produk.name = update_data.get('name', produk.name)
    produk.descrip = update_data.get('descrip', produk.descrip)
    produk.price = update_data.get('price', produk.price)
    produk.stock = update_data.get('stock', produk.stock)
    produk.created_at = update_data.get('created_at', produk.created_at)

    db.session.commit()
    return jsonify({'message': 'Produk updated successfully!', 'produk': {
        'id': produk.id,
        'seller_id': produk.seller_id,
        'name': produk.name,
        'descrip': produk.descrip,
        'price': produk.price,
        'stock': produk.stock,
        'created_at': produk.created_at
    }}), 200

@jwt_required()
def delete_produk(produk_id):
    produk = Produk.query.get(produk_id)
    if not produk:
        return jsonify({'error': 'Produk not found'}), 404

    db.session.delete(produk)
    db.session.commit()
    return jsonify({'message': 'Produk deleted successfully!'}), 200
