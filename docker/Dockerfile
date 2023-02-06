FROM python:3.9

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80

ADD app.py .

CMD python -m uvicorn app:app --host 0.0.0.0 --port 80
