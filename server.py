from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = "euwgyw"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():

    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']

    return render_template('process.html')

if __name__ == "__main__":
    app.run(debug=True)