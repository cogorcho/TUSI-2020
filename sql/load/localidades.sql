-- --------------------------------------
-- TSSI-2020. administracion de BD
-- DML: Insert into table
-- Tabla: Localidad
-- Generar data, FK 
-- --------------------------------------
insert into Localidad(idDepartamento, codigo, nombre)
select distinct Departamento.id, DatosBase.Codigo_Localidad, DatosBase.Localidad
from DatosBase
inner join Departamento
on Departamento.nombre = DatosBase.Departamento
inner join Provincia
on Provincia.nombre = DatosBase.Jurisdiccion
and Departamento.idProvincia = Provincia.id
order by 1,2,3;
