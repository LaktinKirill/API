from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    insult = None
    if request.method == 'POST':
        insult = get_insult()
    return render_template("index.html", insult=insult)

def get_insult():
    url = f'https://evilinsult.com/generate_insult.php?lang=ru&type=json'
    resource = requests.get(url)
    return resource.json()

if __name__ == '__main__':
    app.run(debug=True)
    