import pandas as pd

csv_url = "https://docs.google.com/spreadsheets/d/1AbCDefGHIJKLMNO1234567890abcdEFGH/export?format=csv"
df = pd.read_csv(csv_url)

print(df.head())  # Show first few rows
