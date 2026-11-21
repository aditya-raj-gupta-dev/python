
# 🐍 Snake Game — with Pygame

Classic Snake game made in *Python 3 + Pygame* — the player steers the snake to eat food, the snake grows, the score increases, and the game ends when it hits a wall or itself.

---

## 🎮 Demo / Gameplay
Action | Key
Snake Up | `↑` Arrow Key
Snake Down | `↓` Arrow Key
Snake Left | `←` Arrow Key
Snake Right | `→` Arrow Key
Restart (After Game Over) | `R`
Quit (After Game Over) | `Q`
Window Close | `X` Button
*Rules:*
- On eating food — *+10 Score* and *+1 Length*
- Hitting the wall → *Game Over*
- Hitting yourself → *Game Over*
- Immediate reverse move is not allowed (e.g. while moving Right, you cannot press Left)

---

## ✨ Features

- [x] 15 × 15 Grid (600 × 600 Window)
- [x] Snake as a list of coordinates — moves one cell at a time
- [x] Random food spawn — always inside the grid and outside the snake
- [x] Score + High Score HUD
- [x] Dynamic Speed — FPS increases as score increases (8 FPS → up to 20 FPS)
- [x] Wall Collision + Self Collision Detection
- [x] Game Over Overlay — with Final Score
- [x] Restart without closing the game — Press `R`

> *Note:* The problem statement mentioned a 10 × 10 grid (x and y from 0 to 9). In this implementation, for better gameplay, the grid is kept *15 × 15*. Logic, movement, scoring and collision — everything is same, only the play area is bigger.

---

## 🛠️ Tech Stack
Item | Details
**Language** | Python 3
**Library** | Pygame
**Concepts Used** | Loops, Lists, Coordinates, Game Loop, Event Handling, Collision Detection
---

## 📁 Project Structure
Snake-Game/
│
├── snake_game.py       # Main game file (entire game is in this one .py file)
└── README.md           # This file
---

## 🚀 How to Run

### 1. Install Python
Python 3.8+ is required. To check:
python --version
### 2. Install Pygame
pip install pygame
### 3. Run the Game
python snake_game.py
That's it! The game window will open. Play with arrow keys.

---

## 🧠 How It Works (Logic)
# Snake is a list — each element is an (x, y) coordinate
snake = [(7, 7)]

# In every frame:
# 1. Calculate new head according to direction
#    RIGHT -> x + 1, LEFT -> x - 1, UP -> y - 1, DOWN -> y + 1
# 2. If new head is outside the wall or inside the snake -> Game Over
# 3. Insert new head at front
# 4. If new head == food -> score += 10, do not remove tail (snake grows)
#    Else remove tail (snake stays same length)
# 5. Spawn new food at a random place (not on the snake)
Concept | Where It Is Used
**List** | To store the snake's body
**Tuple / Coordinates** | `(x, y)` position of each segment
**Loop** | Game loop + Grid draw + Snake draw
**Condition** | Collision, Food eaten, Reverse move block
**Random** | Food spawn
---

## 🧪 Test Cases (As Per Problem Statement)

The test cases in the problem statement were given assuming a 10 × 10 grid, start `(5, 5)` moving Right, and first food fixed at `(7, 5)`. This game follows the same logic.

### Test Case 1: Normal Input
Input | Expected Output
Moves: `R, R` | Head: `(6, 5)` → Food eaten at `(7, 5)`!
Score: `10` \| Length: `2` \| Head: `(7, 5)`
### Test Case 2: Boundary / Minimum Input
Input | Expected Output
Moves: `R, R, R, R, R` | Food eaten at `(7, 5)`! Score: `10`
Head: `(8, 5)`, then `(9, 5)`
Game Over! Wall hit at `(10, 5)`. Final Score: `10`
### Test Case 3: Invalid Input
Input | Expected Output
(a) Key: `X` | (a) Invalid key. Use R, L, U or D.
(b) Key: `L` (snake is moving Right) | (b) Reverse move not allowed. Snake continues Right.
> In this implementation arrow keys are used, so case `(a)` does not come from keyboard, and case `(b)` is blocked in code — by the `direction != opposite` check.

### Test Case 4: Different Valid Scenario
Input | Expected Output
Moves: `R, R, U, U` | Food eaten at `(7, 5)`! Score: `10`
Snake: `(7, 3), (7, 4)`
Length: `2` \| Head: `(7, 3)`
---

## ⚙️ Game Settings (You Can Change In Code)

Everything is controlled from the constants at the top of `snake_game.py`:
GRID_WIDTH  = 15      # Width of grid (in cells)
GRID_HEIGHT = 15      # Height of grid (in cells)
CELL_SIZE   = 40      # Size of each cell (in pixels)
# Speed: 8 + (score // 30) FPS, max 20 FPS
---

## 📝 Bare Minimum Requirements — Checklist

- [x] Solution in Python 3, in one `.py` file, with Pygame window
- [x] Snake stored as a list of coordinates, moves one cell at a time in game loop
- [x] Food generates randomly, on eating snake grows + score increases
- [x] Wall collision and self collision detected, shows Game Over + Final Score
- [x] Control with Arrow keys, immediate reverse move not allowed

---

## 👨‍💻 Author

*Aditya Raj Gupta*
B.Tech CSE

---

## 📄 License

This project is made for college assignment / learning purpose. Free to use and modify.
