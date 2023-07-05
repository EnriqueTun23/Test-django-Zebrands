from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.authentication import TokenAuthentication

from django.http import Http404
from django.shortcuts import render, get_object_or_404

from .models import Product, ProductView
from .serializers import ProductSerializer, ProductViewSerializer

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

# View that is responsible for displaying the product counter
class DemoView(APIView):
    authentication_classes  = ()
    permission_classes = ()
    
    def get(self, request):
        productViews = ProductView.objects.all()
        serializer = ProductViewSerializer(productViews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# View that is responsible for listing and creating products
class ProductListAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    @swagger_auto_schema(
        operation_description="Retrieve a list of products",
        responses={200: openapi.Response('OK',  schema=ProductSerializer)},
    )
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Create a new product",
        request_body=ProductSerializer,
        responses={
            201: openapi.Response('Created', schema=ProductSerializer),
            400: 'Bad request',
        },
        authentication_classes=[TokenAuthentication],
    )
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# View that is responsible for obtaining a product, updating a product and deleting a product
class ProductDetailAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404("Question does not exist")
    
    def product_detail(self, req, pk):
        product = get_object_or_404(Product, pk=pk)
        # Check if the user is anonymous
        if not req.user.is_authenticated:
            ProductView.objects.create(
                content_object=product,
                user_ip=req.META['REMOTE_ADDR']
            )
    @swagger_auto_schema(
        operation_description="Retrieve a product by ID",
        responses={
            200: openapi.Response('OK', schema=ProductSerializer),
            404: 'Product not found',
        }
    )   
    def get(self, request, pk):
        product = self.get_object(pk)
        self.product_detail(request, pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
    @swagger_auto_schema(
        operation_description="Update a product by ID",
        request_body=ProductSerializer,
        responses={
            200: openapi.Response('OK', schema=ProductSerializer),
            404: 'Product not found',
            400: 'Bad request',
        },
        authentication_classes=[TokenAuthentication],
    )
    def patch(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(
        operation_description="Delete a product by ID",
        responses={204: 'No content', 404: 'Product not found'},
        authentication_classes=[TokenAuthentication],
    )
    def delete(self, request, pk):
        product = self.get_object(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)