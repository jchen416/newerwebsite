
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    pages = ['Publications', 'Projects', 'About']
    return render_template('index.html', mountain=pages)

@app.route('/<mt>')
def mountain(mt):
    return(f'{str(mt)} Page')

if  __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


