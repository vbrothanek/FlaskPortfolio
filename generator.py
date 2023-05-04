import random
import string

class Generator:

    def __init__(self, capital_letters=True, letters=True, numbers=True, symbols=False):
        self._password = string.ascii_lowercase if letters else ""
        self._password += string.ascii_uppercase if capital_letters else ""
        self._password += string.digits if numbers else ""
        self._password += "!@#$%^&*(_+=-§`~\';/.,}<>?:{)" if symbols else ""


    def generated_password(self, lenght=8):
            return "".join([random.choice(self._password) for l in range(lenght)])
    

# if __name__ == '__main__':
#      generate = Generator(capital_letters=True, letters=True, numbers=True, symbols=True)
#      print(generate.generated_password(lenght=8))
     
    