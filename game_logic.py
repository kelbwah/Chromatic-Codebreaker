import import_handler as shared
class Sequence:
    def __init__(self):
        self.colors = ['black', 'red', 'green', 'blue', 'orange', 'yellow', 'gray', 'pink', 'purple']
        self.guess = None #This is also in the form of a list of strings of a color
        self.correct = False
        self.sequence = self.create_random_sequence()

    def create_random_sequence(self):
        self.sequence = [shared.random.choice(self.colors) for i in range(6)]
        return self.sequence
    
    def guess_sequence(self):
        max_length_each_color = {} #This dictionary is to take the max occurences of each color in the actual sequence

        list_of_correct_or_incorrect = {
            0 : None,
            1 : None,
            2 : None,
            3 : None,
            4 : None,
            5 : None
        } 
        # This list contains for each part of the sequence, whether the color isn't in the sequence (NIS) or if it needs to be placed somewhere else (NIP) or in correct position (ICP)
        # NIS = Not in sequence ---------- NIP = Not in place ---------- ICS = In correct position
        
        for color in self.sequence:
            if color not in max_length_each_color.keys():
                max_length_each_color[color] = 1
            elif color in max_length_each_color.keys():
                max_length_each_color[color]+=1
        
        amount_of_colors_seen = max_length_each_color.copy() #This dictionary is to keep track of the amount of colors we have currently seen
        for key in amount_of_colors_seen.keys():
            amount_of_colors_seen[key] = 0
        

        #There's probably a very easier way to do this, this is the laziest way
        if self.guess == self.sequence:
            self.correct = True
            return 'You got the correct sequence!'
        elif self.guess != self.sequence:
            self.correct = False
            for i in range(len(self.guess)): #First checking correct guesses 
                if self.guess[i] in amount_of_colors_seen.keys():
                    if amount_of_colors_seen[self.guess[i]] < max_length_each_color[self.guess[i]]:
                        if self.guess[i] == self.sequence[i]:
                            list_of_correct_or_incorrect[i] = 'ICP'
                            amount_of_colors_seen[self.guess[i]]+=1

            for i in range(len(self.guess)): #Then checking incorrect guesses
                if list_of_correct_or_incorrect[i] != "ICP": #making sure not to iterate through correct guesses
                    if self.guess[i] in amount_of_colors_seen.keys():
                        if amount_of_colors_seen[self.guess[i]] < max_length_each_color[self.guess[i]]:
                            if self.guess[i] != self.sequence[i]:
                                list_of_correct_or_incorrect[i] = 'NIP'
                                amount_of_colors_seen[self.guess[i]]+=1
                        else:
                            list_of_correct_or_incorrect[i] = "NIS"
                    else:
                        list_of_correct_or_incorrect[i] = "NIS"

        return list_of_correct_or_incorrect


"""TEST CODE"""
# sequence = Sequence()
# sequence.sequence = ['black', 'red', 'red', 'black', 'black', 'black']
# print(sequence.sequence)
# sequence.guess = ['black', 'red', 'red', 'red', 'black', 'black']
# print(sequence.guess)
# print(sequence.guess_sequence())
