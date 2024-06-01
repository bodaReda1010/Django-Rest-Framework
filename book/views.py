from django.shortcuts import render
from django.http import JsonResponse
from . models import Book , Author , Review
from rest_framework import status 
from rest_framework.response import Response
from rest_framework.decorators import api_view 
from . serializers import BookSerializer , AuthorSerializer
from rest_framework.views import APIView
from rest_framework import mixins , generics , viewsets
from rest_framework.authentication import BasicAuthentication , TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

# Static (No Models)
def no_models(request):
    data = {
        'Book Name':'Python',
    }
    return JsonResponse(data)


# 2 Model API With Django (With Models)
def model_api_no_rest(request):
    books = Book.objects.all()
    data = {
        'books':list(books.values()),
    }
    return JsonResponse(data)



# 3.1 [FBV] GET POST
@api_view(['GET' , 'POST'])
def fbv(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books , many = True)
        return Response(serializer.data , status = status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = BookSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status = status.HTTP_201_CREATED)
        return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)



# 3.2 [FBV] GET PUT DELETE
@api_view(['GET' , 'PUT' , 'DELETE'])
def fbv_pk(request , pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data , status = status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = BookSerializer(book , data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status = status.HTTP_202_ACCEPTED)
        return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        book.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    


# 4.1 [CBV] GET POST
class CBV(APIView):
    def get(self , request):
        books = Book.objects.all()
        serializer = BookSerializer(books , many = True)
        return Response(serializer.data , status = status.HTTP_200_OK)
    def post(self, request):
        serializer = BookSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status = status.HTTP_201_CREATED)
        return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)



# 4.2 [CBV] GET PUT DELETE
class Cbv_Pk(APIView):
    def get_object(self , pk):
        return Book.objects.get(pk=pk)
    def get(self , request , pk):
        serializer = BookSerializer(self.get_object(pk))
        return Response(serializer.data , status = status.HTTP_200_OK)
    def put(self , request , pk):
        serializer = BookSerializer(self.get_object(pk) , data = request.data)
        if serializer.is_valid():
            return Response(serializer.data , status = status.HTTP_202_ACCEPTED)
        return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)
    def delete(self , request , pk):
        self.get_object(pk).delete()
        return Response(status = status.HTTP_204_NO_CONTENT)



# 5.1 [mixins] GET POST
class Mixins(mixins.ListModelMixin , mixins.CreateModelMixin , generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    def get(self , request):
        return self.list(request)
    def post(self , request):
        return self.create(request)


# 5.2 [mixins] GET PUT DELETE
class Mixins_Pk(mixins.RetrieveModelMixin , mixins.UpdateModelMixin , mixins.DestroyModelMixin , generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    def get(self , request , pk):
        return self.retrieve(request)
    def put(self , request , pk):
        return self.update(request)
    def delete(self , request , pk):
        return self.destroy(request)



# 6.1 [generic] GET POST
class Generic(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]



# 6.2 [generic] GET PUT DELETE
class Generic_Pk(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


# 7.1 [viewset]
class Viewset(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer