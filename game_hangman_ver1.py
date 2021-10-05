class HangMan:
    def __init__(self, keyword):
        self.keyword = keyword
    
    def tranfer_to_dashes(self):
        self.dashes = []
        for key in self.keyword:
            self.dashes += ['_']
        return self.dashes

    def play_game(self):
        hanged_man = 0
        result = self.tranfer_to_dashes()
        while (hanged_man < 6 and '_' in result):
            try_guess = input('Input 1 letter: ')
            if len(try_guess) != 1:
                try_guess = input('Please input only 1 letter: ')
            elif len(try_guess) == 1 and not try_guess in self.keyword:
                hanged_man += 1
                print(hanged_man)
            elif len(try_guess) == 1 and try_guess in self.keyword:
                for i in range(len(self.keyword)):
                    if self.keyword[i] == try_guess:
                            result[i] = try_guess
                            print(result)
        if hanged_man == 6:
            print('Game over')
        elif hanged_man < 6 and not '_' in result:
            print('Congratulation, you win. The answer is {}.'.format(''.join(result)))

    def __repr__(self):
        return self.keyword

        
        
word1 = input('What word do you want to play: ')

play1 = HangMan(word1)
play1.play_game()