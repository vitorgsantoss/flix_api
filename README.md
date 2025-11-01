# 🎬 **Flix API**

API REST desenvolvida em **Django Rest Framework** para o gerenciamento de **filmes**, **atores**, **gêneros** e **reviews**.  
Inclui autenticação segura de usuários via **JWT (JSON Web Token)**.

---

## 🚀 **Principais Funcionalidades**

- ✅ CRUD completo de **filmes**, **atores**, **gêneros** e **reviews**  
- 🔒 Autenticação e autorização com **JWT**  
- 👤 Registro e login de usuários  
- 🎞️ Associação entre filmes, gêneros e elenco  
- 📝 Sistema de avaliações (reviews)  
- ⚙️ Estrutura totalmente baseada em **RESTful APIs**

---

## 🧰 **Tecnologias Utilizadas**

- **Python 3.10+**  
- **Django 5+**  
- **Django Rest Framework (DRF)**  
- **Simple JWT (Autenticação)**  
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

### 5️⃣ Crie um superusuário (opcional, para acessar o admin)

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

Com o corpo:
```json
{
  "username": "seu_usuario",
  "password": "sua_senha"
}
```

Você receberá:
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
  "genres": [1, 2],
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

## 🧩 **Estrutura do Projeto**

```
flix_api/
│
├── flix_api/          # Configurações principais do projeto Django
├── movies/            # Aplicação responsável por filmes, gêneros e atores
├── reviews/           # Aplicação de avaliações (reviews)
├── users/             # Aplicação de autenticação e usuários
│
├── manage.py
└── requirements.txt
```

---

## 🧪 **Testes**

Para executar os testes automatizados:
```bash
python manage.py test
```

---

## 🧠 **Melhorias Futuras**

- Implementar paginação e filtros avançados nas listagens  
- Adicionar upload de imagens de filmes e atores  
- Documentação automática com **Swagger / drf-spectacular**  
- Integração com banco de dados PostgreSQL  

---

## 📄 **Licença**

Este projeto é distribuído sob a licença **MIT**.  
Sinta-se livre para usar, modificar e contribuir.  

---

## 👨‍💻 **Autor**

**Vítor Santos**  
🔗 [GitHub](https://github.com/vitorgsantoss)