FROM python:3

EXPOSE 80

# Avoid user input prompts during installs
ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /opt/app
COPY app/requirements.txt .

RUN apt update && apt -y install nginx
RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["sh", "./start.sh"]
