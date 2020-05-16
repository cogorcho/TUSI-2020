DELIMITER //

DROP PROCEDURE IF EXISTS getLocalDept;

CREATE PROCEDURE getLocalDept(deptID INT)
BEGIN
    SELECT id, idDepartamento, codigo, nombre 
    from Localidad 
    where idDepartamento = deptID;
END //

DELIMITER ;