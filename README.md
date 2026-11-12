# 🐍 Snake Game

A classic Snake game built with Python and the `turtle` graphics library. Guide the snake to eat food and grow longer, without hitting the walls or yourself.

## 🎥 Demo



https://github.com/user-attachments/assets/e38b745e-83f0-4276-9793-9d6691573265







## How It Works

- The snake moves continuously in one direction until the player changes it.
- Each time the snake eats the food, it grows longer and the score increases.
- The game ends if the snake:
  - Collides with itself
  - Collides with the boundaries of the playing field

## Controls

| Key | Action |
| --- | ------ |
| ⬆️ Up | Move up |
| ⬇️ Down | Move down |
| ⬅️ Left | Move left |
| ➡️ Right | Move right |

## Project Structure

| File | Purpose |
| ---- | ------- |
| `main.py` | Runs the game loop and handles collisions |
| `snake.py` | Snake class: creating, moving, growing, and steering the snake |
| `food.py` | Food class: placing food at random positions |
| `scoreboard.py` | Scoreboard class: displaying the score and game over message |

## Run It Locally

1. Make sure Python 3 is installed (the `turtle` library comes with it).
2. Clone the repository:
   ```bash
   git clone https://github.com/christine-osama/snake-game.git
   cd snake-game
   ```
3. Run the game:
   ```bash
   python main.py
   ```

## Concepts Practiced

- Object-oriented programming (classes and objects across multiple files)
- Game loops and screen updates with `turtle`
- Keyboard event handling
- Collision detection
- Working with modules and project structure

## About

Built while learning Python as a beginner project.
