FROM python:3.7.4

COPY . /app
WORKDIR /app

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt


CMD streamlit run --server.port 8080 --server.enableCROS false app.py