FROM svizor/zoomcamp-model:3.11.5-slim

WORKDIR /app

RUN pip install pipenv && pipenv install waitress flask scikit-learn==1.5.2 numpy pandas

COPY ["model1.bin", "dv.bin", "./"]
COPY ["load.py", "./"]

EXPOSE 9696

CMD ["pipenv", "run", "waitress-serve", "--listen=0.0.0.0:9696", "load:app"]
