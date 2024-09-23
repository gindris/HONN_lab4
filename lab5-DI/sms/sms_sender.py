from injector import inject


class SmsSender:
    @inject
    def send(self, number: str, message: str):
        print(f'sending "{message}" to {number}')