FROM python:3.11-slim

ENV TZ=Europe/Madrid
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

WORKDIR /app

COPY requeriments.txt .
COPY newsTelegram.py .

RUN pip install --no-cache-dir -r requeriments.txt

CMD ["python", "-u", "newsTelegram.py"]