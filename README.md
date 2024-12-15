# Insta-clone

Insta Clone is a social media platform clone that mimics the core features of Instagram, built using Django for the backend and React for the frontend. This project demonstrates the integration of a backend API with a frontend interface to create a basic version of Instagram's functionality.

## Features

- User authentication (signup, login, and logout)
- Post creation (images and captions)
- Feed displaying posts from users
- Like and comment on posts
- Follow and unfollow users
- User profile pages
- Responsive design

## Tech Stack

- **Frontend**: React.js, HTML, CSS
- **Backend**: Django, Django REST Framework
- **Database**: SQLite (for development), PostgreSQL (recommended for production)
- **Authentication**: JWT (JSON Web Tokens) for user authentication

## Project Structure
Insta-clone/ 
├── backend/ # Backend (Django) application 
│ ├── users/ # User-related functionalities 
│ ├── posts/ # Post-related functionalities 
│ ├── manage.py # Django management script 
│ └── db.sqlite3 # SQLite database (development) 
├── frontend/ # Frontend (React) application 
│ ├── src/ # React components and pages 
│ ├── public/ # Static assets (images, icons) 
│ └── package.json # Frontend dependencies and scripts 
├── requirements.txt # Backend dependencies 
└── .gitignore # Ignored files (node_modules, env, etc.)

Acknowledgements
Django for backend development
React.js for frontend development
SQLite and PostgreSQL for database management
JWT for secure user authentication