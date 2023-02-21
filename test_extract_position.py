import pytest
from extract_position import extract_position

def test_extract_pos_none():
    line = None
    assert extract_position(line) == None

def test_extract_pos_debug():
    line = "|debug| wduhiwuq wqekd ewkuqh eq."
    assert extract_position(line) == None

def test_extract_pos_error():
    line = "|error| numerical calculations could not converge."
    assert extract_position(line) == None

def test_extract_pos_no_x():
    line = "|update| the positron location in the particle accelerator is y:21.432."
    assert extract_position(line) == None

def test_extract_pos():
    line = '|update| the positron location in the particle accelerator is x:21.432'
    assert extract_position(line) == '21.432'
