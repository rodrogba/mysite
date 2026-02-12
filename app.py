from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Isso envia seu HTML que está na pasta templates
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)