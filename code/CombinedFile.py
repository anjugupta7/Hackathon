import pandas as pd

# Load the Excel file
file_path = "CustomerProfileOrg.xlsx"

# Read Sheet1 and Sheet2
df1 = pd.read_excel(file_path, sheet_name="Sheet1")
df2 = pd.read_excel(file_path, sheet_name="Sheet2")
df3 = pd.read_excel(file_path, sheet_name="Sheet3")


merged_data = pd.merge(df1, df2, on='Customer_Id', how='left')
merged_data = pd.merge(merged_data, df3, on='Customer_Id', how='left')


output_file = "flattened_output.xlsx"
merged_data.to_excel(output_file, index=False)
    
