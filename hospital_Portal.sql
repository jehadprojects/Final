CREATE DATABASE hospital_portal;
USE hospital_portal;

CREATE TABLE patients (
    patient_id INT NOT NULL AUTO_INCREMENT,
    patient_name VARCHAR(45) NOT NULL,
    age INT NOT NULL,
    admission_date DATE,
    discharge_date DATE,
    PRIMARY KEY (patient_id),
    UNIQUE KEY unique_patient_name (patient_name)
);

CREATE TABLE Appointments (
    appointment_id INT NOT NULL AUTO_INCREMENT,
    patient_id INT NOT NULL,
    doctor_id INT NOT NULL,
    appointment_date DATE NOT NULL,
    appointment_time DECIMAL(5,2) NOT NULL,
    PRIMARY KEY (appointment_id)
);


INSERT INTO patients (patient_name, age, admission_date, discharge_date)
VALUES 
    ('Maria Jozef', 67, '2023-10-01', '2023-10-07'),
    ('John Smith', 45, '2023-09-15', '2023-09-20'),
    ('Alice Johnson', 30, '2023-11-05', '2023-11-10');

DELIMITER //
CREATE PROCEDURE ScheduleAppointment(IN patientID INT, IN doctorID INT, IN appDate DATE, IN appTime DECIMAL)
BEGIN
    INSERT INTO appointments (patient_id, doctor_id, appointment_date, appointment_time)
    VALUES (patientID, doctorID, appDate, appTime);
END //
DELIMITER ;


DELIMITER //
CREATE PROCEDURE DischargePatient(IN patientID INT, IN disDate DATE)
BEGIN
    UPDATE patients SET discharge_date = disDate WHERE patient_id = patientID;
END //
DELIMITER ;

CREATE TABLE doctors (
    doctor_id INT NOT NULL AUTO_INCREMENT,
    doctor_name VARCHAR(45) NOT NULL,
    specialization VARCHAR(45),
    PRIMARY KEY (doctor_id)
);

CREATE VIEW doctor_appointment_patient_view AS
SELECT
    a.appointment_id,
    a.appointment_date,
    a.appointment_time,
    p.patient_name,
    p.age,
    p.admission_date,
    p.discharge_date,
    d.doctor_name,
    d.specialization
FROM appointments a
JOIN patients p ON a.patient_id = p.patient_id
JOIN doctors d ON a.doctor_id = d.doctor_id;
