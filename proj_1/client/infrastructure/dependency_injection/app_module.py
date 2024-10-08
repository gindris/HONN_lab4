
from injector import Module
from client.infrastructure.settings.settings import Settings

#ATH þessi additional import, gætu verið off
# from structured_logging.logger import Logger
# from structured_logging.configuration.logger_config import LoggerConfig
# from structured_logging.command_queue.queue import Queue
# from structured_logging.i_logger import ILogger
# from client.repositories.order_repository import OrderRepository
# from client.services.payment_service_stub import PaymentServiceStub
# from client.services.order_service import OrderService

class AppModule(Module):
    def __init__(self, settings: Settings) -> None:
        self.__settings = settings

    #TODO: dependency injection, eitthvað svona?
    # @transient
    # @provider
    # def provide_payment_service(self) -> PaymentServiceStub:
    #     return PaymentServiceStub()
    
    # @transient
    # @provider
    # def provide_order_repository(self) -> OrderRepository:
    #     return OrderRepository()
    
    # @transient
    # @provider
    # def provide_logger(self) -> ILogger:
    #     return Logger(LoggerConfig(self.__settings), Queue())
    
    # @transient
    # @provider
    # def provide_order_service(self, payment_service: PaymentServiceStub, order_repository: OrderRepository, logger: ILogger) -> OrderService:
    #     return OrderService(payment_service, order_repository, logger)

