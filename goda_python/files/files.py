fname="open_file.txt"
fhand=open(fname)
coun_lines=0
coun_words=0
coun_chars=0
for line in fhand:
    line =line.rstrip()
    coun_lines+=1
    print(line)
    for word in line.split():
        coun_words=coun_words+1
        for char in word:
            coun_chars+=1

print(f"count of lines= {coun_lines}\nCount of words= {coun_words}\nCount of characters = {coun_chars}")
    # line=line.rstrip()
    
