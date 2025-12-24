# FDM – Football Database Model

FDM (Football Database Model) is a simple and efficient web application built with the **Django** framework to manage a football database.  
This project was developed as a hands-on exercise to practice and implement **CRUD (Create, Read, Update, Delete)** operations in a real-world scenario.

---

## 🚀 Features

The application provides the following core functionalities:

- **Add New Player**  
  Register basic player information such as first name, last name, age, and height.

- **Add Player Stats**  
  Record performance statistics for each player, including team, position, goals, and rating.

- **Unified Dashboard**  
  Display a complete list of all players along with their corresponding stats on a single, user-friendly page.

- **Edit Information**  
  Update the details of existing players and their statistics.

- **Delete Records**  
  Remove players or specific stat entries from the database with confirmation.

---

## 🛠️ Tech Stack

- **Backend:** Python, Django  
- **Frontend:** HTML, CSS  
- **Database:** PostgreSQL (configurable in `settings.py`)

---

## 📦 Project Structure

The project contains a single Django app named **`players`**, which handles the core logic.

### Data Models (`models.py`)

Two primary models are used for data persistence:

#### Player
Stores personal information about a player:
- `fname` – First Name  
- `lname` – Last Name  
- `age` – Age  
- `height` – Height  

#### Stats
Stores performance-related statistics for a player:
- `player` – ForeignKey relation to `Player`  
- `position` – Player's field position  
- `team` – Player's team  
- `goals` – Total goals scored  
- `rating` – Performance rating  

---

## 🧠 Views (`views.py`)

Function-Based Views are used to handle all CRUD operations:

- **Create:**  
  - `PlayerFormView`  
  - `StatsFormView`

- **Read:**  
  - `showView`

- **Update:**  
  - `PlayersUpdateView`  
  - `StatsUpdateView`

- **Delete:**  
  - `PlayerDeleteView`  
  - `StatsDeleteView`

---

## 🎨 Templates

- `show.html` – Main dashboard displaying all players and their stats  
- `player.html` – Form for adding or editing player information  
- `stats.html` – Form for adding or editing player statistics  
- `confirmation.html` – Confirmation page for delete actions  

---

## ⚙️ Installation and Setup

Follow these steps to run the project locally:

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Alirezadn7/FDM.git
cd FDM
