import grpc
import user_service_pb2_grpc
import user_service_pb2
from google.protobuf import empty_pb2

channel = grpc.insecure_channel('127.0.0.1:50051')
stub = user_service_pb2_grpc.UserServiceStub(channel)
user_by_id_request = user_service_pb2.GetUserbyIdRequest(user_id=1)

user_by_id_response = stub.GetUserbyId(user_by_id_request)
print(f'Полуен пользователь по ID:\n{user_by_id_response}')

all_users_response = stub.GetAllUsers(empty_pb2.Empty())
print(f'Полуены все пользователи:\n{all_users_response}')

