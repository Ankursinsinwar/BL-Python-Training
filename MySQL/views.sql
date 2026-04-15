use Learning;

# 12.	Views

CREATE VIEW name_GPA AS
SELECT sName as name, GPA
FROM Student;

select * from name_GPA;

drop view name_GPA;

CREATE VIEW SA AS
SELECT Student.sName, Apply.cName, Apply.major
FROM Student
iNNER JOIN Apply
ON Student.sID = Apply.sID;

select * from SA;

CREATE VIEW TOPERCLG AS
SELECT cName 
FROM Apply
WHERE sID IN (
	select sID 
    from Student 
    where GPA = (
		SELECT MAX(GPA) FROM Student
	)
);

select * from TOPERCLG;
