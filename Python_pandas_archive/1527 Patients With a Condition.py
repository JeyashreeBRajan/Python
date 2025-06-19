#Write a solution to find the patient_id, patient_name, and conditions of the patients who have Type I Diabetes. Type I Diabetes always starts with DIAB1 prefix.

#Return the result table in any order.

import pandas as pd

data = [[1,'Daniel','YFEV COUGH'],[2,'Alice',''],[3,'Bob','DIAB100 MYOP'],[4,'George','ACNE DIAB100'],[5,'Alain','DIAB201']]
patients = pd.DataFrame(data,columns=['patient_id','patient_name','conditions'])

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    check_conditions = pd.DataFrame()
    check_conditions['patient_id'] = patients['patient_id']
    check_conditions['conditions'] = patients['conditions'].str.split(" ")
    check_conditions['is_DIAB1'] = check_conditions['conditions'].apply(lambda cond: any(cond.startswith("DIAB1") for cond in cond))
    output = patients[check_conditions['is_DIAB1'] == True]
    return output

output = find_patients(patients)
print(output)

    