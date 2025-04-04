# Sudoku
This Python project implements a 4x4 Sudoku-like board game that enforces three classic rule constraints: horizontal, vertical, and square uniqueness. The user is prompted to fill in the board one cell at a time, and the game checks for rule violations after each input until the board is successfully completed.

🔍 Features
1. ✅ Validates user input against horizontal, vertical, and 2x2 square rules

2. 🟩 Adds visual feedback by coloring accepted values green

3. ⌨️ Interactive gameplay: input row, column, and value (A–D)

4. 🎯 Ends only when all board cells are correctly filled

5. 🧠 Helpful error messages when rules are violated

🛠 Technologies Used
1. Python (core logic)

2. ANSI Escape Codes for terminal color formatting

3. 2D Lists for board structure and display

📌 Key Functions
1. horizontal_rule_violated(row, col, value)

2. vertical_rule_violated(row, col, value)

3. square_rule_violated(row, col, value)

4. all_cells_filled(board)

5. display_board(board)

6. board_filler(input)

🧪 How to Run
Run the script in any Python interpreter.

Input a valid 4x4 board as a 2D list when prompted.

Follow the instructions to input row, column, and a letter (A–D).

Fix rule violations if any appear. Keep going until you solve the puzzle!
