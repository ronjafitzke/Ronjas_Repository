from vowels_eingabe import vowels


def test_a():
    assert vowels("a"), 1
def test_i():
    assert vowels("i"), 1
def test_o():
    assert vowels("o"), 1
def test_u():
    assert vowels("u"), 1
def test_A():
    assert vowels("A"), 1
def test_E():
    assert vowels("E"), 1
def test_I():
    assert vowels("I"), 1
def test_O():
    assert vowels("O"), 1
def test_U():
    assert vowels("U"), 1
def test_1():
    assert vowels("Hallo Welt"), 3
def test_2():
    assert vowels("Bananen sind toll"), 5
def test_3():
    assert vowels("AEIOUaeiou"), 10