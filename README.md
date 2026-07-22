# 📈 Market Analyzer

A production-ready full-stack stock market analytics platform built using **FastAPI**, **Streamlit**, and **PostgreSQL**.

The application enables users to search stocks, analyze historical price movements, monitor technical indicators, manage personalized watchlists, and visualize market data through an interactive dashboard.

---

## Features

- JWT Authentication
- Secure User Registration & Login
- Dashboard with Market Overview
- Stock Search
- Detailed Stock Information
- Historical Price Charts
- Technical Indicators
- Personal Watchlist
- Company Information
- Responsive Streamlit UI
- PostgreSQL Database
- REST API using FastAPI

---

## Application Screenshots

### 🔑 Authentication & Entry

Onboarding interface for user authentication:

<p align="center">
  <img src="streamlit-app/assets/images/landing_page.png" width="800" alt="Landing Page">
</p>

### 📊 Interactive Dashboard

Market overview metrics and comprehensive analytical trends:

<p align="center">
  <img src="streamlit-app/assets/images/dashboard_full.png" width="800" alt="Full Dashboard View">
  <br><br>
  <img src="streamlit-app/assets/images/dashboard.png" width="800" alt="Dashboard Core Metrics">
</p>

### 🔍 Stock Search & Discovery

Finding assets and reviewing matches within the framework:

<p align="center">
  <img src="streamlit-app/assets/images/searchbox.png" width="800" alt="Search Component">
  <br><br>
  <img src="streamlit-app/assets/images/searchbox_with_output.png" width="800" alt="Search Results Interface">
</p>

### 📈 Stock Details & Analytics

Deep dives into charts, metrics, and parameters:

<p align="center">
  <img src="streamlit-app/assets/images/stock_details_1.png" width="800" alt="Stock Overview Metrics">
  <br><br>
  <img src="streamlit-app/assets/images/stock_details_2.png" width="800" alt="Historical Analysis Chart">
  <br><br>
  <img src="streamlit-app/assets/images/stock)details_3.png" width="800" alt="Technical Indicators Panel">
</p>

### ⭐ Watchlist & Settings

Tracking asset metrics and managing user context parameters:

<p align="center">
  <img src="streamlit-app/assets/images/watchlist.png" width="800" alt="User Watchlist Tracker">
  <br><br>
  <img src="streamlit-app/assets/images/settings.png" width="800" alt="User Settings Profile">
</p>

## Technology Stack

### Backend

- FastAPI
- PostgreSQL
- psycopg2
- JWT Authentication
- Passlib (bcrypt)
- Pydantic
- yfinance

### Frontend

- Streamlit
- Plotly
- Pandas
- Requests

---

## Project Structure

```text
Market-Analyzer/

app/
streamlit-app/
scripts/
tests/
README.md
```

---

## REST APIs

### Authentication

| Method | Endpoint           |
| ------ | ------------------ |
| POST   | `/sma/v1/signup` |
| POST   | `/sma/v1/login`  |
| GET    | `/sma/v1/me`     |

### Dashboard

| Method | Endpoint              |
| ------ | --------------------- |
| GET    | `/sma/v1/dashboard` |

### Search

| Method | Endpoint           |
| ------ | ------------------ |
| GET    | `/sma/v1/search` |

### Stocks

| Method | Endpoint                        |
| ------ | ------------------------------- |
| GET    | `/sma/v1/stocks/{symbol}`     |
| GET    | `/sma/v1/{symbol}/history`    |
| GET    | `/sma/v1/{symbol}/indicators` |

### Watchlist

| Method | Endpoint                |
| ------ | ----------------------- |
| GET    | `/watchlist`          |
| POST   | `/watchlist`          |
| DELETE | `/watchlist/{symbol}` |

---

## Installation

Clone the repository

```bash
git clone https://github.com/<username>/Market-Analyzer.git
```

```bash

pip install requirements.txt

Backend

```bash

uvicorn app.main:app --reload
```

Frontend

```bash
cd streamlit-app

streamlit run app.py
```

## Future Improvements

- Portfolio Tracking
- AI Stock Insights
- Email Alerts
- Real-time Streaming
- News Sentiment Analysis
- Price Prediction Models

---

## License

MIT License
