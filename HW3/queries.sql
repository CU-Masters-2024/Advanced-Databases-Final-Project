/*
Which patients, including their personal details and medical information, have been diagnosed with either Anxiety Disorder or Depression?

The query joins the `Patient` and `MedicalProfile` tables to combine personal and medical details, linking them through a matching patient ID. 
It specifically filters for records where the diagnosis is either "Anxiety Disorder" or "Depression," ensuring only relevant medical conditions
are considered. By selecting patient identifiers, names, age, gender, and corresponding medical details, it effectively lists individuals diagnosed 
with these specific mental health issues.
*/
SELECT 
    p.PatientID, 
    p.FirstName, 
    p.LastName, 
    p.Age, 
    p.Gender,
    mp.Diagnosis,
    mp.CurrentMedication,
    mp.MedicalImages
FROM 
    Patient p
JOIN 
    MedicalProfile mp ON p.PatientID = mp.ProfileID
WHERE 
    mp.Diagnosis IN ('Anxiety Disorder', 'Depression');


/*
How many patients of each gender are there for every diagnosis?

The query links each medical profile with patient records to correlate diagnoses with patient gender. It groups these combined records by both 
diagnosis and gender, enabling a count of patients for each unique pair of diagnosis and gender. Finally, the results are ordered by diagnosis 
and gender, providing a clear breakdown of patient counts for every diagnosis, segmented by gender.
*/
SELECT 
    mp.Diagnosis,
    p.Gender,
    COUNT(*) AS NumberOfPatients
FROM 
    MedicalProfile mp
JOIN 
    Patient p ON mp.ProfileID = p.PatientID
GROUP BY 
    mp.Diagnosis, p.Gender
ORDER BY 
    mp.Diagnosis, p.Gender;


/*
What are the minimum and maximum ages of male and female patients diagnosed with migraines?

The query performs an inner join between the `Patient` and `MedicalProfile` tables using the patient's ID to associate each patient with their medical conditions, 
specifically targeting those with a diagnosis of "Migraine." It then groups the resulting records by gender to separately aggregate minimum and maximum ages 
for males and females diagnosed with migraines. The `MIN` and `MAX` functions calculate the youngest and oldest ages within each gender group, providing the age 
distribution among patients suffering from migraines.
*/

SELECT 
    p.Gender,
    MIN(p.Age) AS MinAge,
    MAX(p.Age) AS MaxAge
FROM 
    Patient p
JOIN 
    MedicalProfile mp ON p.PatientID = mp.ProfileID
WHERE 
    mp.Diagnosis = 'Migraine'
GROUP BY 
    p.Gender;


/*
Which physicians, along with their specialties, have patients with medical profiles that include X-ray or MRI images?

This query identifies physicians who have provided treatments associated with medical profiles that include either X-ray or MRI imaging, 
using two inner joins to link the Physician, Treatment, and MedicalProfile tables based on physician and patient IDs. It lists each qualifying 
physician's ID, first name, last name, and specialty without duplicates. The results are ordered by the physician's ID to organize the data systematically.
*/

SELECT DISTINCT
    ph.PhysicianID,
    ph.FirstName,
    ph.LastName,
    ph.Specialty
FROM 
    Physician ph
JOIN 
    Treatment tr ON ph.PhysicianID = tr.PhysicianID
JOIN 
    MedicalProfile mp ON tr.PatientID = mp.ProfileID
WHERE 
    mp.MedicalImages = 'X-ray'
    OR mp.MedicalImages = 'MRI'
ORDER BY 
    ph.PhysicianID;



/*
Which physicians (by ID, name, and specialty) have treated patients (identified by PatientID) diagnosed with conditions 
that required X-ray or MRI imaging, and what were those diagnoses?

The query retrieves distinct records of physicians (ID, first name, last name, and specialty) and 
the patient IDs and diagnoses of those patients who have either X-ray or MRI images in their medical profiles. 
It joins the `Physician` table with the `Treatment` table to match physicians to treatments, and then joins the `Treatment` table with the `MedicalProfile` table to connect 
treatments to specific medical profiles based on patient ID. The result is sorted by physician ID and patient ID, focusing on the intersection of healthcare providers and diagnostic imaging. 
*/

SELECT DISTINCT
    ph.PhysicianID,
    ph.FirstName AS PhysicianFirstName,
    ph.LastName AS PhysicianLastName,
    ph.Specialty,
    mp.ProfileID AS PatientID,  
    mp.Diagnosis
FROM 
    Physician ph
JOIN 
    Treatment tr ON ph.PhysicianID = tr.PhysicianID
JOIN 
    MedicalProfile mp ON tr.PatientID = mp.ProfileID
WHERE 
    mp.MedicalImages = 'X-ray'
    OR mp.MedicalImages = 'MRI'
ORDER BY 
    ph.PhysicianID, mp.ProfileID;




/*
What are the specialties of physicians who have treated more than 10 unique patients?

This query calculates the number of unique patients treated by physicians within each medical specialty, 
grouping the results by the specialty field. It then filters these groups to only include those where more than 10 distinct patients have been treated.
The query uses an inner join to link physicians to their treatments by matching PhysicianID in both the Physician and Treatment tables which allows for the aggregation of unique patient counts by specialty.
*/
SELECT 
    p.Specialty,
    COUNT(DISTINCT t.PatientID) AS NumberOfPatients
FROM 
    Physician p
JOIN 
    Treatment t ON p.PhysicianID = t.PhysicianID
GROUP BY 
    p.Specialty
HAVING 
    COUNT(DISTINCT t.PatientID) > 10;
