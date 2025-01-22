from flask import jsonify, request
from models.UserModel import User
from config import db
import bcrypt
from flask_jwt_extended import create_access_token, jwt_required
from datetime import timedelta, datetime

# Fungsi untuk login
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({'message': 'User not found'}), 404
    
    if not check_password_hash(user.password, password):
        return jsonify({'message': 'Invalid password'}), 401
    
    access_token = create_access_token(identity=user.username, expires_delta=timedelta(days=1))
    return jsonify({'access_token': access_token}), 200

# Fungsi untuk meng-hash password
def hash_password(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed

# Fungsi untuk membandingkan password
def check_password_hash(hashed_password, user_password):
    return bcrypt.checkpw(user_password.encode('utf-8'), hashed_password.encode('utf-8'))

# Mendapatkan semua user
@jwt_required()
def get_users():
    users = User.query.all()
    users_data = []
    for user in users:
        users_data.append({
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'fullname': user.fullname,
            'status': user.status,
            'role': user.role,
            'created_at': user.created_at
        })

    response = {
        'status': 'success',
        'data': {'users': users_data},
        'message': 'Users retrieved successfully!'
    }
    return jsonify(response), 200

# Mendapatkan user berdasarkan ID
@jwt_required()
def get_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    user_data = {
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'fullname': user.fullname,
        'status': user.status,
        'role': user.role,
        'created_at': user.created_at
    }

    response = {
        'status': 'success',
        'data': {'user': user_data},
        'message': 'User retrieved successfully!'
    }
    return jsonify(response), 200

# Menambahkan user baru
@jwt_required()
def add_user():
    new_user_data = request.get_json()
    hashed_password = hash_password(new_user_data['password'])
    
    new_user = User(
        username=new_user_data['username'],
        password=hashed_password,  # Menyimpan hashed password, bukan password asli
        email=new_user_data['email'],
        fullname=new_user_data['fullname'],
        status=new_user_data['status'],
        role=new_user_data['role'],
        created_at=new_user_data.get('created_at') or datetime.now()  # Gunakan datetime saat ini jika tidak ada
    )
    
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({'message': 'User added successfully!', 'user': new_user.to_dict()}), 201

# Mengupdate user berdasarkan ID
@jwt_required()
def update_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    update_data = request.get_json()
    user.username = update_data.get('username', user.username)
    user.email = update_data.get('email', user.email)
    user.fullname = update_data.get('fullname', user.fullname)
    user.status = update_data.get('status', user.status)
    
    # Cek jika ada perubahan password
    if 'password' in update_data:
        user.password = hash_password(update_data['password'])  # Meng-hash password yang baru
    
    user.role = update_data.get('role', user.role)

    db.session.commit()
    
    return jsonify({'message': 'User updated successfully!', 'user': user.to_dict()}), 200

# Menghapus user berdasarkan ID
@jwt_required()
def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted successfully!'}), 200

# Update sebagian data user (patch)
@jwt_required()
def patch_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    patch_data = request.get_json()
    if 'username' in patch_data:
        user.username = patch_data['username']
    if 'password' in patch_data:
        user.password = patch_data['password'] # Meng-hash password baru
    if 'email' in patch_data:
        user.email = patch_data['email']
    if 'fullname' in patch_data:
        user.fullname = patch_data['fullname']
    if 'status' in patch_data:
        user.status = patch_data['status']
    if 'role' in patch_data:
        user.role = patch_data['role']

    db.session.commit()
    
    return jsonify({'message': 'User updated successfully!', 'user': user.to_dict()}), 200
