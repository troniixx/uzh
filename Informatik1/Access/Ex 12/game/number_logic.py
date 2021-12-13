from public.game_logic import GameLogic #Access Ready import
from random import choice
from string import digits


class NumberLogic(GameLogic):

    def check(self, guess):
        if len(set(guess)) != self.len_words:
            raise Warning('duplicate digits')
        else:
            return super().check(guess)

    def _word_selection(self):
        def gen():
            for _ in range(self.num_words):
                num = ""
                while len(num) < self.len_words:
                    temp = choice(digits)
                    if temp not in num:
                        num += temp
                yield num
        return list(gen())
    
    def _generate_feedback(self, guess):
        matching = 0
        for i in guess:
            if i in self.password:
                matching += 1
        self.num_attempts -= 1
        return "%d/%d correct" % (matching, self.len_words)
