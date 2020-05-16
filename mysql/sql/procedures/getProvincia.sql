DELIMITER //

DROP PROCEDURE IF EXISTS getProvincia;

CREATE PROCEDURE getProvincia(pciaID INT)
BEGIN
    IF pciaID = -1 THEN
        SELECT id, nombre from Provincia order by nombre;
    ELSE
        SELECT id, nombre from Provincia where id = pciaID;
    END IF;
END //

DELIMITER ;