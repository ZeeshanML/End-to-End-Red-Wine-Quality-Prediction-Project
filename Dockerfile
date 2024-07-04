FROM python:3.10.0-slim-buster

RUN apt update -y && apt install awscli -y
WORKDIR /app

COPY . /app

# Install any needed packages specified in requirements.txt
# First, update and install git
RUN apt-get update && apt-get install -y git

RUN pip install -r requirements.txt

CMD ["python3", "app.py"]