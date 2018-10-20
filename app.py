from flask import Flask, render_template
from pdfupload import PDFUpload

app = Flask(__name__, template_folder='./templates/')
pdfupload = PDFUpload()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/status')
def status():
    return pdfupload.Status()

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)