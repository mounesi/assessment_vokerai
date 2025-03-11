# 🚀 Voker Burger backend

## 🛠️ Setup

### ✅ Requirements
- Python **3.11** (other Python 3.x versions should work as well)  
- [FastAPI](https://fastapi.tiangolo.com/) – already set up in `main.py`  
- [OpenAI Python Library](https://github.com/openai/openai-python) – for processing AI requests  

---

### 1️⃣ Create a Virtual Environment
Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate
```


###  2️⃣ Install Dependencies
Use pip to install all required dependencies:
`pip install -r requirements.txt`


### 3️⃣ Set Up OpenAI API Key
Create a .env file in the backend directory:
`touch backend/.env`

Add your Open API key to `.env`:
`OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`

### 4️⃣ Verify API Key is Loaded
To confirm the API key is loaded correctly:
`python backend/config.py`

expected output:

`Loaded OPENAI_API_KEY: sk-abc*****`


5️⃣ Run the Application
To start the FastAPI application:

`uvicorn backend.main:app --reload`

## Alternatively Use Poetry to run the application 
You can run the application from the root repository using the following:
Please ensure that the environment varialbes are properly exported.
`poetry run uvicorn backend.main:app --host 0.0.0.0 --port 8000 --reload`

## Testing the Endpoints
You can manually test the endpoints using curl:

Place an Order
```curl -X POST "http://127.0.0.1:8000/place_order/?tenant_id=test" \
-H "Content-Type: application/json" \
-d '{"message": "I want 2 burgers and 1 fries"}'
```

Cancel an order
```curl -X POST "http://127.0.0.1:8000/cancel_order/?tenant_id=test" \
-H "Content-Type: application/json" \
-d '{"message": "Cancel order #<ORDER ID>"}'
```


## Run Tests:
`pytest backend/tests`

## Backend Structure
assessment_vokerai
├── backend
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── services.py
│   ├── dependencies.py
│   ├── config.py
│   ├── .env
│   ├── README.md
│   ├── tests
│       ├── test_main.py
│       ├── test_openai.py
├── requirements.txt

