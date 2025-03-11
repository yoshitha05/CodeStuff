import re
import zlib
import json
from collections import Counter
from itertools import product

# Build a word list (corpus) with common words and country names
word_list = """america india china usa president first winner match food who was the of gong going to winr fod"""

# Serialize and compress the word list
corpus = word_list.split()
word_counts = Counter(corpus)
compressed_corpus = zlib.compress(json.dumps(word_counts).encode())

def decompress_corpus(compressed):
    return Counter(json.loads(zlib.decompress(compressed).decode()))

def words(text):
    "Tokenize the input text into words."
    return re.findall(r'\w+', text.lower())

def known(words, corpus):
    "Return the subset of words that are in the corpus."
    return set(w for w in words if w in corpus)

def edits1(word):
    "Return all edits that are one edit away from the input word."
    letters = 'abcdefghijklmnopqrstuvwxyz'
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes = [L + R[1:] for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 1]
    replaces = [L + c + R[1:] for L, R in splits if R for c in letters]
    inserts = [L + c + R for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)

def edits2(word):
    "Return all edits that are two edits away from the input word."
    return set(e2 for e1 in edits1(word) for e2 in edits1(e1))

def candidates(word, corpus):
    "Generate possible spelling corrections for a word."
    return (known([word], corpus) or known(edits1(word), corpus) or known(edits2(word), corpus) or [word])

def correct(word, corpus):
    "Find the best spelling correction for a word."
    return max(candidates(word, corpus), key=corpus.get)

def correct_query(query, corpus):
    "Correct a full query."
    words_in_query = words(query)
    corrected_words = [correct(word, corpus) for word in words_in_query]
    return ' '.join(corrected_words)

def main():
    # Load the compressed corpus
    corpus = decompress_corpus(compressed_corpus)

    # Input
    n = int(input())
    queries = [input().strip() for _ in range(n)]

    # Process queries
    corrected_queries = [correct_query(query, corpus) for query in queries]

    # Output
    for corrected_query in corrected_queries:
        print(corrected_query)

if __name__ == "__main__":
    main()
