'''

Tutorial de execução: https://fastapi.tiangolo.com/tutorial/
run server: uvicorn app:app --reload

'''
#imports
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

import utils as ut
from pathlib import Path
import os
import subprocess
import time

#start
app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

timer = 1

#Rotas

#Função para testar se o servidor está em execução
@app.get("/")
def root():
    sum = ut.sum(2, 2)
    return {"message": "Servidor Rodando"}

#Função para enivar imagem gerada para o frontend
@app.get("/image")
async def get_image():
    cmd_str = "pyreverse -o png __init__.py"
    os.system(cmd_str)
    #time.sleep(timer)

    return FileResponse("classes.png")

#Função para eniar log para o frontend
@app.get("/log")
async def get_log():
    output = subprocess.getoutput("pyreverse -o png __init__.py")
    lines = str(output)
    lines = lines.replace('\n', '<br>')
    lines = lines.replace('Format png is not supported natively. Pyreverse will try to generate it using Graphviz...', '')
    lines = lines.replace('<br>parsing __init__.py...', '')
    print(lines)
    #time.sleep(timer)

    return lines

#Função para receber o gódigo e converter em python
@app.post("/recive_data")
def upload(file: UploadFile = File(...)):

    contents = file.file.read()

    with open(file.filename, 'wb') as f:
        f.write(contents)
    file.file.close()

    check_file = os.path.isfile('__init__.py')
    if not check_file:
        #Renomear arquivo para formato python
        os.rename('blob', '__init__.py')
    else:
        cmd_str = "del __init__.py"
        os.system(cmd_str)
        os.rename('blob', '__init__.py')
        
