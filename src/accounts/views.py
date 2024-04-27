from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from .serializers import UserRegistrationSerializer


class UserRegisterView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            serializer.save(request)
            return Response({"message": "User Created Successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
