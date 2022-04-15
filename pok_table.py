
import pandas as pd
import os
import numpy as np
from datetime import datetime
employee_records_df = pd.read_excel('data/EmployeeRecords.xlsx')

# n_full = []
n_middle = []
n_last = []
# doc_full = []
doc_middle = []
doc_last = []
# df_table_full = pd.DataFrame()
df_table_middle = pd.DataFrame()
df_table_last = pd.DataFrame()

def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        read = f.read()
        return read

def get_records():
    for lastname in range(len(n_last)):
        for middlename in range(len(n_middle)):
           return employee_records_df[(employee_records_df['LastName'] == n_last[0]) | \
                                       (employee_records_df['LastName'] == n_last[1]) | \
                                       (employee_records_df['LastName'] == n_last[2]) | \
                                       (employee_records_df['LastName'] == n_last[3]) | \
                                       (employee_records_df['LastName'].str.contains(n_middle[0])) | 
                                       (employee_records_df['LastName'].str.contains(n_middle[1])) ] 

def search_on_names():
    # read employee records
    # firstnames = list(employee_records_df.FirstName)
    lastnames  = list(employee_records_df.LastName)
    middlenames = []
    # fullnames = []

    # for i in range(len(employee_records_df)):
    #     fullnames.append(firstnames[i] + ' ' + lastnames[i])

    for item in list(employee_records_df['LastName'].str.split(" ")):
        if len(item) > 1:
            middlenames.append(item[0])


    names = ['pok', 'POK', 'protectors']

    directory = "data/HistoricalDocuments/txt versions/"
    for file in os.listdir(directory):
        read = read_text_file(directory + file)
        for row in file:
            for word in names:
                if word in read:
                    for name in lastnames:
                        if name in read:
                            if name not in n_last:
                                n_last.append(name)
                                doc_last.append(file)
                    # for name in fullnames:
                    #     if name in read:
                    #         if name not in n_full:
                    #             n_full.append(name)
                    #             doc_full.append(file) 
                    for name in middlenames:
                        if name in read:
                            if name not in n_middle:
                                n_middle.append(name)
                                doc_middle.append(file)
    
    # df_table_full['doc_full'] = doc_full
    df_table_last['doc_last'] = doc_last
    df_table_last['employee_last_name'] = n_last
    # df_table_full['employee_full_name'] = n_full
    df_table_middle['doc_middle'] = doc_middle
    df_table_middle['employee_middle_name'] = n_middle

    # df_search_all = pd.concat([df_table_last, df_table_full, df_table_middle]).replace(np.nan, '-')
    # df_results_search_final = df_search_all.reset_index(drop=True)

    # df_get_associated_members_data = get_records().set_index(['CurrentEmploymentType', 'LastName', 'FirstName'])
    df_get_associated_members_data = get_records().copy()
    df_get_associated_members_data['BirthDate'] = df_get_associated_members_data['BirthDate'].dt.date
    df_get_associated_members_data['PassportIssueDate'] = df_get_associated_members_data['PassportIssueDate'].dt.date
    df_get_associated_members_data['PassportExpirationDate'] = df_get_associated_members_data['PassportExpirationDate'].dt.date
    df_get_associated_members_data['CitizenshipStartDate'] = df_get_associated_members_data['CitizenshipStartDate'].dt.date
    df_get_associated_members_data['CurrentEmploymentStartDate'] = df_get_associated_members_data['CurrentEmploymentStartDate'].dt.date
    df_get_associated_members_data['MilitaryDischargeDate'] = df_get_associated_members_data['MilitaryDischargeDate'].dt.date
    df_get_associated_members_data['POK member'] = ['Valentine Mies', '', 'Valentine Mies', 'Valentine Mies', 'Carmine Osvaldo', 'Isia Vann', 'Isia Vann', 'Henk Bodrogi']
    
    df_get_associated_members_data = df_get_associated_members_data.set_index('POK member')

    return df_get_associated_members_data
