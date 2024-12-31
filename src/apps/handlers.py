from src.apps.users.handlers import grpc_handlers as user_grpc_handlers

# register all apps handlers
def grpc_handlers(server):
    user_grpc_handlers(server)
