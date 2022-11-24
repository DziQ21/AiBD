import pandas as pd

# Set path to data
DIR = "../AnalysisData/"

# Read original data
data = pd.read_csv(f"../OriginalData/tb.csv", sep=';')
print(data)

# Choose the most inteesting columns
interestingData = data[['iso2', 'year', 'new_sp']]
print(interestingData)

result = interestingData.sort_values(['iso2', 'year'])

# Preparing the dataframe for sum
maleCasesData = data[
    [ 'new_sp_m014', 'new_sp_m1524', 'new_sp_m2534', 'new_sp_m3544', 'new_sp_m4554',
     'new_sp_m5564', 'new_sp_m65', 'new_sp_mu']]
femaleCasesData = data[
    [ 'new_sp_f014', 'new_sp_f1524', 'new_sp_f2534', 'new_sp_f3544', 'new_sp_f4554',
     'new_sp_f5564', 'new_sp_f65', 'new_sp_fu']]

result.loc[:, 'male_cases'] = maleCasesData.sum(numeric_only=True, axis=1)
result.loc[:, 'female_cases'] = femaleCasesData.sum(numeric_only=True, axis=1)
result.rename(columns = {'new_sp':'new_ases'}, inplace = True)
print(result)
result.to_csv(path_or_buf=f"{DIR}result.csv", sep=";")
