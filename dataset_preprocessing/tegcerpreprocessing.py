# -*- coding: utf-8 -*-
"""TegcerPreprocessing.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1mlDZ8RU4Vu6JcBt-iiBjh9zXtz5Tth-A
"""
'''
data['is_single_function'] = data['sourceText'].apply(has_single_function)
single_function_data = data[data['is_single_function']]

# Drop the helper column used for filtering
single_function_data = single_function_data.drop(columns=['is_single_function'])

output_path = '/content/drive/MyDrive/ANLPDatasets/single_function_programs_all_columns.csv'
single_function_data.to_csv(output_path, index=False)

print(single_function_data.head())

single_function_data

single_function_data[['sourceText', 'targetText']]

print("Total number of single-function programs:", len(single_function_data))
print("Sample source text (buggy code):", single_function_data['sourceText'].iloc[0])
print("Sample target text (corrected code):", single_function_data['targetText'].iloc[0])

# Filter the dataset for programs with only a single function and no 'struct'
data['is_single_function_without_struct'] = data['sourceText'].apply(has_single_function)
filtered_data = data[data['is_single_function_without_struct']]

# Drop the helper column used for filtering
filtered_data = filtered_data.drop(columns=['is_single_function_without_struct'])

# Keep only the 'sourceText' and 'targetText' columns
filtered_data = filtered_data[['sourceText', 'targetText']]

# Rename the columns to 'buggyCode' and 'correctedCode'
filtered_data.rename(columns={'sourceText': 'buggyCode', 'targetText': 'correctedCode'}, inplace=True)

# Function to normalize and compare code
def is_code_different(buggy, corrected):
    # Normalize code by stripping whitespace and empty lines
    buggy_lines = [line.strip() for line in buggy.splitlines() if line.strip()]
    corrected_lines = [line.strip() for line in corrected.splitlines() if line.strip()]
    # Compare normalized lines
    return buggy_lines != corrected_lines

# Filter rows where the code differs after normalization
filtered_data = filtered_data[filtered_data.apply(lambda row: is_code_different(row['buggyCode'], row['correctedCode']), axis=1)]

# Reset the ProblemID after filtering
filtered_data.reset_index(drop=True, inplace=True)
filtered_data.insert(0, 'ProblemID', range(1, len(filtered_data) + 1))

# Save the updated dataset to a new CSV file
output_path = '/content/drive/MyDrive/ANLPDatasets/line_by_line_comparison.csv'
filtered_data.to_csv(output_path, index=False)

# Display the updated dataset
print(filtered_data.head())

filtered_data

filtered_data.columns

filtered_data

print("Total number of single-function programs:", len(filtered_data))

data_line= pd.read_csv('/content/drive/MyDrive/ANLPDatasets/line_by_line_comparison.csv')
print("Total number of single-function programs:", len(data_line))

# Filter the dataset for programs with only a single function and no 'struct'
data['is_single_function_without_struct'] = data['sourceText'].apply(has_single_function)
filtered_data = data[data['is_single_function_without_struct']]

# Drop the helper column used for filtering
filtered_data = filtered_data.drop(columns=['is_single_function_without_struct'])

# Keep only the 'sourceText' and 'targetText' columns
filtered_data = filtered_data[['sourceText', 'targetText']]

# Rename the columns to 'buggyCode' and 'correctedCode'
filtered_data.rename(columns={'sourceText': 'buggyCode', 'targetText': 'correctedCode'}, inplace=True)

# Add a new column 'ProblemID' for ordering
filtered_data.insert(0, 'ProblemID', range(1, len(filtered_data) + 1))

# Save the updated dataset to a new CSV file
output_path = '/content/drive/MyDrive/ANLPDatasets/single_function_programs.csv'
filtered_data.to_csv(output_path, index=False)

# Display the updated dataset
print(filtered_data.head())

#All columns code with just 2 renamed
# Filter the dataset for programs with only a single function and no 'struct'
data['is_single_function_without_struct'] = data['sourceText'].apply(has_single_function)
filtered_data = data[data['is_single_function_without_struct']]

# Drop the helper column used for filtering
filtered_data = filtered_data.drop(columns=['is_single_function_without_struct'])

# Keep only the 'sourceText' and 'targetText' columns
filtered_data = filtered_data[['sourceText', 'targetText']]

# Rename the columns to 'buggyCode' and 'correctedCode'
filtered_data.rename(columns={'sourceText': 'buggyCode', 'targetText': 'correctedCode'}, inplace=True)

# Add a new column 'ProblemID' for ordering
filtered_data.insert(0, 'ProblemID', range(1, len(filtered_data) + 1))

# Save the updated dataset to a new CSV file
output_path = '/content/drive/MyDrive/ANLPDatasets/single_function_programs_v3.csv'
filtered_data.to_csv(output_path, index=False)

# Display the updated dataset
print(filtered_data.head())

data = pd.read_csv('/content/drive/MyDrive/ANLPDatasets/single_function_programs_v1.csv')

data

data2 = pd.read_csv('/content/drive/MyDrive/ANLPDatasets/Tegcer_v2_ProblemID_buggyCode_correctedCode.csv')

data2
'''
#Final Code for preprocessing Tegcer
from google.colab import drive
drive.mount('/content/drive')
import pandas as pd
import re
import sys
sys.path.append('/content/drive/MyDrive/ANLPDatasets')
dataset_path = '/content/drive/MyDrive/ANLPDatasets/tegcer.csv'



file_path = dataset_path
data = pd.read_csv(file_path)

data = data.loc[:, ~data.columns.str.contains('^Unnamed')]

data

data[['sourceText', 'targetText']]

print("Total number of programs:", len(data))
print("Sample source text (buggy code):", data['sourceText'].iloc[0])
print("Sample target text (corrected code):", data['targetText'].iloc[0])

data

data.columns

# Function to check if a program has only a single function
def has_single_function(source_code):
    # Use regex to find all function definitions
    functions = re.findall(r'\b(?:int|void|char|float|double|long|short)\s+\w+\s*\([^)]*\)\s*{', str(source_code))
    # Return True if there is only one function
    return len(functions) == 1 and 'struct' not in source_code
import pandas as pd

data = pd.read_csv('/content/drive/MyDrive/ANLPDatasets/tegcer.csv')

# Rename the unnamed column to "problem id from original dataset"
data.rename(columns={'Unnamed: 0': 'ProblemID_from_original_dataset_unnamed'}, inplace=True)

# Filter the dataset for programs with only a single function
data['is_single_function_without_struct'] = data['sourceText'].apply(has_single_function)
filtered_data = data[data['is_single_function_without_struct']]

# Drop the helper column used for filtering
filtered_data = filtered_data.drop(columns=['is_single_function_without_struct'])

filtered_data.rename(columns={'sourceText': 'buggyCode', 'targetText': 'correctedCode'}, inplace=True)

# Add a new column 'ProblemID' for ordering
filtered_data.insert(0, 'ProblemID', range(1, len(filtered_data) + 1))

# Keep only the desired columns
filtered_data = filtered_data[['ProblemID', 'ProblemID_from_original_dataset_unnamed', 'buggyCode', 'correctedCode']]

# Save the updated dataset to a new CSV file
output_path = '/content/drive/MyDrive/ANLPDatasets/Tegcer_ProblemID_UnnamedOriginal_buggyCode_correctedCode.csv'
filtered_data.to_csv(output_path, index=False)

print(filtered_data.head())

filtered_data.columns

filtered_data
