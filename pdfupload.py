#!/usr/bin/python

class PDFUpload:
    def __init__(self):
        self.almacen = []    

    def Status(self):
        return "OK"

    def IsUser(self, user):
        """ 
        Check if the user exists in the database.
    
        Parameters: 
        user -- the id of the user to find.
    
        Returns: 
        bool: if the user exist or not.
    
        """
        sql = """SELECT * FROM usuarios WHERE id_user = %s"""

        conn = self.get_conn()
        cur = conn.cursor()
        cur.execute(sql, (user,))
        filas = cur.rowcount
        cur.close()

        return filas != 0

    def CreateUser(self, user):
        """ 
        Add a new user to the data base. Must be an different user that is not in the database.
    
        Parameters: 
        user -- the id of the user.
    
        Returns: 
        bool: created succesfully.
    
        """

        sql = """INSERT INTO usuarios VALUES (%s,%s) RETURNING id_user;"""

        user_id = None

        if(not self.IsUser(user)):
            try:
                conn = self.get_conn()
                cur = conn.cursor()
                cur.execute(sql, (user,"/tmp/"))
                user_id = str(cur.fetchone()[0])
                conn.commit()
                cur.close()
            except (Exception, psycopg2.DatabaseError) as error:
                print(error)
        
        return user_id == user

    def DeleteUser(self, user):
        """ 
        Delete a user from the data base. Must exist the user in the database.
    
        Parameters: 
        user -- the id of the user.
    
        Returns: 
        bool: delete succesfully.
    
        """
        sql = """DELETE FROM usuarios WHERE user_id = %s;"""

        try:
            conn = self.get_conn()
            cur = conn.cursor()
            
            cur.execute(sql, (user,))
            rows_deleted = cur.rowncount
            conn.commit()
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
    
        return rows_deleted != 0

    def IsFile(self, user,path):
        """ 
        Check if the path exists in the database and if the pdf file is on the file system.
    
        Parameters: 
        path -- the path of the pdf file to find.
    
        Returns: 
        bool: if the pdf exist or not.
    
        """
        
        sql = """SELECT * FROM usuarios WHERE id_user = %s and dir_file = %s"""

        conn = self.get_conn()
        cur = conn.cursor()
        cur.execute(sql, (user,path))
        filas = cur.rowcount
        cur.close()

        return filas != 0

    def AddNewFile(self, path):
        """ 
        Add a new file to the data base. The name of the file must be different from the others in the same directory.
    
        Parameters: 
        path -- the path of the file.
    
        Returns: 
        bool: added succesfully.
    
        """


    def DeleteFile(self, path):
        """ 
        Add a new file to the data base. The name of the file must be different from the others in the same directory.
    
        Parameters: 
        path -- the path of the file.
    
        Returns: 
        bool: added succesfully.
    
        """
