import pandas as pd

# Load the CSV file
file_path = r"C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0083__Day79_Analyzing_Nobel_Prize_w_Plotly_Matplotlib_Seaborn__240827\NewProject\r00-r09 START\r00_env_START\nobel_prize_data.csv"
df = pd.read_csv(file_path)

# Find the unique categories in which prizes are awarded
unique_categories = df['category'].unique()

# Count the number of unique categories
num_categories = len(unique_categories)

# Display the results
print(f"Number of different categories in which prizes are awarded: {num_categories}")
print("Categories:")
print(unique_categories)
