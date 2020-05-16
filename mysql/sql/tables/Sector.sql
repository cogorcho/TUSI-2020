-- --------------------------------------
-- TSSI-2020. administracion de BD
-- DDL: Create table
-- Tabla: Sector
-- --------------------------------------
create table Sector (
    id INT NOT NULL AUTO_INCREMENT,
    nombre varchar(256) not null,
    Primary key (id)
);

create unique index uidx_Sector
on Sector(nombre);