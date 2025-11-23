# 📡 Arquitetura de Aplicação Distribuída com Balanceamento DNS (Round Robin) e Sessão Centralizada

## 📌 Visão Geral do Projeto

Este projeto implementa uma aplicação web distribuída, com **escala horizontal** e **persistência de sessão entre múltiplos servidores**, conforme solicitado no Trabalho 02 da disciplina *Redes de Computadores*.

A arquitetura segue o padrão **3 camadas**:

- **Frontend:** React  
- **Backend:** Python + Flask  
- **Banco de Dados:** MySQL  
- **Infraestrutura:** Hospedada 100% em nuvem (Railway)  
- **Balanceamento de Carga:** Round Robin via DNS

---

## 🌐 Domínio do Projeto

A aplicação completa está publicada em:

# 👉 **www.meutrabalhoredes.online**

Este domínio está configurado com **Round Robin DNS**, alternando entre três servidores distintos para simular escalabilidade horizontal.

---

## 🏗️ Arquitetura Geral

O sistema é composto por **5 servidores na nuvem**, conforme exigência:

| Função | Quantidade | Tecnologia | Hospedagem |
|--------|-----------|-------------|-------------|
| Servidores HTTP | **3** | Python + Flask | Railway |
| Servidor DNS | **1** | Cloudflare (DNS) | Cloudflare |
| Banco de Dados | **1** | MySQL 8 | Railway |

---

# 🖥️ Frontend (React)

- Desenvolvido com **React + Vite**
- Realiza chamadas ao backend via REST
- Exibe:
  - Tela de login
  - Perfil do usuário logado
  - Nome do servidor backend que atendeu a requisição
  - Data e hora do login
  - ID da sessão centralizada


---

# 🔧 Backend (Python + Flask)

Os três backends são **instâncias idênticas**, cada uma rodando em um servidor Railway.

### 🔹 Persistência de Sessão

- Nenhum backend armazena sessão localmente.
- Toda sessão é gravada no banco MySQL.
- Qualquer backend consegue validar e carregar uma sessão pelo ID armazenado no cookie.
- Assim, o usuário **permanece logado mesmo que o DNS o mande para outro servidor**.

### 🔹 Endpoints principais

| Rota | Método | Função |
|------|--------|---------|
| `/login` | POST | Autentica o usuário |
| `/meu-perfil` | GET | Retorna informações do usuário e hostname do servidor |

Os backends utilizam:

```python
from flask_cors import CORS
CORS(app, supports_credentials=True)
```
# 📦 Infraestrutura (Railway)

A infraestrutura contém:

- 3 backends Flask

- 1 frontend React

- 1 banco MySQL

# 🔁 Balanceamento Round Robin DNS

O domínio www.meutrabalhoredes.online aponta para 3 endereços IP distintos, um para cada backend:
```
A → IP_APP1
A → IP_APP2
A → IP_APP3
```

O DNS responde alternando os IPs.

# 🗺️ Documentação da Rede (Diagrama)
![documentação redes](https://github.com/user-attachments/assets/9d4d613e-3894-47ed-8635-f57072ec64aa)

# 🧪 Testes Automatizados

O projeto inclui testes automatizados em Python usando pytest.

Eles verificam:

- Login

- Criação de sessão

- Acesso autenticado ao perfil

- Validação de sessão entre servidores diferentes

# ▶️ Rodando os testes:
```
pytest -v
```
