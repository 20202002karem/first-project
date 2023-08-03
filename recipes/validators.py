import pint
from pint.errors import UndefinedUnitError
from django.core.exceptions import ValidationError

def validat_unit_of_measure(value):
    ureg = pint.UnitRegistry()
    try:
        single_unit = ureg[value]
    except UndefinedUnitError as e :
        raise ValidationError(f'{value} is not avalid unit of mesure')
    except:
        raise ValidationError(f'{value} is not avalid unit of mesure')