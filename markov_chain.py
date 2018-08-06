import random
import json


class MarkovChain:

    def __init__(self, start="$START$", end=" $END$", json_str=""):
        """
        :param start: key in dict from where to start
        :param end: word on which to end generate_chain
        """
        self.start = start
        self.end = end
        self.uniqueWordDict = json.loads(json_str) if json_str else {self.start: {}}

    def append_to_matrix(self, text):
        """
        Adds the text to the probability dictionary
        """
        text = text + self.end
        prev_word = self.start
        # Add words and their links to the dict
        for word in text.split():
            if word not in self.uniqueWordDict:
                self.uniqueWordDict[word] = {}
            if word not in self.uniqueWordDict[prev_word]:
                self.uniqueWordDict[prev_word][word] = 1
            else:
                self.uniqueWordDict[prev_word][word] += 1
            prev_word = word

    def generate_chain(self):
        """
        returns the generated markov chain
        without the start or end tags
        """
        chain = ""
        word_to_add = self.get_random_word(self.start)
        while word_to_add != self.end[1:]:
            chain += word_to_add + " "
            word_to_add = self.get_random_word(word_to_add)
        return chain[:-1]

    def get_random_word(self, prev_word):
        """
        chooses random word from the dictionary weighted
        by probability
        """
        print(self.uniqueWordDict)
        return random.choice(  # Magic
            [key for key, value in self.uniqueWordDict[prev_word].items()
             for x in range(value)])

    def to_json(self):
        return json.dumps(self.uniqueWordDict)
