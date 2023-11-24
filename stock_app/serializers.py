from rest_framework import serializers, validators

from stock_app.models import Store, Product, \
    ProductInStore, ApiUser, UserGroup


class UserSerializer(serializers.Serializer):
    email = serializers.EmailField(
        max_length=20,
        validators=[validators.UniqueValidator(ApiUser.objects.all())]
    )
    password = serializers.CharField(min_length=8, write_only=True)
    user_group = serializers.CharField()

    def update(self, instance, validated_data):
        if email := validated_data.get("email"):
            instance.email = email
        if user_group_id := validated_data.get("user_group"):
            user_group = UserGroup.objects.get(pk=user_group_id)
            instance.user_group = user_group
        if password := validated_data.get("password"):
            instance.set_password(password)
            instance.save(updated_fields=["password"])
        return instance

    def create(self, validated_data):
        print(validated_data)
        user_group_id = validated_data["user_group"]
        user_group = UserGroup.objects.get(pk=user_group_id)
        user = ApiUser.objects.create(
            email=validated_data["email"],
            user_group=user_group
        )
        user.set_password(validated_data["password"])
        user.save()
        return user


class UserGroupSerializer(serializers.ModelSerializer):
    apiusers = UserSerializer(many=True)

    class Meta:
        model = UserGroup
        fields = ['name', 'apiusers']
        read_only_fields = ['id']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name']


class ProductInStoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductInStore
        fields = ['product', 'quantity']


class ProductInStoreDetailedSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    quantity = serializers.IntegerField()

    class Meta:
        model = ProductInStore
        fields = ['product', 'quantity']


class StoreSerializer(serializers.ModelSerializer):
    products = ProductInStoreDetailedSerializer(many=True)

    class Meta:
        model = Store
        fields = ['id', 'name', 'address', 'products']
        read_only_fields = ['id']


class SimpleProductInStoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductInStore
        fields = ['product', 'quantity']
