SELECT * FROM esquema_dojo_ninjas.dojos;
INSERT INTO dojos (nombre)
VALUES ("Chicago"), ("Seattle"),("Online");

INSERT INTO ninjas (nombre,apellido,edad,dojos_id)
VALUES ("Marisa","Goode",37,5),("Todd","Enders",36,5),("Sadie","Flick",29,5);

INSERT INTO ninjas (nombre,apellido,edad,dojos_id)
VALUES ("Adrien","Dion",39,4),("Anne","Jurack",34,4),("Ryan","Magley",30,4);

INSERT INTO ninjas (nombre,apellido,edad,dojos_id)
VALUES ("Mr. Nibbles","Pancakes",54,6),("Benny Bob","McBob",65,6),("Mitch","Golden",26,6);

SELECT *
FROM dojos
LEFT JOIN ninjas ON dojos.id = ninjas.dojos_id
WHERE dojos.id = 4;

SELECT * FROM dojos
WHERE dojos.id = (SELECT dojos_id FROM ninjas ORDER BY dojos_id DESC LIMIT 1);

SELECT * FROM dojos
LEFT JOIN ninjas ON dojos.id = ninjas.dojos_id
	WHERE dojos.id = (SELECT id FROM dojos ORDER BY id DESC LIMIT 1);

SELECT * FROM dojos;

SELECT nombre, COUNT(*) as cantidad
FROM dojos
GROUP BY nombre
HAVING COUNT(*) > 1;

DELETE FROM dojos
WHERE nombre IN (
    SELECT nombre
    FROM dojos
    GROUP BY nombre
    HAVING COUNT(*) > 1
);


CREATE TEMPORARY TABLE temp_duplicados AS (
    SELECT nombre
    FROM dojos
    GROUP BY nombre
    HAVING COUNT(*) > 1
);

DELETE FROM dojos
WHERE nombre IN (
    SELECT nombre
    FROM temp_duplicados
);

DELETE FROM ninjas
WHERE dojos_id IN (
    SELECT id
    FROM dojos
    WHERE nombre IN (
        SELECT nombre
        FROM temp_duplicados
    )
);

sql
Copy code
DELETE FROM dojos
WHERE nombre IN (
    SELECT nombre
    FROM temp_duplicados
);

DELETE FROM ninjas
WHERE dojos_id IN (
    SELECT id
    FROM dojos
    WHERE nombre IN (
        SELECT nombre
        FROM temp_duplicados
    )
);

DELETE FROM dojos
WHERE nombre IN (
    SELECT nombre
    FROM temp_duplicados
);

SELECT * FROM esquema_dojo_ninjas.dojos;
INSERT INTO dojos (nombre)
VALUES ("Chicago"), ("Seattle"),("Online");


INSERT INTO ninjas (nombre,apellido,edad,dojos_id)
VALUES ("Marisa","Goode",37,111),("Todd","Enders",36,111),("Sadie","Flick",29,111);

INSERT INTO ninjas (nombre,apellido,edad,dojos_id)
VALUES ("Adrien","Dion",39,112),("Anne","Jurack",34,112),("Ryan","Magley",30,112);


INSERT INTO ninjas (nombre,apellido,edad,dojos_id)
VALUES ("Mr. Nibbles","Pancakes",54,113),("Benny Bob","McBob",65,113),("Mitch","Golden",26,113);