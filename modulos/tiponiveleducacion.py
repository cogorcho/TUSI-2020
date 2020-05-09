class TipoNivelEducacion:

        def __init__(self):
            self.results = None
            
        def get(self,conn,tedID=-1):
            try:
                self.cursor = conn.cursor()                     # crear el cursor
                args = (tedID,)                                 # tupla de parametros
                self.cursor.callproc('getTipoNivelEducacion',args)  # ejecutamos la sp
                self.results = self.cursor.stored_results()     # traemos los resultados
                for result in self.results:                     # navegamos los resultados
                    self.results = result.fetchall()            # cargamos la variable de la clase
                self.cursor.close()                             # cerramos el cursor
            except Exception as e:
                print(str(e))
            finally:
                if self.cursor is not None:
                    self.cursor.close()
                conn.close()
                return self.genJson(self.results)               # la retornamos

        def genJson(self, data):
            out = "["
            cnt = 0
            for r in data:
                if cnt > 0 :
                    out += ','
                cnt += 1
                out += '{"id" : "%d", "idTipoEducacion" : "%s", "nombreTipoEducacion" :"%s", "idNivelEducacion" : "%s", "nombreNivelEducacion" : "%s"}' % (r[0], r[1], r[2].replace('_', ' '), r[3], r[4].replace('_',' '))
            out += "]"
            return out