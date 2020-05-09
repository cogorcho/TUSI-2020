from .util import genJSON as GenJson
from .util import genFORM as GenForm

class Column:

        def __init__(self):
            self.results = None
            
        def getJson(self,conn,tabla):
            try:
                self.cursor = conn.cursor()                     # crear el cursor
                args = (tabla,)                                 # tupla de parametros
                self.cursor.callproc('getTableColumns', args)   # ejecutamos la sp
                self.results = self.cursor.stored_results()     # traemos los resultados
                for result in self.results:                     # navegamos los resultados
                    self.description = result.description
                    self.results = result.fetchall()            # cargamos la variable de la clase
                self.cursor.close()                             # cerramos el cursor
            except Exception as e:
                print('Exception', str(e))
                conn.close()
            finally:
                if self.cursor is not None:
                    self.cursor.close()  
                conn.close()
                return GenJson(self.description, self.results)



        def getForm(self, conn, tabla):
            try:
                self.cursor = conn.cursor()                     # crear el cursor
                sql = "select * from " + tabla + " limit 1"                
                self.cursor.execute(sql)     
                row = self.cursor.fetchone()
                self.description = self.cursor.description
                self.cursor.close()                            # cerramos el cursor
            except Exception as e:
                print('Exception', str(e))
                conn.close()
            finally:
                if self.cursor is not None:
                    self.cursor.close()  
                return GenForm(tabla, self.description, conn)
