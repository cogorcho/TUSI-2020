DELIMITER //

DROP PROCEDURE IF EXISTS getEducEscuela;

CREATE PROCEDURE getEducEscuela(eID INT)
BEGIN
    select
        tnes.id, 
        ted.id as idTipoEducacion,
        ted.nombre as Tipo,
        ned.id as idNivelEducacion,
        ned.nombre as Nivel         
    from TedNivEscuela tnes
    inner join TipoNivelEducacion tned
        on tned.id = tnes.idTipoNivel
    inner join TipoEducacion ted 
        on ted.id = tned.idTipoEducacion
    inner join NivelEducacion ned 
        on ned.id = tned.idNivelEducacion
    where tnes.idEscuela = eID;

END //

DELIMITER ;