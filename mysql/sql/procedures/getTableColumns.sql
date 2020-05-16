DELIMITER //

DROP PROCEDURE IF EXISTS getTableColumns;

CREATE PROCEDURE getTableColumns(IN pTab varchar(64))
BEGIN
    select 
        ordinal_position
        , column_name 
        , is_nullable
        , data_type
        , character_maximum_length
        , character_octet_length
        , character_set_name
    from information_schema.columns 
    where table_schema = DATABASE()
    and upper(table_name) = upper(pTab)
    order by ordinal_position;
END //

DELIMITER ;

