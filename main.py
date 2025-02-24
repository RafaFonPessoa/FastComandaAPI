from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return 'API está funcionando! Em caso de duvida, use /docs.'

@app.get("/categorias")
def categories():
    pass