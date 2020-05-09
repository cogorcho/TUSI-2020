DELIMITER //

DROP PROCEDURE IF EXISTS getLocalId;

CREATE PROCEDURE getLocalId(localID INT)
BEGIN
    SELECT id, idDepartamento, codigo, nombre 
    from Localidad 
    where id = localID;
END //

DELIMITER ;