-- TABLE FOR THE PATIENT ENTITIES
CREATE TABLE Patient (
    PatientID INT NOT NULL PRIMARY KEY UNIQUE,   
    FirstName VARCHAR(255),
    LastName VARCHAR(255),
    Age INT,
    Gender VARCHAR(255)
);

-- TABLE FOR THE PHYSICIANS
CREATE TABLE Physician (
    PhysicianID INT NOT NULL PRIMARY KEY UNIQUE,
    FirstName VARCHAR(255),
    LastName VARCHAR(255),
    Specialty VARCHAR(255)
);

-- TABLE FOR THE MEDICAL PROFILE
CREATE TABLE MedicalProfile (
    ProfileID INT NOT NULL PRIMARY KEY UNIQUE,
    Diagnosis TEXT,
    CurrentMedication TEXT,
    MedicalImages TEXT,
    FOREIGN KEY (ProfileID) REFERENCES Patient(PatientID)
);


-- TREATMENT RELATIONSHIP BETWEEN PHYSICIAN AND PATIENT
CREATE TABLE Treatment (
    PatientID INT,
    PhysicianID INT,
    PRIMARY KEY (PatientID, PhysicianID),
    FOREIGN KEY (PatientID) REFERENCES Patient(PatientID),
    FOREIGN KEY (PhysicianID) REFERENCES Physician(PhysicianID)
);
