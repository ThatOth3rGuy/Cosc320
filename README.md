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

Space complexity: 


Time Complexity:



### Running Time for Algorithm B: {Plot here}


Space complexity:


Time Complexity:
