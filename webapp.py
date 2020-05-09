from flask import Flask, render_template, jsonify, request
import sys
import os
import logging
import datetime
from modulos import *

app = Flask(__name__)

CFG = config.Config(os.getcwd(),'./config/config.dat')
db = db.DB(CFG)
pool = db.pool()

V = version.Version()
P = provincia.Provincia()
S = sector.Sector()
A = ambito.Ambito()
T = tipoeducacion.TipoEducacion()
N = niveleducacion.NivelEducacion()
TN = tiponiveleducacion.TipoNivelEducacion()
E = escuela.Escuela()
L = localidad.Localidad()
D = departamento.Departamento()
Se = sesiones.Sesion()
C = columns.Column()

logfile = "%s/%s-%s.log" % (CFG.getval('LOGDIR'),datetime.date.today(), __name__)
logging.basicConfig(filename=logfile,format=CFG.getval('LOGFMT'), datefmt=CFG.getval('LOGDATEFMT'), level=CFG.getval('LOGLEVEL'))

@app.route('/')
def home():
    logging.info("Origen: %s" % (request.remote_addr))
    return render_template('index.html')

@app.route('/cargar/<id>',  methods=['GET', 'POST'] )
def cargar(id):
    if request.method == 'GET':
        c = columns.Column()
        return c.getForm(pool.get_connection(), id)
    elif request.method == 'POST':
        print(request.form)
        return dict(resultado="OK")

@app.route('/version')
def version():
    return V.get(pool.get_connection())

@app.route('/sesiones')
def sesiones():
    return Se.get(pool.get_connection())

@app.route('/provincias')
def provincias():
    return P.get(pool.get_connection()) 

@app.route('/provincia/<id>')
def provincia(id):
    return P.get(pool.get_connection(),id) 

@app.route('/sectores')
def sectores():
    return S.get(pool.get_connection()) 

@app.route('/sector/<id>')
def sector(id):
    return S.get(pool.get_connection(),id) 

@app.route('/ambitos')
def ambitos():
    return A.get(pool.get_connection()) 

@app.route('/ambito/<id>')
def ambito(id):
    return A.get(pool.get_connection(),id) 

@app.route('/tiposeducacion')
def tiposeducacion():
    return T.get(pool.get_connection()) 

@app.route('/tipoeducacion/<id>')
def tipoeducacion(id):
    return T.get(pool.get_connection(),id) 

@app.route('/niveleseducacion')
def niveleseducacion():
    return N.get(pool.get_connection()) 

@app.route('/niveleducacion/<id>')
def niveleducacion(id):
    return N.get(pool.get_connection(),id) 

@app.route('/tiposniveleseducacion')
def tiposniveleseducacion():
    return TN.get(pool.get_connection()) 

@app.route('/tiponiveleseducacion/<id>')
def tiponiveleseducacion(id):
    return TN.get(pool.get_connection(),id) 

@app.route('/escuelasxlocalidad/<id>')
def escuelasxlocalidad(id):
    return E.getLoc(pool.get_connection(),id) 

@app.route('/escuela/<id>')
def escuelaxid(id):
    es = '{ "escuela" : ' + E.get(pool.get_connection(),id) 
    te = ', "ted" : ' + E.getEduc(pool.get_connection(),id) + '}'
    return (es + te) 

@app.route('/tedescuela/<id>')
def tedescuelas(id):
    return E.getEduc(pool.get_connection(),id) 

@app.route('/localidades/<id>')
def localidades(id):
    return L.getXPcia(pool.get_connection(),id) 

@app.route('/localidadesxdepto/<id>')
def localidadesxdepto(id):
    return L.getXDepto(pool.get_connection(),id) 

@app.route('/localidad/<id>')
def localidad(id):
    return L.get(pool.get_connection(),id) 

@app.route('/departamentos/<id>')
def departamentos(id):
    return D.getXPcia(pool.get_connection(),id)

@app.route('/departamento/<id>')
def departamento(id):
    return D.get(pool.get_connection(),id)

@app.route('/configs')
def cfgs():
    return CFG.getAll()

@app.route('/config/<id>')
def cfg(id=None):
    if id is None:
        return CFG.getAll()
    else:
        return CFG.get(id)

@app.route('/req')
def req():
    s = 'request.' + 'environ'
    out = "<ul>"
    for r in dir(request):
        if r is not None:
            s = 'request.' + r
            if eval(s) is not None:
                li = "%s: %s" % (r,eval(s))
            out += "<li>%s</li>" % li

    out += "</ul>"
    return out

@app.route('/tabla/<id>')
def tabla(id):
    return C.getJson(pool.get_connection(), id)


