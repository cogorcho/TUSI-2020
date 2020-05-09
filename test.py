# ---------------------------------------------------------
#
#       Script para test de modulos
#
# ---------------------------------------------------------

import sys
import os
from modulos import *

# Control de parametros
if len(sys.argv) != 2:
    print("No pasaste un argumento del 1 al 7. Chau!")
    sys.exit(1)

arg = sys.argv[1]

CFG = config.Config(os.getcwd(),'./config/config.dat')
db = db.DB(CFG)
pool = db.pool()

def testVersion():
    v = version.Version()
    print(v.get(pool.get_connection()))

def testProvincia():
    p = provincia.Provincia()
    print(p.get(pool.get_connection()))
    print(p.get(pool.get_connection(),23))

def testAmbito():
    a = ambito.Ambito()
    print(a.get(pool.get_connection()))
    print(a.get(pool.get_connection(),1))
    print(a.get(pool.get_connection(),30))

def testSector():
    s = sector.Sector()
    print(s.get(pool.get_connection()))
    print(s.get(pool.get_connection(),1))

def testTipoEducacion():
    t = tipoeducacion.TipoEducacion()
    print(t.get(pool.get_connection()))
    print(t.get(pool.get_connection(),1))

def testNivelEducacion():
    n = niveleducacion.NivelEducacion()
    print(n.get(pool.get_connection()))
    print(n.get(pool.get_connection(),1))

def testTipoNivelEducacion():
    n = tiponiveleducacion.TipoNivelEducacion()
    print(n.get(pool.get_connection()))
    print(n.get(pool.get_connection(),1))

def testLocalidad():
    l = localidad.Localidad()
    print(l.getXPcia(pool.get_connection(),23))
    print(l.get(pool.get_connection(),8560))
    print(l.getXDepto(pool.get_connection(),2))

def testDepartamento():
    d = departamento.Departamento()
    print(d.getXPcia(pool.get_connection(),23))
    print(d.get(pool.get_connection(),132))
    print(d.get(pool.get_connection(),135))
    print(d.get(pool.get_connection(),119))

def testEscuela():
    e = escuela.Escuela()
    es = '"escuela" : ' + e.get(pool.get_connection(),10404) 
    te = '"ted" : ' + e.getEduc(pool.get_connection(),10404) 
    print('{' + es + ',' + te + '}')

def testColumns():
    c = columns.Column()
    print(c.getJson(pool.get_connection(), 'escuela'))
    
def testSesiones():
    s = sesiones.Sesion()
    print(s.get(pool.get_connection()))

def testTablas():
    t = tables.Table()
    print(t.get(pool.get_connection()))

def testViews():
    v = views.View()
    print(v.get(pool.get_connection()))

def testForm():
    c = columns.Column()
    print(c.getForm(pool.get_connection(), 'TipoNivelEducacion'))

def testConfig():
    cfg = config.Config(os.getcwd(),'config.dat')
    print(cfg.getAll())

def main(arg):
    if arg == 1:
        testVersion()
    elif arg == 2:
        testProvincia()
    elif arg == 3:
        testAmbito()
    elif arg == 4:
        testSector()
    elif arg == 5:
        testLocalidad()
    elif arg == 6:
        testDepartamento()
    elif arg == 7:
        testEscuela()
    elif arg == 8:
        testTipoEducacion()
    elif arg == 9:
        testNivelEducacion()
    elif arg == 10:
        testTipoNivelEducacion()
    elif arg == 11:
        testSesiones()
    elif arg == 12:
        testColumns()
    elif arg == 13:
        testTablas()
    elif arg == 14:
        testViews()
    elif arg == 15:
        testForm()
    elif arg == 16:
        testConfig()
    else:
        print("El argumento es del 1 al 16, GIL!")


if __name__ == '__main__':
    try:
        argu = int(arg)
        main(argu)
        sys.exit(0)
    except Exception as e:
        print(e)
        sys.exit(2)
