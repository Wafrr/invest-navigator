"""Подбор мер: жёсткие фильтры + баллы Б = 40 + 30·Ц + 10·(Ф + С + О + Р)."""
from datetime import date

OKVED_RANGES = [("A",1,3),("B",5,9),("C",10,33),("D",35,35),("E",36,39),("F",41,43),("G",45,47),
    ("H",49,53),("I",55,56),("J",58,63),("K",64,66),("L",68,68),("M",69,75),("N",77,82),
    ("O",84,84),("P",85,85),("Q",86,88),("R",90,93),("S",94,96)]

def okved_section(code: str):
    try:
        n = int(code.strip()[:2])
    except ValueError:
        return None
    return next((s for s, a, b in OKVED_RANGES if a <= n <= b), None)

def split(v: str):
    return [x for x in (v or "").split(",") if x]

def score(m, p: dict):
    """Возвращает баллы, причины подбора и «чего не хватает» (blockers)."""
    sec, goals = okved_section(p.get("okved", "")), set(p.get("goals", []))
    checks = [("form", "форма деятельности", p.get("form"), split(m.forms)),
              ("stage", "стадия проекта", p.get("stage"), split(m.stages)),
              ("okved", "раздел ОКВЭД", sec, split(m.okved)),
              ("region", "регион", p.get("region"), split(m.regions))]
    blockers, reasons, pts = [], [], 40
    if m.valid_until and m.valid_until < date.today():
        blockers.append({"field": "date", "text": "срок действия меры истёк"})
    for key, label, val, allowed in checks:
        if not allowed:
            continue
        if val in allowed:
            pts += 10
            reasons.append(f"{label}: подходит")
        else:
            blockers.append({"field": key, "text": f"{label} — нужно: {', '.join(allowed)}"})
    if m.goal in goals:
        pts += 30
        reasons.append(f"совпадает с целью «{m.goal}»")
    return {"score": min(pts, 100), "eligible": not blockers, "reasons": reasons, "blockers": blockers}
