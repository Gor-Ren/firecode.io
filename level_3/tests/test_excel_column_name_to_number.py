# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 21:20:09 2017

@author: Gor-Ren
"""


import pytest
from level_3.excel_column_name_to_number import excel_column_name_to_number

def test_A():
    assert excel_column_name_to_number('A') == 1

def test_Z():
    assert excel_column_name_to_number('Z') == 26

def test_AA():
    assert excel_column_name_to_number('AA') == 27