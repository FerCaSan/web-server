# Web-server with fastapi and uvicorn

## Without docker

1. Create virtual enviorment
```sh
python3 -m venv env
```
2. Install modules
```sh
pip3 install -r requirements.txt
```
3. Run web server:
```sh
uvicorn main:app --reload
```
, where 'main' is the file with the app and 'reload' is to keep listening it .

4. To access localhost to show web

## With docker

1. Build docker
```sh
docker-compose build
```
2. Up docker
```sh
docker-compose up -d
```
3. To check docker
```sh
docker-compose ps
```




