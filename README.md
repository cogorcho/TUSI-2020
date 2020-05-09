# API REST con MySQL y python

Proyecto integrando Bases de Datos (mysql) y programacion avanzada (python)de la Tecnitatura Superior en Sistemas Informaticos (TUSI) de la Regional San Nicolas de la UTN.


# Servicio

El servicio a proveer, en una primera etapa, es solo de consulta.

# Prerrequisitos

**Instalar:**  
[Mysql](https://dev.mysql.com/downloads/) - La base de datos  
* [python](https://www.python.org/downloads/) - El lenguaje a utilizar  
* [virtualenv](https://pypi.org/project/virtualenv/) - Ambiente de desarrollo  

* Como instalar virtualenv en Windows(https://programwithus.com/learn-to-code/Pip-and-virtualenv-on-Windows/)
# Instalacion

### 1. Bajar el zip
Obtener el archivo de datos de:
[datos.gob.ar](https://datos.gob.ar/dataset/educacion-padron-oficial-establecimientos-educativos)

Descomprimir el zip **mae_actualizado\_AAAA\_MM\_DD.zip** y abrir un cmd (o terminal)
en ese directorio.

### 2. Crear la base (y el usuario si no existe)
mysql -u root -p  
msyql> create database tusi;  
msyql> use tusi;  
mysql> ALTER DATABASE tusi CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;  
mysql> create user 'tssi'@'%' identified by 'tssi-2020';  
mysql> grant all privileges on tusi.* to 'tssi'@'%' identified by 'tssi-2020';  

### 3. Cargar csv a la base
3.1. Crear table DatosBase  
mysql -u tssi -p  
mysql> use tusi;  
mysql> source sql/tables/DatosBase.sql  
mysql> source sql/load/loadcsv.sql  
Query OK, 63390 rows affected, 4 warnings (1.81 sec)  
Records: 63390  Deleted: 0  Skipped: 0  Warnings: 4  

mysql> select count(*) from DatosBase;  
+----------+  
| count(*) |  
+----------+  
|    63390 |  
+----------+  


### 4. Creacion de tablas auxiliares
**4.1. Provincia:**  
mysql> source sql/tables/Provincia.sql  
Query OK, 0 rows affected (0.02 sec)  
mysql> source sql/load/provincias.sql  
mysql> select count(*) from Provincia;  
+----------+  
| count(*) |  
+----------+  
|       24 |  
+----------+  

**4.2 Ambito** 
mysql> source sql/tables/Ambito.sql    
mysql> source sql/load/ambitos.sql  
mysql> select count(*) from Ambito;  
+----------+  
| count(*) |  
+----------+  
|        3 |  
+----------+  

**4.3. Sector**  
mysql> source sql/tables/Sector.sql  
mysql> source sql/load/sectores.sql  
mysql> select count(*) from Sector;  
+----------+  
| count(*) |  
+----------+  
|        3 |  
+----------+  

**4.3. Departamento**  
mysql> source sql/tables/Departamento.sql  
mysql> source sql/load/departamentos.sql  
mysql> select count(*) from Departamento;  
+----------+  
| count(*) |  
+----------+  
|      527 |  
+----------+  

**4.4. Localidad**  
mysql> source sql/tables/Localidad.sql  
mysql> source sql/load/localidades.sql  
mysql> select count(*) from Localidad;  

| count(*) |
|:--------:|
|     9020 |

**4.5. Mail y Telefono**  
mysql> source sql/tables/MailTel.sql  
Nota: Crea la tabla y carga los Datos  


### 5. Stored Procedures
**5.1. Provincia**  
mysql> source sql/procedures/getProvincia.sql  
mysql> call getProvincia(1);  
+----+--------------+  
| id | nombre       |  
+----+--------------+  
|  1 | Buenos Aires |  
+----+--------------+  

**5.2. Ambito**  
mysql> source sql/procedures/getAmbito.sql  
mysql> call getAmbito(1)  
+----+--------+  
| id | nombre |  
+----+--------+  
|  1 | Urbano |  
+----+--------+  

**5.3. Sector**  
mysql> source sql/procedures/getSector.sql    
mysql> call getSector(1);  
+----+---------+  
| id | nombre  |
+----+---------+  
|  1 | Estatal |  
+----+---------+  

**5.4. Departamento**  

**5.4.1. Por Provincia**  

mysql> source sql/procedures/getDeptPcia.sql  
mysql> call getDeptPcia(24);  
+-----+----------------+  
| id  | nombre         |  
+-----+----------------+  
| 511 | BURRUYACU      |  
| 512 | CAPITAL        |  
| 513 | CHICLIGASTA    |  
| 514 | CRUZ ALTA      |  
| 515 | FAMAILLA       |  
| 516 | GRANEROS       |  
| 517 | JUAN B ALBERDI |  
| 518 | LA COCHA       |  
| 519 | LEALES         |  
| 520 | LULES          |  
| 521 | MONTEROS       |  
| 522 | RIO CHICO      |  
| 523 | SIMOCA         |  
| 524 | TAFI DEL VALLE |  
| 525 | TAFI VIEJO     |  
| 526 | TRANCAS        |  
| 527 | YERBA BUENA    |  
+-----+----------------+  
17 rows in set (0.00 sec)  

**5.4.2. Por Departamento id**

mysql> source sql/procedures/getDeptId.sql  
mysql> call getDeptId(527);  
+-----+-------------+-------------+  
| id  | idProvincia | nombre      |  
+-----+-------------+-------------+  
| 527 |          24 | YERBA BUENA |  
+-----+-------------+-------------+  

**5.5. Localidad**

**5.5.1. Por Provincia**

mysql> source sql/procedures/getLocalPcia.sql  
mysql> call getLocalPcia(23);  
+------+----------------+----------+-----------------------+  
| id   | idDepartamento | codigo   | nombre                |  
+------+----------------+----------+-----------------------+  
| 8558 |            508 | 94028004 | BASE ESPERANZA        |  
| 8559 |            509 | 94007012 | CULLEN                |  
| 8560 |            509 | 94007058 | ESTANCIA MARIA BEHETY |  
| 8561 |            509 | 94007078 | ESTANCIA SARA         |  
| 8562 |            509 | 94007152 | RIO GRANDE            |  
| 8563 |            509 | 94007153 | TOLHUIN               |  
| 8564 |            509 | 94007154 | SAN SEBASTIAN         |  
| 8565 |            510 | 94014022 | LAGUNA ESCONDIDA      |  
| 8566 |            510 | 94014024 | PUESTO ALMANZA        |  
| 8567 |            510 | 94014028 | USHUAIA               |  
+------+----------------+----------+-----------------------+  

**5.5.2. por Departamento**

mysql> source sql/procedures/getLocalDept.sql  
mysql> call getLocalDept(510);  
+------+----------+------------------+  
| id   | codigo   | nombre           |  
+------+----------+------------------+  
| 8565 | 94014022 | LAGUNA ESCONDIDA |  
| 8566 | 94014024 | PUESTO ALMANZA   |  
| 8567 | 94014028 | USHUAIA          |  
+------+----------+------------------+  

**5.5.3. por ID**

mysql> source sql/procedures/getLocalId.sql  
mysql> call getLocalId(8567);  
+------+----------------+----------+---------+  
| id   | idDepartamento | codigo   | nombre  |  
+------+----------------+----------+---------+  
| 8567 |            510 | 94014028 | USHUAIA |  
+------+----------------+----------+---------+  


### 6. Escuela
**6.1. Crear la tabla Escuela**

mysql> source sql/tables/Escuela.sql  
mysql> source sql/load/escuelas.sql  
mysql> select count(*) from Escuela;  
+----------+  
| count(*) |  
+----------+  
|    63387 |  
+----------+  

**6.2. Escuelas por Id**
 
mysql> source sql/procedures/getEscuelaXId.sql  
mysql> call getEscuelaXId(1);  

**6.3 Escuelas por Localidad**

mysql> source sql/procedures/getEscuelasXLoc.sql  
mysql> call getEscuelasXLoc(511);  


### 7. Educacion, tablas de referencia

**7.1. TipoEducacion**

mysql> source sql/tables/TipoEducacion.sql  
mysql> source sql/load/tiposeducacion.sql  
mysql> select * from TipoEducacion order by id;  
+----+---------------------------+  
| id | nombre                    |  
+----+---------------------------+  
|  1 | Comun                     |  
|  2 | Especial                  |  
|  3 | Adultos                   |  
|  4 | Artistica                 |  
|  5 | Hospitalaria_Domiciliaria |  
|  6 | Intercultural_Bilingue    |  
|  7 | Contexto_de_Encierro      |  
|  8 | Servicios_Complementarios |  
+----+---------------------------+  

**7.2 NivelEducacion**

mysql> source sql/tables/NivelEducacion.sql  
mysql> source sql/load/niveleseducacion.sql  
mysql> select * from NivelEducacion order by id;  
+----+--------------------------------+  
| id | nombre                         |  
+----+--------------------------------+  
|  1 | Jardin_maternal                |  
|  2 | Inicial                        |  
|  3 | Primaria                       |  
|  4 | Secundaria                     |  
|  5 | Secundaria_Tecnica_INET        |  
|  6 | Superior_no_Universitario      |  
|  7 | Superior_No_Universitario_INET |  
|  8 | Cursos_y_Talleres              |  
|  9 | Temprana                       |  
| 10 | Integración                    |  
| 11 | EGB3                           |  
| 12 | Alfabetización                 |  
| 13 | Formación_Profesional          |  
| 14 | Formación_Profesional_INET     |  
+----+--------------------------------+  

**7.3. TipoNivelEducacion**

mysql> source sql/tables/TipoNivelEducacion.sql  
mysql> source sql/load/tiposniveleseducacion.sql  
112 Records  

Nota: Revisar q no haya quedado procedures sin crear  
  
### 8. Educacion, views

mysql> source sql/views/comun.sql  
mysql> source sql/views/especial.sql  
mysql> source sql/views/adultos.sql  
mysql> source sql/views/arte.sql  
mysql> source sql/views/hospital.sql  
mysql> source sql/views/encierro.sql  
mysql> source sql/views/bilingue.sql  
mysql> source sql/views/servicios.sql  

### 9. Educacion, Tabla concentradora

mysql> source sql/tables/TedNivEscuela.sql  
mysql> source sql/load/tednivescuelas.sql(tarda...)  
Query OK, 85216 rows affected (14.66 sec)  
Records: 85216  Duplicates: 0  Warnings: 0  

### 10. Procedures

mysql> source sql/procedures/getEducEscuela.sql  
mysql> call getEducEscuela(10404);  
+-------+---------------------------+-------------------------+  
| id    | Tipo                      | Nivel                   |  
+-------+---------------------------+-------------------------+  
| 68489 | Especial                  | Primaria                |  
| 69209 | Especial                  | Secundaria              |  
| 70520 | Especial                  | Secundaria_Tecnica_INET |  
| 67874 | Especial                  | Temprana                |  
| 71541 | Especial                  | Integración             |  
| 72755 | Hospitalaria_Domiciliaria | Inicial                 |  
| 72849 | Hospitalaria_Domiciliaria | Primaria                |  
| 72970 | Hospitalaria_Domiciliaria | Secundaria              |  
+-------+---------------------------+-------------------------+  
8 rows in set (0.00 sec)

mysql> select Codigo from Escuela where id =  
 10404;  
+-----------+  
| Codigo    |  
+-----------+  
| 061155700 |  
+-----------+  

mysql> select * from DatosBase where CUE_Anexo = '061155700' \G  
*************************** 1. row ***************************  
                           Jurisdiccion: Buenos   Aires  
                              CUE_Anexo: 061155700  
                                 Nombre: ESCUELA ESPECIAL Nº502  
                                 Sector: Estatal
                                 Ámbito: Urbano
                              Domicilio: ATAHUALPA YUPANQUI 104    
                                     CP: 1862  
                         Código_de_area: 02224  
                               Telefono: 47-7976  
                       Codigo_localidad: 06648001  
                              Localidad: GUERNICA  
                           Departamento: PRESIDENTE PERON  
                                   Mail: eee502guernica@gmail.com; ee129502@abc.gov.ar  
                               Ed_Comun:   
                            Ed_Especial: X  
                             Ed_Adultos:   
                           Ed_Artistica: 
           Ed_Hospitalaria_Domiciliaria: X  
              Ed_Intercultural_Bilingue:   
                Ed_Contexto_de_Encierro:     
               Ed_Comun_Jardin_maternal:     
                       Ed_Comun_Inicial:  
                      Ed_Comun_Primaria:   
                    Ed_Comun_Secundaria:   
       Ed_Comun_Secundaria_Tecnica_INET:   
     Ed_Comun_Superior_no_Universitario:   
Ed_Comun_Superior_No_Universitario_INET:   
                Ed_Artistica_Secundaria:   
 Ed_Artistica_Superior_no_Universitario:   
         Ed_Artistica_Cursos_y_Talleres:   
         Ed_Especial_Educación_Temprana: X  
                    Ed_Especial_Inicial: X  
                   Ed_Especial_Primaria: X  
                 Ed_Especial_Secundaria: X  
                Ed_Especial_Integración: X  
                    Ed_Adultos_Primaria:   
                        Ed_Adultos_EGB3:   
                  Ed_Adultos_Secundaria:   
             Ed_Adultos_Alfabetización:   
      Ed_Adultos_Formación_Profesional:   
Ed_Adultos_Formación_Profesional_INET_:   
   Ed_Hospitalaria_Domiciliaria_Inicial: X  
  Ed_Hospitalaria_Domiciliaria_Primaria: X  
Ed_Hospitalaria_Domiciliaria_Secundaria: X  
              Servicios_complementarios:   


## Modulos Python:
**columns.py**  
**sesiones.py**  
**tables.py**  
**views.py** 
** util.py**  

##Rutas
localhost:5000/  
localhost:5000/version  
localhost:5000/provincias  
localhost:5000/provincia/23  
localhost:5000/sectores  
localhost:5000/sector/3  
localhost:5000/ambitos  
localhost:5000/ambito/1  
localhost:5000/tiposeducacion  
localhost:5000/tipoeducacion/4  
localhost:5000/niveleseducacion  
localhost:5000/niveleducacion/11  
localhost:5000/tiposniveleseducacion  
localhost:5000/tiponiveleseducacion/5  
localhost:5000/escuelasxlocalidad/915  
localhost:5000/escuelaxid/10404  
localhost:5000/tedescuelas/10404  
localhost:5000/localidades/23  
localhost:5000/localidadesxdepto/915  
localhost:5000/localidad/1000  
localhost:5000/departamentos/1  
localhost:5000/departamento/18  
localhost:5000/cargar/escuela  
localhost:5000/cargar/departamento  
localhost:5000/cargar/sector  


#### Nota de desarrollo
En la primera version, la generacion de datos en json se hacia 
en cada uno de los modulos.
Con el uso de la informacion disponible en el objeto **cursor.description** se creo una funcion
generica que genera json pasandole los datos y la descripcion del cursor.

La idea es utilizar la metadata q tiene la base de datos en
el schema **information_schema**.
Y tambien la metadata que tienen los objetos relacionados a 
la conexion a la base y sus funciones.

La url es **localhost:5000/tabla/<nombre la tabla>**
A mejorar: Hay q nombrar la tabla exactamente igual a como 
se llama en la base. O sea, **case sensitive**.

La url **localhost:5000/cargar/<nombre de la tabla>**
genera un form para cargar datos de la tabla.
Solo esta la generacion de un form basico y es solo un ejemplo de como usar la metadata obtenida de la descripcion de un cursor para automatizar la generacion de codigo. En este caso, forms HTML basicos.

Lo siguiente seria enviar los datos del form de carga
a la base de datos.
Para eso hay q agregarle al form la accion a realizar Y
capturar el metodo POST con su data.
```

## Test

Manual. No se utilizo TDD

### Break down into end to end tests


## Autores

* **Juan Arce** - Trabajo Inicial* - [github](https://github.com/cogorcho)

**Participantes**  
*   **Manuel Cepeda**  
*   **Gianluca Sparvoli**  
*   **Gaston Albornoz**  
*   **Virginia Molinelli**  
   **Nicolas D'Imperio**  

## Licencia

Totalmente libre

## Agradeciemientos
    A Manuel Cepeda, Gianluca Sparvoli, Gaston Albornoz, Virginia Molinelli 
    y Nicolas D'Imperio.