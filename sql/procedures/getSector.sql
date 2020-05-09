DELIMITER //

DROP PROCEDURE IF EXISTS getSector;

CREATE PROCEDURE getSector(pciaID INT)
BEGIN
    IF pciaID = -1 THEN
        SELECT id, nombre from Sector order by nombre;
    ELSE
        SELECT id, nombre from Sector where id = pciaID;
    END IF;
END //

DELIMITER ;