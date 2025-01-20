from flask import jsonify, request
from models.KategoriModel import Kategori
from config import db
from flask_jwt_extended import jwt_required

@jwt_required()
def get_kategori():
    kategoris = Kategori.query.all()
    kategori_data = []
    for kategori in kategoris:
        kategori_data.append({
            'id': kategori.id,
            'name': kategori.name,
            'descrip': kategori.descrip,
            'created_at': kategori.created_at
        })

    response = {
        'status': 'success',
        'data': {
            'kategoris': kategori_data
        },
        'message': 'Kategori retrieved successfully!'
    }
    return jsonify(response), 200

@jwt_required()
def get_kategori_by_id(kategori_id):
    kategori = Kategori.query.get(kategori_id)
    if not kategori:
        return jsonify({'error': 'Kategori not found'}), 404

    kategori_data = {
        'id': kategori.id,
        'name': kategori.name,
        'descrip': kategori.descrip,
        'created_at': kategori.created_at
    }

    response = {
        'status': 'success',
        'data': {
            'kategori': kategori_data
        },
        'message': 'Kategori retrieved successfully!'
    }
    return jsonify(response), 200

@jwt_required()
def add_kategori():
    new_kategori_data = request.get_json()
    new_kategori = Kategori(
        name=new_kategori_data['name'],
        descrip=new_kategori_data.get('descrip'),
        created_at=new_kategori_data.get('created_at')
    )
    db.session.add(new_kategori)
    db.session.commit()
    return jsonify({'message': 'Kategori added successfully!', 'kategori': {
        'id': new_kategori.id,
        'name': new_kategori.name,
        'descrip': new_kategori.descrip,
        'created_at': new_kategori.created_at
    }}), 201

@jwt_required()
def update_kategori(kategori_id):
    kategori = Kategori.query.get(kategori_id)
    if not kategori:
        return jsonify({'error': 'Kategori not found'}), 404

    update_data = request.get_json()
    kategori.name = update_data.get('name', kategori.name)
    kategori.descrip = update_data.get('descrip', kategori.descrip)
    kategori.created_at = update_data.get('created_at', kategori.created_at)

    db.session.commit()
    return jsonify({'message': 'Kategori updated successfully!', 'kategori': {
        'id': kategori.id,
        'name': kategori.name,
        'descrip': kategori.descrip,
        'created_at': kategori.created_at
    }}), 200

@jwt_required()
def delete_kategori(kategori_id):
    kategori = Kategori.query.get(kategori_id)
    if not kategori:
        return jsonify({'error': 'Kategori not found'}), 404

    db.session.delete(kategori)
    db.session.commit()
    return jsonify({'message': 'Kategori deleted successfully!'}), 200
