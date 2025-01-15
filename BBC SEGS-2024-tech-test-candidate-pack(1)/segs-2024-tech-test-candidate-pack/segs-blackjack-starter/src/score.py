class Score:

    def __init__(self, givenSet):
        self.toScore = givenSet
        self.score = 0
        self.ace = False
        self.alt = 0

    def calculate(self):
        for i in self.toScore:
            if isinstance(i[1], list):
                #if the card is an ace, must create the score if 1 was used and if 11 was used
                self.ace = True
                if self.score +11 > 21:
                    #unless 11 would push it over 21, in which case both are updated with 1
                    self.score += 1
                else:
                    self.score += 11
                self.alt += 1
            else:
                #if the card is not an ace, both scores are updated equally
                self.score += i[1]
                self.alt += i[1]
        if self.ace == False:
            #if there isn't an ace, both scores are equal so self.score is returned
            if self.score > 21:
                return "bust"
            else:
                return self.score
        elif (self.score > 21 and self.alt <= 21) or self.alt == 21:
            #in this case self.score is bust but self.alt is valid so self.alt is returned
            return self.alt
        elif (self.alt > 21 and self.score <= 21) or self.score == 21:
            #self.alt is bust but self.alt is valid so self.score is returned
            return self.score
        elif self.score > 21 and self.alt > 21:
            #both are bust
            return "bust"
        elif self.score > self.alt:
            #if neither are bust, the higher score is the better one so that is returned
            return self.score
        else:
            return self.alt
