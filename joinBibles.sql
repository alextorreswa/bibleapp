CREATE TABLE joinBibles AS
SELECT 'American Standard' AS Bible, 't_asv' AS idBible, * 
FROM t_asv 
UNION
SELECT 'Bible in Basic English' AS Bible, 't_bbe' AS idBible, *  
FROM t_bbe 
UNION
SELECT 'King James Version' AS Bible, 't_kjv' AS idBible, *  
FROM t_kjv 
UNION
SELECT 'World English Bible' AS Bible, 't_web' AS idBible, *  
FROM t_web 
UNION
SELECT 'Young''s Literal Translation' AS Bible, 't_ylt' AS idBible, *  
FROM t_ylt;