#!/usr/bin/python
from flask import Flask
app = Flask(__name__)

class PDFUpload:
    def __init__(self):
        self.almacen = {}    

    def Status(self):
        return "OK"

    def IsUser(self, user):
        """ 
        Check if the user exists in the dictionary.
    
        Parameters: 
        user -- the id of the user to find.
    
        Returns: 
        bool: if the user exist or not.
    
        """
        return user in self.almacen

    def CreateUser(self, user):
        """ 
        Add a new user to the dictionary. Must be an different user that is not in the dictionary.
    
        Parameters: 
        user -- the id of the user.
    
        Returns: 
        bool: created succesfully.
    
        """
        self.almacen.update({user : []})
        self.IsUser(user)


    def DeleteUser(self, user):
        """ 
        Delete a user from the dictionary. Must exist the user in the dictionary.
    
        Parameters: 
        user -- the id of the user.
    
        Returns: 
        bool: delete succesfully.
    
        """

    def IsFile(self, user,path):
        """ 
        Check if the path exists in the dictionary and if the pdf file is on the file system.
    
        Parameters: 
        path -- the path of the pdf file to find.
    
        Returns: 
        bool: if the pdf exist or not.
    
        """

    def AddNewFile(self, user, pdffile):
        """ 
        Add a new file to the dictionary. The name of the file must be different from the others in the same directory.
    
        Parameters: 
        user -- the id of the user.
        pdffile -- the file of the user.
    
        Returns: 
        bool: added succesfully.
    
        """
        if self.IsUser(user):
            self.almacen[user[0]].append(pdffile)


    def DeleteFile(self, path):
        """ 
        Add a new file to the dictionary. The name of the file must be different from the others in the same directory.
    
        Parameters: 
        path -- the path of the file.
    
        Returns: 
        bool: added succesfully.
    
        """
