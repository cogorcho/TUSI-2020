-- --------------------------------------
-- TSSI-2020. administracion de BD
-- DDL: Create table
-- Tabla: Provincia 
-- --------------------------------------
create table if not exists Provincia (
    id INT NOT NULL AUTO_INCREMENT,
    nombre varchar(128) NOT NULL,
    PRIMARY KEY (id)
);

create unique index uidx_Provincia on Provincia(nombre);