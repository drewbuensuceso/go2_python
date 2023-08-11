# products/views.py

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Product
from .serializers import ProductSerializer
from django.core.exceptions import ObjectDoesNotExist
from .tasks import process_order as async_process_order


@api_view(['POST'])
def process_order(request):
    order_data = request.data
    items = order_data['items']
    out_of_stock_items = []

    for item in items:
        # check if oos or there's enough quantity for the SKU
        try:
            product = Product.objects.get(sku=item['sku'])
            if product.quantity <= 0 | product.status == False:
                out_of_stock_items.append(product.name)
            if product.quantity < item['quantity']:
                out_of_stock_items.append(product.name)
        except ObjectDoesNotExist:
            return Response({"error": f"Product with SKU {item['sku']} not found"}, status=400)

    if out_of_stock_items:
        return Response({"error": f"The following items are out of stock: {', '.join(out_of_stock_items)}"}, status=400)

    # All items are in stock, create a Celery task to process the order asynchronously
    async_process_order.delay(order_data)

    return Response({"message": "Order received and will be processed."}, status=200)

@api_view(['GET'])
def available_product_list(request):
    products = Product.objects.filter(status=True).exclude(quantity=0)
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def out_of_stock_product_list(request):
    products = Product.objects.filter(status=False)
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
def update_product_status(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_product(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


