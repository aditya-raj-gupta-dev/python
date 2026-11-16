# 🐍 Snake Game — with Pygame

Classic Snake game made in **Python 3 + Pygame** — player snake ko steer karke food khilata hai, snake grow hota hai, score badhta hai, aur game wall ya khud se takrane par over ho jata hai.

---

## 🎮 Demo / Gameplay

| Action | Key |
| :--- | :--- |
| Snake Up | `↑` Arrow Key |
| Snake Down | `↓` Arrow Key |
| Snake Left | `←` Arrow Key |
| Snake Right | `→` Arrow Key |
| Restart (Game Over ke baad) | `R` |
| Quit (Game Over ke baad) | `Q` |
| Window Close | `X` Button |

**Rules:**
- Food khane par **+10 Score** aur **+1 Length**
- Wall se takrao → **Game Over**
- Khud se takrao → **Game Over**
- Immediate reverse move allowed nahi hai (e.g. Right jaate hue Left nahi dab sakta)

---

## ✨ Features

- [x] 15 × 15 Grid (600 × 600 Window)
- [x] Snake as list of coordinates — ek cell at a time move hota hai
- [x] Random food spawn — hamesha grid ke andar aur snake ke bahar
- [x] Score + High Score HUD
- [x] Dynamic Speed — score badhne par FPS badhta hai (8 FPS → 20 FPS tak)
- [x] Wall Collision + Self Collision Detection
- [x] Game Over Overlay — Final Score ke saath
- [x] Sound Effects — `eat.wav` (food khane par) aur `game_over.wav` (game over par)
- [x] Restart without game band kiye — `R` dabao

> **Note:** Problem statement me grid 10 × 10 (x aur y 0 se 9 tak) bola gaya tha. Is implementation me better gameplay ke liye grid **15 × 15** rakha gaya hai. Logic, movement, scoring aur collision — sab same hai, bas play area bada hai.

---

## 🛠️ Tech Stack

| Cheez | Details |
| :--- | :--- |
| **Language** | Python 3 |
| **Library** | Pygame |
| **Concepts Used** | Loops, Lists, Coordinates, Game Loop, Event Handling, Collision Detection |

---

## 📁 Project Structure

```
Snake-Game/
│
├── snake_game.py       # Main game file (poora game isi ek .py file me hai)
├── README.md           # Ye file
├── eat.wav             # (Optional) Food khane ki sound
└── game_over.wav       # (Optional) Game Over ki sound
```

> Agar `eat.wav` / `game_over.wav` folder me nahi honge, to game bina sound ke chalega — warning print hogi, crash nahi hoga.

---

## 🚀 How to Run

### 1. Python Install Karo
Python 3.8+ chahiye. Check karne ke liye:

```bash
python --version
```

### 2. Pygame Install Karo

```bash
pip install pygame
```

### 3. Game Run Karo

```bash
python snake_game.py
```

Bas! Game window khul jayegi. Arrow keys se khelo.

---

## 🧠 How It Works (Logic)

```python
# Snake ek list hai — har element ek (x, y) coordinate hai
snake = [(7, 7)]

# Har frame me:
# 1. Direction ke hisaab se naya head calculate karo
#    RIGHT -> x + 1, LEFT -> x - 1, UP -> y - 1, DOWN -> y + 1
# 2. Agar naya head wall ke bahar hai ya snake ke andar hai -> Game Over
# 3. Naya head aage insert karo
# 4. Agar naya head == food -> score += 10, tail mat hatao (snake bada)
#    Warna tail pop karo (snake same length)
# 5. Naya food random jagah spawn karo (snake wali jagah par nahi)
```

| Concept | Kahan Use Hua |
| :--- | :--- |
| **List** | Snake ki body store karne ke liye |
| **Tuple / Coordinates** | Har segment ki `(x, y)` position |
| **Loop** | Game loop + Grid draw + Snake draw |
| **Condition** | Collision, Food eaten, Reverse move block |
| **Random** | Food spawn |

---

## 🧪 Test Cases (Problem Statement ke Hisaab Se)

Problem statement ke test cases 10 × 10 grid, start `(5, 5)` moving Right, pehla food `(7, 5)` par fixed maan kar diye gaye the. Ye game usi logic ko follow karta hai.

### Test Case 1: Normal Input

| Input | Expected Output |
| :--- | :--- |
| Moves: `R, R` | Head: `(6, 5)` → Food eaten at `(7, 5)`! <br> Score: `10` \| Length: `2` \| Head: `(7, 5)` |

### Test Case 2: Boundary / Minimum Input

| Input | Expected Output |
| :--- | :--- |
| Moves: `R, R, R, R, R` | Food eaten at `(7, 5)`! Score: `10` <br> Head: `(8, 5)`, then `(9, 5)` <br> Game Over! Wall hit at `(10, 5)`. Final Score: `10` |

### Test Case 3: Invalid Input

| Input | Expected Output |
| :--- | :--- |
| (a) Key: `X` | (a) Invalid key. Use R, L, U or D. |
| (b) Key: `L` (snake is moving Right) | (b) Reverse move not allowed. Snake continues Right. |

> Is implementation me arrow keys use hote hain, isliye `(a)` wala case keyboard se aata hi nahi, aur `(b)` wala case code me block hai — `direction != opposite` check se.

### Test Case 4: Different Valid Scenario

| Input | Expected Output |
| :--- | :--- |
| Moves: `R, R, U, U` | Food eaten at `(7, 5)`! Score: `10` <br> Snake: `(7, 3), (7, 4)` <br> Length: `2` \| Head: `(7, 3)` |

---

## ⚙️ Game Settings (Code me Badal Sakte Ho)

`snake_game.py` ke upar wale constants se sab control hota hai:

```python
GRID_WIDTH  = 15      # Grid ki chaudai (cells me)
GRID_HEIGHT = 15      # Grid ki lambai (cells me)
CELL_SIZE   = 40      # Har cell kitna bada (pixels me)
# Speed: 8 + (score // 30) FPS, max 20 FPS
```

---

## 📝 Bare Minimum Requirements — Checklist

- [x] Solution Python 3 me, ek `.py` file me, Pygame window ke saath
- [x] Snake ko coordinates ki list ke roop me store kiya, game loop me ek cell at a time move
- [x] Food randomly generate hota hai, khane par snake grow + score badhta hai
- [x] Wall collision aur self collision detect karke Game Over + Final Score dikhata hai
- [x] Arrow keys se control, immediate reverse move allowed nahi

---

## 👨‍💻 Author

**Aditya**
B.Tech CSE

---

## 📄 License

Ye project college assignment / learning purpose ke liye banaya gaya hai. Free to use aur modify karo.
