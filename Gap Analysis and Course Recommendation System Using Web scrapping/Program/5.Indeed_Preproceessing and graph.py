############# preprocessing On Indeed Dataset ########
import pandas as pd

# Load the dataset
file_path = "I:/My Drive/study/Final Year/Final_year_Project/Dataset/6.Indeed_Data_science_Fields.csv"

df = pd.read_csv(file_path)

# Step 1: Clean the 'Skills' column by removing extra spaces and standardizing delimiters
df['Skills'] = df['Skills'].str.replace(r'\s*,\s*', ',').str.replace(r'\s*\|\s*', ',').str.strip()
df.head()
# Step 2: Replace empty strings or strings with just spaces with None (to handle missing values properly)
df['Company'] = df['Company'].replace(r'^\s*$', None, regex=True).str.strip()
df['Job Description'] = df['Job Description'].replace(r'^\s*$', None, regex=True).str.strip()
df['Skills'] = df['Skills'].replace(r'^\s*$', None, regex=True)

# Step 3: Split the 'Skills' column into a list for easier analysis
df['Skills'] = df['Skills'].str.split(',')

# Step 4: Check for missing or null values (both NaN and empty/whitespace strings)
missing_values = df.isnull().sum()

# Step 5: Clean the 'Name' column by removing job titles and company names
df['Company'] = df['Company'].str.split('-').str[0].str.strip()

# Output the cleaned data and report missing values
print("Missing values per column after cleaning:")
print(missing_values)
print("\nCleaned Data (first 5 rows):")
print(df.head())

######################Expand the skill of each row #####################################
import pandas as pd

# Load your CSV file
file_path = "I:/My Drive/study/Final Year/Final_year_Project/Dataset/6.Indeed_Data_science_Fields.csv"
df = pd.read_csv(file_path)

# Clean and preprocess the 'Skills' column
df['Skills'] = df['Skills'].str.replace(r'\s*,\s*', ',').str.replace(r'\s*\|\s*', ',').str.strip()
df['Skills'] = df['Skills'].str.split(',')

# Strip leading/trailing spaces from each skill in the list
df['Skills'] = df['Skills'].apply(lambda x: [skill.strip() for skill in x])

# Expand the list of skills into separate columns
skills_expanded = pd.DataFrame(df['Skills'].to_list(), index=df.index)

# Combine the expanded skills back into the original dataframe
df_expanded = df.drop('Skills', axis=1).join(skills_expanded)

# Save the expanded skills to a new CSV file
df_expanded.to_csv('I:/My Drive/study/Final Year/Final_year_Project/Dataset/Expanded_Skills.csv', index=False)

# Display the first few rows of the expanded dataframe
print(df_expanded.head())




#################### Count the skills ########################
import re
import pandas as pd

# Load your dataset
df = pd.read_csv('I:/My Drive/study/Final Year/Final_year_Project/Dataset/8.Indeed_Expanded_Skills.csv')

# Focus only on columns '0' and '1' for job titles
job_titles = df[['0', '1']].fillna('').apply(lambda row: ' '.join(row), axis=1)

# Normalize job titles by removing special characters and making everything lowercase
def normalize_title(title):
    title = title.lower()  # Make lowercase for case-insensitive matching
    title = re.sub(r'[^\w\s]', ' ', title)  # Replace any non-alphanumeric characters with a space
    return title

# Apply normalization to all job titles
job_titles_normalized = job_titles.apply(normalize_title)

# Split the strings by spaces to extract individual words (potential skills)
skills_flattened = job_titles_normalized.str.split().explode()

# Remove empty entries and spaces
skills_flattened = skills_flattened[skills_flattened != '']

# Count occurrences of each skill (unique word)
skills_count = skills_flattened.value_counts()

# Save the results to a new CSV file
skills_count_df = pd.DataFrame({'Skill': skills_count.index, 'Count': skills_count.values})
skills_count

# Save the results to a new CSV file
skills_count_df.to_csv('I:/My Drive/study/Final Year/Final_year_Project/Dataset/Indeed_skills_count.csv', index=False)

############### Graph plot #########################
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = "I:/My Drive/study/Final Year/Final_year_Project/Dataset/9.Indeed_skills_count.csv"
skills_df = pd.read_csv(file_path)

# Sort the dataset by 'Count' to get the top 10 skills
top_10_skills = skills_df.nlargest(10, 'Count')
top_10_skills
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
plt.title('Indeed Top 10 Skills by Count')

# Add counts in front of each bar
for bar in bars:
    plt.text(bar.get_width() + 5, bar.get_y() + bar.get_height()/2,
             f'{int(bar.get_width())}', va='center', color='black')

# Display the plot
plt.tight_layout()
plt.show()
