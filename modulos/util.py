from mysql.connector import FieldType
from mysql.connector import FieldFlag

def genJSON(cols, rows):
    """ Columnas seleccionadas por la stored procedure """
    sRec = "{"
    cnt = 0
    for i in range(len(cols)):
        rec = cols[i]
        if cnt == 0:
            sRec += '"%s" : ' % (rec[0])
            cnt = 1
        else:
            sRec += ', "%s" : ' % (rec[0])
        sRec += '"%s"'
    sRec += '}'

    """ Armado de la cadena de salida """
    sOut = "["
    cnt = 0
    for row in rows:
        tStr = sRec % (row)
        if cnt == 0:
            sOut += tStr
            cnt = 1
        else:
            sOut += ", " + tStr
    sOut += "]"
    return sOut

def genFORM(tabla, cols, conn):
    """ Columnas seleccionadas por la stored procedure """
    out = header(tabla)
    out += '<form name="%s" action="http://192.168.1.102:5000/cargar/%s" method="post">\n' % (tabla.title(), tabla)
    
    for col in cols:
        tipo = FieldType.get_info(col[1])
        flg = FieldFlag.get_bit_info(col[7])

        if 'AUTO_INCREMENT' in flg:
            continue

        if 'NOT_NULL' in flg:
             required = 'required'
        else:
            required = '' 

        if 'MULTIPLE_KEY' in flg:
            out += '<div class="form-group">\n'
            nom = col[0].replace('id','',1).title()
            out += '\t<label for="%s">%s</label>\n' % (nom, nom)
            out += '\t<select name="%s">\n' % (nom)
            for opt in getCombo(conn, col[0].replace('id','',1)):
                out += '\t\t' + opt + '\n'
            out += '\t</select>\n'
            out += '</div>\n'        
        else:
            out += '<div class="form-group">\n'
            nom = col[0].title()
            out += '\t<label for="%s">%s:</label>\n' % (nom, nom)
            out += '\t<input type="%s" class="form-control" id="%s" name="%s" placeholder="%s" %s/>\n' % (tipo, nom, nom, nom, required)
            out += '</div>\n'        

    out += '<hr>\n'
    out += '<button type="submit" formmethod="post">Confirmar</button>\n'
    out += '</form>\n'
    out += footer()
    conn.close()
    return out

def getCombo(conn, tabla):
    try:
        retv = []
        sql = "select id, nombre from " + tabla + " limit 50"
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            s = '<option value="%s">%s</option>' % (row)
            retv.append(s)
    except Exception as e:
        print('Exception', str(e))
        conn.close()
    finally:
        if cursor is not None:
            cursor.close()  
        return retv

def header(tabla):
    out = """
    <html>
    <head>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
        <title>Python API</title>
    </head>
    <body>
        <div class="container">
    """
    out += '<br><h1>Carga de datos: %s</h1><br>\n' % (tabla.title())
    return out

def footer():
    out = """
        </div>
    </body>
</html>
    """
    return out