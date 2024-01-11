
# Python Docker Environment

A minimalistic **Python Docker Environment** to start your project in __Docker__.

| ***Note** : For test purpose I install [FastAPI](https://fastapi.tiangolo.com/).


## Setup Instruction 

* Clone this repo to your local machine and go to your project directory.

```bash
cd my-project
```
* Build docker image
```bash
docker-compose up --build
docker-compose up --build -d [Optional: If you want to build in detach mode ]
```
| Notes: After successfull build verify API Route. Go through postman or your browser and hit on http://0.0.0.0:8000/ . In response you will get a very cool JSON Object of saying 
```json
{
    "message": "Hello World."
}
```

## Development Instruction 
Very first problem what you will get that no virtual environment and python intellisense work in your first setup so far and that's why we have to run this project in docker container.

* Extensions you need to install : **Docker**, **Dev Container**,  
* Open dialog box of remote machine clicking bottom left **Remot Window** button and select your container what you build previously.It will open **new window** of **VSCODE**.
* For the first time you may don't get intellisense support of python.If you don't get any support please install again **Python Extension** again . For this time install this extension inside your container. After that you don't need to install it again and again.
