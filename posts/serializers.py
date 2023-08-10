from rest_framework import serializers
from .models import Practice, Creation, QnA
from .models.models import TargetPost


class CreationSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        creation = Creation.objects.create(**validated_data)
        return creation

    class Meta:
        model = Creation
        fields = '__all__'


class PracticeSerializer(serializers.ModelSerializer):
    creations = CreationSerializer(many=True)

    def create(self, validated_data):
        creations_data = validated_data.pop('creations')
        practice = Practice.objects.create(**validated_data)
        for creation_data in creations_data:
            Creation.objects.create(practice=practice, **creation_data)
        return practice

    class Meta:
        model = Practice
        fields = '__all__'


class QnASerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        qna = QnA.objects.create(**validated_data)
        return qna

    class Meta:
        model = QnA
        fields = '__all__'


class TargetPostSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        target_post = TargetPost.objects.create(**validated_data)
        return target_post

    class Meta:
        model = TargetPost
        fields = '__all__'
