# CodeAlpha: Hangman Game (Task 1)

A classic text-based **Hangman Game** built using Python. This project was developed as part of my Python Programming Internship at **CodeAlpha**.

## 📝 Project Overview
The objective of this task is to create a simple, interactive console game where the player attempts to guess a hidden word one letter at a time within a limited number of attempts.

### Key Features
* **Word Bank:** Randomly selects from a predefined list of programming terms (`python`, `codealpha`, `internship`, `program`, `developer`).
* **Attempt Tracking:** Provides the user with exactly **6 incorrect attempts** before the game ends.
* **Input Validation:** Filters out multi-character inputs, numbers, and symbols.
* **State Memory:** Tracks and displays previously guessed letters to avoid redundant inputs.

## ⚙️ Core Concepts Used
* **`random` Module:** To choose a secret word from the list randomly.
* **Control Flow:** `while` loops for handling game iterations and `if-else` blocks for conditional logic.
* **Data Structures:** Lists for keeping track of guessed letters and strings for rendering the hidden word structure (`_ _ _`).
