DROP TABLE IF EXISTS Bibles;
CREATE TABLE bibles AS
SELECT joinBibles.bible, joinBibles.idBible ,joinBibles.id AS idVerser, joinBibles.b AS idBook, joinbibles.c AS idChapter, joinbibles.t AS verse, title_short AS book
FROM joinBibles 
JOIN book_info 
ON book_info."order" = joinBibles.b;