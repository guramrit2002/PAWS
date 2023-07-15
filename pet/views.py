from rest_framework.views import APIView
from .models import Pet
from rest_framework.response import Response
from .serializers import PetSerializer
from rest_framework.decorators import action
from rest_framework import status
# Create your views here.

class PetRetreiveCreate(APIView):

    @action(detail=True, methods=['GET'])
    def get(self, request):
        queryset = Pet.objects.all()
        serializer = PetSerializer(queryset,many=True)
        return Response({"all_pet":serializer.data},status= status.HTTP_200_OK)

    @action(detail=True, methods=['POST'])
    def post(self,request):
        data = request.data
        data['pet_owner'] = request.user.id
        serializer = PetSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            # implement email saying thanks for saving
            return Response({"new_pet":serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"errors":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
class PetUpdateDeleteDetail(APIView):
    @action(detail=True, methods=['GET'])
    def get(self, request, pk):
        try:
            pet = Pet.objects.get(id=pk)
            serializer = PetSerializer(pet, many=False)
            return Response({'pet_detail': serializer.data}, status=status.HTTP_200_OK)
        except pet.DoesNotExist:
            return Response({"errors": 'Pet not found'}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=True, methods=['PUT'])
    def put(self, request, pk):
        try:
            pet = Pet.objects.get(id=pk)
        except pet.DoesNotExist:
            return Response({"errors": 'Pet not found'}, status=status.HTTP_404_NOT_FOUND)
        data = request.data
        try:
            fields_to_update = [
                'pet_category', 'pet_name', 'pet_age', 'pet_breed', 'pet_gender', 'pet_vaccinated',
                'pet_neutered', 'pet_sprayed', 'pet_good_kids', 'pet_address', 'pet_good_pets',
                'pet_desc', 'pet_owner', 'pet_interest', 'pet_not_interest', 'pet_status'
            ]

            for field in fields_to_update:
                if field in data:
                    setattr(pet, field, data[field])

            pet.save()
            # implement email for telling updates
            return Response({"new_pet": pet}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    @action(detail=True,methods=['DELETE'])
    def delete(self,request,pk):
        try:
            pet = Pet.objects.get(id=pk)
            pet.delete()
            return Response({'message': 'pet deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except pet.DoesNotExist:
            return Response({"errors": 'Pet not found'}, status=status.HTTP_404_NOT_FOUND)


