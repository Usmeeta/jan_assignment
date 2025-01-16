from collections import Counter
paragraph = """
    Honesty is the practice of speaking and acting truthfully and with integrity, and it is essential to building trust and respect in our relationships. Whether it's being honest with ourselves and others about our thoughts and feelings, admitting our mistakes and shortcomings, or communicating clearly and transparently, honesty can create a sense of authenticity and connection in our interactions with others.  
"""

words = paragraph.lower().split()
word_count = Counter(words)
top_repeated = word_count.most_common(3)

print("Word Frequences:")
for word, count in top_repeated:
    print(f"{word}: {count}")

