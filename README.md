# Tic-Tac-Toe with Alpha-Beta Pruning

This project is a Tic-Tac-Toe game developed with an AI opponent that uses the Alpha-Beta pruning algorithm for optimal gameplay. The game is built using Python, with key logic for the AI opponent in `alpha_beta.py`. The UI is built with Kivy, utilizing `.kv` files to define the layout and design.

## Features

- **Human vs AI Gameplay**: Play Tic-Tac-Toe against an AI opponent that always chooses the best moves, making the game more challenging.
- **Alpha-Beta Pruning**: The AI employs the Alpha-Beta pruning algorithm to minimize the search time and maximize efficiency, resulting in a quick response time even when running on limited hardware.
- **Customizable UI**: The game interface is developed using Kivy, providing a smooth and visually appealing design that’s customizable.

## Files and Structure

- **`main.py`**: The main script that initializes and runs the game. It connects the game interface with the AI logic and handles player interactions.
- **`alpha_beta.py`**: This file contains the AI implementation using the Alpha-Beta pruning algorithm. It includes the logic for evaluating game states and selecting optimal moves.
- **`.kv file`**: Defines the graphical layout and design of the game using Kivy’s language, allowing customization of the interface.

## Requirements

- **Python 3.x**
- **Kivy**: For graphical interface and game layout.

To install Kivy, run:
```bash
pip install kivy
```

## How to Play

1. Clone this repository to your local machine.
2. Install the dependencies.
3. Run the game with the following command:
   ```bash
   python main.py
   ```
4. The game will launch, allowing you to play Tic-Tac-Toe against the AI. Simply click on the grid to make your move.

## Game Logic Overview

The AI in this game uses Alpha-Beta pruning, a refined version of the Minimax algorithm, which helps the AI make optimal moves by reducing the number of possible moves it needs to evaluate. This makes the AI’s decisions faster without compromising its ability to play optimally.

## Customization

You can modify the `.kv` file to change the UI layout, colors, and styles to suit your preference. The AI difficulty and other game parameters can be adjusted within `alpha_beta.py`.

## Contributing

Feel free to fork this repository, make improvements, and create pull requests. Contributions are welcome!

## License

This project is open-source and available under the MIT License.

---

Enjoy the challenge of facing off against a strategic AI in this classic game of Tic-Tac-Toe!
