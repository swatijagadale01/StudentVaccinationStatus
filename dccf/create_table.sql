CREATE TABLE students (
    RegNo INT PRIMARY KEY,
    Name VARCHAR(50) NOT NULL,
    Vaccination_Status ENUM('Yes', 'No') NOT NULL
);
