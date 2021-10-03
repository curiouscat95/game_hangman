class HangMan:
    def __init__(self, keyword):
        self.keyword = keyword
    
    def __repr__(self):
        return self.keyword

        
        
word1 = input('What word do you want to play: ')
play1 = HangMan(word1)

print(play1)