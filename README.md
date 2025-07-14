# 📄 Credit Register App
Web application developed with **Python Flask**, **SQLite**, **HTML/CSS**, **JavaScript**, and **Chart.js** to register and visualize credits.

## 📑 Table of Contents

- [🚀 Objective](#-objective)
- [⚙️ Technologies used](#️-technologies-used)
- [📝 Instructions](#-instructions)
- [🕋 Architecture](#-architecture)
- [💎 Data model](#-data-model)
- [🧩 Main flow](#-main-flow)
- [💻 Backend](#-backend--api-documentation)


## 🚀 Objective
Allow users to register credits, store them in a SQLite database, and visualize total credits by charts.


## ⚙️ Technologies used

- Flask (backend/API)
- SQLite (database)
- SQLAlchemy (ORM)
- HTML, CSS, JavaScript (frontend)
- Chart.js (charts)

## 📝 Instructions
### 💻Instalation
1. Clone the repository

```
git clone https://github.com/your-user/credit-register.git
cd credit-register
```
2. Clone dependencies
```
pip install -r requirements.txt
```
3. Execute the app
```
python run.py
```
If execution doesn't work, initialize database instead and repeat step 4
```
python
>>> from app import db
>>> db.create_all()
>>> exit()
```
### ✅ ✨ Features

#### ✅ User-Friendly Interface
Modern and responsive design using HTML, CSS, and JavaScript, providing a smooth user experience.
![Main_page](https://github.com/Jesuszenro/credit-register/blob/main/images/main%20page.png)

#### ✅ Interactive Visualization
View a dynamic chart showing the total credits granted and a table of lastest credits.
![Chart](https://github.com/Jesuszenro/credit-register/blob/main/images/chart.png)

#### ✅ Register Credits
Users can register new credits using a simple form with fields for client name, amount, interest rate, term (months), and disbursement date. Basic form validations are included to ensure correct input.
![Register](https://github.com/Jesuszenro/credit-register/blob/main/images/register_credit.png)

#### ✅ View All Credits
View a table listing all registered credits. Users can easily review each credit's details at a glance.
![Credits](https://github.com/Jesuszenro/credit-register/blob/main/images/credits.png)

#### ✅ Edit and Delete Credits
Update existing credits directly from the table. Credits can also be deleted with a single click (with confirmation).
![Edit](https://github.com/Jesuszenro/credit-register/blob/main/images/edit_credit.png)
![Delete](https://github.com/Jesuszenro/credit-register/blob/main/images/delete_credit.png)
A upcoming message will be shown once the deletion is completed
![Delete_success](https://github.com/Jesuszenro/credit-register/blob/main/images/delete_successful.png)

⚠️ Note: The credits.db file included here is for demonstration purposes only. You can delete it and generate a new empty database by running db.create_all().


## 🕋 Architecture
The application follows a  Model-View-Component (MVC)-like structure where:
- **Models** are represented with SQLite
- **Controllers** routes and manage API logic using Flask
- **Views** madden with HTML/CSS/JS

### 📌 Components diagram

![Components Diagram](https://github.com/Jesuszenro/credit-register/blob/main/images/components%20diagram.png)

## 💎 Data model

### 💡 Class diagram

![Class Diagram](https://github.com/Jesuszenro/credit-register/blob/main/images/class%20diagram.png)

## 🧩 Main flow

### 🔄 Sequence diagram

Describes the flow for registering a credit:
![Sequence Diagram](https://github.com/Jesuszenro/credit-register/blob/main/images/sequence%20diagram.png)

## 💻 Backend — API Documentation
### ✅ Overview
This project was built using Flask and SQLite, following a REST API structure to provide CRUD operations for credits like registration, listing, udpating, and deletion.
It uses SQLAlchemy as the ORM to interact with the SQLite database.
| Column      | Type    | Description                  |
|--------------|---------|------------------------------|
| id           | Integer | Primary key, auto-increment |
| client      | String  | Client name                 |
| amount        | Float   | Credit amount              |
| interest_rate | Float   | Annual interest rate (%)   |
| term        | Integer | Term in months            |
| grant_day | String | Grant date (YYYY-MM-DD) |

### 🔄 Workflow
#### 1️. Database connection
When the app starts, it connects to the SQLite database (credits.db), which is defined and managed in the instance/ folder.

#### 2️. Models
The Credit model (defined in models/credit.py) describes the structure of each credit record, including fields like client name, amount, interest rate, term, and disbursement date.

#### 3️. Routing
The main routes (defined in controllers/app.py or app.py) handle:

Registering a new credit: Receives form data and saves it to the database.

Listing credits: Queries and displays all stored credits in a table view.

Editing credits: Updates existing records in the database.

Deleting credits: Removes selected records.

#### 4️. Validations and feedback
Flask's built-in features (like flash messages) are used to give users feedback after operations (e.g., "Credit added successfully!").
