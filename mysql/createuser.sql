drop user if exists 'tusi2'@'%';
create user 'tusi2'@'%' identified by 'tusi2-2020';
grant all privileges on tusi2.* to 'tusi2'@'%' identified by 'tusi2-2020';
