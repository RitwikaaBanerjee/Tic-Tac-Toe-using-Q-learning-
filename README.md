# 🤖 Tic-Tac-Toe Q-Learning Agent (with Streamlit UI)

This project implements a **Tic-Tac-Toe AI Agent** using **Q-Learning (Reinforcement Learning)**.  
You can play against the trained agent (X) directly in your browser using **Streamlit**.

---

## 🧠 About the Project

The agent learns how to play Tic-Tac-Toe by playing thousands of games against a random opponent.  
Through reinforcement learning, it updates its **Q-table** — a mapping of game states to action values — to maximize its chances of winning.

- **X (Agent)** → AI trained via Q-learning  
- **O (You)** → Human player  
- The board positions are numbered from **0–8** as:

```
0 | 1 | 2
---------
3 | 4 | 5
---------
6 | 7 | 8
```

---

## 🚀 Features

- Trains a Q-learning agent to play Tic-Tac-Toe intelligently  
- Streamlit web app to play interactively  
- Real-time board updates  
- Simple, lightweight, and easy to understand  

---

## 🧩 Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/tic-tac-toe-q-agent.git
cd tic-tac-toe-q-agent
```

### 2️⃣ Install dependencies
```bash
pip install streamlit
```

(Optional, if not installed yet)
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the app
```bash
streamlit run tic_tac_toe_q_agent.py
```

The app will open automatically in your browser at [http://localhost:8501](http://localhost:8501).

---

## 🕹️ How to Play

- You are **O**, and the AI agent is **X**.
- Enter your move (0–8) in the input field.
- The agent will respond automatically.
- Continue until the game ends with a win, loss, or draw!

---

## 📘 Q-Learning Concept (Short Summary)

Q-learning is a **model-free reinforcement learning algorithm**.  
It learns an optimal action-value function `Q(s, a)` which tells the best action `a` to take in a given state `s`.

**Update rule:**
```
Q(s, a) = Q(s, a) + lr * [(reward + γ * max(Q(s’, a’))) - Q(s, a)]
```
Where:
- `lr` = learning rate  
- `γ` = discount factor  
- `reward` = immediate feedback after taking action `a`  



---

## 🏆 Future Improvements
- Add a smarter opponent (Minimax agent)
- Save and load trained Q-table
- Visual animations for moves
- Difficulty levels

---

## 👩‍💻 Author
**Ritwika Bandyopadhyay**  
✨ Passionate about AI, ML, and Python Development.  

---

## 🪪 License
This project is licensed under the **MIT License** — feel free to modify and use it.
