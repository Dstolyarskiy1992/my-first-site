
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Мой сайт</title>
        <style>
            body {
                font-family: Arial;
                text-align: center;
                padding: 50px;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
            }
            h1 { font-size: 3em; }
        </style>
    </head>
    <body>
        <h1>🚀 Мой первый сайт на Python!</h1>
        <p>Сайт работает успешно!</p>
        <p>Создано за один день</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
