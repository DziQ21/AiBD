# Laboratorium 5 - TIER protocol i tidy data

Original data tb.csv is available in /OriginalData folder.

The whole script is in /CommandFiles/Command.py

Data after analysis is available in:
- /AnalysisData/result.csv - file contains chosen info from tb.csv. Only information about yearly new cases per country, divided by sex because rest of them is unconsistent and hard or impossible to data analysis:
  - iso2 - string, country name coded in ISO alpha 2.
  - year - int, a year in which the data was taken.
  - new_cases - int, all new cases 
  - male_cases - int, male new cases
  - female_cases - int, female new cases 
  <br><br>
- /OrginaData/tb.csv - file contains information from tb.csv. Headers of file are:
  - iso2 - string, country name coded in ISO alpha 2.
  - year - int, a year in which the data was taken.
  - new_sp - int, all new cases 
  - 20 headers coded with new_sp_{f/m}age - int, new cases divided by age and sex