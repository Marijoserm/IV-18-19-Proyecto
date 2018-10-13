#!/usr/bin/python

class PDFUpload:
    def __init__(self):
        self.almacen = {}    

    def Status(self):
        """
        Return the status of the class
        
        Returns:
        string: return OK
        """
        return "OK"

    def DeleteStore(self):
        """
        Clear the storage

        Returns:
        bool: if the dictionary is empty
        """
        self.almacen.clear()
        return not bool(self.almacen)

    def IsUser(self, user):
        """ 
        Check if the user exists in the dictionary.
    
        Parameters: 
        user -- the id of the user to find.
    
        Returns: 
        bool: if the user exist or not.
    
        """
        if type(user) is int or type(user) is float:
            return False

        if not user:
            return False

        return user in self.almacen

    def CreateUser(self, user):
        """ 
        Add a new user to the dictionary. Must be an different user that is not in the dictionary.
    
        Parameters: 
        user -- the id of the user.
    
        Returns: 
        bool: created succesfully.
    
        """
        if type(user) is int or type(user) is float:
            return False

        if not user:
            return False

        self.almacen.update({user : set()))
        return self.IsUser(user)


    def DeleteUser(self, user):
        """ 
        Delete a user from the dictionary. Must exist the user in the dictionary.
    
        Parameters: 
        user -- the id of the user.
    
        Returns: 
        bool: delete succesfully.
    
        """
        if type(user) is int or type(user) is float:
            return False

        if not user:
            return False

        if self.IsUser(user):
            self.almacen.pop(user, None)
            return True
        else:
            return False

    def IsFile(self, user, f):
        """ 
        Check if the path exists in the dictionary and if the pdf file is on the file system.
    
        Parameters: 
        path -- the path of the pdf file to find.
    
        Returns: 
        bool: if the pdf exist or not.
    
        """
        if type(user) is int or type(user) is float:
            return False

        if type(f) is int or type(f) is float:
            return False

        if not user or not f:
            return False

        return user in self.almacen and f in self.almacen[user]

    def AddNewFile(self, user, f):
        """ 
        Add a new file to the dictionary. The name of the file must be different from the others in the same directory.
    
        Parameters: 
        user -- the id of the user.
        f -- the file of the user.
    
        Returns: 
        bool: added succesfully.
    
        """
        if type(user) is int or type(user) is float:
            return False
        
        if type(f) is int or type(f) is float:
            return False
        
        if not user or not f:
            return False

        if self.IsUser(user):
            self.almacen[user].add(f)
            return self.IsFile(user,f)
        else:
            return False

    def DeleteFile(self, user, f):
        """ 
        Add a new file to the dictionary. The name of the file must be different from the others in the same directory.
    
        Parameters: 
        path -- the path of the file.
    
        Returns: 
        bool: added succesfully.
    
        """
        if type(user) is int or type(user) is float:
            return False
        
        if type(f) is int or type(f) is float:
            return False
        
        if not user or not f:
            return False
        
        if self.IsUser(user) and self.IsFile(user,f):
            self.almacen[user].remove(f)
            return True
        else:
            return False