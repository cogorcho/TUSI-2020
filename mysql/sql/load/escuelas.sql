insert into Escuela
(idLocalidad,idSector,idAmbito,codigo,nombre,domicilio,codpos)     
select l.id, a.id, s.id, b.CUE_Anexo, b.nombre,
    b.Domicilio, b.cp
from DatosBase b 
inner join Departamento d
on d.nombre = b.Departamento
inner join Provincia p
on p.nombre = b.Jurisdiccion
and p.id = d.idProvincia
inner join Localidad l
on l.nombre = b.localidad
and l.codigo = b.codigo_localidad
and l.idDepartamento = d.id
inner join Sector s
on s.nombre = b.sector
inner join Ambito a
on a.nombre = b.Ambito;