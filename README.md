# Organizzare Back-end
## Description 
This is my first backend API. The main objective is make easier the work of apartement managers. In this API you will find management of bills sources. In this project I used Docker, Postgres, Flask and JWT.
## How to
To prepare enviroment execute

```
docker-compose build
docker-compose up
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

To run execute

```
python organizzare-back/app/main.py 
```

After access the port http://127.0.0.1:5000/