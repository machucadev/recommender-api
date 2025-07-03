# 🧠 Product Recommender API
***
An intelligent and lightweight API that recommends products based on user purchase history. Built with **FastAPI**, ready for deployment and monetization via **RapidAPI**.

---

## 🚀 Features
***
- Create and store product data
- Generate product recommendations based on shared categories
- Fast, asynchronous API using FastAPI
- Ready for real-world usage and commercial integration

---

## 📦 Tech Stack
***
- Python 3.11+
- FastAPI
- SQLite (can be upgraded to PostgreSQL)
- SQLAlchemy
- scikit-learn & pandas (future smart recommendations)

---

## ⚙️ Installation

1. **Clone the repository**:

```bash
python -m venv venv

source venv/bin/activate  # or venv\Scripts\activate on Windows
```


---
## Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```


---
## Install dependencies:
```bash
pip install -r requirements.txt
```

---
## Run the API:
```bash
uvicorn app.main:app --reload
```


---
## 🔌 API Endpoints

### POST /products/
Create a new product.

Request Body:

```bash
{
  "name": "Wireless Headphones",
  "category": "Electronics",
  "description": "Noise-cancelling Bluetooth headphones"
}
```
***

### GET /products/
Returns a list of all stored products.

***
### POST /recommendations/
Returns product recommendations based on one or more product IDs.

Request Body:
```bash
{
  "product_ids": [1, 4]
}
```

Response:

```bash
{
  "recommended": [
    {
      "id": 2,
      "name": "Mechanical Keyboard",
      "category": "Electronics",
      "description": "RGB backlit keyboard with blue switches"
    }
  ]
}
```

📄 License
This project is licensed under the MIT License.

📬 Contact
Made with ❤️ by Santiago Machuca
📧 santi.machuca@gmail.com

