-- --------------------------------------
-- TSSI-2020. administracion de BD
-- DDL: Create table
-- Tabla: NivelEducacion
-- --------------------------------------
drop table if exists TipoNivelEducacion;

create table TipoNivelEducacion (
    id INT NOT NULL AUTO_INCREMENT,
    idTipoEducacion INT NOT NULL,
    idNivelEducacion INT NOT NULL,
    Primary key (id),
    CONSTRAINT fk_nte_te FOREIGN KEY (idTipoEducacion) REFERENCES TipoEducacion(id),
    CONSTRAINT fk_nte_niv FOREIGN KEY (idNivelEducacion) REFERENCES NivelEducacion(id)
);

create unique index uidx_TipoNivelEducacion
on TipoNivelEducacion(idTipoEducacion,idNivel);
