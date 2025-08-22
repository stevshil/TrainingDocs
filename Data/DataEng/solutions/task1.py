import re

# Open the file
sp = open("../data/a-midsummer-nights-dream.txt","r")

wordsinplay={}

for line in sp:
    words = re.split(r'\W+', line)
    for word in words:
        newword="".join(ch.lower() for ch in word if ch.isalnum())
        if newword == "":
            continue
        if newword in wordsinplay:
            wordsinplay[newword]+=1
        else:
            wordsinplay[newword]=1

# All words unsorted
# print(wordsinplay)

top5 = sorted(wordsinplay.items(), key=lambda x: x[1], reverse=True)[:5]
print("Top 5 words in the play: ")
for word, count in top5:
    print(f"{word}: {count}")