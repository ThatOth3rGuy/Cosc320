## COSC 320 - Analysis of Algorithms. 

### Milestone 1
We used a naïve approach to read in the dataset and replace abbreviation with the keywords. With this following pseudocode: 
`f(D, A) = D' for i = 1 to n:  for j = 1 to m:  if d[i] = a[j]:  d[i] = b[j]  break  D'.append(d[i]) return D' `

### Milestone 2 
We implemented a hash table as an improvement upon the naïve algorithm and it provided a good balance of efficiency and memory usage for this problem, making it a good choice for storing the dictionary of abbreviations. Bringing down the O(nm) complexity to O(1) in lookup search time.

### Milestone 3
We compiled sample files in a single csv formatted document, as the input file and performed graphical analysis on the runtime of our algorithms. We utilised the python’s Pandas package to set the data frames, and matplotlib.pyplot package to generate the graph results.

### Milestone 4
We tested our improved algorithm which uses a hashMap. `Acronyms.csv` acts as the dictionary for the hashmap. The `.csv` files in the `AppReviews` folder is the data we are parsing through to replace keywords. The folder has around 3000 files and about 2.8 million data entries in total. We are implenting both algorithms and comparing the runtimes for each.

### Running Time for Algorithm A: {Plot here}

Time complexity: The time complexity of this algorithm would be O(N*M) where N is the number of words in the reviews and M is the number of acronyms in the AcronymsFile.csv

Space Complexity: The space complexity of this code would be O(N), since we are storing the expanded_text list which is proportional to the length of the input text.

### Running Time for Algorithm B: {Plot here}


Time complexity:The time complexity of function `read_acronym_file` is O(n) where n is the number of rows in the `AcronymsFile.csv` file. For `replace_acronyms` function it is O(m) where m is the number of words in the input string. `process_csv_file` function is O(km) where k is the number of rows in the CSV file and m is the maximum number of words in a row that need to be replaced, and the time complexity of `process_all_csv_files` function is O(nkm) where n is the number of CSV files in the AppReviews folder and k and m are as defined above.

Space Complexity:The space complexity of this code is O(n) where n is the number of rows in the AcronymsFile.csv file as the acronym dictionary is stored in memory


### Unexpect edge cases: 
- Misinterpreting certain short word such as "it" as an abbreviation and replacing that. Similar to autocorrect.
- Matching the formatting exactly, is a challenge. We have handled null-exceptions or invalid input exceptions still.

### Task Contributions: 
- Implementation- with graph functionality: Shreya, Brendan
- Tracking execution time through the time module: Shreya, Brendan, Shreyasi
- Creating and editing the readme.md report: Shreya, Shreyasi, Brendan.
- Unexpected edge cases - Shreya, Brendan, Shreyasi
- Video recording: Shreyasi
