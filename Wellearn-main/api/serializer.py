from rest_framework import routers, serializers
from core.models import Blog, Category, Subscriber, Basket


class CategoryGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title']

class BlogGetSerializer(serializers.ModelSerializer):
    category = CategoryGetSerializer()
    class Meta:
        model = Blog
        fields = ['title', 'description', 'category', 'image', 'created_at']



class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['title', 'description', 'category', 'image']


class SubscriberSerializer(serializers.ModelSerializer):
    
    class Meta():
        model = Subscriber
        fields = ['email',]





class BasketSerializer(serializers.ModelSerializer):
    # authentication_classes = (TokenAuthentication,)
    price = serializers.SerializerMethodField()
    class Meta:
        model = Basket
        fields = (
            'id',
            'product',
            'quantity',
            'total_price',
            'price',
        )
        
            
    def get_price(self, obj):
        return obj.product.price
    
    def create(self, validated_data):
        product = validated_data['product']
        total_price = product.price * validated_data['quantity'] if validated_data.get('quantity') else product.price

        validated_data['total_price'] = total_price
        
        user = self.context['user']
        basket = Basket.objects.create(user=user, **validated_data)
        return basket