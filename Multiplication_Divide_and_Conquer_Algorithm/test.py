from multiplication import multi
import random


def test_mult1():
    assert multi(0, 2233) == 0
    assert multi(2332, 0) == 0
    assert multi(1, 2333) == 2333
    assert multi(2333, 1) == 2333


def test_mult2():
    assert multi(2, 22) == 44
    assert multi(10, 60) == 600
    assert multi(44, 2) == 88
    assert multi(22, 22) == 484


def test_mult3():
    num_1 = random.randint(0, 100)
    num_2 = random.randint(0, 100)
    assert multi(num_1, num_2) == num_1 * num_2


def test_mult4():
    assert multi(123, 456) == 56088
    assert multi(9999, 1111) == 11108889
    assert multi(123456, 7890) == 974530640
    assert multi(98765, 4321) == 425352965


def test_mult5():
    assert multi(1, 1) == 1
    assert multi(1, 2) == 2
    assert multi(2, 2) == 4
    assert multi(9, 9) == 81
