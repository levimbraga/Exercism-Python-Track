class HighScores:
    def __init__(self, scores):
        self.scores = scores

    def latest(self):
        latest_score = self.scores[-1]
        return latest_score
    
    def personal_best(self):
        pb = 0
        for score in self.scores:
            if score > pb:
                pb = score
        return pb
    
    def personal_top_three(self):
        pb_3 = [0]
        for score in self.scores:
            if score > pb_3[0]:
                pb_3.insert(0, score)
            elif score > pb_3[1]:
                pb_3.insert(1, score)
            elif score > pb_3[2]:
                pb_3.insert(2, score)

        if len(self.scores) < 3:
            return pb_3[:len(self.scores)]
        else:
            return pb_3[0:3]
    
