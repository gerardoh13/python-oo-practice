from random import choice
class WordFinder:
    """Word Finder: finds random words from a dictionary."""
    def __init__(self, path):
        self.file = open(path)
        self.words = self.read_words(self.file)
        self.words_read()

    def read_words(self, file):
        """returns list of words read from a file"""
        return [word.strip() for word in file]

    def words_read(self):
        """prints the number of words read from a file"""
        print(f"{len(self.words)} words read")
    
    def random(self):
        """returns random word from dictionary"""
        return choice(self.words)

class SpecialWordFinder(WordFinder):
    """Finds random words in a dictionary ignoring empty spaces or words following #"""
    def read_words(self, file):
        return [word.strip() for word in file if word.strip() and not word.startswith('#')]
        

