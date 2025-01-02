

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Order
from .serializers import OrderSerializer


class OrderAPIList(APIView):
    permission_classes = [IsAuthenticated] 

    def get(self, request):
        query = Order.objects.all()
        serializer = OrderSerializer(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Order added"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderAPIDetail(APIView):
    permission_classes = [IsAuthenticated] 
    def get(self, request, id):
        try:
            query = Order.objects.get(id=id)
            serializer = OrderSerializer(query)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Order.DoesNotExist:
            return Response({"message": "Order not found"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id):
        try:
            query = Order.objects.get(id=id)
        except Order.DoesNotExist:
            return Response({"message": "Order not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = OrderSerializer(query, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Order updated successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            query = Order.objects.get(id=id)
        except Order.DoesNotExist:
            return Response({"message": "Order not found"}, status=status.HTTP_404_NOT_FOUND)
        query.delete()
        return Response({"message": "Order deleted"}, status=status.HTTP_204_NO_CONTENT)

