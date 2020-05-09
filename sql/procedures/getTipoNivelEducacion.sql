DELIMITER //

DROP PROCEDURE IF EXISTS getTipoNivelEducacion;

CREATE PROCEDURE getTipoNivelEducacion(tedID INT)
BEGIN
    IF tedID = -1 THEN
        SELECT 
            tne.id as ID, 
            ted.id as idTipoEducacion, 
            ted.nombre as nombreTipoEducacion, 
            ne.id as idNivelEducacion, 
            ne.nombre as nombreNivelEducacion
        from TipoNivelEducacion as tne
        inner join  TipoEducacion as ted
            on ted.id = tne.idTipoEducacion
        inner join NivelEducacion ne
            on ne.id = tne.idNivelEducacion
        order by tne.id;
    ELSE
        SELECT 
            tne.id as ID, 
            ted.id as idTipoEducacion, 
            ted.nombre as nombreTipoEducacion, 
            ne.id as idNivelEducacion, 
            ne.nombre as nombreNivelEducacion
        from TipoNivelEducacion as tne
        inner join  TipoEducacion as ted
            on ted.id = tne.idTipoEducacion
        inner join NivelEducacion ne
            on ne.id = tne.idNivelEducacion
        where ted.id = tedID
        order by tne.id;
    END IF;
END //

DELIMITER ;
