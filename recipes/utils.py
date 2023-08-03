from fractions import Fraction

def number_str_to_float(amount_str: str):
    """
    Take in a amount string to return float(if possible)
    
    valid string return:
    float
    Boolean-> True
    
    Invalid stirng return:
    original string
    Boolean-> Flse
    
    Example:
    1 1/2 -> 1.5  , True
    32    -> 32.0 , True
    abc   -> abc  , False
    """
    success = False
    number_as_float = amount_str
    try:
        number_as_float = float(sum( [Fraction(s) for s in f'{amount_str}'.split()] ))
    except:
        pass
    if isinstance(number_as_float, float):
        success = True
    return number_as_float, success