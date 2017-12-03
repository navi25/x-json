#######################################################
## TEAM X-JSON
## Sprint 2
## Navendra Jha & Soham Das Gupta
## JSON to CSV Converter
## Module 2
#######################################################

import json
import csv
from xjson.Constants import *

import os

def get_file_name(f):
    filename = f.name
    filename = filename.split(".")[0] + '.csv'
    return filename

def convert_from_json(f):
    data = json.load(f)
    # open a file for writing
    filename = get_file_name(f)
   # UpdatePath(filename)
   # os.remove(converted_file_path+filename)
    filename = "download.csv"
    employee_data = open(converted_file_path+filename, 'w', newline='')
    csvwriter = csv.writer(employee_data)

    csvwriter.writerow(["EffectiveDate","Status", "EmployeeID","ClientID", "FirstName", "MiddleName", "LastName",
                "SSN", "DOB", "Address1", "Address2", "City", "State", "Zip", "Phone", "Email" ,"Relationship", "Primary"])

    try:
        companies = data["Data"]["Companies"]["Company"]


        for company in companies:
            employees = company["Employees"]
            if(len(employees)!=0):
                for x in employees:
                    emp = employees[x]
                    employee = []
                    eff_date=emp[SALARY_EFFECTIVE_DATE]
                    employee.append(eff_date)
                    status=emp[EMPLOYMENT_STATUS]
                    employee.append(status)
                    emp_id=emp[EXT_EMPL_ID]
                    employee.append(emp_id)
                    client_id=""
                    employee.append(client_id)
                    fname=emp[FIRST_NAME]
                    employee.append(fname)
                    mname=emp[MIDDLE_NAME]
                    employee.append(mname)
                    lname=emp[LAST_NAME]
                    employee.append(lname)
                    ssn=emp[SSN]
                    employee.append(ssn)
                    dob=emp[DOB]
                    employee.append(dob)
                    add1=emp[ADDRESS_1]
                    employee.append(add1)
                    add2=emp[ADDRESS_2]
                    employee.append(add2)
                    city=emp[CITY]
                    employee.append(city)
                    state=emp[STATE]
                    employee.append(state)
                    zip=emp[ZIP]
                    employee.append(zip)
                    phone=emp[PHONE]
                    employee.append(phone)
                    email=emp[EMAIL]
                    employee.append(email)
                    employee.append("P")
                    employee.append("Y")
                    csvwriter.writerow(employee)

                    dependents = emp["Dependents"]
                    if(len(dependents)!=0):
                        dependnt = dependents["Dependent"]
                        for dep in dependnt:
                            dependent=[]
                            #effective_date = emp.find(SALARY_EFFECTIVE_DATE).text
                            dependent.append("")
                            #status=emp.find(EMPLOYMENT_STATUS).text
                            dependent.append("")
                            #emp_id=emp.find(EXT_EMPL_ID).text
                            dependent.append("")
                            fname=dep[FIRST_NAME]
                            dependent.append(fname)
                            mname=dep[MIDDLE_NAME]
                            dependent.append(mname)
                            lname=dep[LAST_NAME]
                            dependent.append(lname)
                            #ssn=emp.find(SSN).text
                            dependent.append("")
                            dob=dep[DOB]
                            dependent.append(dob)
                            add1=dep[ADDRESS_1]
                            dependent.append(add1)
                            add2=dep[ADDRESS_2]
                            dependent.append(add2)
                            city=dep[CITY]
                            dependent.append(city)
                            state=dep[STATE]
                            dependent.append(state)
                            zip=dep[ZIP]
                            dependent.append(zip)
                            #phone=emp.find(PHONE).text
                            dependent.append("")
                            #email=emp.find(EMAIL).text
                            dependent.append("")
                            relationship=dep[RELATIONSHIP]
                            dependent.append(relationship[0])
                            dependent.append("N")
                            csvwriter.writerow(dependent)



        employee_data.close()
        return download_file_path+filename
    except:
        print("[JSONCSV] - ",DATA_ERROR_CONSTANT )
        return DATA_ERROR_CONSTANT



# End of Function







