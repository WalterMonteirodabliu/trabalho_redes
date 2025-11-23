import requests

BASE_URL = "https://api.meutrabalhoredes.online"


# ===============================
# 1) Testa se o servidor responde
# ===============================
def test_home():
    r = requests.get(f"{BASE_URL}/")
    assert r.status_code == 200
    assert "Servidor ativo" in r.text


# ===============================
# 2) Teste de login
# ===============================
def test_login():
    payload = {
        "login": "teste",     # coloque o login REAL cadastrado no seu MySQL
        "senha": "senha"        # coloque a senha REAL (aqui vai ser hasheada)
    }

    r = requests.post(f"{BASE_URL}/login", json=payload)
    assert r.status_code == 200
    assert "session_id" in r.cookies  # Cookie precisa existir!


# ===============================
# 3) Teste do /meu-perfil usando o cookie da sessão
# ===============================
def test_meu_perfil():
    login_payload = {
        "login": "teste",      # mesmo usuário acima
        "senha": "senha"
    }

    # 1) Faz login
    login = requests.post(f"{BASE_URL}/login", json=login_payload)
    assert login.status_code == 200

    # Captura cookie de sessão
    cookies = login.cookies
    assert "session_id" in cookies

    # 2) Acessa /meu-perfil usando esse cookie
    perfil = requests.get(f"{BASE_URL}/meu-perfil", cookies=cookies)

    assert perfil.status_code == 200
    data = perfil.json()

    # Verifica se os campos corretos vieram
    assert "nome" in data
    assert "data_login" in data
    assert "servidor" in data
    assert "session_id" in data
