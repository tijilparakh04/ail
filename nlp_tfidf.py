import os
import math
import string

# Preprocess: lowercase, remove punctuation, split
def preprocess(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    return words

# Read files
def read_documents(file_list):
    documents = []
    for file in file_list:
        with open(file, 'r', encoding='utf-8') as f:
            text = f.read()
            words = preprocess(text)
            documents.append(words)
    return documents

# Build vocabulary
def build_vocabulary(documents):
    vocab = set()
    for words in documents:
        vocab.update(words)
    return sorted(list(vocab))

# Calculate Term Frequency (TF)
def compute_tf(words, vocab):
    tf_dict = {}
    total_words = len(words)
    for word in vocab:
        tf_dict[word] = words.count(word) / total_words
    return tf_dict

# Calculate Inverse Document Frequency (IDF)
def compute_idf(documents, vocab):
    idf_dict = {}
    N = len(documents)
    for word in vocab:
        count = sum(1 for doc in documents if word in doc)
        idf_dict[word] = math.log(N / (1 + count)) + 1  # smoothing
    return idf_dict

# Calculate TF-IDF
def compute_tf_idf(tf_dict, idf_dict):
    tfidf_dict = {}
    for word in tf_dict:
        tfidf_dict[word] = tf_dict[word] * idf_dict[word]
    return tfidf_dict

# Print nicely
def print_tfidf(tfidf_matrix, vocab):
    print("TF-IDF Scores:\n")
    for i, doc in enumerate(tfidf_matrix):
        print(f"Document {i+1}:")
        for word in vocab:
            print(f"{word}: {doc[word]:.4f}", end=" | ")
        print("\n")

# Main
if __name__ == "__main__":
    files = ['place1.txt', 'place2.txt', 'place3.txt']

    documents = read_documents(files)
    vocab = build_vocabulary(documents)

    idf_dict = compute_idf(documents, vocab)

    tfidf_matrix = []
    for words in documents:
        tf = compute_tf(words, vocab)
        tfidf = compute_tf_idf(tf, idf_dict)
        tfidf_matrix.append(tfidf)

    print_tfidf(tfidf_matrix, vocab)
