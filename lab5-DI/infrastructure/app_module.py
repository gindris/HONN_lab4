from injector import Module, provider, singleton
from environment import Environment
from phone_book.phone_number_validator import PhoneNumberValidator
import sqlite3
from phone_book.i_phone_book import IPhoneBook
from phone_book.phone_book import PhoneBook
from phone_book.phone_book_fake import PhoneBookFake
from database.phone_book_sqlite_repository import PhoneBookSqliteRepository
from database.phone_book_file_repository import PhoneBookFileRepository

class AppModule(Module):
    def __init__ (self, enviroment: Environment, file_path: str):
        self.environment = enviroment
        self.file_path = file_path

    @provider
    def provide_validation(self) -> PhoneNumberValidator:
        return PhoneNumberValidator()
    
    @singleton
    @provider
    def provide_sqlite_connection(self) -> sqlite3.Connection:
        return sqlite3.connect(self.file_path)
    
    @provider
    def provide_phone_book(self, validator: PhoneNumberValidator, connection: sqlite3.Connection) -> IPhoneBook:
        # Resolve PhoneBook implementation based on environment
        if self.environment == Environment.DEVELOPMENT:
            return PhoneBookFake(validator)
        elif self.environment == Environment.STAGING:
            repository = PhoneBookFileRepository(self.file_path)
            return PhoneBook(repository, validator)
        elif self.environment == Environment.PRODUCTION:
            repository = PhoneBookSqliteRepository(connection)
            return PhoneBook(repository, validator)
        
    