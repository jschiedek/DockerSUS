FROM python:3.12-slim

# Vytvoření neprivilegovaného systémového uživatele (Bonus 1)
RUN groupadd -r appuser && useradd -r -g appuser appuser

WORKDIR /app

# Instalace závislostí dříve kvůli efektivnímu využití Docker cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Kopírování zdrojových kódů
COPY app.py .

USER appuser

EXPOSE 8080

CMD ["python", "app.py"]
