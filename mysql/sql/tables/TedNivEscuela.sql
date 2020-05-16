-- --------------------------------------
-- TSSI-2020. administracion de BD
-- DDL: Create table
-- Tabla: TedNivEscuela 
-- --------------------------------------
drop table if Exists TedNivEscuela;

create table TedNivEscuela (
    id INT NOT NULL AUTO_INCREMENT,
    idEscuela INT NOT NULL,
    idTipoNivel INT NOT NULL,
    Primary key (id),
    CONSTRAINT fk_TedNiv_Esc foreign key (idEscuela) references Escuela(id),
    CONSTRAINT fk_TedNiv_TedNiv foreign key (idTipoNivel) references TipoNivelEducacion(id)
);

create unique index uidx_esctednivel on TedNivEscuela(idEscuela,idTipoNivel);

