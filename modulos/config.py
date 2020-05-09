import os
class Config:

    def __init__(self, cfgdir, cfgfile):
        self.d = {}

        if not self.checkcfgdir(cfgdir):
            return

        self.cfgfile = cfgdir + '/' + cfgfile
        self.leerArchivo()

    def leerArchivo(self):
        print("Leyendo %s" % (self.cfgfile))
        with open(self.cfgfile) as f:
            for line in f:
                (key, val) = line.split(':')
                self.d[key] = val.strip('\n')

    def checkcfgdir(self, dirtocheck):
        if not os.path.exists(dirtocheck):
            print("No existe el directorio %s" % (dirtocheck))
            return False
        return True

    def get(self,k="ALL"):
        if k == "ALL":
            return getAll()
        else:
            return '{ "%s" : "%s" }' % (k, self.d[k])

    def getval(self,k):
        return self.d[k]

    def getAll(self):
        cnt = 0
        out = '['
        for k in self.d:
            if cnt == 0:
                cnt = 1
                out += '{ "%s" : "%s" }' % (k, self.d[k])
            else:
                out += ',{ "%s" : "%s" }' % (k, self.d[k])
        out += ']'
        return out
