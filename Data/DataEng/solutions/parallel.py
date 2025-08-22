import threading
from collections import Counter, defaultdict

wsmsnd = open("../data/a-midsummer-nights-dream.txt","r")

lines = wsmsnd.readlines()
chunk_size = len(lines) // 5
arrays = [lines[i*chunk_size : (i+1)*chunk_size] for i in range(4)]
arrays.append(lines[4*chunk_size:])

wsmsnd.close()

def count_words(lines, result, idx):
    counter = Counter()
    for line in lines:
        words = [word.strip(".,!?;:'\"()[]{}").lower() for word in line.split()]
        counter.update(words)
    result[idx] = counter

results = [None] * len(arrays)
threads = []

for i, arr in enumerate(arrays):
    t = threading.Thread(target=count_words, args=(arr, results, i))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

final_counts = defaultdict(int)
for counter in results:
    for word, count in counter.items():
        final_counts[word] += count

# final_counts now contains the word frequencies
# print(final_counts)

top5 = sorted(final_counts.items(), key=lambda x: x[1], reverse=True)[:5]
print("Top 5 words in the play: ")
for word, count in top5:
    print(f"{word}: {count}")