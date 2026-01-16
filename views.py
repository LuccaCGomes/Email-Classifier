from main import app

@app.route("/")
def start():
    return "está funcionando"