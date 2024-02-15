import requests
from bs4 import BeautifulSoup


class FileHandler:
    @staticmethod
    def create_word_file(words, filename):
        with open(filename, 'w') as file:
            for word in words:
                file.write(word + '\n')

    def load_words_from_file(self, filename):
        words = []
        with open(filename, 'r') as file:
            for line in file:
                word = line.strip()
                words.append(word)
        return words

    @staticmethod
    def parse_website(url):
        words = []
        try:
            # Send a GET request to the URL
            response = requests.get(url)

            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                # Parse the HTML content using BeautifulSoup
                soup = BeautifulSoup(response.text, 'html.parser')

                # Find the section containing the words
                word_section = soup.find('div', class_='section-starts-with')

                # Extract words from the section
                if word_section:
                    word_list = word_section.find_all('a')
                    for word_element in word_list:
                        word = word_element.text.strip()
                        words.append(word)
            else:
                print(f"Failed to retrieve data from {url}. Status code: {response.status_code}")
        except Exception as e:
            print(f"An error occurred: {e}")

        return words

    @staticmethod
    def suggest_words(words):
        approved_words = []
        for word in words:
            print(f"Do you want to add '{word}' to the word list? (yes/no)")
            response = input().lower()
            if response == 'yes':
                approved_words.append(word)
        return approved_words


# Test the suggest_words method
url = "https://www.merriam-webster.com/browse/dictionary/b"
words = FileHandler.parse_website(url)
approved_words = FileHandler.suggest_words(words)
print("Approved words:")
print(approved_words)
