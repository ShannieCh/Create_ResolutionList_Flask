# Create_ResolutionList_Flask

A Flask web application that allows users to register, log in, and create, update, or delete their own posts.

## Features

- Secure user registration with password hashing (bcrypt)  
- User login and logout functionality with session management (Flask-Login)  
- User-specific post creation, editing, and deletion  
- Authorization to restrict post deletion to post owners  
- Dynamic HTML rendering with Flask and Jinja2 templates  
- SQLite database using SQLAlchemy ORM

## Agentic Development with GitHub Copilot CLI

This project was refined using **GitHub Copilot CLI (v0.0.410)** in **Agent Mode**. 

- **Security Auditing:** Used `@workspace` commands to identify a critical **Open Redirect** vulnerability in the authentication logic.
- **Agentic Planning:** Leveraged the CLI's **Plan Mode** to architect a multi-step fix, including the creation of a robust `is_safe_url` validation utility.
- **Database Refactoring:** Orchestrated a terminal-native refactor to implement `cascade delete` logic across SQLAlchemy models, ensuring zero orphaned records.

## Getting Started

### Prerequisites

- Python 3.x installed

### Installation and Setup

1. **Clone the repository**

```bash
git clone https://github.com/ShannieCh/Create_ResolutionList_Flask.git
```
2. **Go to the folder**

```bash
cd Create_ResolutionList_Flask
```

3. **Create a virtual environment**

```bash
python3 -m venv venv
```

4. **Activate the virtual environment**

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

5. **Install dependencies**

```bash
pip install -r requirements.txt
```

6. **Run the Flask app**

```bash
flask run
```

##  Testing the App

To verify the secure login and resolution features, you can use the following pre-configured test account:

- **Email:** `hanna@gmail.com`
- **Password:** `hanna123`

> [!TIP]
> This account was used during the **Agentic Security Audit** to verify that the `is_safe_url` validation successfully prevents malicious redirects while allowing legitimate access to user resolutions.

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


