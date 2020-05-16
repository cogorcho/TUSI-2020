-- --------------------------------------
-- TSSI-2020. administracion de BD
-- DDL: Create table
-- Tabla: Ambito
-- --------------------------------------
create table Ambito (
    id INT NOT NULL AUTO_INCREMENT,
    nombre varchar(256) not null,
    Primary key (id)
);

create unique index uidx_Ambito
on Ambito(nombre);