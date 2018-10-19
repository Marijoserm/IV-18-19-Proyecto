from flask import Flask
from datetime import datetime
from pdfupload import PDFUpload

app = Flask(__name__)
pdfupload = PDFUpload()

@app.route('/')
def home():
    return "Hello world"

@app.route('/status')
def status():
    return pdfupload.Status()

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)