Word=input("enter the string ")
def most_frequent(string):
    d=dict()
    for key in string:
        if key not in d:
            d[key]=1
        else:
            d[key]+=1
    return d

#using the most frequent function 
output = most_frequent(Word)
frequency = dict( sorted(output.items(),
        key=lambda item: item[1],
        reverse=True))

print(frequency)
