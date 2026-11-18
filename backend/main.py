from datetime import date
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy import Column, Date, Integer, String, Text, create_engine, select
from sqlalchemy.orm import declarative_base, Session
import os
from scoring import score, split

DB_URL = os.getenv("DATABASE_URL", "postgresql+psycopg2://postgres:postgres@localhost/invest_navigator")
engine = create_engine(DB_URL)
Base = declarative_base()

class Measure(Base):
    __tablename__ = "measures"
    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    operator = Column(String(200))
    goal = Column(String(50))
    forms = Column(String(100), default="")      # ИП,ООО,Самозанятый ("" = любые)
    stages = Column(String(100), default="")     # Идея,Запуск,Рост
    okved = Column(String(50), default="")       # разделы A–S
    regions = Column(Text, default="")
    max_sum = Column(Integer, default=0)
    description = Column(Text)
    valid_until = Column(Date)

# name, operator, goal, forms, stages, okved, regions, sum, description
SEED = [
 ("Налог на профессиональный доход","ФНС России","Налоги","Самозанятый","","","",0,"Ставка 4–6% без отчётности и взносов."),
 ("Налоговые каникулы для ИП","Региональные власти","Налоги","ИП","Запуск","","Татарстан,Краснодарский край,Свердловская область",0,"Нулевая ставка налога в первые два года."),
 ("Патентная система налогообложения","ФНС России","Налоги","ИП","","","",0,"Фиксированная стоимость патента вместо налога."),
 ("Пониженные страховые взносы для МСП","ФНС России","Налоги","ИП,ООО","","","",0,"Сниженный тариф взносов на выплаты свыше МРОТ."),
 ("Льготное кредитование МСП","Корпорация МСП и банки","Финансирование","ИП,ООО","Запуск,Рост","","",100000000,"Кредит по ставке до 15% на развитие бизнеса."),
 ("Поручительства для МСП","Корпорация МСП, гарантийные фонды","Финансирование","ИП,ООО","Запуск,Рост","","",25000000,"Поручительство вместо залога."),
 ("Микрозаймы региональных фондов","Региональные МФО","Финансирование","ИП,ООО,Самозанятый","","","",5000000,"Быстрый заём на пополнение оборотных средств."),
 ("Социальный контракт на бизнес","Органы соцзащиты","Финансирование","ИП,Самозанятый","Идея,Запуск","","",350000,"Выплата на старт бизнеса малоимущим гражданам."),
 ("Грант «Мой бизнес» начинающим","Центры «Мой бизнес»","Финансирование","ИП,ООО","Идея,Запуск","","Москва,Санкт-Петербург,Татарстан,Новосибирская область",500000,"Безвозмездная часть расходов на старт."),
 ("Грант «Старт»","Фонд содействия инновациям","Инновации","ООО","Идея,Запуск","J,M,C","",4000000,"Финансирование технологических стартапов."),
 ("Льготный лизинг оборудования","Корпорация МСП, лизинговые компании","Оборудование","ИП,ООО","Запуск,Рост","C,A,F,H","",50000000,"Лизинг со сниженным удорожанием."),
 ("Аренда госимущества","Региональные власти","Помещение","ИП,ООО","","","Москва,Санкт-Петербург,Татарстан",0,"Помещения по льготной арендной ставке."),
 ("Центр поддержки экспорта","РЭЦ","Экспорт","ИП,ООО","Рост","C,A,J","",3000000,"Компенсация затрат на выход на зарубежные рынки."),
 ("Закупки крупных заказчиков у МСП","Корпорация МСП","Продажи","ИП,ООО","Запуск,Рост","","",0,"Доступ к закупкам госкомпаний."),
 ("Обучение центров «Мой бизнес»","Центры «Мой бизнес»","Обучение","","Идея,Запуск","","",0,"Бесплатные курсы и консультации."),
 ("Агростартап","Региональные органы АПК","Финансирование","ИП","Идея,Запуск","A","",6000000,"Грант на развитие фермерского хозяйства."),
 ("Резидентство в ТОР","Минвостокразвития","Налоги","ООО","","","Приморский край",0,"Пониженные налоги и взносы для резидентов."),
 ("Резидентство в Сколково","Фонд «Сколково»","Инновации","ООО","Запуск,Рост","J,M","",0,"Налоговые льготы и гранты для технологических компаний."),
]

app = FastAPI(title="Инвестиционный навигатор")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

@app.on_event("startup")
def init():
    Base.metadata.create_all(engine)
    with Session(engine) as s:
        if not s.scalar(select(Measure.id).limit(1)):
            s.add_all(Measure(name=a, operator=b, goal=c, forms=d, stages=e, okved=f, regions=g,
                              max_sum=h, description=i, valid_until=date(2027, 12, 31)) for a,b,c,d,e,f,g,h,i in SEED)
            s.commit()

