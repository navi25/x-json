#######################################################
## TEAM X-JSON
## Sprint 2
## Navendra Jha & Soham Das Gupta
## CSV Converter
## Module 1
#######################################################

import xml.etree.ElementTree as ET
import csv

tree = ET.parse("/Users/navi/Downloads/xml_file.xml")

# open a file for writing
employee_data = open('./employees.csv', 'w')

#Constants
EXT_EMPL_ID = "ExternalEmployeeId"
COMP_ID = "CompanyIdentifier"
SSN = "SSN"
FIRST_NAME="FirstName"
MIDDLE_NAME="MiddleName"
LAST_NAME="LastName"
GENDER="Gender"
DOB="DOB"
MARITAL_STATUS="MaritalStatus"
ADDRESS_1="Address1"
ADDRESS_2="Address2"
CITY="City"
STATE="State"
COUNTY="County"
ZIP="ZIP"
COUNTRY="Country"
EMAIL="Email"
PHONE="Phone"
PHONE_EXTENSION="PhoneExtension"
HIRE_DATE="HireDate"
HIRED_ON="HiredOn"
SALARY="Salary"
SALARY_EFFECTIVE_DATE="SalaryEffectiveDate"
LAST_SALARY_REVIEW_DATE="LastSalaryReviewDate"
PAY_FREQUENCY="PayFrequency"
WEEKLY_HOURS="WeeklyHours"
EMPLOYMENT_STATUS="EmploymentStatus"
LEAVE_START="LeaveStart"
LEAVE_END="LeaveEnd"
JOB_TITLE="JobTitle"
RETIRED_DATE="RetiredDate"
TERMINATION_DATE="TerminationDate"
TERMINATED_ON="TerminatedOn"
CLASS="Class"
PAYROLL_GROUP="PayrollGroup"
DISABLED="Disabled"
TOBBACCO_USER="TobaccoUser"
TOBBACCO_SIGN_DATE="TobaccoSignatureDate"
US_CITIZEN="USCitizen"
DISABLED_START_DATE="DisabledStartDate"
DISABLED_END_DATE="DisabledEndDate"
CLASS_EFFECTIVE_DATE="ClassEffectiveDate"
HRIS_COMPLETED="HrisComplete"
RELATIONSHIP="Relationship"
PRIMARY="Primary"

# create the csv writer object
csvwriter = csv.writer(employee_data)
emp_head = []
count =0


for emp in tree.iter(tag="Employee"):
    employee=[]
    if(count==0):
        effective_date = emp.find(SALARY_EFFECTIVE_DATE).tag
        emp_head.append(effective_date);
        status=emp.find(EMPLOYMENT_STATUS).tag
        emp_head.append(status)
        emp_id=emp.find(EXT_EMPL_ID).tag
        emp_head.append(emp_id)
        fname=emp.find(FIRST_NAME).tag
        emp_head.append(fname)
        mname=emp.find(MIDDLE_NAME).tag
        emp_head.append(mname)
        lname=emp.find(LAST_NAME).tag
        emp_head.append(lname)
        ssn=emp.find(SSN).tag
        emp_head.append(ssn)
        dob=emp.find(DOB).tag
        emp_head.append(dob)
        add1=emp.find(ADDRESS_1).tag
        emp_head.append(add1)
        add2=emp.find(ADDRESS_2).tag
        emp_head.append(add2)
        city=emp.find(CITY).tag
        emp_head.append(city)
        state=emp.find(STATE).tag
        emp_head.append(state)
        zip=emp.find(ZIP).tag
        emp_head.append(zip)
        phone=emp.find(PHONE).tag
        emp_head.append(phone)
        email=emp.find(EMAIL).tag
        emp_head.append(email)
        emp_head.append(RELATIONSHIP)
        emp_head.append(PRIMARY)
        csvwriter.writerow(emp_head)
        count +=1

    effective_date = emp.find(SALARY_EFFECTIVE_DATE).text
    employee.append(effective_date)
    status=emp.find(EMPLOYMENT_STATUS).text
    employee.append(status)
    emp_id=emp.find(EXT_EMPL_ID).text
    employee.append(emp_id)
    fname=emp.find(FIRST_NAME).text
    employee.append(fname)
    mname=emp.find(MIDDLE_NAME).text
    employee.append(mname)
    lname=emp.find(LAST_NAME).text
    employee.append(lname)
    ssn=emp.find(SSN).text
    employee.append(ssn)
    dob=emp.find(DOB).text
    employee.append(dob)
    add1=emp.find(ADDRESS_1).text
    employee.append(add1)
    add2=emp.find(ADDRESS_2).text
    employee.append(add2)
    city=emp.find(CITY).text
    employee.append(city)
    state=emp.find(STATE).text
    employee.append(state)
    zip=emp.find(ZIP).text
    employee.append(zip)
    phone=emp.find(PHONE).text
    employee.append(phone)
    email=emp.find(EMAIL).text
    employee.append(email)
    employee.append("P")
    employee.append("Y")
    csvwriter.writerow(employee)

    for dep in emp.iter(tag="Dependent"):
        dependent=[]
        #effective_date = emp.find(SALARY_EFFECTIVE_DATE).text
        dependent.append("")
        #status=emp.find(EMPLOYMENT_STATUS).text
        dependent.append("")
        #emp_id=emp.find(EXT_EMPL_ID).text
        dependent.append("")
        fname=dep.find(FIRST_NAME).text
        dependent.append(fname)
        mname=dep.find(MIDDLE_NAME).text
        dependent.append(mname)
        lname=dep.find(LAST_NAME).text
        dependent.append(lname)
        #ssn=emp.find(SSN).text
        dependent.append("")
        dob=emp.find(DOB).text
        dependent.append(dob)
        add1=emp.find(ADDRESS_1).text
        dependent.append(add1)
        add2=emp.find(ADDRESS_2).text
        dependent.append(add2)
        city=emp.find(CITY).text
        dependent.append(city)
        state=emp.find(STATE).text
        dependent.append(state)
        zip=emp.find(ZIP).text
        dependent.append(zip)
        #phone=emp.find(PHONE).text
        dependent.append("")
        #email=emp.find(EMAIL).text
        dependent.append("")
        relationship=dep.find(RELATIONSHIP).text
        dependent.append(relationship[0])
        dependent.append("N")
        csvwriter.writerow(dependent)


employee_data.close()
