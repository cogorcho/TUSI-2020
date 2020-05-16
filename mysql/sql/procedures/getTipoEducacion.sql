DELIMITER //

DROP PROCEDURE IF EXISTS getTipoEducacion;

CREATE PROCEDURE getTipoEducacion(tedID INT)
BEGIN
    IF tedID = -1 THEN
        SELECT id, nombre from TipoEducacion order by nombre;
    ELSE
        SELECT id, nombre from TipoEducacion where id = tedID;
    END IF;
END //

DELIMITER ;