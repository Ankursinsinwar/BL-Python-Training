use Learning;

#	Aggregate Functions 


select count(*) from Student;

select * from Student
order by GPA desc
limit 1 offset 3;

select sID 
    from Student 
    where GPA = (
		SELECT MAX(GPA) FROM Student
	);

SELECT sName, GPA FROM Student
where GPA =  ( select MIN(GPA) from Student
);

select SUM(GPA) from Student where GPA = (select MIN(GPA) from Student);

select AVG(GPA) from Student;


select count(sName) from Student
where GPA = (select MAX(GPA) from Student);


SELECT sizeHS, SUM(GPA) AS total
FROM student
GROUP BY sizeHS
HAVING SUM(GPA) > 3.9;

