from injector import Binder, Module, provider, singleton
from environment import Environment
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

class AppModule(Module):
    def __init__ (self, enviroment: Environment):
        self.__environment = enviroment
        self.__file_path = self._get_file_path()
    
    def _get_file_path(self) -> str:
        if self.__environment == Environment.STAGING:
            return "phone_book.json"
        elif self.__environment == Environment.PRODUCTION:
            return "phone_book.db"
        else:
            return ""

    def configure(self, binder: Binder) -> None:
        if self.__environment == Environment.DEVELOPMENT:
            binder.bind(IPhoneBook, to=PhoneBookFake, scope=singleton)
        else:
            binder.bind(IPhoneBook, to=PhoneBook)
            if self.__environment == Environment.STAGING:
                binder.bind(IPhoneBookRepository, to=PhoneBookFileRepository, scope=singleton)
            elif self.__environment == Environment.PRODUCTION:
                binder.bind(IPhoneBookRepository, to=PhoneBookSqliteRepository, scope=singleton)
                
    
    @provider
    def provide_validation(self) -> PhoneNumberValidator:
        return PhoneNumberValidator()

    @singleton
    @provider
    def provide_sqlite_connection(self) -> sqlite3.Connection:
        return sqlite3.connect(self.__file_path)

    @provider
    def provide_sms_sender(self) -> SmsSender:
        return SmsSender()

    @provider
    def provide_phone_book(self) -> PhoneBook:
        return PhoneBook()

    @singleton
    @provider
    def provide_phone_book_fake(self, validator: PhoneNumberValidator) -> PhoneBookFake:
        return PhoneBookFake(validator)

    @provider
    def provide_phone_book_file_repository(self) -> PhoneBookFileRepository:
        return PhoneBookFileRepository(self.file_path)
    @provider
    def provide_phone_book_sqlite_repository(self, connection: sqlite3.Connection) -> PhoneBookSqliteRepository:
        return PhoneBookSqliteRepository(connection)
    
    @provider
    def sales_man_provider(self, sms_sender: SmsSender, phone_book: IPhoneBook) -> SalesMan:
        return SalesMan(sms_sender, phone_book)
    
    