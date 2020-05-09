DELIMITER //

DROP PROCEDURE IF EXISTS getDeptId;

CREATE PROCEDURE getDeptId(depID INT)
BEGIN
    SELECT 
        d.id
        , d.idProvincia as idProvincia
        , p.nombre as nombreProvincia
        , d.nombre 
    from Departamento d 
    inner join Provincia p
        on p.id = d.idProvincia
    where d.id = depID;
END //

DELIMITER ;