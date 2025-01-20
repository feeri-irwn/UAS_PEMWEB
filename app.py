from config import app, db
from routes.User_bp import user_bp
from routes.Detail_Pesanan_bp import detailpesanan_bp
from routes.Kategori_bp import kategori_bp
from routes.Pesanan_bp import pesanan_bp
from routes.Produk_bp import produk_bp
from flask import request,jsonify
from flask_jwt_extended import JWTManager, get_jwt_identity, jwt_required

app.register_blueprint(user_bp)
app.register_blueprint(detailpesanan_bp)
app.register_blueprint(produk_bp)
app.register_blueprint(kategori_bp)
app.register_blueprint(pesanan_bp)

jwt = JWTManager(app)

@app.before_request
def before_request():
    excluded_routes = ['/api/login','/api/register']
    if request.path in excluded_routes:
        return None
    return None

@app.route('/api/protected',methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user),200



db.create_all()
if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)