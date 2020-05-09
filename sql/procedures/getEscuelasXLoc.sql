DELIMITER //

DROP PROCEDURE IF EXISTS getEscuelasXLoc;

CREATE PROCEDURE getEscuelasXLoc(locID INT)
BEGIN
    SELECT 
        e.id          
        ,e.idLocalidad 
        ,l.nombre
        ,e.idSector
        ,s.nombre  
        ,e.idAmbito
        ,a.nombre   
        ,e.codigo     
        ,e.nombre     
        ,e.domicilio  
        ,e.codpos
        ,mt.telefono
        ,mt.mail   
    from Escuela e
    inner join MailTel mt 
        on mt.id = e.id
    inner join Localidad l 
        on l.id = e.idLocalidad
    inner join Sector s
        on s.id = e.idSector
    inner join Ambito a
        on a.id = e.idSector 
    where idLocalidad = locID;
END //

DELIMITER ;