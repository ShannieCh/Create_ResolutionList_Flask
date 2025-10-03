# Create_ResolutionList_Flask

A Flask web application that allows users to register, log in, and create, update, or delete their own posts.

## Features

- Secure user registration with password hashing (bcrypt)  
- User login and logout functionality with session management (Flask-Login)  
- User-specific post creation, editing, and deletion  
- Authorization to restrict post deletion to post owners  
- Dynamic HTML rendering with Flask and Jinja2 templates  
- SQLite database using SQLAlchemy ORM  

## Getting Started

### Prerequisites

- Python 3.x installed

### Installation and Setup

1. **Clone the repository**

```bash
git clone https://github.com/ShannieCh/Create_ResolutionList_Flask.git
cd Create_ResolutionList_Flask
```

2. **Create a virtual environment**

```bash
python3 -m venv venv
```

3. **Activate the virtual environment**

* On **macOS/Linux**:

```bash
source venv/bin/activate
```

* On **Windows (PowerShell)**:

```powershell
.\venv\Scripts\Activate.ps1
```

* On **Windows (Command Prompt)**:

```cmd
venv\Scripts\activate.bat
```

4. **Install dependencies**

```bash
pip install -r requirements.txt
```

5. **Run the Flask app**

```bash
flask run
```

6. Open your browser at [http://localhost:5000](http://localhost:5000)

## Security Considerations & Future Improvements

* Passwords are securely hashed using bcrypt to protect user credentials.
* Currently, email verification and password reset features are not implemented.
* Input validation is in place, but additional measures can be added to prevent injection attacks.
* Future plans include:

  * Adding email confirmation during registration
  * Implementing password reset functionality
  * Enhancing security with rate limiting and account lockout on multiple failed login attempts
  * Integrating OAuth for social login options (e.g., Google, GitHub)

```
```
