DELIMITER //

DROP PROCEDURE IF EXISTS getDeptPcia;

CREATE PROCEDURE getDeptPcia(pciaID INT)
BEGIN
    SELECT 
        d.id 
        ,d.idProvincia as idProvincia
        ,p.nombre as nombreProvincia
        ,d.nombre 
    from Departamento d
    inner join Provincia p
        on p.id = d.idProvincia
    where d.idProvincia = pciaID;
END //

DELIMITER ;