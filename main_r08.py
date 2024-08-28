import pandas as pd

# Load the CSV file
file_path = r"C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0083__Day79_Analyzing_Nobel_Prize_w_Plotly_Matplotlib_Seaborn__240827\NewProject\r00-r09 START\r00_env_START\nobel_prize_data.csv"
df = pd.read_csv(file_path)

# Count the total number of women (where 'sex' column equals 'Female')
total_women = df[df['sex'] == 'Female'].shape[0]

# Print the total number of women
print(f"Total number of women who received a Nobel Prize: {total_women}")
