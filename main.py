"Principal para ejeucicion de servidor web"

import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

#Aplication Instance 
app = FastAPI()

@app.get('/')
def get_list():
    return [1, 2, 3]

@app.get('/contact')
def get_info():
    return {'name': 'FerCaSan'}

#Response with HTML
@app.get('/contacthtml', response_class=HTMLResponse)
def get_info_html():
    return """
        <h1>Hi!!</h1>
        <p>Here you are, in a web page</p>
    """


def run():
    store.get_categories()

if __name__ == '__main__':
    run()
