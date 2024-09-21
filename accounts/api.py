from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import ProfileSerializer
from django.http import JsonResponse
from .models import Profile


# def edit_profile(request, pk):
#     try:
#         profile = Profile.objects.get(pk=pk)
#         serializer = ProfileSerializer(profile)
#         return JsonResponse(serializer.data)
#     except Profile.DoesNotExist:
#         return Response({"error": "Profile does not exist"})   

@api_view(['GET', 'DELETE'])
def user_detail(request, pk):
    try:
        user = Profile.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ProfileSerializer(user)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)  