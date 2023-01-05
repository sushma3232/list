# write a python function that accept a string and calculate the num of uppercase and lowercase letters
# string="The quick Brow Fox"
# output:no. of uppercase letters:3
    #   no. of lowercase letters:12
    
def func(a):
    capital_count=0
    small_count=0
    i=0
    while i<len(a):
        if a[i].isupper():
            capital_count+=1
        if a[i].islower():
            small_count+=1
        i=i+1
    print(capital_count)
    print(small_count)
a="The quick Brow Fox"
func(a)
    
