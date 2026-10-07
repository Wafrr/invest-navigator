from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Инвестиционный навигатор")

# Разрешаем запросы с фронтенда
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Инвестиционный навигатор API работает"}

@app.get("/api/measures")
def get_measures():
    return [
        {
            "id": 1,
            "name": "Грант на оборудование",
            "type": "Грант",
            "region": "Москва",
            "max_employees": 50,
            "sum": 5000000
        },
        {
            "id": 2,
            "name": "Субсидия на аренду",
            "type": "Субсидия",
            "region": "Татарстан",
            "max_employees": 100,
            "sum": 1000000
        },
    ]
