# test_one.py
import math
import pytest
from wallet import Wallet, InsufficientAmount


def calculate_kinetic_energy(mass, velocity):
    """Returns kinetic energy of mass [kg] with velocity [ms]."""
    return 0.5 * mass * velocity ** 2


def test_calculate_kinetic_energy():
    mass = 10  # [kg]
    velocity = 4  # [m/s]
    assert calculate_kinetic_energy(mass, velocity) == 80


def get_average(li):
    if not li:
        return float('NaN')
    sum = 0
    for num in li:
        sum += num
    mean = sum / len(li)
    return mean


def test_get_average_normal_use_case():
    li = [2, 4, 6, 8]
    assert math.isclose(get_average(li), 5)


def test_get_average_empty_list():
    li = []
    assert math.isnan(get_average(li))


def palindrome(word):
    # test_exception.py
    if not isinstance(word, str):
        raise TypeError('Please provide a string argument')
    return word == word[::-1]


def test_palindrome():
    with pytest.raises(TypeError):
        palindrome(44)

# WITHOUT FIXTURES
def test_default_initial_amount():
    wallet = Wallet()
    assert wallet.balance == 0


def test_setting_initial_amount():
    wallet = Wallet(100)
    assert wallet.balance == 100


def test_wallet_add_cash():
    wallet = Wallet(10)
    wallet.add_cash(90)
    assert wallet.balance == 100


def test_wallet_spend_cash():
    wallet = Wallet(20)
    wallet.spend_cash(10)
    assert wallet.balance == 10


def test_wallet_spend_cash_raises_exception_on_insufficient_amount():
    wallet = Wallet()
    with pytest.raises(InsufficientAmount):
        wallet.spend_cash(100)


# WITH FIXTURES 
@pytest.fixture
def empty_wallet():
    '''Returns a Wallet instance with a zero balance'''
    return Wallet()

@pytest.fixture
def wallet():
    '''Returns a Wallet instance with a balance of 20'''
    return Wallet(20)

def test_default_initial_amount(empty_wallet):
    assert empty_wallet.balance == 0

def test_setting_initial_amount(wallet):
    assert wallet.balance == 20

def test_wallet_add_cash(wallet):
    wallet.add_cash(80)
    assert wallet.balance == 100

def test_wallet_spend_cash(wallet):
    wallet.spend_cash(10)
    assert wallet.balance == 10

def test_wallet_spend_cash_raises_exception_on_insufficient_amount(empty_wallet):
    with pytest.raises(InsufficientAmount):
        empty_wallet.spend_cash(100)