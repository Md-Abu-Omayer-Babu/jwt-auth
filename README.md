# JWT Auth

A full-stack authentication system using JWT (JSON Web Tokens), built with a Python FastAPI backend and a Next.js frontend. This project demonstrates secure user registration, login, and protected route access using modern authentication best practices.

## Features

- User registration and login with hashed passwords
- JWT-based authentication and authorization
- Secure token handling and refresh logic
- FastAPI backend with modular route organization
- SQLAlchemy ORM for database management
- Next.js frontend with protected pages and authentication flows
- Utility modules for password hashing, CRUD operations, and more

## Project Structure

```
.
├── backend/
│   ├── api/                # FastAPI route definitions
│   ├── auth/               # JWT and authentication logic
│   ├── db/                 # Database connection and models
│   ├── dependencies/       # Dependency injection for FastAPI
│   ├── models/             # SQLAlchemy models and schemas
│   ├── utils/              # Utility functions (CRUD, password, etc.)
│   └── main.py             # FastAPI app entry point
├── frontend/
│   ├── public/             # Static assets
│   ├── src/                # Next.js app source code
│   └── package.json        # Frontend dependencies
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.10+
- Node.js 18+
- npm or yarn

### Backend Setup

1. Navigate to the backend directory:
   ```powershell
   cd backend
   ```

2. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```

3. Run the FastAPI server:
   ```powershell
   uvicorn main:app --reload
   ```

### Frontend Setup

1. Navigate to the frontend directory:
   ```powershell
   cd frontend
   ```

2. Install dependencies:
   ```powershell
   npm install
   ```

3. Start the Next.js development server:
   ```powershell
   npm run dev
   ```

### Environment Variables

- Configure your backend and frontend environment variables as needed (e.g., secret keys, database URLs, API endpoints).

## Usage

- Register a new user via the frontend or API.
- Log in to receive a JWT token.
- Access protected routes using the token for authentication.

## Technologies Used

- **Backend:** FastAPI, SQLAlchemy, JWT, SQLite
- **Frontend:** Next.js, React
- **Other:** Python, Node.js

## License

This project is licensed under the MIT License.
