import random
import string

# dict_of_used_characters = {
#     'lenght': 8,
#     'capital_letters': True, 
#     'letters': True, 
#     'numbers': True, 
#     'symbols': False
# }

class Generator:

    def __init__(self, capital_letters=True, letters=True, numbers=True, symbols=False):
        self._password = string.ascii_lowercase if letters else ""
        self._password += string.ascii_uppercase if capital_letters else ""
        self._password += string.digits if numbers else ""
        self._password += "!@#$%^&*(_+=-§`~\';/.,}<>?:{)" if symbols else ""

    def set_last_used_characters():
        if dict_of_used_characters["capital_letters"] == True:
            checked_capital_letters = "checked"
        else:
            checked_capital_letters = ""
        
        if dict_of_used_characters["letters"] == True:
            checked_letters = "Checked"
        else:
            checked_letters = ""
        
        if dict_of_used_characters["numbers"] == True:
            checked_numbers = "checked"
        else:
            checked_numbers = ""
        
        if dict_of_used_characters["symbols"] == True:
            checked_symbols = "checked"
        else:
            checked_symbols = ""
            
        checked_characters = {
            "lenght": dict_of_used_characters["lenght"],
            "capital_letters": checked_capital_letters,
            "letters": checked_letters,
            "numbers": checked_numbers,
            "symbols": checked_symbols
        }
        return checked_characters

    def generated_password(self, lenght=8):
            return "".join([random.choice(self._password) for l in range(lenght)])
    


    