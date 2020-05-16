-- --------------------------------------
-- TSSI-2020. administracion de BD
-- DDL: Create table
-- Tabla: Nivel 
-- --------------------------------------
drop table if Exists Nivel;

create table if not exists Nivel (
    id INT NOT NULL AUTO_INCREMENT,
    nombre varchar(128) NOT NULL,
    PRIMARY KEY (id)
);

-- --------------------------------------
-- TSSI-2020. administracion de BD
-- DDL: Create unique index
-- Tabla: Nivel
-- Para q no se repita el nombre y 
-- para acceder mas rapido
-- --------------------------------------
create unique index uidx_Nivel on Nivel(nombre);


insert into Nivel(nombre) values 
('Jardin_maternal'),                
('Inicial'),                        
('Primaria'),                       
('Secundaria'),                     
('Secundaria_Tecnica_INET'),        
('Superior_no_Universitario'),      
('Superior_No_Universitario_INET'), 
('Cursos_y_Talleres'),   
('Temprana'),          
('Integración'),                 
('EGB3'),                         
('Alfabetización'),               
('Formación_Profesional'),        
('Formación_Profesional_INET_')  
;
