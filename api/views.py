from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response 
from .models import StudentModel
from rest_framework import status
from .serializers import StudentSerializers, LoginStudentSerializers

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_student_list(request):
    list = StudentModel.objects.all()
    serializer= StudentSerializers(list, many=True)
    return Response({"Message":"Student list", 'data':serializer.data})

@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_student(request):
    user_id = request.query_params.get('user_id')
    try:
        user_info = StudentModel.objects.get(pk=user_id)
    except StudentModel.DoesNotExist:
        return Response({'message': "User does not exist!"}, status=status.HTTP_404_NOT_FOUND)

    serializer = StudentSerializers(user_info, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Student Updated", 'data': serializer.data})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_student(request):
    user_id= request.query_params.get('user_id')
    try:
        user = StudentModel.objects.get(pk=user_id)
    except StudentModel.DoesNotExist:
        return Response({"message":"User doest not exist"})

    user.delete()
    return Response({"Message":"Delete student successfully"})

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_student(request):
    serializer = StudentSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message':"user created"})
    return Response({"Message":"Something went wrong while created student"})

# @api_view(["POST"])
# @permission_classes([AllowAny])
# def register(request):
#     obj_user = request.data
#     try:
#         serializer = StudentSerializers(data=obj_user)      
#         if serializer.is_valid():
#             serializer.save()
#             return Response({
#                 'message':'Registration has been done!',
#                 'error':serializer.errors,
#                 'isError':False
#             })
#     except StudentModel.DoesNotExist:
#         return Response({
#             'message':'User does not exist!',
#             'error':serializer.errors,
#             'isError':True
#         })

#     return Response({"Message":"Something went wrong in Registration!", 'isError':True})

@api_view(["POST"])
@permission_classes([AllowAny])
def register(request):
    obj_user = request.data
    try:
        serializer = StudentSerializers(data=obj_user)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'Registration has been done!',
                'error': serializer.errors,
                'isError': False
            })
        return Response({
            'message': 'Invalid data!',
            'error': serializer.errors,
            'isError': True
        })
    except Exception as e:
        return Response({
            'message': 'Something went wrong in Registration!',
            'error': str(e),
            'isError': True
        })

@api_view(["POST"])
@permission_classes([AllowAny])
def login(request):
    serializer = LoginStudentSerializers(data=request.data)
    if serializer.is_valid():
        return Response(serializer.validated_data)
    else:
        return Response({
            'message': 'Something went wrong while login!',
            'error': serializer.errors,
            'isError': True
        })

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def get_refresh_token(request):
    return Response({"Message":"Get refresh token"})