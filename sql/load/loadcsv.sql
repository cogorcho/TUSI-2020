-- --------------------------------------
-- TSSI-2020. administracion de BD
-- DDL: Load data from csv file
-- Tabla: DatosBase
-- Puede ser que LOAD no sea ni DDL ni DML
-- sino un extension de mysql.
-- --------------------------------------
LOAD DATA LOCAL INFILE 'sql/data/DatosBase.csv'
IGNORE INTO TABLE DatosBase
CHARACTER SET UTF8
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
