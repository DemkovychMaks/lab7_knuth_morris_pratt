class KnuthMorris:

    def __init__(self, text, pattern):
        self.results = []
        self.pattern = pattern
        self.text = text

    def find_prefix_and_suffix(self):
        prefix_and_suffix = [0] * len(self.pattern)
        index_of_prefix = 0

        for pattern_iterator in range(1, len(self.pattern)):

            if self.pattern[pattern_iterator] == self.pattern[index_of_prefix]:
                prefix_and_suffix[pattern_iterator] = index_of_prefix + 1
                index_of_prefix += 1

            else:

                if index_of_prefix != 0:
                    index_of_prefix = prefix_and_suffix[index_of_prefix - 1]

        return prefix_and_suffix

    def Knuth_Morris_Pratt_algorithm(self):
        prefix_and_suffix = self.find_prefix_and_suffix()
        pattern_iterator = text_iterator = 0

        while pattern_iterator < len(self.text):

            if self.text[pattern_iterator] == self.pattern[text_iterator]:
                pattern_iterator += 1
                text_iterator += 1

                if text_iterator == len(self.pattern):
                    self.results.append(pattern_iterator - text_iterator)
                    text_iterator = prefix_and_suffix[text_iterator - 1]
            else:

                if text_iterator != 0:
                    text_iterator = prefix_and_suffix[text_iterator - 1]

                else:
                    pattern_iterator += 1

        return self.results
