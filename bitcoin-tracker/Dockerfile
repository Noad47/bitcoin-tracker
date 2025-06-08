FROM python:3.10
WORKDIR /app
COPY . .
ENV PYTHONUNBUFFERED=1
RUN pip install -r requirements.txt
CMD ["python", "bitcoin_tracker.py"]
