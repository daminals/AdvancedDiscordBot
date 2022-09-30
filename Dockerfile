FROM python:3.7
WORKDIR /example
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 80
COPY . .
CMD ["python", "bot.py"]