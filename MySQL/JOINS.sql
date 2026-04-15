use Learning;

## JOINs
desc Student;

# 1. Inner Join
SELECT Student.sName, Apply.cName, Apply.major
FROM Student
iNNER JOIN Apply
ON Student.sID = Apply.sID;

# 2. Right Join
SELECT Student.sName, Apply.cName, Apply.major
FROM Student
RIGHT JOIN Apply
ON Student.sID = Apply.sID;

# 3. Left Join
SELECT Student.sName, Apply.cName, Apply.major
FROM Student
Left JOIN Apply
ON Student.sID = Apply.sID;

# 2. Full Join
SELECT Student.sName, Apply.cName, Apply.major
FROM Student 
LEFT JOIN Apply ON Student.sID = Apply.sID
UNION
SELECT Student.sName, Apply.cName, Apply.major
FROM Student 
RIGHT JOIN Apply ON Student.sID = Apply.sID;
