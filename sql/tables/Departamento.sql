-- --------------------------------------
-- TSSI-2020. administracion de BD
-- DDL: Create table
-- Tabla: Departamento
-- --------------------------------------
create table Departamento (
    id INT NOT NULL AUTO_INCREMENT,
    idProvincia INT NOT NULL,
    nombre varchar(256) not null,
    Primary key (id),
    CONSTRAINT fk_depto_pcia foreign key (idProvincia)
    references Provincia(id)
);

create unique index uidx_Departamento
on Departamento(idProvincia, nombre);