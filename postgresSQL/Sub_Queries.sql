use Learning;

# Sub Queres

SELECT sName FROM Student
WHERE sID IN (
    SELECT sID FROM Apply 
    WHERE cName = 'Stanford'
);

SELECT cName 
FROM Apply
WHERE sID IN (
	select sID 
    from Student 
    where GPA = (
		SELECT MAX(GPA) FROM Student
	)
);

