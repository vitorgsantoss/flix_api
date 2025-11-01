# 🎬 **Flix API**

API REST desenvolvida em **Django Rest Framework** para o gerenciamento de **filmes**, **atores**, **gêneros** e **reviews**.  
Inclui autenticação segura de usuários via **JWT (JSON Web Token)** e documentação automática via **Swagger / Redoc**.

---

## 🚀 **Principais Funcionalidades**

- ✅ CRUD completo de **filmes**, **atores**, **gêneros** e **reviews**  
- 🔒 Autenticação e autorização com **JWT**  
- 👤 Registro e login de usuários  
- 🎞️ Associação entre filmes, gêneros e elenco  
- 📝 Sistema de avaliações (reviews)  
- ⚙️ Estrutura totalmente baseada em **RESTful APIs**  
- 📘 Documentação automática com **OpenAPI 3 (drf-spectacular)**

---

## 🧰 **Tecnologias Utilizadas**

- **Python 3.10+**  
- **Django 5+**  
- **Django Rest Framework (DRF)**  
- **drf-spectacular** *(documentação Swagger/OpenAPI 3)*  
- **Simple JWT** *(autenticação)*  
- **SQLite3** *(banco de dados padrão, facilmente substituível por PostgreSQL ou MySQL)*

---

## ⚙️ **Como Executar o Projeto**

### 1️⃣ Clone o repositório

```bash
git clone https://github.com/vitorgsantoss/flix_api.git
cd flix_api
```

### 2️⃣ Crie e ative o ambiente virtual

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux / macOS:**
```bash
python -m venv venv
source venv/bin/activate
```

### 3️⃣ Instale as dependências

```bash
pip install -r requirements.txt
```

### 4️⃣ Aplique as migrações

```bash
python manage.py migrate
```

### 5️⃣ Crie um superusuário (opcional)

```bash
python manage.py createsuperuser
```

### 6️⃣ Execute o servidor local

```bash
python manage.py runserver
```

Acesse o projeto em:  
👉 **http://127.0.0.1:8000/**

---

## 🔑 **Autenticação JWT**

A API utiliza **Django Rest Framework Simple JWT**.  
Após criar um usuário, obtenha o token de acesso enviando um `POST` para:

```
/api/token/
```

**Corpo da requisição:**
```json
{
  "username": "seu_usuario",
  "password": "sua_senha"
}
```

**Resposta:**
```json
{
  "refresh": "token_refresh",
  "access": "token_access"
}
```

Use o token `access` no cabeçalho das requisições:
```
Authorization: Bearer <token_access>
```

---

## 📘 **Documentação Swagger / OpenAPI**

A documentação da API é gerada automaticamente pelo **drf-spectacular**, seguindo o padrão **OpenAPI 3**.

Após iniciar o servidor, acesse:

- 📄 **Schema JSON:** [http://127.0.0.1:8000/api/schema/](http://127.0.0.1:8000/api/schema/)  
- 📘 **Swagger UI:** [http://127.0.0.1:8000/api/docs/](http://127.0.0.1:8000/api/docs/)  
- 📗 **Redoc:** [http://127.0.0.1:8000/api/redoc/](http://127.0.0.1:8000/api/redoc/)

---

## 📡 **Exemplos de Endpoints**

### 🎥 Filmes
- **Listar filmes:** `GET /movies/`
- **Detalhar filme:** `GET /movies/<id>/`
- **Criar filme:** `POST /movies/`
- **Atualizar filme:** `PUT /movies/<id>/`
- **Excluir filme:** `DELETE /movies/<id>/`

**Exemplo de criação:**
```json
POST /movies/
{
  "title": "Inception",
  "release_year": 2010,
  "genres": 1,
  "actors": [3, 5]
}
```

---

### 🎭 Atores
- **Listar atores:** `GET /actors/`
- **Criar ator:** `POST /actors/`

**Exemplo:**
```json
POST /actors/
{
  "name": "Leonardo DiCaprio"
}
```

---

### 🎬 Gêneros
- **Listar gêneros:** `GET /genres/`
- **Criar gênero:** `POST /genres/`

**Exemplo:**
```json
POST /genres/
{
  "name": "Ficção Científica"
}
```

---

### 📝 Reviews
- **Listar reviews:** `GET /reviews/`
- **Criar review:** `POST /reviews/`

**Exemplo:**
```json
POST /reviews/
{
  "movie": 1,
  "rating": 5,
  "comment": "Excelente filme!"
}
```

---


## 📄 **Licença**

Este projeto é distribuído sob a licença **MIT**.  
Sinta-se livre para usar, modificar e contribuir.  

---

## 👨‍💻 **Autor**

**Vítor Santos**  
🔗 [GitHub](https://github.com/vitorgsantoss)