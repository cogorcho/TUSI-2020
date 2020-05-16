-- --------------------------------------
-- TSSI-2020. administracion de BD
-- DDL: Create table
-- Tabla: TipoEducacion
-- --------------------------------------
create table TipoEducacion (
    id INT NOT NULL AUTO_INCREMENT,
    nombre varchar(256) not null,
    Primary key (id)
);

create unique index uidx_TipoEducacion
on TipoEducacion(nombre);