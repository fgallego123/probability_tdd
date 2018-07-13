from src.coin import Coin
from pytest import approx

def test_coin():
    c = Coin()
    assert isinstance(c, Coin)

def test_flip():
    c = Coin()
    assert c.flip() in c.states

def test_fair_coin():
    c = Coin()
    outcomes = []
    for i in range(100_000):
        outcome = c.flip()
        outcomes.append(outcome)
    assert (outcomes.count('H')/100_000) == approx(0.5, rel = 1e-2)