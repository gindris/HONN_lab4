from injector import Module, Binder, singleton, provider, noscope
from phone_book.phone_number_validator import PhoneNumberValidator
import sqlite3
from phone_book.i_phone_book import IPhoneBook
from phone_book.phone_book import PhoneBook
from phone_book.phone_book_fake import PhoneBookFake
from database.phone_book_sqlite_repository import PhoneBookSqliteRepository
from database.phone_book_file_repository import PhoneBookFileRepository
from database.i_phone_book_repository import IPhoneBookRepository
from sms.sms_sender import SmsSender
from sales_man import SalesMan
from environment import Environment

class AppModule(Module):
    def __init__(self, environment: Environment):
        self.__environment = environment
        self.__file_path = self._get_file_path()

    @provider 
    def _get_file_path(self) -> str:
        if self.__environment == Environment.STAGING:
            return "phone_book.json"
        elif self.__environment == Environment.PRODUCTION:
            return "phone_book.db"
        return ""
        
    def configure(self, binder: Binder) -> None:
        if self.__environment == Environment.DEVELOPMENT:
            binder.bind(IPhoneBook, to=PhoneBookFake, scope=noscope)
        else:
            binder.bind(IPhoneBook, to=PhoneBook, scope=noscope)
            if self.__environment == Environment.STAGING:
                binder.bind(IPhoneBookRepository, to=PhoneBookFileRepository, scope=noscope)
            elif self.__environment == Environment.PRODUCTION:
                binder.bind(IPhoneBookRepository, to=PhoneBookSqliteRepository, scope=singleton)

    @provider
    def provide_validation(self) -> PhoneNumberValidator:
        return PhoneNumberValidator()

    @singleton
    @provider
    def provide_sqlite_connection(self) -> sqlite3.Connection:
        if self.__environment == Environment.PRODUCTION:
            return sqlite3.connect(self.__file_path)
        return None 

    @provider
    def provide_sms_sender(self) -> SmsSender:
        return SmsSender()

    @provider
    def provide_phone_book(self, validator: PhoneNumberValidator, repository: IPhoneBookRepository) -> IPhoneBook:
        if self.__environment == Environment.DEVELOPMENT:
            return PhoneBookFake(validator)
        else:
            return PhoneBook(repository, validator)

    @provider
    def provide_phone_book_file_repository(self) -> PhoneBookFileRepository:
        if self.__environment == Environment.STAGING:
            return PhoneBookFileRepository(self.__file_path)
        return None

    @provider
    def provide_phone_book_sqlite_repository(self, connection: sqlite3.Connection) -> PhoneBookSqliteRepository:
        if self.__environment == Environment.PRODUCTION:
            return PhoneBookSqliteRepository(connection)
        return None

    @provider
    def sales_man_provider(self, sms_sender: SmsSender, phone_book: IPhoneBook) -> SalesMan:
        return SalesMan(sms_sender, phone_book)
