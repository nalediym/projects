import re
import os
from typing import Callable as method, Type as type

# TODO: add method type to Callable
# TODO: add class type to Callable



def create_dummy_empty_input(input_type: type):
    """
    Perform edge cases for empty input of any type.

    Example:
    """
    if isinstance(input, type(None)):
        return None
    if isinstance(input, str):
        return ""
    if isinstance(input, list):
        return []
    if isinstance(input, dict):
        return {}
    if isinstance(input, tuple):
        return ()
    if isinstance(input, set):
        return set()
    if isinstance(input, bytes):
        return bytes()
    if isinstance(input, int):
        return 0
    if isinstance(input, float):
        return 0.0
    if isinstance(input, os.PathLike):
        return None
    if isinstance(input, bool):
        return False

def create_dummy_input(edge_case_function: method, input_type: type):
    """
    Create dummy input for given edge case function 
    Input:
        edge_case_function: method : edge case function to be tested (e.g. empty_input)
        input_type: type : type of input for given edge case function (e.g. str, list, etc.)
    Output:
        dummy_input: any : dummy input for given edge case function (e.g. 0, "", [], etc.)
    """
    pass

def invalid_input(input: any):
    """
    Perform edge cases.
    """
    pass
def perform_edge_cases():
    """
    Perform all edge case functions
    """
    EDGE_CASE_FUNCTIONS = [
        invalid_input,
    ]
    for edge_case_function in EDGE_CASE_FUNCTIONS:
        for input_type in [int, str, list, dict, tuple, set, bytes, os.PathLike]:
            dummy_input = create_dummy_input( edge_case_function, input_type)
            edge_case_function(dummy_input)   
