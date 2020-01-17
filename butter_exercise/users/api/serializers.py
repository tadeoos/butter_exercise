from django.contrib.auth import get_user_model
from rest_framework import serializers

from butter_exercise.users.models import Agreement


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = (
            'pk',
            'username',
            'first_name',
            'last_name',
            'email',
            'is_active',
            'date_joined',
        )


class AgreementSerializer(serializers.ModelSerializer):
    html = serializers.CharField(read_only=True, source='get_html')

    class Meta:
        model = Agreement
        fields = (
            'pk',
            'category',
            'date',
            'data',
            'html',
        )

    def validate_data(self, value):
        required = Agreement.get_required_data_keys()
        if required <= set(value.keys()):
            return value
        raise serializers.ValidationError(f'Data must contain all of the below keys: {required}')

    def create(self, validated_data):
        user_id = self.context['view'].get_parents_query_dict()['user']
        validated_data.update({'user_id': user_id})
        return super(AgreementSerializer, self).create(validated_data)
