import pandas as pd

# Load the CSV file
file_path = r"C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0083__Day79_Analyzing_Nobel_Prize_w_Plotly_Matplotlib_Seaborn__240827\NewProject\r00-r09 START\r00_env_START\nobel_prize_data.csv"
df = pd.read_csv(file_path)

# Filter the dataset to include only women
women_df = df[df['sex'] == 'Female']

# Sort the DataFrame by year to find the first 3 women
first_three_women = women_df.sort_values(by='year').head(3)

# Display the first three women along with their motivation, birth country, and organization name
print("The first three women to win the Nobel Prize along with their motivation, birth country, and organization name:")
print(first_three_women[['full_name', 'year', 'category', 'prize', 'motivation', 'birth_country', 'organization_name']])
