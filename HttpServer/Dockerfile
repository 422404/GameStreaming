FROM python:3

WORKDIR /opt/app
COPY app/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["sh", "./start.sh"]
