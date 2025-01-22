from flask import jsonify, request
from models.PesananModel import Pesanan
from config import db
from flask_jwt_extended import jwt_required

# Get all pesanan
@jwt_required()
def get_pesanan():
    pesanans = Pesanan.query.all()
    pesanan_data = []
    
    for pesanan in pesanans:
        pesanan_data.append({
            'id': pesanan.id,
            'user_id': pesanan.user_id,  # Ganti 'buyer_id' menjadi 'user_id'
            'kategori_id': pesanan.kategori_id,  # Ganti 'order_date' menjadi 'kategori_id'
            'total_harga': pesanan.total_harga,
            'created_at': pesanan.created_at.isoformat()  # Ubah format tanggal menjadi ISO string
        })

    response = {
        'status': 'success',
        'data': {
            'pesanans': pesanan_data
        },
        'message': 'Pesanan retrieved successfully!'
    }
    return jsonify(response), 200

# Get pesanan by ID
@jwt_required()
def get_pesanan_by_id(pesanan_id):
    pesanan = Pesanan.query.get(pesanan_id)
    if not pesanan:
        return jsonify({'error': 'Pesanan not found'}), 404

    pesanan_data = {
        'id': pesanan.id,
        'user_id': pesanan.user_id,
        'kategori_id': pesanan.kategori_id,
        'total_harga': pesanan.total_harga,
        'created_at': pesanan.created_at.isoformat()  # Ubah format tanggal menjadi ISO string
    }

    response = {
        'status': 'success',
        'data': {
            'pesanan': pesanan_data
        },
        'message': 'Pesanan retrieved successfully!'
    }
    return jsonify(response), 200

# Add new pesanan
@jwt_required()
def add_pesanan():
    new_pesanan_data = request.get_json()
    new_pesanan = Pesanan(
        user_id=new_pesanan_data['user_id'],  # Ganti 'buyer_id' menjadi 'user_id'
        kategori_id=new_pesanan_data['kategori_id'],  # Ganti 'order_date' menjadi 'kategori_id'
        total_harga=new_pesanan_data['total_harga'],
        created_at=new_pesanan_data['created_at']  # Pastikan 'created_at' disertakan
    )
    db.session.add(new_pesanan)
    db.session.commit()

    return jsonify({
        'message': 'Pesanan added successfully!',
        'pesanan': {
            'id': new_pesanan.id,
            'user_id': new_pesanan.user_id,
            'kategori_id': new_pesanan.kategori_id,
            'total_harga': new_pesanan.total_harga,
            'created_at': new_pesanan.created_at.isoformat()  # Format tanggal ISO
        }
    }), 201

# Update pesanan by ID
@jwt_required()
def update_pesanan(pesanan_id):
    pesanan = Pesanan.query.get(pesanan_id)
    if not pesanan:
        return jsonify({'error': 'Pesanan not found'}), 404

    update_data = request.get_json()
    pesanan.user_id = update_data.get('user_id', pesanan.user_id)  # Ganti 'buyer_id' menjadi 'user_id'
    pesanan.kategori_id = update_data.get('kategori_id', pesanan.kategori_id)  # Ganti 'order_date' menjadi 'kategori_id'
    pesanan.total_harga = update_data.get('total_harga', pesanan.total_harga)
    pesanan.created_at = update_data.get('created_at', pesanan.created_at)  # Pastikan 'created_at' disertakan

    db.session.commit()
    return jsonify({
        'message': 'Pesanan updated successfully!',
        'pesanan': {
            'id': pesanan.id,
            'user_id': pesanan.user_id,
            'kategori_id': pesanan.kategori_id,
            'total_harga': pesanan.total_harga,
            'created_at': pesanan.created_at.isoformat()  # Format tanggal ISO
        }
    }), 200

# Delete pesanan by ID
@jwt_required()
def delete_pesanan(pesanan_id):
    pesanan = Pesanan.query.get(pesanan_id)
    if not pesanan:
        return jsonify({'error': 'Pesanan not found'}), 404

    db.session.delete(pesanan)
    db.session.commit()
    return jsonify({'message': 'Pesanan deleted successfully!'}), 200
