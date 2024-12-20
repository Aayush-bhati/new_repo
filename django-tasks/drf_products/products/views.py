from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer

# Create your views here.
@api_view(['GET','POST'])
def product_list(request):
    if request.method =='GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    elif request.method =='POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def product_detail(request,id):
    try:
        product = Product.objects.get(pk=id)
    except Product.DoesNotExist:
        return Response({'error':'Product not Found'},status =status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ProductSerializer(product,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status =status.HTTP_400_BAD_REQUEST)
    
    elif request.method =='DELETE':
        product.delete()
        return Response({'message':'Product deleted succesfully'},status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def product_total(request,id):
    try:
        product = Product.objects.get(pk=id)
    except Product.DoesNotExist:
        return Response({'error':'Product not found'},status = status.HTTP_404_NOT_FOUND)
    
    total_price = product.calculate_total_price()
    return Response({'total_price':total_price})
    


        



