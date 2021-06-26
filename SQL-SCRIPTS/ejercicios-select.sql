#TODAS LAS FRUTAS CUYO NOMBRE TERMIUNA EN a
SELECT * FROM mydb.producto 
WHERE idCategoria = 1 AND nombre LIKE "%a";
#LOS PRODUCTOS MAS CAROS
SELECT * FROM mydb.producto
ORDER BY precio DESC LIMIT 5;
#VEGETALES CUYOS PRECIO ESTÉ ENTRE 10 Y 12 
SELECT * FROM mydb.producto
WHERE idCategoria = 2 
AND precio BETWEEN 10 AND 12;
#CUANTO GANARIA SI VENDO TODO EL STOCK
SELECT SUM(precio * stock) AS TOTAL 
FROM mydb.producto;