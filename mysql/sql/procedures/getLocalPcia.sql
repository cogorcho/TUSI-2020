DELIMITER //

DROP PROCEDURE IF EXISTS getLocalPcia;

CREATE PROCEDURE getLocalPcia(pciaID INT)
BEGIN
    SELECT l.id, l.idDepartamento, l.codigo, l.nombre 
    from Localidad l
    inner join Departamento d
        on d.id = l.idDepartamento
        and idProvincia = pciaID;
END //

DELIMITER ;