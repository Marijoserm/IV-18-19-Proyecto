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

    def CheckArguments(self, text='none', text1='none'):
        """
        Check if the arguments are not int, float or None. Must be a string

        Parameters:
        text -- first argument. Default 'none'
        text1 -- second argument. Default 'none'

        Returns:
        bool: if the arguments are string
        """

        if text != 'none':
            if type(text) is int or type(text) is float or not text:
                salida = False
            else:
                salida = True
        else:
            if text != 'none' and text1 != 'none':
                if (type(text) is int or type(text) is float) and (type(text1) is int or type(text1) is float) and (not text or not text1):
                    salida = False
                else:
                    salida = True
            else:
                salida = False

        return salida

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
        salida = self.CheckArguments(user)
        
        if salida:
            return user in self.almacen

        return salida

    def CreateUser(self, user):
        """ 
        Add a new user to the dictionary. Must be an different user that is not in the dictionary.
    
        Parameters: 
        user -- the id of the user.
    
        Returns: 
        bool: created succesfully.
    
        """
        salida = self.CheckArguments(user)
        
        if salida:
            s = set()
            self.almacen.update({user : s})
            return self.IsUser(user)

        return salida

    def DeleteUser(self, user):
        """ 
        Delete a user from the dictionary. Must exist the user in the dictionary.
    
        Parameters: 
        user -- the id of the user.
    
        Returns: 
        bool: delete succesfully.
    
        """
        salida = self.CheckArguments(user)
        
        if salida:
            if self.IsUser(user):
                self.almacen.pop(user, None)
                return True
            else:
                return False
        
        return salida

    def IsFile(self, user, f):
        """ 
        Check if the path exists in the dictionary and if the pdf file is on the file system.
    
        Parameters: 
        path -- the path of the pdf file to find.
    
        Returns: 
        bool: if the pdf exist or not.
    
        """
        salida = self.CheckArguments(user, f)
        
        if salida:
            return user in self.almacen and f in self.almacen[user]
        
        return salida

    def AddNewFile(self, user, f):
        """ 
        Add a new file to the dictionary. The name of the file must be different from the others in the same directory.
    
        Parameters: 
        user -- the id of the user.
        f -- the file of the user.
    
        Returns: 
        bool: added succesfully.
    
        """
        salida = self.CheckArguments(user, f)

        if salida:
            if self.IsUser(user):
                self.almacen[user].add(f)
                return self.IsFile(user,f)
            else:
                return False
        
        return salida

    def DeleteFile(self, user, f):
        """ 
        Add a new file to the dictionary. The name of the file must be different from the others in the same directory.
    
        Parameters: 
        path -- the path of the file.
    
        Returns: 
        bool: added succesfully.
    
        """
        salida = self.CheckArguments(user,f)
        
        if salida:
            if self.IsUser(user) and self.IsFile(user,f):
                self.almacen[user].remove(f)
                return True
            else:
                return False

        return salida

    def SearchFile(self, user, search):
        """
        Search all the files that are similar to name.

        Parameters:
        user -- the id of the user.
        search -- the search of the user´s storage.

        Returns:
        Array: the files resulting from the search
        """
        salida = self.CheckArguments(user)
        matching = []

        if salida:
            if self.IsUser(user):
                list = self.almacen[user]
                matching = [s for s in list if search in s]
        
        return matching