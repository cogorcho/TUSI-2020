

DELIMITER //

DROP PROCEDURE IF EXISTS getTables;

CREATE PROCEDURE getTables()
BEGIN
    select table_name 
    from information_schema.tables 
    where table_schema = DATABASE()
    and table_type = 'BASE TABLE'
    order by table_name;
END //

DELIMITER ;