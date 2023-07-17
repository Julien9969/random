from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello')
def hello():
    name = request.args.get('name', 'Anonymous')
    return f"Hello, {name}!"

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form.get('name')
        return f"Hello, {name}!"
    return render_template('form.html')

@app.route('/test')
def test():
    return render_template('test.html')

if __name__ == '__main__':
    app.run()
