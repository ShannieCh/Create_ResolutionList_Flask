
#  Resolution Tracker: Secure & Agent-Augmented

This is a Full-Stack Flask application built for the **GitHub Copilot CLI Challenge (Feb 2026)**. It allows users to track their 2026 goals with a focus on zero-trust security and clean architecture.

##  Agentic Development (GitHub Copilot CLI)

This project was developed and audited using the **GitHub Copilot CLI (v0.0.410)** in **Agent Mode**. I utilized the CLI's advanced terminal capabilities to oversee the application's lifecycle:

* **Security Audit:** Used the terminal agent to perform a `@workspace` scan, which identified a critical **Open Redirect** vulnerability in the `login` route.
* **Agentic Planning:** Leveraged **Plan Mode** to architect a robust `is_safe_url` validation utility, ensuring all redirects remain within the local domain.
* **CRUD Refactoring:** Directed the agent to implement secure `Update` and `Delete` routes, ensuring that unauthorized users cannot modify resolutions belonging to others.

##  Testing the App

To verify the secure features and log in as the test user, use these credentials:

* **Email:** `hanna@gmail.com`
* **Password:** `hanna123`

##  Features

* **Full CRUD:** Create, Read, Update, and Delete resolutions.
* **Advanced Validation:** Protection against Open Redirect attacks using `urllib.parse`.
* **Secure Auth:** Password hashing via `Flask-Bcrypt` and session management via `Flask-Login`.
* **Database:** SQLite with SQLAlchemy ORM.

## Getting Started

### 1. Installation

```bash
git clone https://github.com/ShannieCh/Create_ResolutionList_Flask.git
cd Create_ResolutionList_Flask
python -m venv venv

```

### 2. Setup (Windows PowerShell)

```powershell
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt

```

### 3. Run

```powershell
flask run

```

Access the app at: [http://127.0.0.1:5000](http://127.0.0.1:5000)

## 🛡️ Security Remediation

A major vulnerability was identified where the `?next=` parameter could be manipulated to redirect users to external malicious sites.

**The Fix:** We implemented a `netloc` validation check that compares the redirect target against the host URL. This "Zero-Trust" pattern ensures users stay within the secure application environment.

---