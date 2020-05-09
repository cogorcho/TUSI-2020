
from .util import genJSON as GenJson

class Escuela:

        def __init__(self):
            self.results = None
             
        def getEduc(self,conn,eID):
            try:
                self.cursor = conn.cursor()                     # crear el cursor
                args = (eID,)                                   # tupla de parametros
                self.cursor.callproc('getEducEscuela',args)     # ejecutamos la sp
                self.results = self.cursor.stored_results()     # traemos los resultados
                for result in self.results:                     # navegamos los resultados
                    self.description = result.description
                    self.results = result.fetchall()            # cargamos la variable de la clase
                self.cursor.close()                             # cerramos el cursor
            except Exception as e:
                print(str(e))
            finally:
                if self.cursor is not None:
                    self.cursor.close()
                conn.close()
                return GenJson(self.description, self.results)           # la retornamos como json

        def genEducJson(self, data):
            out = "["
            cnt = 0
            for r in data:
                if cnt > 0 :
                    out += ','
                cnt += 1
                out += '{"id" : "%s", "Tipo" : "%s", "Nivel" :"%s"}' % (r[0], r[1], r[2])
            out += "]"
            return out

        def get(self, conn, escID):
            try:
                self.cursor = conn.cursor()
                args = (escID,)
                self.cursor.callproc('getEscuelaXId', args)
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
                return GenJson(self.description, self.results)           # la retornamos como json

        def getLoc(self, conn, locID):
            try:
                self.cursor = conn.cursor()
                args = (locID,)
                self.cursor.callproc('getEscuelasXLoc', args)
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
                return GenJson(self.description, self.results)           # la retornamos como json
                
