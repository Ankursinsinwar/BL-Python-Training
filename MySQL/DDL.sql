## DDL (Data Definition Language)

# 1. CREATE
create database Learning;

use Learning;

CREATE TABLE Student (
    sID INT PRIMARY KEY,
    sName VARCHAR(255),
    GPA DECIMAL(3, 2),
    sizeHS float,
    DoB DATE
);

CREATE TABLE Apply (
    sID INT,
    cName VARCHAR(255),
    major VARCHAR(255),
    decision CHAR(1)
);


# 2. DROP

-- drop table Student;
-- drop table Apply;

# 3. ALTER
ALTER TABLE Student modify COLUMN sizeHS INT;

desc Student;

# 4. TRUNCATE

TRUNCATE Student;

