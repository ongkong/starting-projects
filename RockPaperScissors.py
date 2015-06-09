# improvement: use modulus to decide winner
from random import choice 
class RockPaperScissors:
    # choices
    options = ('rock','paper','scissors')
    
    def __init__(self):
    # to keep track 
        self.picked = []
        self.score = []
        
    def pick(self): self.picked.append(choice(RockPaperScissors.options))
    # randomly choose one of the above choices
    
    def __cmp__(self, user):
        # sets up the logic to decide who wins (probably should have just created a new function...
        # instead of overriding)
        if self.picked[len(self.picked)-1] == 'rock':
            logic = {'rock':0,'paper':1,'scissors':-1}
            if logic[user] > 0:
                return 1
                
            elif logic[user] == 0:
                return 0
                
            else:
                return -1
                


        elif self.picked[len(self.picked)-1] == 'paper':
            logic = {'rock':-1,'paper': 0,'scissors':1}
            if logic[user] > 0:
                return 1
                
            elif logic[user] == 0:
                return 0
                
            else:
                return -1
                

        else:
            logic = {'rock':1,'paper':-1,'scissors':0}
            if logic[user] > 0:
                return 1
                
            elif logic[user] == 0:
                return 0
                
            else:
                return -1
    # the outcomes and actions            
    def win(self):
        self.score.append('Win')
        print "Darn, I chose: %s" % self.picked[len(self.picked)-1]\
              +"\nYou Win!"
    def tie(self):
        self.score.append('Tie')
        print "Boring...I chose: %s" % self.picked[len(self.picked)-1]\
              +"\nIt's a tie"
    def lose(self):
        self.score.append('Lose')
        print "WOOP WOOP, I chose: %s" % self.picked[len(self.picked)-1]\
              +"\nYou Lose!"
        
    # lists rounds and results
    def display(self):
        round = 1
        for x in self.score:
            print "Round %d: %s" % (round,x)
            round = round + 1
            
if __name__ == "__main__":
    game = RockPaperScissors()
    play = True
    while play:
        game.pick()
        user = raw_input('Choose rock, paper, or scissors\n').lower()
        if cmp(game,user) == 1:
            game.win()
        elif cmp(game,user) == 0:
            game.tie()
        else:
            game.lose()
            
        if raw_input('Do you want to see the results so far? (Y for yes and N for no)\n').lower() == 'y':
            game.display()
        if raw_input('Play again? (Y for yes and N for no)\n').lower() == 'n':
            play = False
            
