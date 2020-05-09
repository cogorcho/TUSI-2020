insert into TipoNivelEducacion (idTipoEducacion, idNivel)
select te.id, ni.id
from TipoEducacion te, NivelEducacion ni 
order by 1,2;