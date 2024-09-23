from injector import inject


class PhoneNumberValidator:
    @inject
    def validate(self, number: str) -> bool:
        return number is not None and number.isdecimal() and len(number) == 7
