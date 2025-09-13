import grpc
from concurrent import futures
import user_service_pb2
import user_service_pb2_grpc


class UserServiceServicer(user_service_pb2_grpc.UserServiceServicer):
    def GetUserbyId(self, request, context):
        print('Получен запрос на получение пользователя по ID')
        return user_service_pb2.GetUserbyIdResponse(
            user_id = request.user_id,
            name = 'Dima',
            age = 34
        )

    def GetAllUsers(self, request, context):
        print('Получен запрос на получение всех пользователей')
        return user_service_pb2.GetAllUsersResponse(
            users = [
                user_service_pb2.GetUserbyIdResponse(user_id =1, name = 'Dima', age = 34),
                user_service_pb2.GetUserbyIdResponse(user_id=2, name='Sasha', age=30)
            ]
        )

def serve():
    server = grpc.server(thread_pool=futures.ThreadPoolExecutor(max_workers=10))
    user_service_pb2_grpc.add_UserServiceServicer_to_server(UserServiceServicer(),server)
    server.add_insecure_port('127.0.0.1:50051')
    server.start()
    print('gRPC server is running...')
    server.wait_for_termination()

if __name__ == '__main__':
    serve()