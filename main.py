from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    weather = None
    if request.method == 'POST':
        city = request.form['city']
        weather = get_weather(city)
    return render_template("index.html", weather=weather)

def get_weather(city):
    api_key = "e4dc5c5b8795b7f64925f2ecf2207301"
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    resource = requests.get(url)
    return resource.json()

if __name__ == '__main__':
    app.run(debug=True)
    