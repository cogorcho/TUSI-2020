DELIMITER //

DROP PROCEDURE IF EXISTS getSesiones;

CREATE PROCEDURE getSesiones()
BEGIN
    select id,user,host,db,command,time,state,info from information_schema.processlist;
END //

DELIMITER ;