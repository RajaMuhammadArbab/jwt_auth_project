from rest_framework import generics, permissions,status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.models import User
from .serializers import RegistrationSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.exceptions import TokenError , InvalidToken


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = [permissions.AllowAny]
    
    
    def creat(self , request ,*args, **kwargs ):
        serializer = self.get_serializer(data = request.data)
        try:
            serializer.is_valid(raise_exception = True)
        except serializer.ValidationError as e:
            return Response ({"errors" : serializer.errors} , status= status.HTTP_400_BAD_REQUEST) 
        
        self.perform_create(serializer)
        return Response ({
            
            "message" : "User Registered Successfully",
            "user" : serializer.data
        },status=status.HTTP_201_CREATED)  
    
    


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def dashboard(request):
    try:
        return Response({
            "message": f"Welcome {request.user.username}, this is your dashboard!",
            "email": request.user.email,
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": "Something went wrong."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)