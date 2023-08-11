from rest_framework import serializers
from .models.practice import Practice, Creation
from .models.models import TargetPost
from .models.baeumteo import QnA, QnA_Image, Agora
from .models.nanumteo import Tip, Tip_Image, Tip_Tag_Map


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
    file = serializers.SerializerMethodField(allow_null=True)

    def get_file(self, obj):
        qna_images = QnA_Image.objects.filter(qna=obj.id)
        image_list = []
        for qna_image in qna_images:
            image_list.append(qna_image.file.url)
        return image_list
    
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


class AgoraSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        agora = Agora.objects.create(**validated_data)
        return agora

    class Meta:
        model = Agora
        fields = '__all__'

class Tip_Tag_MapSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        tip_tag_map = Tip_Tag_Map.objects.create(**validated_data)
        return tip_tag_map
    
    class Meta:
        model = Tip_Tag_Map
        fields = '__all__'

class TipSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField(allow_null=True)
    tag = serializers.SerializerMethodField()

    def get_image(self, obj):
        tip_images = Tip_Image.objects.filter(tip=obj.id)
        image_list = []
        for tip_image in tip_images:
            image_list.append(tip_image.image.url)
        return image_list
    
    def get_tag(self, obj):
        tip_tag_map = Tip_Tag_Map.objects.filter(tip=obj.id)
        tag_list = []
        for tip_tag in tip_tag_map:
            tag_list.append(tip_tag.tag.name)
        return tag_list
    
    def create(self, validated_data):
        tip = Tip.objects.create(**validated_data)
        return tip
    
    class Meta:
        model = Tip
        fields = '__all__'