def dump(m, extra=None):
    return {"id": m.id, "name": m.name, "operator": m.operator, "goal": m.goal, "max_sum": m.max_sum,
            "description": m.description, "regions": split(m.regions), "valid_until": str(m.valid_until), **(extra or {})}

@app.get("/api/meta")
def meta():
    return {"forms": ["ИП","ООО","Самозанятый"], "stages": ["Идея","Запуск","Рост"],
            "goals": sorted({m[2] for m in SEED}),
            "regions": ["Москва","Санкт-Петербург","Татарстан","Свердловская область","Краснодарский край",
                        "Новосибирская область","Приморский край","Ленинградская область"]}

@app.get("/api/measures")
def measures(q: str = "", goal: str = ""):
    with Session(engine) as s:
        rows = s.scalars(select(Measure)).all()
    return [dump(m) for m in rows if q.lower() in (m.name + m.description).lower() and (not goal or m.goal == goal)]

class Profile(BaseModel):
    form: str = "ИП"
    stage: str = "Запуск"
    region: str = "Москва"
    okved: str = ""
    goals: list[str] = []

@app.post("/api/recommend")
def recommend(p: Profile):
    """Все меры с баллами; подходящие — сверху. Нужен и для сценария «а что если»."""
    with Session(engine) as s:
        rows = s.scalars(select(Measure)).all()
    res = [dump(m, score(m, p.model_dump())) for m in rows]
    return sorted(res, key=lambda r: (not r["eligible"], -r["score"], len(r["blockers"])))


# ---------- Пользователи, профиль, заявки ----------
import hashlib, json, secrets
from datetime import datetime
from fastapi import Depends, Header, HTTPException
from sqlalchemy import DateTime, ForeignKey

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String(200), unique=True, nullable=False)
    pwd = Column(String(200), nullable=False)       # соль$pbkdf2-хэш
    token = Column(String(64), index=True)
    profile = Column(Text)                          # JSON анкеты

class Application(Base):
    __tablename__ = "applications"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    measure_id = Column(Integer, ForeignKey("measures.id"))
    status = Column(String(30), default="Новая")
    created = Column(DateTime, default=datetime.utcnow)

def hash_pwd(p, salt=None):
    salt = salt or secrets.token_hex(8)
    return salt + "$" + hashlib.pbkdf2_hmac("sha256", p.encode(), salt.encode(), 100_000).hex()

def current_user(authorization: str = Header(default="")):
    tok = authorization.removeprefix("Bearer ").strip()
    with Session(engine) as s:
        u = s.scalar(select(User).where(User.token == tok)) if tok else None
    if not u:
        raise HTTPException(401, "Нужно войти")
    return u

class Cred(BaseModel):
    email: str
    password: str

def issue(s, u):
    u.token = secrets.token_hex(24); s.commit()
    return {"token": u.token, "email": u.email}

@app.post("/api/auth/register")
def register(c: Cred):
    if "@" not in c.email or len(c.password) < 6:
        raise HTTPException(422, "Укажите e-mail и пароль от 6 символов")
    with Session(engine) as s:
        if s.scalar(select(User).where(User.email == c.email.lower())):
            raise HTTPException(409, "Этот e-mail уже зарегистрирован")
        u = User(email=c.email.lower(), pwd=hash_pwd(c.password)); s.add(u); s.flush()
        return issue(s, u)

@app.post("/api/auth/login")
def login(c: Cred):
    with Session(engine) as s:
        u = s.scalar(select(User).where(User.email == c.email.lower()))
        if not u or hash_pwd(c.password, u.pwd.split("$")[0]) != u.pwd:
            raise HTTPException(401, "Неверный e-mail или пароль")
        return issue(s, u)

@app.get("/api/profile")
def get_profile(u=Depends(current_user)):
    return json.loads(u.profile) if u.profile else None

@app.put("/api/profile")
def put_profile(p: Profile, u=Depends(current_user)):
    with Session(engine) as s:
        s.get(User, u.id).profile = p.model_dump_json(); s.commit()
    return p

@app.post("/api/applications")
def apply(measure_id: int, u=Depends(current_user)):
    with Session(engine) as s:
        if s.scalar(select(Application.id).where(Application.user_id == u.id, Application.measure_id == measure_id)):
            raise HTTPException(409, "Заявка на эту меру уже подана")
        s.add(Application(user_id=u.id, measure_id=measure_id)); s.commit()
    return {"ok": True}

@app.get("/api/applications")
def my_apps(u=Depends(current_user)):
    with Session(engine) as s:
        rows = s.execute(select(Application, Measure).join(Measure, Measure.id == Application.measure_id)
                         .where(Application.user_id == u.id).order_by(Application.id.desc())).all()
    return [{"id": a.id, "status": a.status, "created": a.created.strftime("%d.%m.%Y"), "measure": m.name,
             "operator": m.operator, "max_sum": m.max_sum} for a, m in rows]