def printreq(request):
    print('__class__', request.__class__)
    print('__delattr__', request.__delattr__)
    print('__dict__', request.__dict__)
    print('__dir__', request.__dir__)
    print('__doc__', request.__doc__)
    print('__enter__', request.__enter__)
    print('__eq__', request.__eq__)
    print('__exit__', request.__exit__)
    print('__format__', request.__format__)
    print('__ge__', request.__ge__)
    print('__getattribute__', request.__getattribute__)
    print('__gt__', request.__gt__)
    print('__hash__', request.__hash__)
    print('__init__', request.__init__)
    print('__init_subclass__', request.__init_subclass__)
    print('__le__', request.__le__)
    print('__lt__', request.__lt__)
    print('__module__', request.__module__)
    print('__ne__', request.__ne__)
    print('__new__', request.__new__)
    print('__reduce__', request.__reduce__)
    print('__reduce_ex__', request.__reduce_ex__)
    print('__repr__', request.__repr__)
    print('__setattr__', request.__setattr__)
    print('__sizeof__', request.__sizeof__)
    print('__str__', request.__str__)
    print('__subclasshook__', request.__subclasshook__)
    print('__weakref__', request.__weakref__)
    print('_cached_json', request._cached_json)
    print('_get_data_for_json', request._get_data_for_json)
    print('_get_file_stream', request._get_file_stream)
    print('_get_stream_for_parsing', request._get_stream_for_parsing)
    print('_load_form_data', request._load_form_data)
    print('_parse_content_type', request._parse_content_type)
    print('accept_charsets', request.accept_charsets)
    print('accept_encodings', request.accept_encodings)
    print('accept_languages', request.accept_languages)
    print('accept_mimetypes', request.accept_mimetypes)
    print('access_control_request_headers', request.access_control_request_headers)
    print('access_control_request_method', request.access_control_request_method)
    print('access_route', request.access_route)
    print('application', request.application)
    print('args', request.args)
    print('authorization', request.authorization)
    print('base_url', request.base_url)
    print('blueprint', request.blueprint)
    print('cache_control', request.cache_control)
    print('charset', request.charset)
    print('close', request.close)
    print('content_encoding', request.content_encoding)
    print('content_length', request.content_length)
    print('content_md5', request.content_md5)
    print('content_type', request.content_type)
    print('cookies', request.cookies)
    print('data', request.data)
    print('date', request.date)
    print('dict_storage_class', request.dict_storage_class)
    print('disable_data_descriptor', request.disable_data_descriptor)
    print('encoding_errors', request.encoding_errors)
    print('endpoint', request.endpoint)
    print('environ', request.environ)
    print('files', request.files)
    print('form', request.form)
    print('form_data_parser_class', request.form_data_parser_class)
    print('from_values', request.from_values)
    print('full_path', request.full_path)
    print('get_data', request.get_data)
    print('get_json', request.get_json)
    print('headers', request.headers)
    print('host', request.host)
    print('host_url', request.host_url)
    print('if_match', request.if_match)
    print('if_modified_since', request.if_modified_since)
    print('if_none_match', request.if_none_match)
    print('if_range', request.if_range)
    print('if_unmodified_since', request.if_unmodified_since)
    print('input_stream', request.input_stream)
    print('is_json', request.is_json)
    print('is_multiprocess', request.is_multiprocess)
    print('is_multithread', request.is_multithread)
    print('is_run_once', request.is_run_once)
    print('is_secure', request.is_secure)
    print('json', request.json)
    print('json_module', request.json_module)
    print('list_storage_class', request.list_storage_class)
    print('make_form_data_parser', request.make_form_data_parser)
    print('max_content_length', request.max_content_length)
    print('max_form_memory_size', request.max_form_memory_size)
    print('max_forwards', request.max_forwards)
    print('method', request.method)
    print('mimetype', request.mimetype)
    print('mimetype_params', request.mimetype_params)
    print('on_json_loading_failed', request.on_json_loading_failed)
    print('origin', request.origin)
    print('parameter_storage_class', request.parameter_storage_class)
    print('path', request.path)
    print('pragma', request.pragma)
    print('query_string', request.query_string)
    print('range', request.range)
    print('referrer', request.referrer)
    print('remote_addr', request.remote_addr)
    print('remote_user', request.remote_user)
    print('routing_exception', request.routing_exception)
    print('scheme', request.scheme)
    print('script_root', request.script_root)
    print('shallow', request.shallow)
    print('stream', request.stream)
    print('trusted_hosts', request.trusted_hosts)
    print('url', request.url)
    print('url_charset', request.url_charset)
    print('url_root', request.url_root)
    print('url_rule', request.url_rule)
    print('user_agent', request.user_agent)
    print('values', request.values)
    print('view_args', request.view_args)
    print('want_form_data_parsed', request.want_form_data_parsed)

