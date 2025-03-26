FROM python:3.9-slim

WORKDIR /app

COPY app/requirements.txt .
RUN pip install --no-cache-dir --force-reinstall -r requirements.txt && \
    rm -rf requirements.txt

COPY app/ .

EXPOSE 7890

CMD ["python", "main.py"]