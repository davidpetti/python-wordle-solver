class wordleSolver:
    def __init__(self):
        self.wordList = self.generate_wordlist()

    def generate_wordlist(self,
                          green_letters={},
                          yellow_letters={},
                          grey_letters=[]):
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
            # at this point, wordList = all words with green letters in correct spots
                
            # yellow_keys = list(yellow_letters.keys())
            # for pos in yellow_keys:
            #     tempWordList = []
            #     for word in wordList:
            #         if yellow_letters[
            #                 pos] in word and yellow_letters[pos] != word[pos]:
            #             tempWordList.append(word)
            #     wordList = tempWordList
            # yellow_values = set(yellow_letters.values())
            # print(yellow_values)
            # for i in yellow_values:
            #     tempWordList = []
            #     for word in wordList:
            #         if i in word:
            #             tempWordList.append(word)
            #     wordList = tempWordList

                
            print(wordList)
        else:
            return wordList

    def get_green_letters(self):
        print("Enter green letters:\n")
        if input('Are there any green letters?(YES/NO): ').upper() == 'NO':
            x = False
        else:
            x = True
        letters = {}
        while x == True:
            let = input("Enter a Letter: ").lower()
            pos = int(input("Enter the letter's position(0-4): "))
            letters[pos] = let
            if input("Add another letter?(YES/NO): ").upper() == 'NO':
                x = False
        return letters

    def get_yellow_letters(self):
        pass

    def main(self):
        green_letters = self.get_green_letters()
        yellow_letters = self.get_yellow_letters()
        grey_letters = input(
            "Enter all grey letters(x,y,z...): ").lower().split(',')
        self.generate_wordlist(green_letters, yellow_letters, grey_letters)


w = wordleSolver()
# print(w.wordList)
w.main()
