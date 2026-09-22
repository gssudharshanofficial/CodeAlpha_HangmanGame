# CodeAlpha: Hangman Game (Task 1)

A classic text-based **Hangman Game** built using Python. This project was developed as part of my Python Programming Internship at **CodeAlpha**.

## 📝 Project Overview
The objective of this task is to create a simple, interactive console game where the player attempts to guess a hidden word one letter at a time within a limited number of attempts.

### Key Features
* **Word Bank:** Randomly selects from a predefined list of programming terms (`python`, `codealpha`, `internship`, `programer`, `developer`).
* **Attempt Tracking:** Provides the user with exactly **6 incorrect attempts** before the game ends.
* **Input Validation:** Filters out multi-character inputs, numbers, and symbols.
* **State Memory:** Tracks and displays previously guessed letters to avoid redundant inputs.

## ⚙️ Core Concepts Used
* **`random` Module:** To choose a secret word from the list randomly.
* **Control Flow:** `while` loops for handling game iterations and `if-else` blocks for conditional logic.
* **Data Structures:** Lists for keeping track of guessed letters and strings for rendering the hidden word structure (`_ _ _`).

## 🎮 Sample Gameplay Example
Here is an example of how the game plays out directly inside the terminal window:

```text
====================================
      Welcome to Hangman Game!      
====================================
Try to guess the secret word.

Word to guess: _ _ _ _ _ _
Attempts left: 6
Guessed letters: None
Guess a letter : p

 Good job!!! 'p' is in the word.

Word to guess: p _ _ _ _ _
Attempts left: 6
Guessed letters: p
Guess a letter : z

 Oops!!! 'z' is not in the word.

Word to guess: p y _ _ _ _
Attempts left: 5
Guessed letters: p, z, y
Guess a letter : y

 Good job!!! 'y' is in the word.

```
