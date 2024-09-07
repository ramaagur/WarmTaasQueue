import openpyxl as myexcel

# Load the workbook and select the sheet
workbook = myexcel.load_workbook(r"C:\Users\ramaa\Desktop\New folder\myexcel.xlsx")
worksheet = workbook['Sheet1']  # Ensure the sheet name matches exactly

# Access a range of cells (A2 to C2)
data = worksheet['A2':'C2']

# Iterate through the range and print the values
for row in data:
    for cell in row:
        print(cell.value)

for row in data:
    for col in row:
     print(col.value,end=" ")
     #Stop here to push the backup-main