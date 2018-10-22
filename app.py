from flask import Flask, render_template, json
from pdfupload import PDFUpload

app = Flask(__name__, template_folder='./templates/')
pdfupload = PDFUpload()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/status')
def status():
    salida = pdfupload.Status()

    if salida == 'OK':
        f = open("status.json","r")
        data = f.read()
        response = app.response_class(
            response=json.dumps(data),
            status=200,
            mimetype='application/json'
        )
        return response
        
@app.route('/home')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)