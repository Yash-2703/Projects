import pandas as pd
import re

# Load the dataset
file_path = "I:/My Drive/study/Final Year/Final_year_Project/Dataset/5. Data_Scientist_Naukri_jobs.csv"
data = pd.read_csv(file_path)

# Preprocessing: Clean the 'Skills' column by removing extra spaces and converting to lowercase
data['Skills'] = data['Skills'].str.strip().str.lower()

# Drop rows where 'Skills' is missing
data_cleaned = data.dropna(subset=['Skills'])

# Split the 'Skills' column by delimiters (commas, hyphens, etc.)
data_cleaned['Skills_Split'] = data_cleaned['Skills'].apply(lambda x: re.split(r'[,-]', x))

# Explode the list of skills into individual rows
skills_exploded = data_cleaned.explode('Skills_Split')

# Clean up individual skills (remove extra spaces, lowercase)
skills_exploded['Skills_Split'] = skills_exploded['Skills_Split'].str.strip().str.lower()

# Count occurrences of each skill
skills_count = skills_exploded['Skills_Split'].value_counts()
len(skills_count)
    
skills_count.to_csv('I:/My Drive/study/Final Year/Final_year_Project/Dataset/Naukri_skills_count.csv', header=['Count'], index_label='Skill')

# Display the top 10 most common skills
print(skills_count.head(10))


############# Graph ##################

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = "I:/My Drive/study/Final Year/Final_year_Project/Dataset/6.Naukri_skills_count.csv"
skills_df = pd.read_csv(file_path)

# Sort the dataset by 'Count' to get the top 10 skills
top_10_skills = skills_df.nlargest(10, 'Count')

# Set up the color palette
colors = sns.color_palette('husl', len(top_10_skills))

# Create a bar graph for the top 10 skills
plt.figure(figsize=(10, 6))
bars = plt.barh(top_10_skills['Skill'], top_10_skills['Count'], color=colors)

# Invert y-axis to have the highest skill at the top
plt.gca().invert_yaxis()

# Add labels and title
plt.xlabel('Count')
plt.ylabel('Skill')
plt.title('Naukri Top 10 Skills by Count')

# Add counts in front of each bar
for bar in bars:
    plt.text(bar.get_width() + 5, bar.get_y() + bar.get_height()/2,
             f'{int(bar.get_width())}', va='center', color='black')

# Display the plot
plt.tight_layout()
plt.show()
