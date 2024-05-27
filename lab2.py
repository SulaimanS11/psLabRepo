import pandas as pd
import pyreadstat

# Load the SPSS dataset
file_path = r"Location of .sav file"
df, meta = pyreadstat.read_sav(file_path)

# Number of participants
num_participants = df.shape[0]
print(f"Q1: {num_participants}")

# Participant 16 - Good Student
participant_16_good_student = df.loc[15, 'Good_Student']
print(f"Q2: {participant_16_good_student}")

# Participant 25 - Relationship Status
participant_25_relationship_status = df.loc[24, 'Relationship_Status']
print(f"Q3: {participant_25_relationship_status}")

# Number of participants who did not answer Liberal_Conserv
num_missing_liberal_conserv = df['Liberal_Conserv'].isnull().sum()
print(f"Q4: {num_missing_liberal_conserv}")

# Participants who did not indicate number of siblings
missing_siblings_participants = df[df['Siblings'].isnull()].index.tolist()
print(f"Q5: {missing_siblings_participants}")

# Check which multi-item scale participant 405 did not complete
participant_405 = df.loc[404]
incomplete_scales = participant_405.isnull()
incomplete_scale_names = incomplete_scales[incomplete_scales].index.tolist()
print(f"Q6: {incomplete_scale_names}")