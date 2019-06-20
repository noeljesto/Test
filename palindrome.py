def if_palindrome(number_list):
    if(number_list[0]=='-'):
        return ['-1']
    else:
        if(number_list == number_list[::-1]):
            return number_list
        else:
            return ['-1']
Input_string=input('Enter string: ')
number_list=[]
if(Input_string[0]=='-'): 
    number_list.append(Input_string[0])
for i in Input_string:
    for j in range(0,10):
        try:
            if(int(i)==j):
                number_list.append(i)
        except:
            pass
        else:
            pass
m=[]
final_list=if_palindrome(number_list)    
final_string=''.join(final_list)
print(final_string)