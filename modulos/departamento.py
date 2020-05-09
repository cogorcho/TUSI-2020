from .util import genJSON as GenJson

class Departamento:

        def __init__(self):
            self.results = None
            
        def getXPcia(self,conn,pciaID):
            try:
                self.cursor = conn.cursor()                     # crear el cursor
                args = (pciaID,)                                # tupla de parametros
                self.cursor.callproc('getDeptPcia',args)        # ejecutamos la sp
                self.results = self.cursor.stored_results()     # traemos los resultados
                for result in self.results:                     # navegamos los resultados
                    self.description = result.description       # Lista de columnas del query
                    self.results = result.fetchall()            # cargamos la variable de la clase
                self.cursor.close()                             # cerramos el cursor
            except Exception as e:
                print(str(e))
            finally:
                if self.cursor is not None:
                    self.cursor.close()
                conn.close()
                return GenJson(self.description,self.results)               # la retornamos

        def get(self, conn, deptID):
            try:
                self.cursor = conn.cursor()
                args = (deptID,)
                self.cursor.callproc('getDeptId', args)
                self.results = self.cursor.stored_results()
                for result in self.results:
                    self.description = result.description
                    self.results = result.fetchall()
                self.cursor.close()
            except Exception as e:
                print(str(e))
            finally:
                if self.cursor is not None:
                    self.cursor.close()
                conn.close()
                return GenJson(self.description,self.results)               # la retornamos

