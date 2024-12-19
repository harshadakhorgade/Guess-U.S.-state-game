# U.S. State Guessing Game

## 🗺️ About the Project
The **U.S. State Guessing Game** is an interactive Python project built using the **Turtle Graphics** library and **Pandas**. The game displays a blank map of the United States, and players are challenged to correctly guess all 50 states. It's a fun and educational way to test your knowledge of U.S. geography!

---

## 🎮 How to Play
1. A map of the United States is displayed on the screen.
2. Players type the name of a U.S. state in the input box.
3. If the state is correct, it is marked on the map at its corresponding location.
4. The game continues until:
   - All 50 states are guessed, or
   - The player types "Exit" to end the game.

---

## 🚀 Features
- **Interactive Map**: Visual representation of the United States map.
- **State Tracking**: Displays guessed states on the map in real time.
- **Missed States Report**: If the game ends prematurely, a CSV file (`new_data.csv`) is generated with the names of the states the player missed.

---

## 📁 Files in the Project
- **`main.py`**: The main Python script for running the game.
- **`blank_states_img.gif`**: An image of the blank U.S. map used as the game background.
- **`50_states.csv`**: A dataset containing the names and coordinates of all 50 U.S. states.
- **`new_data.csv`**: A dynamically generated file containing the list of states missed during the game.

---

## 🛠️ Requirements
- **Python 3.6+**
- **Required Libraries**:
  - `turtle`
  - `pandas`

---

## 📦 Setup and Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/U.S.-state-game.git
   cd U.S.-state-game
   ```
2. Install the required Python libraries:
   ```bash
   pip install pandas
   ```
3. Run the game:
   ```bash
   python main.py
   ```
📸 Screenshots
Application Interface:
(image/Screenshot%202024-12-19%20215854.png)

   

Enjoy the game and see how many states you can guess correctly! 🌟
