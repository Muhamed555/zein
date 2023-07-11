from ._utils import clean_txt, check_text
import pandas as pd
import re
import pkg_resources
import pickle


class ar():
    def __init__(self, path: object = pkg_resources.resource_filename('zein', 'data/data.csv')) -> object:
        # default argument
        self.insulting_words = pd.read_csv(path)
        # load the vectorizer and the model
        self.model_path_prompt_vectorizer = pkg_resources.resource_filename('zein', 'models/prompt_vectorizer.pkl')
        self.prompt_vectorizer = pickle.load(open(self.model_path_prompt_vectorizer, "rb"))

        self.model_path_prompt_model = pkg_resources.resource_filename('zein', 'models/prompt_svm_model.pkl')
        self.prompt_model = pickle.load(open(self.model_path_prompt_model, "rb"))

    def filter_text(self, text: str, symbol='*') -> str:
        if check_text(text) == 'OFF':
            # Compile a regular expression pattern.
            pattern = re.compile('|'.join(self.insulting_words['words']), re.IGNORECASE)

            # Replace the matching words with asterisks.
            censored_text = re.sub(pattern, lambda match: symbol * len(match.group()), text)

            # Return the censored text.
            return censored_text
        else:
            return text

    def is_profane(self, text: str) -> bool:
        if check_text(text) == 'OFF':
            # compile a regular expression pattern
            pattern = re.compile('|'.join(self.insulting_words['words']), re.IGNORECASE)

            # check if the text matches the pattern
            match = re.search(pattern, text)

            # return True if there is a match, False otherwise
            return bool(match)
        else:
            return False

    def find_insulting_words(self, text: str) -> list:
        # create an empty list to store the results
        results = []

        # split the text into words
        words = text.split()

        # loop through the words and their indices
        for index, word in enumerate(words):
            if check_text(text) == 'OFF':
                # loop through the insulting words
                for insult in self.insulting_words['words']:
                    # create a regular expression pattern with some variations
                    # for example, allow optional spaces and punctuation around the word
                    pattern = re.compile(r'\s*[.,:;!?]*\s*' + insult + r'\s*[.,:;!?]*\s*', re.IGNORECASE)
                    # check if the word matches the pattern
                    match = re.search(pattern, word)
                    # if there is a match, append a tuple of the word and the index to the results list
                    if match:
                        results.append((word, index))
                        # break the inner loop to avoid duplicate matches
                        break
            else:
                return None

        # return the results list
        return results
    
    def check_prompt(self, text: str) -> bool:
      # transform the text into features using the vectorizer
      features = self.prompt_vectorizer.transform([clean_txt(text)])
      # predict the label using the model
      label = self.prompt_model.predict(features)[0]

      if label == 1:
        return True
      else:
        return False


