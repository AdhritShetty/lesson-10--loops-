word=str(input("enter a word:"))
char=str(input("enter a character:"))
count=0
i=0
while (i<len(word)):
    if word [i]==char:
        count=count+1
    i=i+1
print(count)
