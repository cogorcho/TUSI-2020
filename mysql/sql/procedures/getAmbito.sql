DELIMITER //

DROP PROCEDURE IF EXISTS getAmbito;

CREATE PROCEDURE getAmbito(pciaID INT)
BEGIN
    IF pciaID = -1 THEN
        SELECT id, nombre from Ambito order by nombre;
    ELSE
        SELECT id, nombre from Ambito where id = pciaID;
    END IF;
END //

DELIMITER ;