from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Sistema de Gerenciamento de Biblioteca"

@app.route("/sobre")
def sobre():
    return "Sistema desenvolvido em Flask para estudo de CI/CD"

if __name__ == "__main__":
    app.run(debug=True, port=8000)
