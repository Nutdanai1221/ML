# syntax=docker/dockerfile:1
FROM python:3.9-slim

# install app dependencies
# RUN apt-get update && apt-get install -y python3 python3-pip

# RUN pip install numpy scikit-learn
WORKDIR /app

COPY . /app
# install app
RUN pip3 install -r requirement.txt
# final configuration

EXPOSE 600

CMD ["python3", "app.py"]