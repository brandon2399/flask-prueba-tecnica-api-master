select * from mascotas;

select * from mascotas where propietario is null;

select
    count(*),
    tm.descripcion 
from
    mascotas m
inner join tipo_mascota tm on
    m.tipo_mascota = tm.idtipo_mascota
group by
    tm.descripcion;
                
select
    p.nombre,
    count(*)
from
    mascotas m
inner join propietario p on
    m.propietario = p.idpropietario
group by
    p.nombre
having
    count(*)>1;
                
               
               
select
    p.nombre ,
    tm.descripcion ,
    count(*)
from
    propietario p
inner join mascotas m on
    p.idpropietario = m.propietario
inner join tipo_mascota tm on
    m.tipo_mascota = tm.idtipo_mascota 
group by 
p.nombre,tm.descripcion 
;
            
   
   
select
    p.nombre
from
    propietario p
except 
select
    p.nombre
from
    propietario p
inner join mascotas m on
    p.idpropietario = m.propietario ;