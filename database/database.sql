-- Create table for students and their vaccination details
CREATE TABLE students (
    reg_no VARCHAR(10) PRIMARY KEY,
    name VARCHAR(50),
    vaccinated ENUM('Yes', 'No')
);

-- Insert sample data
INSERT INTO students (reg_no, name, vaccinated) VALUES
    ('111', 'John', 'Yes'),
    ('222', 'Jane', 'No'),
    ('333', 'Alice', 'Yes');
