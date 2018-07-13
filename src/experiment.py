from src.coin import Coin

class Experiment:
    def p_2_heads(self):
        c = Coin()
        successes = []
        trials = 100_000
        for _ in range(trials):
            is_success = [c.flip() for _ in range(2)].count('H') == 2
            successes.append(is_success)
        return sum(successes) / trials

    def pattern(self, sequence):
        trials = len(sequence)
        c = Coin()
        sample = []
        for _ in range(10_100_000):
            trial = ''.join([c.flip() for _ in range(trials)])
            sample.append(trial)
        return sample.count(sequence)/len(sample)
