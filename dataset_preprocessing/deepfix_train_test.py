import pandas as pd
from sklearn.model_selection import train_test_split

file_path = 'Deepfix_ProblemID_buggyCode_correctedCode.csv'  
dataset = pd.read_csv(file_path)


train_data, test_data = train_test_split(dataset, test_size=0.2, random_state=42)


train_file_path = 'train_buggy_corrected.csv'
test_file_path = 'test_buggy_corrected.csv'

train_data.to_csv(train_file_path, index=False)
test_data.to_csv(test_file_path, index=False)

print(f"Training dataset saved to: {train_file_path}")
print(f"Testing dataset saved to: {test_file_path}")




print("\n--- Dataset Information ---")
print(dataset.info())


print("\n--- Basic Statistics ---")
print(dataset.describe(include='all'))


print("\n--- Missing Values ---")
print(dataset.isnull().sum())


duplicates = dataset.duplicated()
print("\n--- Duplicate Rows ---")
print(f"Number of duplicate rows: {duplicates.sum()}")



