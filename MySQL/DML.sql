use Learning;

## DML (Data Manipulation Language)

# 1. INSERT
INSERT INTO Student (sID, sName, GPA, sizeHS, DoB) VALUES(123, 'Amy', 3.9, 1000, '1996-06-26'),
(234, 'Bob', 3.6, 1500, '1995-04-07'),
(345, 'Craig', 3.5, 500, '1995-02-04'),
(456, 'Doris', 3.9, 1000, '1997-07-24'),
(567, 'Edward', 2.9, 2000, '1996-12-21'),
(678, 'Fay', 3.8, 200, '1996-08-27'),
(789, 'Gary', 3.4, 800, '1996-10-08'),
(987, 'Helen', 3.7, 800, '1997-03-27'),
(876, 'Irene', 3.9, 400, '1996-03-07'),
(765, 'Jay', 2.9, 1500, '1998-08-08'),
(654, 'Amy', 3.9, 1000, '1996-05-26'),
(543, 'Craig', 3.4, 2000, '1998-08-27');


INSERT INTO Apply (sID, cName, major, decision) VALUES
(123, 'Stanford', 'CS', 'Y'),
(123, 'Stanford', 'EE', 'N'),
(123, 'Berkeley', 'CS', 'Y'),
(123, 'Cornell', 'EE', 'Y'),
(234, 'Berkeley', 'biology', 'N'),
(345, 'MIT', 'bioengineering', 'Y'),
(345, 'Cornell', 'bioengineering', 'N'),
(345, 'Cornell', 'CS', 'Y'),
(345, 'Cornell', 'EE', 'N'),
(678, 'Stanford', 'history', 'Y'),
(987, 'Stanford', 'CS', 'Y'),
(987, 'Berkeley', 'CS', 'Y'),
(876, 'Stanford', 'CS', 'N'),
(876, 'MIT', 'biology', 'Y'),
(876, 'MIT', 'marine biology', 'N'),
(765, 'Stanford', 'history', 'Y'),
(765, 'Cornell', 'history', 'N'),
(765, 'Cornell', 'psychology', 'Y'),
(543, 'MIT', 'CS', 'N');

select * from Student;
select * from Apply;

# 2. UPDATE
UPDATE student SET GPA = GPA * 1.10;
select * from Student;

# 3. DELETE
DELETE FROM student WHERE GPA < 3.2;
select * from Student;

