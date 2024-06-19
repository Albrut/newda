from rest_framework import serializers
from .models import Sweet, Order
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator

class SweetNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sweet
        fields = ['name']

class SweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sweet
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    sweet = SweetNameSerializer(read_only=True)  # Use the custom SweetNameSerializer

    class Meta:
        model = Order
        fields = ['id', 'sweet', 'quantity', 'address', 'ordered_at', 'status', 'user']

class OrderStatusUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'status']

class UserRegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
    
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()

        # Add user to 'customer' group
        customer_group, created = Group.objects.get_or_create(name='customer')
        user.groups.add(customer_group)

        return user
