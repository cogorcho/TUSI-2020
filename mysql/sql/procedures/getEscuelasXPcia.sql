DELIMITER //

DROP PROCEDURE IF EXISTS getEscuelasXPcia;

CREATE PROCEDURE getEscuelasXPcia(pciaID INT)
BEGIN
    select 
        e.id as idEscuela,
        e.nombre as nombreEscuela,
        p.id as idProvincia,
        p.nombre as nombrePcia,
        l.id as idLocalidad,
        l.nombre as nombreLocalidad
    from Escuela e
    inner join Localidad l
        on l.id = e.idLocalidad
    inner join Departamento d
        on d.id = l.id
    inner join Provincia p
        on d.idProvincia = p.id
    where p.id = pciaID
    order by e.nombre;
END //

DELIMITER ;

