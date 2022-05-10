class wordleSolver:
    def __init__(self):
        self.wordList = self.generate_wordlist()

    def generate_wordlist(self, green_letters={}, yellow_letters={}, grey_letters=[]):
        # creates variable wordList with contents [word1, word2, word3, ...]
        with open('words', 'r') as wordList_file:
            wordList = []
            for row in wordList_file:
                wordList.append(row.strip('\n'))
        if green_letters != {} or yellow_letters != {} or grey_letters != []:
            for let in grey_letters:
                tempWordList = []
                for word in wordList:
                    if not let in word:
                        tempWordList.append(word)
                wordList = tempWordList
            green_keys = list(green_letters.keys())
            for pos in green_keys:
                tempWordList = []
                for word in wordList:
                    if word[pos] == green_letters[pos]:
                        tempWordList.append(word)
                wordList = tempWordList
            # at this point, wordList = all words with green letters in correct spots and without grey letters
            yellow_keys = list(yellow_letters.keys())
            for pos in yellow_keys:
                for list_pos, letter in enumerate(yellow_letters[pos]):
                    tempWordList = []
                    for word in wordList:
                        if letter in word and pos != word.index(letter):
                            tempWordList.append(word)
                    wordList = tempWordList
            return wordList
        else:
            return wordList

    def get_green_letters(self):
        print("Enter green letters:\n")
        if input('Are there any green letters?(Y/n): ').upper() == 'N':
            x = False
        else:
            x = True
        letters = {}
        while x == True:
            let = input("Enter a Letter: ").lower()
            pos = int(input("Enter the letter's position(0-4): "))
            letters[pos] = let
            if input("Add another letter?(Y/n): ").upper() == 'N':
                x = False
        return letters

    def get_yellow_letters(self):
        print("Enter yellow letters:\n")
        if input('Are there any yellow letters?(Y/n): ').upper() == 'N':
            x = False
        else:
            x = True
        letters = {0: [], 1: [], 2: [], 3: [], 4: []}
        while x == True:
            let = input("Enter a Letter: ").lower()
            pos = int(input("Enter the letter's position(0-4): "))
            letters[pos].append(let)
            if input("Add another letter?(Y/n): ").upper() == 'N':
                x = False
        return letters

    def main(self):
        green_letters = self.get_green_letters()
        yellow_letters = self.get_yellow_letters()
        grey_letters = input("Enter all grey letters(x,y,z...): ").lower().split(',')
        solved_wordList = self.generate_wordlist(green_letters, yellow_letters, grey_letters)
        # ', '.join(solved_wordList)
        print(solved_wordList)


w = wordleSolver()
w.main()