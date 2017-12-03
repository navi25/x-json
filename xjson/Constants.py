converted_file_path = "./xjson/documents/"
download_file_path="./xjson/documents/"
DATA_ERROR_CONSTANT = "File is Corrupt!!"
INVALID_FILE_FORMAT = "Invalid File Format!!"

global const_fileName
const_fileName=""
global download_filePath
download_filePath=""

def UpdatePath(file):
    global const_fileName
    const_fileName= file
    global download_filePath
    download_filePath= "documents/" + const_fileName
    print("[UpdatePath] const_filename - {0}; path - {1}",const_fileName, download_filePath)


#CONSTANTS FOR XML FILE
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
