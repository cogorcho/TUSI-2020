DELIMITER //

DROP PROCEDURE IF EXISTS getEscuelaXId;

CREATE PROCEDURE getEscuelaXId(eID INT)
BEGIN
    SELECT 
        e.id          
        ,e.idLocalidad 
        ,l.nombre as nombreLocalidad
        ,e.idSector
        ,s.nombre  as nombreSector
        ,e.idAmbito
        ,a.nombre   as nombreAmbito
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
    where e.id = eID;
END //

DELIMITER ;