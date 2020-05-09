import mysql.connector
from mysql.connector import Error
from mysql.connector import pooling
import logging
logger = logging.getLogger(__name__)

class DB:

    # Inicializador
    def __init__(self, cfg):
        self.host = cfg.getval('DBhost')
        self.user= cfg.getval('DBuser')
        self.password = cfg.getval('DBpassword')
        self.db = cfg.getval('DBdb')
        self.charset = cfg.getval('DBcharset') 
        self.use_unicode = cfg.getval('DBuse_unicode')
    
    def pool(self):
        try:
            dbconfig = {
                "host" : self.host,
                "database": self.db,
                "user":     self.user,
                "password" : self.password
            }

            self.cnx = mysql.connector.pooling.MySQLConnectionPool(
                pool_name = "mypool", 
                pool_size = 3, 
                **dbconfig)

            logger.info("%s: Connection Pool OK" % (__name__))
        except Exception as e:
            logger.critical("Connection Pool: %s" % (str(e)))
        finally:
            return self.cnx

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                                host=self.host,
                                user=self.user,
                                password=self.password,
                                db=self.db,
                                charset=self.charset,
                                use_unicode=self.use_unicode)
        except mysql.connector.Error as e:
            logger.error("connect(): %s" % (str(e)))
        else:
            print("Accessing DB: ", self.db)

    def getConnection(self):
        if self.connection == None:
            self.connect()
        return self.connection

    def status(self):
        if self.connection == None:
            print("Connection Status: Not connected")
        else:
            print("Connection Status: Connected!")

