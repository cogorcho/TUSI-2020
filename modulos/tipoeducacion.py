from .util import genJSON as GenJson

class TipoEducacion:

    def __init__(self):
        self.results = None
        
    def get(self,conn,tedID=-1):
        try:
            self.cursor = conn.cursor()                # crear el cursor
            args = (tedID,)                                 # tupla de parametros
            self.cursor.callproc('getTipoEducacion',args)   # ejecutamos la sp
            self.results = self.cursor.stored_results()     # traemos los resultados
            for result in self.results:
                self.description = result.description       # Lista de columnas del query                     # navegamos los resultados
                self.results = result.fetchall()            # cargamos la variable de la clase
            self.cursor.close()                             # cerramos el cursor
        except Exception as e:
            print(str(e))
        finally:
            if self.cursor is not None:
                self.cursor.close() 
            conn.close()
            return GenJson(self.description,self.results)               # la retornamos
