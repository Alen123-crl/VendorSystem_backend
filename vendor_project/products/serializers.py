from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):

    name = serializers.CharField(
        min_length=2,
        max_length=255,
        error_messages={
            "required": "Product name is required",
            "blank": "Product name cannot be empty"
        }
    )

    description = serializers.CharField(
        error_messages={
            "required": "Description is required"
        }
    )

    price = serializers.DecimalField(
        max_digits=10,
        decimal_places=2,
        min_value=0.01,
        error_messages={
            "required": "Price is required",
            "min_value": "Price must be greater than 0"
        }
    )

    quantity = serializers.IntegerField(
        min_value=0,
        error_messages={
            "required": "Quantity is required",
            "min_value": "Quantity cannot be negative"
        }
    )

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "description",
            "price",
            "quantity",
            "created_at"
        ]
        read_only_fields = ["id", "created_at"]