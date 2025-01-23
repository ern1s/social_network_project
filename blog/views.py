from rest_framework import generics, permissions
 
from .serializers import CategorySerializer, PublicationSelializer
from .models import Category, Publication
 
class CategoryListCreateAPIView(generics.ListCreateAPIView): 
    serializer_class = CategorySerializer 
    queryset = Category.objects.all() 
 
 
class CategoryRetrieveUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView): 
    serializer_class = CategorySerializer 
    queryset = Category.objects.all()

class PublicationListCreateAPIVew(generics.ListCreateAPIView):
    queryset = Publication.objects. filter(is_archivees=False)
    serializer_class = PublicationSelializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
       serializer.save(user=self.request.user)