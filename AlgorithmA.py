import pandas as pd
import os

def algorithmA(file,list):
    abbreviation_dict = pd.read_csv(list,header=None,sep="-",usecols=[i for i in range(2)])

    input_file = file
    output_file = os.path.abspath("Milestone3/AppReviews") + "/output.txt"

    df = pd.DataFrame(input_file)
    expanded_text = []
    for text in df['content']:
        words = text
        expanded_line = []
        for word in words:
            if word in abbreviation_dict[0].values:
                full_form = abbreviation_dict.loc[abbreviation_dict[0] == word, 1]
                expanded_line.append(full_form)
            else:
                expanded_line.append(word)  # word is not replaced.
        expanded_text.append(' '.join(expanded_line))
    df[1] = expanded_text

    df.to_csv(output_file, header=False, index=False) 
    return df.to

def testA():
    i = 0
    path = os.path.abspath("Milestone3/AppReviews")
    f_list = os.listdir(path)
    df = pd.DataFrame()
    #append all files together
    # for file in f_list:
    #     df_temp = pd.read_csv("Milestone3/AppReviews/"+file,sep=',',header=None,index_col='content',na_filter=False)
    #     df_temp
    # df_append
    for f in range(0,10):
        file = path+"/"+f_list[i]
        i = i+1
        #print(i)
        temp = pd.read_csv(file,usecols=['content'],on_bad_lines='skip',skip_blank_lines=True)
        df = pd.concat([df,temp])
    abv = 'Milestone3/AcronymsFile.csv'
    print(algorithmA(df,abv))
    
    
testA()