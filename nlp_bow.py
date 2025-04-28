import os
import string

# Function to preprocess text
def preprocess(text):
    # Lowercase
    text = text.lower()
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Tokenize (split into words)
    words = text.split()
    return words

# Read and preprocess all files
def read_reviews(file_list):
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
    return sorted(list(vocab))  # sorted for nice order

# Build Bag of Words matrix
def build_bow(documents, vocab):
    bow_matrix = []
    for words in documents:
        word_count = {}
        for word in vocab:
            word_count[word] = words.count(word)
        bow_matrix.append(word_count)
    return bow_matrix

# Print BoW matrix
def print_bow(bow_matrix, vocab):
    print("Vocabulary:", vocab)
    print("\nBag of Words Matrix:")
    for i, doc in enumerate(bow_matrix):
        print(f"Document {i+1}:")
        for word in vocab:
            print(f"{word}: {doc[word]}", end=" | ")
        print("\n")

# Main
if __name__ == "__main__":
    # List of files
    files = ['review1.txt', 'review2.txt', 'review3.txt']

    # Read and preprocess
    documents = read_reviews(files)

    # Build vocab
    vocab = build_vocabulary(documents)

    # Build BoW
    bow_matrix = build_bow(documents, vocab)

    # Print result
    print_bow(bow_matrix, vocab)
