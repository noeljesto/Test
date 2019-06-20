from collections import Counter  
def if_anagram(input1, input2): 
    return Counter(input1) == Counter(input2) 
string=""
with open('sample.txt') as file_sample:
    for i in file_sample:
        string=string+i
string=string.replace(',','').strip()
string=string.replace('.','').strip()
string=string.replace('?','').strip()
# print(string.split(' '))
no_of_words=string.split(' ')
# print(no_of_words)
result=[]
word=[]
for i in range(len(set(no_of_words))):
    # unique_words=[]
    word=[]
    unique_words=set()
    for j in range(i+1,len(no_of_words)):
        if(no_of_words[j] not in result and no_of_words[i] != no_of_words[j]):
            if(if_anagram(no_of_words[i],no_of_words[j])):
                # word.append(no_of_words[i])
                if (no_of_words[i] and no_of_words[j] not in word):
                    # print(no_of_words[i])
                    # print(no_of_words[j])
                    # print(word)
                    unique_words.add(no_of_words[i])
                    unique_words.add(no_of_words[j])
    if(len(unique_words)!=0):
        result.append(list(unique_words))
# print(result)
for i in result:
    i=str(i).replace('[','').strip()
    i=str(i).replace(']','').strip()
    i=str(i).replace(' ','').strip()
    print(i)

