DELIMITER //

DROP PROCEDURE IF EXISTS getViews;

CREATE PROCEDURE getViews()
BEGIN
    select table_name as view_name
    from information_schema.tables 
    where table_schema = DATABASE()
    and table_type = 'VIEW'
    order by table_name;
END //

DELIMITER ;