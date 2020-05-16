#!/bin/bash
#-------------------------------------#
#
# Creacion de la BD del proyecto
#
#-------------------------------------#

FECHA=`date +"%Y%m%d%H%M%S"`
LOGFILE="crdb_$[FECHA].log"

TIEMPO=`date +"%Y-%m-%d-%H:%M:%S"`
echo "Crear Base: ${TIEMPO}"
mysql -u root -pneheik <<EOF 2>$LOGFILE
source createdb.sql
source createuser.sql
EOF

TIEMPO=`date +"%Y-%m-%d-%H:%M:%S"`
echo "Datos base: ${TIEMPO}" 
mysql -u tusi2 -ptusi2-2020 tusi2 <<EOF2 2>>$LOGFILE
source datosbase.sql
EOF2

TIEMPO=`date +"%Y-%m-%d-%H:%M:%S"`
echo "Crear tablas: ${TIEMPO}"
mysql -u tusi2 -ptusi2-2020 tusi2 <<EOF3 2>>$LOGFILE
source sql/tables/Provincia.sql
source sql/tables/Ambito.sql
source sql/tables/Sector.sql
source sql/tables/Departamento.sql
source sql/tables/Localidad.sql
source sql/tables/Escuela.sql
source sql/tables/MailTel.sql
source sql/tables/TipoEducacion.sql
source sql/tables/NivelEducacion.sql
source sql/tables/TipoNivelEducacion.sql
source sql/tables/TedNivEscuela.sql
EOF3

TIEMPO=`date +"%Y-%m-%d-%H:%M:%S"`
echo "Crear views: ${TIEMPO}"
mysql -u tusi2 -ptusi2-2020 tusi2 <<EOF4 2>>$LOGFILE
source sql/views/adultos.sql
source sql/views/arte.sql
source sql/views/bilingue.sql
source sql/views/comun.sql
source sql/views/encierro.sql
source sql/views/especial.sql
source sql/views/hospital.sql
source sql/views/servicios.sql
EOF4

TIEMPO=`date +"%Y-%m-%d-%H:%M:%S"`
echo "Carga de datos: ${TIEMPO}"
mysql -u tusi2 -ptusi2-2020 tusi2 <<EOF5 2>>$LOGFILE
source sql/load/provincias.sql
source sql/load/sectores.sql
source sql/load/ambitos.sql
source sql/load/departamentos.sql
source sql/load/localidades.sql
source sql/load/escuelas.sql
source sql/load/tiposeducacion.sql
source sql/load/niveleseducacion.sql
source sql/load/tiposniveleseducacion.sql
source sql/load/tednivescuelas.sql
EOF5

TIEMPO=`date +"%Y-%m-%d-%H:%M:%S"`
echo "Control de datos: ${TIEMPO}"
mysql -u tusi2 -ptusi2-2020 tusi2 <<EOF6 2>>$LOGFILE
select count(*) as Ambto from Ambito        ;
select count(*) as Sector from Sector        ;
select count(*) as Provincia from Provincia     ;
select count(*) as Departamento from Departamento  ;
select count(*) as Localidad from Localidad     ;
select count(*) as Escuela from Escuela       ;
select count(*) as MailTel from MailTel       ;
select count(*) as TipoEducacion from TipoEducacion ;
select count(*) as NivelEducacion from NivelEducacion;
select count(*) as TipoNivelEducacion from TipoNivelEducacion;
select count(*) as TedNIvelEscuela from TedNivEscuela ;
EOF6

TIEMPO=`date +"%Y-%m-%d-%H:%M:%S"`
echo "Listo: ${TIEMPO}"

