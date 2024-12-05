#############preprocessing########
import pandas as pd

# Load the dataset
file_path = "I:/My Drive/study/Final Year/Final_year_Project/Dataset/2. Updated_Linkedin_profile_skills.csv"

df = pd.read_csv(file_path)

# Step 1: Clean the 'Skills' column by removing extra spaces and standardizing delimiters
df['Skills'] = df['Skills'].str.replace(r'\s*,\s*', ',').str.replace(r'\s*\|\s*', ',').str.strip()
df.head()
# Step 2: Replace empty strings or strings with just spaces with None (to handle missing values properly)
df['Name'] = df['Name'].replace(r'^\s*$', None, regex=True).str.strip()
df['URL'] = df['URL'].replace(r'^\s*$', None, regex=True).str.strip()
df['Skills'] = df['Skills'].replace(r'^\s*$', None, regex=True)

# Step 3: Split the 'Skills' column into a list for easier analysis
df['Skills'] = df['Skills'].str.split(',')

# Step 4: Check for missing or null values (both NaN and empty/whitespace strings)
missing_values = df.isnull().sum()

# Step 5: Clean the 'Name' column by removing job titles and company names
df['Name'] = df['Name'].str.split('-').str[0].str.strip()

# Output the cleaned data and report missing values
print("Missing values per column after cleaning:")
print(missing_values)
print("\nCleaned Data (first 5 rows):")
print(df.head())

######################Expand the skill of each row #####################################
import pandas as pd

# Load your CSV file
file_path = "I:/My Drive/study/Final Year/Final_year_Project/Dataset/2. Updated_Linkedin_profile_skills.csv"
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
#df_expanded.to_csv('Expanded_Skills.csv', index=False)

# Display the first few rows of the expanded dataframe
#print(df_expanded.head())




#################### Count the skills ########################
import pandas as pd
import re

# Load the dataset
df = pd.read_csv("I:/My Drive/study/Final Year/Final_year_Project/Dataset/3.Linkdin_Expanded_Skills.csv")  

# Combine all skill columns into one series
skills_columns = df.iloc[:, 3:].stack()  # Stack all skill columns into a single series
skills_cleaned = skills_columns.dropna().str.strip()  # Remove NaN and strip any leading/trailing spaces

# Function to normalize the skill names using regular expressions
def normalize_skill(skill):
    # Simplify skills by removing anything inside parentheses and extra spaces
    return re.sub(r'\s*\(.?\)\s', '', skill).strip().lower()

# Apply the normalization function to all skills
normalized_skills = skills_cleaned.apply(normalize_skill)

# Count occurrences of each normalized skill
skills_count = normalized_skills.value_counts()
len(skills_count)
# Save the results to a new CSV file
skills_count_df = pd.DataFrame({'Skill': skills_count.index, 'Count': skills_count.values})
#output_file = "G:/My Drive/Study/Final Year/Final_year_Project/test/skills_count.csv"
#skills_count_df.to_csv(output_file, index=False)

#print(f"Skill count has been saved to {output_file}.")

###############Graph plot#########################
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = "I:/My Drive/study/Final Year/Final_year_Project/Dataset/4. Linkdin_skills_count_dataset.csv"
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
plt.title('Linkedin Top 10 Skills by Count')

# Add counts in front of each bar
for bar in bars:
    plt.text(bar.get_width() + 5, bar.get_y() + bar.get_height()/2,
             f'{int(bar.get_width())}', va='center', color='black')

# Display the plot
plt.tight_layout()
plt.show()
