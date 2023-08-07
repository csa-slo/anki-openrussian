class Word:

    def __init__(self, rank, word, url, translations):
        self.rank = rank
        self.word = word
        self.url = url
        self.translations = translations

    def add_rank(self, rank):
        self.rank = rank
    def add_url(self, url):
        self.url = url
    def add_word(self, word):
        self.word = word
    def add_translation(self, translation):
        self.translations.append(translation)
    
    def get_rank(self):
        return self.rank
    def get_url(self):
        return self.url
    def get_word(self):
        return self.word
    def get_translations(self):
        return self.translations

    def __str__(self):
        sep = '\t'
        return self.word + sep + str(self.translations) + sep + self.rank + sep + self.url + '\n'