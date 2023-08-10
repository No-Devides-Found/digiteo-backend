from rest_framework import serializers
from .models import Report
from posts.models.models import TargetPost
from posts.models import QnA, Practice
from posts.serializers import TargetPostSerializer


class ReportSerializer(serializers.ModelSerializer):
    target_post = TargetPostSerializer()

    def create(self, validated_data):
        target_post_data = validated_data.pop('target_post')
        target_post_type = target_post_data['target_post_type']
        qna = target_post_data['qna']
        practice = target_post_data['practice']

        if target_post_type == "qna":
            target_post = TargetPost.objects.create(
                qna=qna, target_post_type=target_post_type)
        elif target_post_type == "practice":
            target_post = TargetPost.objects.create(
                practice=practice, target_post_type=target_post_type)
        # elif ...
        else:
            raise (AssertionError(
                f"target_post_type '{target_post_type}' is invalid"))

        report = Report.objects.create(
            target_post=target_post, **validated_data)
        return report

    class Meta:
        model = Report
        fields = '__all__'
