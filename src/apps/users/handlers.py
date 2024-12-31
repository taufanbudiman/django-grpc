from django_socio_grpc.services.app_handler_registry import AppHandlerRegistry

from src.apps.users.services import UserService

# Register user handlers gRPC
def grpc_handlers(server):
    app_registry = AppHandlerRegistry("users", server)
    app_registry.register(UserService)