# 📄 Credit Register App
Web application developed with **Python Flask**, **SQLite**, **HTML/CSS**, **JavaScript**, and **Chart.js** to register and visualize credits.

## 📑 Table of Contents

- [🚀 Objective](#-objective)
- [⚙️ Technologies used](#️-technologies-used)
- [📝 Instructions](#️-instructions)
- [🗂️ Architecture](#️-general-architecture)
- [🏛️ Data model](#️-data-model)
- [🔄 🧩 Main flow](#️-main-flow)
- [💻 Backend](#-backend--api-documentation)
- [🖥️ Frontend](#-frontend)
- [📊 Visualization](#-visualization)
- [📝 Notes](#-notes)
- [🤝 Contributions](#-contributions)
- [📄 License](#-license)

## 🚀 Objective
Allow users to register credits, store them in a SQLite database, and visualize total credits by charts.


## ⚙️ Technologies used

- Flask (backend/API)
- SQLite (database)
- SQLAlchemy (ORM)
- HTML, CSS, JavaScript (frontend)
- Chart.js (charts)

## 📝 Instructions

##  🗂️ General architecture
The application follows a  Model-View-Component (MVC)-like structure where:
- **Models** are represented with SQLite
- **Controllers** routes and manage API logic using Flask
- **Views** madden with HTML/CSS/JS

### 📌 Components diagram

![Components Diagram](https://github.com/Jesuszenro/credit-register/blob/main/images/components%20diagram.png)

## 🏛️ Data model

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

