# Late Show API

A RESTful API for managing guests, episodes, and appearances for a late-night show.

---

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
- [How to Run](#how-to-run)
- [Authentication Flow](#authentication-flow)
- [API Routes](#api-routes)
- [Sample Requests & Responses](#sample-requests--responses)
- [Postman Usage Guide](#postman-usage-guide)
- [Repository](#repository)

---

## Features

- Manage guests, episodes, and appearances
- JWT-based authentication
- RESTful endpoints
- PostgreSQL database support

---

## Prerequisites

- Python 3.8+
- PostgreSQL
- pipenv or pip
- [Postman](https://www.postman.com/) (optional, for API testing)

---

## Setup Instructions

1. **Clone the Repository**

    ```sh
    git clone https://github.com/kingkelly12/late-show-api-challenge.git
    cd late-show-api-challenge
    ```

2. **Set Up PostgreSQL**

    - Create a database (default: `late_show_db`):

      ```sh
      createdb late_show_db
      ```

3. **Configure Environment Variables**

    - Create a `.env` file in the `server/` directory:

      ```
      DATABASE_URL=postgresql://postgres:postgres@localhost:5432/late_show_db
      JWT_SECRET_KEY=your-secret-key
      ```

4. **Install Dependencies**

    ```sh
    cd server
    pipenv install
    # or
    pip install -r requirements.txt
    ```

---

## How to Run

1. **Migrate the Database**

    ```sh
    flask db upgrade
    ```

2. **Seed the Database**

    ```sh
    python seed.py
    ```

3. **Run the Application**

    ```sh
    python app.py
    ```

    The API will be available at `http://localhost:5432/`.

---

## Authentication Flow

### Register

- **POST** `/auth/register`
- Body:
  ```json
  {
    "username": "testuser",
    "password": "testpass"
  }
  ```
- Response:
  ```json
  { "message": "User created successfully" }
  ```

### Login

- **POST** `/auth/login`
- Body:
  ```json
  {
    "username": "testuser",
    "password": "testpass"
  }
  ```
- Response:
  ```json
  { "access_token": "<JWT_TOKEN>" }
  ```

### Token Usage

Include the JWT token in the `Authorization` header for protected routes:

```
Authorization: Bearer <JWT_TOKEN>
```

---

## API Routes

### Auth

- `POST /auth/register` — Register a new user
- `POST /auth/login` — Login and receive a JWT token

### Guests

- `GET /guests` — List all guests

### Episodes

- `GET /episodes` — List all episodes
- `GET /episodes/<id>` — Retrieve an episode by ID (with appearances)
- `DELETE /episodes/<id>` — Delete an episode (requires authentication)

### Appearances

- `POST /appearances` — Create a new appearance (requires authentication)

---

## Sample Requests & Responses

### Get All Guests

**Request**
```http
GET /guests
```
**Response**
```json
[
  { "id": 1, "name": "John Doe", "occupation": "Actor" }
]
```

### Get All Episodes

**Request**
```http
GET /episodes
```
**Response**
```json
[
  { "id": 1, "date": "2023-01-01", "number": 101 }
]
```

### Get Episode by ID

**Request**
```http
GET /episodes/1
```
**Response**
```json
{
  "id": 1,
  "date": "2023-01-01",
  "number": 101,
  "appearances": [
    {
      "id": 1,
      "rating": 4,
      "guest": {
        "id": 1,
        "name": "John Doe",
        "occupation": "Actor"
      }
    }
  ]
}
```

### Create Appearance

**Request**
```http
POST /appearances
Authorization: Bearer <JWT_TOKEN>
Content-Type: application/json

{
  "rating": 5,
  "guest_id": 1,
  "episode_id": 1
}
```
**Response**
```json
{
  "id": 1,
  "rating": 5,
  "guest_id": 1,
  "episode_id": 1
}
```

---

## Postman Usage Guide

1. Import [`challenge-4-lateshow.postman_collection.json`](challenge-4-lateshow.postman_collection.json) into Postman.
2. Set the base URL to `http://localhost:5432`.
3. Register and login to obtain a JWT token.
4. For protected routes, add an `Authorization` header:
    ```
    Bearer <your_token>
    ```
5. Use the collection to test all endpoints.

---

## Repository

[https://github.com/kingkelly12/late-show-api-challenge](https://github.com/kingkelly12/late-show-api-challenge)

