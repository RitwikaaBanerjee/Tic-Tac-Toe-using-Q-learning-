import streamlit as st
import random
from collections import defaultdict

# --- Q-Learning Setup ---
Q = defaultdict(lambda: [0]*9)
lr, gamma, eps = 0.5, 0.9, 0.2

def check_win(b):
    wins = [(0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)]
    for x,y,z in wins:
        if b[x]==b[y]==b[z]!=0:
            return b[x]
    return 0

def choose(state, available, train=True):
    if train and random.random() < eps:
        return random.choice(available)
    q = Q[state]
    m = max(q[i] for i in available)
    return random.choice([i for i in available if q[i]==m])

# --- Train Agent (Once) ---
for _ in range(20000):
    b=[0]*9; done=False
    while not done:
        s=''.join(map(str,b))
        a=choose(s,[i for i,v in enumerate(b) if v==0])
        b[a]=1
        win=check_win(b)
        if win or 0 not in b:
            r = 1 if win==1 else 0
            Q[s][a]+=lr*(r-Q[s][a])
            break
        opp=random.choice([i for i,v in enumerate(b) if v==0])
        b[opp]=-1
        win=check_win(b)
        r = -1 if win==-1 else 0
        ns=''.join(map(str,b))
        na=[i for i,v in enumerate(b) if v==0]
        mx=max(Q[ns][i] for i in na) if na else 0
        Q[s][a]+=lr*((r+gamma*mx)-Q[s][a])
        if win or 0 not in b: break

# --- Streamlit App ---
st.title("🤖 Tic-Tac-Toe with Q-learning Agent (X)")
st.write("You are **O (0–8 range)**. Click a cell to play!")

if "board" not in st.session_state:
    st.session_state.board = [0]*9
    st.session_state.done = False
    st.session_state.msg = ""

b = st.session_state.board

def show_board():
    cols = st.columns(3)
    for i in range(9):
        with cols[i%3]:
            cell = 'X' if b[i]==1 else 'O' if b[i]==-1 else ' '
            if not st.session_state.done and b[i]==0:
                if st.button(f"{cell or i}", key=i):
                    human_move(i)
            else:
                st.button(cell, disabled=True, key=i)

def agent_move():
    s=''.join(map(str,b))
    avail=[i for i,v in enumerate(b) if v==0]
    if not avail: return
    a=choose(s,avail,train=False)
    b[a]=1

def human_move(i):
    if b[i]==0:
        b[i]=-1
        if check_win(b)==-1:
            st.session_state.msg="🎉 You Win!"
            st.session_state.done=True
            return
        if 0 not in b:
            st.session_state.msg="😐 Draw!"
            st.session_state.done=True
            return
        agent_move()
        w=check_win(b)
        if w==1:
            st.session_state.msg="🤖 Agent Wins!"
            st.session_state.done=True
        elif 0 not in b:
            st.session_state.msg="😐 Draw!"
            st.session_state.done=True

show_board()
st.write("---")
st.subheader(st.session_state.msg)

if st.button("🔄 Restart Game"):
    st.session_state.board = [0]*9
    st.session_state.done = False
    st.session_state.msg = ""
    st.rerun()