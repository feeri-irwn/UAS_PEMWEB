from flask import jsonify, request
from datetime import datetime
import pytz  # Import pytz untuk zona waktu
from models.ProdukModel import Produk
from config import db
from flask_jwt_extended import jwt_required

# Zona waktu Jakarta (WIB)
jakarta_tz = pytz.timezone('Asia/Jakarta')

# Fungsi untuk mendapatkan waktu saat ini di zona waktu Jakarta (WIB)
def get_current_time_in_wib():
    return datetime.now(jakarta_tz)

@jwt_required()
def get_produk():
    produks = Produk.query.all()
    produk_data = [produk.to_dict() for produk in produks]  # Menggunakan metode to_dict() yang sudah ada di model

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

    response = {
        'status': 'success',
        'data': {
            'produk': produk.to_dict()  # Menggunakan metode to_dict() untuk mengonversi objek produk ke dictionary
        },
        'message': 'Produk retrieved successfully!'
    }
    return jsonify(response), 200

@jwt_required()
def add_produk():
    new_produk_data = request.get_json()
    created_at = new_produk_data.get('created_at', get_current_time_in_wib())  # Menggunakan waktu Indonesia (WIB)
    new_produk = Produk(
        nama=new_produk_data['nama'],
        deskripsi=new_produk_data['deskripsi'],
        harga=new_produk_data['harga'],
        stok=new_produk_data['stok'],
        kategori_id=new_produk_data['kategori_id'],  # Menggunakan kategori_id dari request
        created_at=created_at  # Mendapatkan tanggal created_at dengan waktu Indonesia
    )
    db.session.add(new_produk)
    db.session.commit()

    response = {
        'message': 'Produk added successfully!',
        'produk': new_produk.to_dict()  # Menggunakan metode to_dict() untuk mengonversi objek produk ke dictionary
    }
    return jsonify(response), 201

@jwt_required()
def update_produk(produk_id):
    produk = Produk.query.get(produk_id)
    if not produk:
        return jsonify({'error': 'Produk not found'}), 404

    update_data = request.get_json()
    produk.nama = update_data.get('nama', produk.nama)
    produk.deskripsi = update_data.get('deskripsi', produk.deskripsi)
    produk.harga = update_data.get('harga', produk.harga)
    produk.stok = update_data.get('stok', produk.stok)
    produk.kategori_id = update_data.get('kategori_id', produk.kategori_id)  # Update kategori_id
    produk.created_at = update_data.get('created_at', produk.created_at)

    db.session.commit()

    response = {
        'message': 'Produk updated successfully!',
        'produk': produk.to_dict()  # Menggunakan metode to_dict() untuk mengonversi objek produk ke dictionary
    }
    return jsonify(response), 200

@jwt_required()
def delete_produk(produk_id):
    produk = Produk.query.get(produk_id)
    if not produk:
        return jsonify({'error': 'Produk not found'}), 404

    db.session.delete(produk)
    db.session.commit()
    return jsonify({'message': 'Produk deleted successfully!'}), 200
