DELIMITER //

DROP PROCEDURE IF EXISTS getNivelEducacion;

CREATE PROCEDURE getNivelEducacion(nivID INT)
BEGIN
    IF nivID = -1 THEN
        SELECT id, nombre from NivelEducacion order by nombre;
    ELSE
        SELECT id, nombre from NivelEducacion where id = nivID;
    END IF;
END //

DELIMITER ;