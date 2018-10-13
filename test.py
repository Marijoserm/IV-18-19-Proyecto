from pdfupload import PDFUpload

pdfupload = PDFUpload()

# Test del status

def testStatus():
    assert pdfupload.Status() == "OK"

# Test de verificar la existencia del usuario

def testIsUser():
    assert pdfupload.IsUser(1) == False
    assert pdfupload.IsUser(1.0) == False
    assert pdfupload.IsUser('test') == False
    pdfupload = PDFUpload()

# Test de creacion de usuario

def testCreateUser():
    assert pdfupload.CreateUser('') == False
    assert pdfupload.CreateUser(1) == False
    assert pdfupload.CreateUser(1.0) == False
    assert pdfupload.CreateUser('test') == True
    pdfupload = PDFUpload()

# Test de eliminacion del usuario

def testDeleteUser():
    assert pdfupload.DeleteUser('') == False
    assert pdfupload.DeleteUser(1) == False
    assert pdfupload.DeleteUser(1.0) == False
    assert pdfupload.DeleteUser('test') == False

    pdfupload.CreateUser('test')
    assert pdfupload.DeleteUser('test') == True
    pdfupload = PDFUpload()

# Test de verificar la existencia del archivo

def testIsFile():
    assert pdfupload.IsFile(1,1) == False
    assert pdfupload.IsFile(1.0,1.0) == False
    assert pdfupload.IsFile(1,1.0) == False
    assert pdfupload.IsFile(1.0,1) == False
    assert pdfupload.IsFile('test','pdftest.pdf') == False
    pdfupload = PDFUpload()

# Test de agregar el archivo

def testAddNewFile():
    assert pdfupload.AddNewFile('','') == False
    assert pdfupload.AddNewFile(1,1) == False
    assert pdfupload.AddNewFile(1.0,1) == False
    assert pdfupload.AddNewFile(1,1.0) == False
    assert pdfupload.AddNewFile(1.0,1.0) == False
    assert pdfupload.AddNewFile('test','pdftest') == False

    pdfupload.CreateUser('test')
    assert pdfupload.AddNewFile('test','pdftest.pdf') == True
    pdfupload = PDFUpload()

# Test de eliminacion del archivo

def testDeleteFile():
    assert pdfupload.DeleteFile('','') == False
    assert pdfupload.DeleteFile(1,1) == False
    assert pdfupload.DeleteFile(1.0,1) == False
    assert pdfupload.DeleteFile(1,1.0) == False
    assert pdfupload.DeleteFile(1.0,1.0) == False
    assert pdfupload.DeleteFile('test','pdftest') == False

    pdfupload.CreateUser('test')
    pdfupload.AddNewFile('test', 'pdftest.pdf')
    assert pdfupload.DeleteFile('test','pdftest.pdf') == True
    pdfupload = PDFUpload()