from .util import genJSON as GenJson

class Table:

        def __init__(self):
            self.results = None
            
        def get(self,conn):
            try:
                self.cursor = conn.cursor()                     # crear el cursor
                args = ()                                       # tupla de parametros
                self.cursor.callproc('getTables', args)          # ejecutamos la sp
                self.results = self.cursor.stored_results()     # traemos los resultados
                for result in self.results:                     # navegamos los resultados
                    self.description = result.description
                    self.results = result.fetchall()            # cargamos la variable de la clase
                self.cursor.close()                             # cerramos el cursor
            except Exception as e:
                print('Exception', str(e))
            finally:
                if self.cursor is not None:
                    self.cursor.close()  
                conn.close()
                return GenJson(self.description,self.results)   # la retornamos

