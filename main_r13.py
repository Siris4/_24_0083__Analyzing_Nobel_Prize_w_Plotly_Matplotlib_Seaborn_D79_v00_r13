import pandas as pd
import plotly.graph_objects as go

# Load the CSV file
file_path = r"C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0083__Day79_Analyzing_Nobel_Prize_w_Plotly_Matplotlib_Seaborn__240827\NewProject\r00-r09 START\r00_env_START\nobel_prize_data.csv"
df = pd.read_csv(file_path)

# Count the number of prizes awarded in each category
category_counts = df['category'].value_counts()

# Create a bar chart with the Aggrnyl color scale and no color axis
fig = go.Figure(data=[
    go.Bar(x=category_counts.index, y=category_counts.values, text=category_counts.values, textposition='inside',
           marker=dict(color=category_counts.values, colorscale='Aggrnyl', showscale=False))
])

# Update layout
fig.update_layout(
    title='Number of Nobel Prizes Awarded by Category',
    xaxis_title='Category',
    yaxis_title='Number of Prizes',
    uniformtext_minsize=8,
    uniformtext_mode='hide'
)

# Show the figure
fig.show()
