# Rock-Paper-Scissors Game using Flask

This is a **Rock-Paper-Scissors** game built using **Python (Flask)** as part of a project for **CodSoft Internship**.

The traditional logic usually handled by JavaScript on the frontend has been moved to the backend using Python, showcasing how simple game logic can be executed server-side with Flask.

---
**📸 Screenshot**
![Image](https://github.com/user-attachments/assets/c8f6f8f7-cd0e-4245-8552-70a227b2d005)

---
## 🚀 Features

- Interactive web UI
- Game logic handled by Python (not JavaScript)
- Clean and minimal interface
- Flask-based routing and backend logic
- Randomized computer move

---

## 📁 Folder Structure
```bash
Rock-Paper-scissors-game-using-flask/
│
├── static/
│ └── style.css # CSS styles for the game UI
│
├── templates/
│ └── index.html # HTML template rendered by Flask
│
├── app.py # Main Flask application (Python handles game logic)
├── README.md # Project documentation (this file)
```

---

## 🔄 JavaScript Replaced by Python (Backend Logic)

In most web-based Rock-Paper-Scissors games, the game logic (random selection, win/draw/lose decisions) is written in JavaScript. In this project, all such logic is moved to **Python** using Flask:

- The user's choice is sent to the Flask backend via an HTML form (`POST` method).
- The server randomly selects the computer's move.
- Game outcome is calculated in Python.
- The result is rendered back on the same page (`index.html`) using Jinja2 templating.

This server-side handling demonstrates how simple games or logic-based interactions can be done entirely with Python and Flask without needing JavaScript.

---

## 🛠️ How to Run the Project Locally

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Dhruvhere-24/Rock-Paper-scissors-game-using-flask
   cd Rock-Paper-scissors-game-using-flask
   ```

2. **Install dependencies (Flask):**
   ```bash
   pip install flask
   ```
3. **Run the app:**
   ```bash
   python app.py
   ```
4. **Open in your browser:**
   ```bash
   http://localhost:5000
   ```
🧑‍💻 Author

- Dhruv Singh
- GitHub: @Dhruvhere-24

-------------------------------------------------------
📢 Acknowledgement

This project was completed as part of the CodSoft Internship program.
