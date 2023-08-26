from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import UserDetails
from .serializers import UserDetailsSerializer
from .serializers import LoginDetailsSerializer
from rest_framework import generics
# @api_view(['POST'])
# def create_user(request):
#     print("this")
#     serializer = UserDetailsSerializer
#     print("dfg")
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# class dashboardpost(generics.GenericAPIView):
#     serializer_class = UserDetailsSerializer
#     def post(self,request):
#         g = UserDetailsSerializer(data=request.data)
#         g.is_valid(raise_exception=True)
#         h = g.save()
#         return Response(UserDetailsSerializer(h).data)
# @api_view(['GET'])
class LoginApiview(generics.GenericAPIView):
    serializer_class = LoginDetailsSerializer
    def post(self,request):
        userid = request.data.get("userid")
        print(userid,"meghana")
        password=request.data.get("password")
        t = UserDetails.objects.get(userid=userid)
        if t.password==password:
            return Response({"message":"login sucess",
                             "Hasserror":False,
                             "status":200})
        else:
            return Response({"message":"login failed",
                             "Hasserror":False,
                             "status":200})
class dashboardpost(generics.GenericAPIView):
    serializer_class = UserDetailsSerializer
    def post(self,request):
        g = UserDetailsSerializer(data=request.data)
        g.is_valid(raise_exception=True)
        h = g.save()
        return Response(UserDetailsSerializer(h).data)
