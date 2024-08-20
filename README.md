# FastAPI Application with JWT Authentication

This project is a simple FastAPI application that uses JWT tokens for authentication. Users can log in, and if authenticated, access protected routes.

## Features

- User authentication with JWT tokens.
- Login page using HTML, which interacts with the FastAPI backend.
- Protected routes that require JWT tokens for access.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.8+
- SQLite (optional, as SQLite is integrated into Python)
- pip package manager

## Installation

1. *Clone the repository:*

   ```bash
   git clone https://github.com/anmol-2000/test_req.git
   cd test_req

2. *Install all the dependency mentioned in requirements.txt file*
    ```bash
    pip install -r requirements.txt

3. *Run the Following command to start the uvicorn server
    ```bash
    python item/main.py

4. Opne the application and Login with the user credentials userid: admin password: abc123

# Application In-Depth Detail

1. This Application will store all your items and give you the total sum. It stores item based on the userid. Only the access user can see items
2. Backend, I'm using Python FastAPI Framework with SQLite as Data Base. We have added the Payload Validation by using Pydantic Models
    - Logging Mechanism is also added with required log statemtent. TO keep Track of the any future issue with backup count as 3 currently
    - JWT Authentication and validation is implented on all the incoming required http request
3. Login Mechanism to facilitate the JWT Authentication in all your api's
    - We're storing the password after hashing it
    - For Login also, we're verifying the hash password using the CryptContext
4. Frontent is just simple HTML, with some js and css file. We have added html files as template with Jinja2 functionality