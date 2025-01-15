import re
import pandas as pd
from collections import Counter

filename = '05\\bearbeitet_scripts.csv'
outputfile = '05\\outputdatei.csv'

with open(filename, 'r', encoding='utf-8') as f:
    lines = f.readlines()

cleaned_lines = []
for line in lines:
    line = line.rstrip('\n')
    fields = line.split(';')
    fields = [field.strip() for field in fields]
    cleaned_line = ';'.join(fields)
    cleaned_lines.append(cleaned_line + '\n')


with open(outputfile, 'w', encoding='utf-8') as f:
    f.writelines(cleaned_lines)

unique_words = set()
total_data_lines = 0

with open(outputfile, 'r', encoding='utf-8') as f:
    header = next(f, None)
    for line in f:
        if not line.strip():
            continue
        
        total_data_lines += 1
        fields = line.rstrip('\n').split(';')
        
        if len(fields) < 3:
            continue
        
        dialog = fields[2]
        
        words_in_dialog = re.findall(r"[a-zA-Z]+", dialog.lower())

        unique_words.update(words_in_dialog)


df = pd.read_csv(
    outputfile,
    sep=';',
    usecols=[1, 2, 3],  
    names=['char', 'dialog', 'movie'],
    header=0,
    engine='python'
)

print(df.head())

# Zweite Frage
film_distribution = df['movie'].value_counts()
print("\nDistribution of lines across films:\n", film_distribution)

# Dritte Frage
top_5_characters = df['char'].value_counts().head(5)
print("\nTop 5 characters:\n", top_5_characters)

# Vierte Frage
all_dialog_text = ' '.join(df['dialog'].astype(str)) 
words = re.findall(r'[a-zA-Z]+', all_dialog_text.lower()) 

char_text = ' '.join(df['char'].astype(str)).lower()
char_words = re.findall(r'[a-zA-Z]+', char_text)

char_words_set = set(char_words)

word_counts = Counter(words) 
top_25_words = word_counts.most_common(25)

common_words = [(word, count) for (word, count) in top_25_words if word in char_words_set]

print("\nWords that appear both in dialogues and in character names (top 5 from dialogues):")
for word, count in common_words:
    print(f"{word}: {count}")

print("Total data lines (excluding header):", total_data_lines)
print("Number of unique words in the 'dialog' column:", len(unique_words))