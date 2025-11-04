from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
import mysql.connector, uuid, socket, datetime, hashlib
from config import DB_CONFIG

app = Flask(__name__)
CORS(app, supports_credentials=True)  # Permite cookies também
def get_db():
    return mysql.connector.connect(**DB_CONFIG)

@app.route('/')
def home():
    return "Servidor ativo: " + socket.gethostname()

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = data.get('login')
    senha = data.get('senha')

    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    senha_hash = hashlib.sha256(senha.encode()).hexdigest()

    cursor.execute("SELECT * FROM usuarios WHERE login=%s AND senha_hash=%s", (user, senha_hash))
    usuario = cursor.fetchone()

    if usuario:
        session_id = str(uuid.uuid4())
        cursor.execute("INSERT INTO sessoes (id_sessao, id_usuario, data_login, ip_servidor) VALUES (%s,%s,%s,%s)", 
                       (session_id, usuario['id'], datetime.datetime.now(), socket.gethostname()))
        conn.commit()
        resp = make_response({"message": "Login efetuado", "nome": usuario['nome']})
        resp.set_cookie('session_id', session_id)
        return resp
    else:
        return jsonify({"error": "Usuário ou senha incorretos"}), 401

@app.route('/meu-perfil')
def perfil():
    session_id = request.cookies.get('session_id')
    if not session_id:
        return jsonify({"error": "Não autenticado"}), 401

    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT u.nome, s.data_login, s.ip_servidor
        FROM sessoes s JOIN usuarios u ON s.id_usuario=u.id
        WHERE s.id_sessao=%s
    """, (session_id,))
    sessao = cursor.fetchone()

    if sessao:
        return jsonify({
            "nome": sessao['nome'],
            "data_login": str(sessao['data_login']),
            "servidor": socket.gethostname(),
            "session_id": session_id
        })
    else:
        return jsonify({"error": "Sessão inválida"}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
