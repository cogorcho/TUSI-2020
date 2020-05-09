import logging
logger = logging.getLogger(__name__)

class Version:
    def __init__(self):
        self.cursor = None
        self.data = None

    def get(self, conn):
        try:
            self.cursor = conn.cursor() # prepare a cursor object using cursor() method
            self.cursor.execute("SELECT VERSION()") # ejecuta el SQL query usando el metodo execute().
            self.data = self.cursor.fetchone() # procesa una unica linea usando el metodo fetchone().
        except Exception as e:
            print(str(e))
            logger.error(str(e))
        finally:
            if self.cursor is not None:
                self.cursor.close()
            conn.close()
            if self.data is not None:
                logger.info("Database version : {0}".format(self.data))
                return "Database version : {0}".format(self.data)
            else:
                logger.info("Error obteniendo la version de la Base")
                return "Imposible obtener version de la DB"