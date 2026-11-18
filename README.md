# Инвестиционный навигатор

Подбор мер поддержки МСП по профилю проекта. Стек: Vue 3 + FastAPI + PostgreSQL.

## Запуск
```bash
# backend (БД invest_navigator должна существовать)
cd backend && python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
export DATABASE_URL=postgresql+psycopg2://USER:PASS@localhost/invest_navigator
uvicorn main:app --reload        # http://localhost:8000/docs

# frontend
cd frontend && npm install && npm run dev
```
Таблицы (меры, пользователи, заявки) и 18 мер создаются при первом запуске backend.
