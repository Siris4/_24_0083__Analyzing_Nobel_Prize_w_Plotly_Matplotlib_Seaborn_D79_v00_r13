import pandas as pd

# Load the CSV file
file_path = r"C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0083__Day79_Analyzing_Nobel_Prize_w_Plotly_Matplotlib_Seaborn__240827\NewProject\r00-r09 START\r00_env_START\nobel_prize_data.csv"
df = pd.read_csv(file_path)

# Group by 'full_name' and count the occurrences of each individual
winners_count = df['full_name'].value_counts()

# Filter to find individuals who have won more than once
multiple_winners = winners_count[winners_count > 1]

# Display the results
print("Individuals who have won the Nobel Prize more than once:")
print(multiple_winners)
