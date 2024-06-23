# Tic-Tac-Toe Game

This project is a simple Tic-Tac-Toe game implemented in Python using the Pygame library. The player can choose to play as X or O against an AI opponent. The AI uses the minimax algorithm to make optimal moves.
## Table of Contents

    Features
    Installation
    Usage
    Game Rules
    Code Structure
    Credits

## Features

    Choose to play as X or O.
    AI opponent using the minimax algorithm.
    Graphical interface using Pygame.
    Display of game status (e.g., player's turn, game over, winner).

# Installation
## Prerequisites

    Python 3.12 or higher
    Pygame library

## Setup

  Clone the repository:
  
      git clone https://github.com/yourusername/tictactoe.git
      cd tictactoe

  Create and activate a virtual environment (recommended):

    python -m venv venv
  ## On Windows
    .\venv\Scripts\activate
  ## On macOS/Linux
    source venv/bin/activate

Install the required packages:

    pip install -r requirements.txt

Run the patch script (if using Python 3.12):

    python patch_pkg_resources.py

## Usage

  Run the game:
  
    python runner.py

  Follow the on-screen instructions:
  
        Choose to play as X or O.
        Click on the tiles to make your move.
        The game will display the current status and declare the winner or a tie at the end.

## Game Rules

    The game is played on a 3x3 grid.
    Players take turns to place their marker (X or O) on an empty cell.
    The first player to get three of their markers in a row (horizontally, vertically, or diagonally) wins.
    If all cells are filled and no player has three in a row, the game is a tie.

## Code Structure

    runner.py: Main script to run the game.
    tictactoe.py: Contains the game logic, including the minimax algorithm for the AI.
    one.py: Script to patch the pkg_resources module for compatibility with Python 3.12.
    requirements.txt: List of required Python packages.
    OpenSans-Regular.ttf: Font file used in the game.

## Credits

    Pygame: The game library used for the graphical interface.
    
