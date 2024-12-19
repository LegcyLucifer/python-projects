from collections import Counter

file_path = 'Q-68.txt'

def count_word_frequency(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()

        words = text.lower().split()

        words = [word.strip('.,!?;:"()[]') for word in words]

        word_count = Counter(words)

        print("Word Frequencies:")
        for word, count in word_count.items():
            print(f"{word}: {count}")
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

count_word_frequency(file_path)