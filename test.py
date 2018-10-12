from pdfupload import PDFUpload

pdfupload = PDFUpload()

# Comprueba si devuelve status OK

def testStatus():
    assert pdfupload.Status() == "OK"

# Comprueba si existe el usuario

def testIsUser():
    pdfupload.CreateUser('test')
    assert pdfupload.IsUser('') == False
    asser pdfupload.IsUser('test') == True
