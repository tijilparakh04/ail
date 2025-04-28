import string

# Preprocess: lowercase, remove punctuation, split into words
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

# One-hot encode
def one_hot_encode(words, vocab):
    encoding = [0] * len(vocab)
    for word in words:
        if word in vocab:
            index = vocab.index(word)
            encoding[index] = 1
    return encoding

# Print nicely
def print_one_hot(encoded_docs, vocab):
    print("Vocabulary:", vocab)
    print("\nOne-Hot Encodings:")
    for i, encoding in enumerate(encoded_docs):
        print(f"Document {i+1}: {encoding}")

# Main
if __name__ == "__main__":
    files = ['tech1.txt', 'tech2.txt', 'tech3.txt']

    documents = read_documents(files)
    vocab = build_vocabulary(documents)

    encoded_docs = []
    for words in documents:
        encoding = one_hot_encode(words, vocab)
        encoded_docs.append(encoding)

    print_one_hot(encoded_docs, vocab)
