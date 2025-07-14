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

#### ✅ Register Credits
Users can register new credits using a simple form with fields for client name, amount, interest rate, term (months), and disbursement date. Basic form validations are included to ensure correct input.

#### ✅ View All Credits
View a table listing all registered credits. Users can easily review each credit's details at a glance.

#### ✅ Edit and Delete Credits
Update existing credits directly from the table. Credits can also be deleted with a single click (with confirmation).

#### ✅ Interactive Visualization
View a dynamic chart showing the total credits granted.
(Optional: distribution by client or by amount ranges can also be displayed.)

#### ✅ User-Friendly Interface
Modern and responsive design using HTML, CSS, and JavaScript, providing a smooth user experience.

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

### 💻 API Endpoints
#### 🟢 Create credit
- Method: POST
- URL: /credit
- Body example (JSON):
```json
{
  "client": "Juan Pérez",
  "amount": 5000,
  "interest_rate": 12.5,
  "term": 12,
  "grant_day": "2025-07-09"
}
```
Response example
```
{
  'message': 'Credit registered successfully!'
}
```
#### 🔵 Get all credits
- Method: GET
- URL: /creditos
- Response example:
```json
[
  {
    "id": 1,
    "client": "Juan Pérez",
    "amount": 5000,
    "interest_rate": 12.5,
    "term": 12,
    "grant_day": "2025-07-09"
  }
]
```
#### 🟠 Update credit
- Method: PUT
- URL: /creditos/{id}
- Body example (JSON):
```json
{
  "client": "John",
  "amount": 5500
}
```
Response example:

```json
{
  'message': 'Credit updated successfully!'
}
```
#### 🔴 Delete credit
- Method: DELETE
- URL: /creditos/{id}
- Response example:
```json
{
  'message': 'Credit deleted successfully!'
}
```

