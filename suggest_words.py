from file_handler import FileHandler


def main():
    # Define the URL of the Merriam-Webster website to parse
    url = 'https://www.merriam-webster.com/browse/dictionary/b'

    # Create an instance of the FileHandler class
    file_handler = FileHandler()

    # Parse the website to extract words
    words = file_handler.parse_website(url)

    # Suggest words for addition to the text file
    approved_words = file_handler.suggest_words(words)

    # Print approved words
    print("Approved words:")
    for word in approved_words:
        print(f"Word: {word['word']}, Category: {word['category']}, Hint: {word['hint']}")

    # Optionally, add approved words to the text file
    # Implement this part based on your file handling logic


if __name__ == "__main__":
    main()
