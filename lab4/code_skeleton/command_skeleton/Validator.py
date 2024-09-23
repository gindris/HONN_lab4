from Validation import Validation

class Validator(Validation):
    def __init__(self):
        self.Allvalidations = []

    def validate(self):
        if all(self.Allvalidations):
            return True
        return False
    
    def add_validation(self, validation):
        self.Allvalidations.append(validation.validate())