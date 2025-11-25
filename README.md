# 🂡 Blackjack — Python Terminal Game

*A small project that helped me understand Python in a practical way.*

This is a simple Blackjack game I built while learning Python basics.

It runs in the terminal, doesn’t use any external libraries, and is mainly focused on practicing logic, functions, and user interaction.

The goal is simple:

**Try to get as close to 21 as possible without crossing it.**

---

## 📚 What I Learned While Building This

This project wasn’t just about making a game — it helped me understand:

- How to structure a Python project across multiple files (`main.py`, `art.py`)
- Working with lists and random selection
- Writing clean functions to handle parts of the game
- How to update values and states during runtime
- Handling user inputs in a loop
- Basic game logic and conditions
- Making the terminal experience a bit more interactive with ASCII art

Overall, it was a great hands-on way to improve my Python fundamentals.

---

## 📁 Project Structure

```
📦 Blackjack-Terminal-Game
 ┣ 📜 main.py      # Game logic and flow
 ┗ 📜 art.py       # ASCII logo for the game
```

- `main.py` includes card dealing, score calculations, hit/stand options, dealer logic, and final result.
- `art.py` includes the ASCII logo that shows at the start.

---

## 🎮 How to Play (Manual)

Once you run the game, you'll be asked:

```
Do you want to play a game of Blackjack? Type 'Y' or 'N':
```

### 👉 Starting the Game

- Press **Y** → start a round
- Press **N** → exit

### 👉 Your Turn

You get **two cards**, and the computer gets **two cards** (one hidden).

Your total is shown.

You now choose:

- **H (Hit)** → Draw another card
- **S (Stand)** → Keep your current hand

### 👉 Game Rules (Simple Version)

- Face cards count as **10**
- Ace counts as **11**
- If your total goes **above 21**, you lose immediately
- Dealer draws cards until reaching **17 or more**
- After both sides stand, the game compares the totals

### 👉 Possible Outcomes

- You hit **21** → Blackjack
- You go **over 21** → Bust
- Dealer goes over → You win
- Higher total under 21 wins
- Same total → Tie

The game then prints both final hands clearly.

### 👉 Replay

At the end of each round, you can choose to play again.

---

## ▶️ How to Run It

Run the game using:

```
python main.py
```

No additional setup or dependencies needed.

---

## 🧠 Why I Chose This Project

Instead of only reading theory, I wanted a small but complete project to apply what I was learning.

Blackjack was perfect because it involves:

- Game flow
- Repeated decisions
- Conditions
- Randomness
- Updating values
- Clean function usage

It helped me build confidence in writing working Python programs from scratch.

---

## 📝 License

This project is open for anyone to use or modify.
