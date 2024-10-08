from typing import List

from infrastructure.app_module import AppModule
from injector import Injector
from database.i_phone_book_repository import IPhoneBookRepository
from database.phone_book_file_repository import PhoneBookFileRepository
from database.phone_book_sqlite_repository import PhoneBookSqliteRepository
from environment import Environment

from phone_book.invalid_number_exception import InvalidNumberException
from phone_book.phone_book_entry import PhoneBookEntry
from phone_book.i_phone_book import IPhoneBook
from phone_book.phone_book import PhoneBook
from phone_book.phone_book_fake import PhoneBookFake
from phone_book.phone_number_validator import PhoneNumberValidator
from sms.message import Message
from sms.sms_sender import SmsSender
from sales_man import SalesMan

def print_messages(messages: List[Message]):
    for message in messages:
        print(message)

def failure_adding_numbers(phone_book: IPhoneBook):
    try:
        phone_book.add(PhoneBookEntry(name="bongo", number="0"))
    except InvalidNumberException:
        print("Invalid number 0")

    try:
        phone_book.add(PhoneBookEntry(name="bongo", number="abcdefg"))
    except InvalidNumberException:
        print("Invalid number abcdefg")

    try:
        phone_book.add(PhoneBookEntry(name="bongo", number="12345678"))
    except InvalidNumberException:
        print("Invalid number 12345678")

    print()


def seed_phone_book(phone_book: IPhoneBook):
    phone_book.add(PhoneBookEntry(name="bob", number="1234577"))

    phone_book.add(PhoneBookEntry(name="bingo", number="7654321"))


def sales_man_one(sales_man: SalesMan, phone_book: PhoneBookFake):
    sales_man.send_message("bob", "bobby boy")
    sales_man.send_message("bingo", "bingo boy")

    phone_book.add(PhoneBookEntry(name="bingo", number="9876543"))

    sales_man.send_message("bingo", "bingo new number")
    sales_man.send_message("bobby", "messages galore")

    print()
    print("successful messages for sales man 1:")
    print_messages(sales_man.sent_messages)

    print()
    print("failed messages for sales man 1:")
    print_messages(sales_man.failed_messages)


def sales_man_two(sales_man: SalesMan):
    sales_man.send_message("Inigo Montoya", "You killed my father. Prepare to die")
    sales_man.send_message("bingo", "bingo from sales man two")

    print()
    print("successful messages for sales man 2:")
    print_messages(sales_man.sent_messages)

    print()
    print("failed messages for sales man 2:")
    print_messages(sales_man.failed_messages)


def main():
    environment = Environment.DEVELOPMENT #ath einhver böggur að nota STAGING, DEVELOPMENT og PRODUCTION virka fínt
    injector = Injector(AppModule(environment))
    phone_book = injector.get(IPhoneBook)
    sales_man_1 = injector.get(SalesMan)
    sales_man_2 = injector.get(SalesMan)
   


    print("\n---------------- failure adding numbers ----------------\n")
    failure_adding_numbers(phone_book)

    print("\n---------------- seeding phone book ----------------\n")
    seed_phone_book(phone_book)

    print("\n---------------- executing operations for sales man 1 ----------------\n")
    sales_man_one(sales_man_1, phone_book)

    print("\n---------------- executing operations for sales man 2 ----------------\n")
    sales_man_two(sales_man_2)


if __name__ == "__main__":
    main()
