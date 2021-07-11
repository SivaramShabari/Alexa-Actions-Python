from flask  import Flask

app = Flask(__name__)

@app.route("/")
def main():
    return {"res":"Hello, World!"}

if __name__=="main":
    app.run()