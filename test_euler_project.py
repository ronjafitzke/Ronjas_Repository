from euler_project import problem_1, problem_2, problem_3, problem_4


def test_1():
    expected_result = 233168
    result = problem_1()
    assert result, expected_result


def test_2():
    expected_result = 4613732
    result = problem_2()
    assert result, expected_result


def test_3():
    expected_result = 6857
    result = problem_3(600851475143)
    assert result, expected_result


def test_4():
    expected_result = 906609
    result = problem_4()
    assert result, expected_result
