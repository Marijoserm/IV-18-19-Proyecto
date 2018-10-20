from flask import Flask, render_template
from datetime import datetime
from pdfupload import PDFUpload

<<<<<<< HEAD
app = Flask(__name__, template_folder='./templates/')
=======
app = Flask(__name__)
>>>>>>> 5943cde5621a4601c6e803a2d58ecf871ec458ab
pdfupload = PDFUpload()

@app.route('/')
def home():
<<<<<<< HEAD
    return render_template('index.html')
=======
    return "Hello world"
>>>>>>> 5943cde5621a4601c6e803a2d58ecf871ec458ab

@app.route('/status')
def status():
    return pdfupload.Status()

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)