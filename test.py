from pdfupload import PDFUpload

pdfupload = PDFUpload()

# Comprueba si devuelve status OK

def testStatus():
    assert pdfupload.Status() == "OK"