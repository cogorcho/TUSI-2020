-- --------------------------------------
-- TSSI-2020. administracion de BD
-- DDL: Create table
-- Tabla: NivelEducacion
-- --------------------------------------
drop table if exists NivelEducacion;

create table NivelEducacion (
    id INT NOT NULL AUTO_INCREMENT,
    nombre varchar(256) not null,
    Primary key (id)
);

create unique index uidx_NivelEducacion
on NivelEducacion(nombre);