import csv
import os
import time
import matplotlib.pyplot as plt

# Define the path to the AcronymsFile.csv file
acronym_file = 'D:/3rd year/COSC 320/Cosc320-master/Cosc320-master/AcronymsFile.csv'

# Define the path to the AppReviews folder
app_reviews_folder = 'D:/3rd year/COSC 320/Cosc320-master/Cosc320-master/AppReviews'

# Read the AcronymsFile.csv file and generate the acronym dictionary
def read_acronym_file(acronym_file):
    acronyms = {}
    with open(acronym_file, 'r', encoding='utf-8-sig',) as f:
        reader = csv.reader(f,skipinitialspace=True)
        for row in reader:
            # if len(row) >= 1 and ',' in row[0]:
            
            if len(row) >= 1:
                 acronym_full_form = [row[0],row[1]]
                 print(acronym_full_form)
                 if len(acronym_full_form) == 2 :
                     acronym, full_form = acronym_full_form
                     acronyms[acronym] = full_form
    return acronyms


acronyms = read_acronym_file(acronym_file)

# Define a function to replace acronyms with full forms in a given string
def replace_acronyms(text, acronyms):
    words = text.split()
    replaced_words = []
    for word in words:
        replaced_word = word
        for acronym, full_form in acronyms.items():   #the naive algorithm. With the nested for loops.
            if acronym == word:
                replaced_word = full_form
        replaced_words.append(replaced_word)
    replaced_text = ' '.join(replaced_words)
    return replaced_text

# Define a function to process a single CSV file
def process_csv_file(input_file_path, output_file_path, acronyms):
    with open(input_file_path, 'r',encoding="utf-8") as input_file, open(output_file_path, 'w',encoding="utf-8") as output_file:
        reader = csv.DictReader(input_file)
        writer = csv.DictWriter(output_file, fieldnames=reader.fieldnames)
        writer.writeheader()
        for row in reader:
            content = row['content']
            replaced_content = replace_acronyms(content, acronyms)
            if content != replaced_content:
                print(f"Replaced acronyms in content: {content} -> {replaced_content}")
            row['content'] = replaced_content
            writer.writerow(row)

# Define a function to process a certain number of CSV files in the AppReviews folder and record the runtime
def process_n_csv_files(acronyms, n):
    total_time = 0
    i = 0
    for root, dirs, files in os.walk(app_reviews_folder):
        for file in files:
            if i >= n or not file.endswith('.csv'):
                break
            input_file_path = os.path.join(root, file)
            output_file_path = os.path.join(root, 'new_' + file)
            start_time = time.time()
            process_csv_file(input_file_path, output_file_path, acronyms)
            end_time = time.time()
            total_time += end_time - start_time
            i += 1
    return total_time

# Call the process_n_csv_files function to replace acronyms in a certain number of CSV files in the AppReviews folder and record the runtime
total_time = process_n_csv_files(acronyms, 10)

# Plot a graph to show the total runtime
plt.plot([1], [total_time], marker='o')
plt.title('Total runtime to replace acronyms in 10 CSV files')
plt.xlabel('Files processed')
plt.ylabel('Total runtime (seconds)')
plt.show()

'''Define a function to process a certain number of CSV files in the AppReviews folder and record the runtime
def process_n_csv_files(acronyms, n):
    times = []
    i = 0
    for root, dirs, files in os.walk(app_reviews_folder):
        for file in files:
            if i >= n or not file.endswith('.csv'):
                break
            input_file_path = os.path.join(root, file)
            output_file_path = os.path.join(root, 'new_' + file)
            start_time = time.time()
            process_csv_file(input_file_path, output_file_path, acronyms)
            end_time = time.time()
            times.append(end_time - start_time)
            i += 1
    return times

# Call the process_n_csv_files function to replace acronyms in a certain number of CSV files in the AppReviews folder and record the runtime
times = process_n_csv_files(acronyms, 10)

# Plot a graph to show the
plt.bar(range(len(times)), times)
plt.title('Runtime to replace acronyms in CSV files')
plt.xlabel('File number')
plt.ylabel('Runtime (seconds)')
plt.show()'''



