from rest_framework import serializers
from .models.practice import Practice, Creation, Practice_Tag_Map
from .models.models import TargetPost, Comment, PostLiked
from .models.baeumteo import QnA, QnA_Image, Agora, AgoraCommentLiked, QnA_Tag_Map
from .models.nanumteo import Tip, Tip_Image, Tip_Tag_Map, TipCommentLiked
from .models.evaluation import Evaluation
from accounts.models import Profile
from accounts.serializers import ProfileSerializer


class CommentSerializer(serializers.ModelSerializer):
    user_profile = serializers.SerializerMethodField()

    def get_user_profile(self, obj):
        user_profile = Profile.objects.filter(user=obj.user)[0]
        serializer = ProfileSerializer(user_profile, many=False)
        return serializer.data

    def create(self, validated_data):
        comment = Comment.objects.create(**validated_data)
        return comment

    class Meta:
        model = Comment
        fields = '__all__'


class CreationSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        creation = Creation.objects.create(**validated_data)
        return creation

    class Meta:
        model = Creation
        fields = ['order', 'filename', 'file', 'file_type']


class PracticeSerializer(serializers.ModelSerializer):
    creations = CreationSerializer(many=True)
    tag = serializers.SerializerMethodField()
    comment = serializers.SerializerMethodField(allow_null=True)
    liked_cnt = serializers.SerializerMethodField(allow_null=True)
    user_profile = serializers.SerializerMethodField()

    def get_user_profile(self, obj):
        user_profile = Profile.objects.filter(user=obj.user)[0]
        serializer = ProfileSerializer(user_profile, many=False)
        return serializer.data

    def get_tag(self, obj):
        practice_tag_map = Practice_Tag_Map.objects.filter(practice=obj.id)
        tag_list = []
        for practice_tag in practice_tag_map:
            tag_list.append(practice_tag.tag.name)
        return tag_list

    def get_comment(self, obj):
        target_posts = TargetPost.objects.filter(comment=obj.id)
        comment_list = []

        for target_post in target_posts:
            comment = Comment.objects.filter(target_post=target_post.id)
            serializer = CommentSerializer(comment, many=True)
            comment_list.extend(serializer.data)
        return comment_list

    def get_liked_cnt(self, obj):
        target_posts = TargetPost.objects.filter(practice=obj.id)
        cnt = 0

        for target_post in target_posts:
            cnt += PostLiked.objects.filter(target_post=target_post.id).count()

        if cnt is None:
            return 0

        return cnt

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
    tag = serializers.SerializerMethodField(read_only=True)
    file = serializers.SerializerMethodField(allow_null=True)
    comment = serializers.SerializerMethodField(allow_null=True)
    liked_cnt = serializers.SerializerMethodField(allow_null=True)
    user_profile = serializers.SerializerMethodField()

    def get_user_profile(self, obj):
        user_profile = Profile.objects.filter(user=obj.user)[0]
        serializer = ProfileSerializer(user_profile, many=False)
        return serializer.data

    def get_tag(self, obj):
        qna_tag_map = QnA_Tag_Map.objects.filter(qna=obj.id)
        tag_list = []
        for qna_tag in qna_tag_map:
            tag_list.append(qna_tag.tag.name)
        return tag_list

    def get_file(self, obj):
        qna_images = QnA_Image.objects.filter(qna=obj.id)
        image_list = []
        for qna_image in qna_images:
            image_list.append(qna_image.file.url)
        return image_list

    def get_comment(self, obj):
        target_posts = TargetPost.objects.filter(qna=obj.id)
        comment_list = []
        for target_post in target_posts:
            comment_list.append(Comment.objects.filter(
                target_post=target_post.id).values())
        return comment_list

    def get_liked_cnt(self, obj):
        target_posts = TargetPost.objects.filter(qna=obj.id)
        cnt = 0

        for target_post in target_posts:
            cnt += PostLiked.objects.filter(target_post=target_post.id).count()

        if cnt is None:
            return 0

        return cnt

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
    pros_and_cons = serializers.SerializerMethodField(allow_null=True)
    comment = serializers.SerializerMethodField(allow_null=True)
    liked_cnt = serializers.SerializerMethodField(allow_null=True)
    user_profile = serializers.SerializerMethodField()

    def get_user_profile(self, obj):
        user_profile = Profile.objects.filter(user=obj.user)[0]
        serializer = ProfileSerializer(user_profile, many=False)
        return serializer.data

    def get_pros_and_cons(self, obj):
        target_posts = TargetPost.objects.filter(agora=obj.id)
        total = target_posts.count()
        pros_cnt = 0

        if total == 0:
            return {"pros": 50, "cons": 50}

        for target_post in target_posts:
            pros_cnt += Comment.objects.filter(pros_and_cons=1,
                                               target_post=target_post.id).count()

        pros_percentage = round(pros_cnt / total * 100, 1)
        pros_and_cons = {"pros": pros_percentage,
                         "cons": 100 - pros_percentage}
        return pros_and_cons

    def get_comment(self, obj):
        target_posts = TargetPost.objects.filter(agora=obj.id)
        comment_list = []

        for target_post in target_posts:
            comments = Comment.objects.filter(target_post=target_post.id)
            comment_data = []

            for comment in comments:
                comment_likes = AgoraCommentLiked.objects.filter(
                    agora_comment=comment.id).count()
                comment_data.append({
                    "comment": CommentSerializer(comment).data,
                    "likes": comment_likes
                })

            comment_list.append(comment_data)
        return comment_list

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
    comment = serializers.SerializerMethodField(allow_null=True)
    liked_cnt = serializers.SerializerMethodField(allow_null=True)
    user_profile = serializers.SerializerMethodField()

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

    def get_comment(self, obj):
        target_posts = TargetPost.objects.filter(tip=obj.id)
        comment_list = []

        for target_post in target_posts:
            comments = Comment.objects.filter(target_post=target_post.id)
            comment_data = []

            for comment in comments:
                comment_likes = TipCommentLiked.objects.filter(
                    tip_comment=comment.id).count()
                comment_data.append({
                    "comment": CommentSerializer(comment).data,
                    "likes": comment_likes
                })
        return comment_list

    def get_user_profile(self, obj):
        user_profile = Profile.objects.filter(user=obj.user)[0]
        serializer = ProfileSerializer(user_profile, many=False)
        return serializer.data

    def create(self, validated_data):
        tip = Tip.objects.create(**validated_data)
        return tip

    class Meta:
        model = Tip
        fields = '__all__'


class EvaluationSerializer(serializers.ModelSerializer):
    user_profile = serializers.SerializerMethodField()

    def create(self, validated_data):
        evaluation = Evaluation.objects.create(**validated_data)
        return evaluation

    def get_user_profile(self, obj):
        user_profile = Profile.objects.filter(user=obj.user)[0]
        serializer = ProfileSerializer(user_profile, many=False)
        return serializer.data

    class Meta:
        model = Evaluation
        fields = '__all__'


class LikedSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostLiked
        fields = '__all__'

    def destroy(self, validated_data):
        instance = self.instance
        user = self.context['request'].user

        # Check if the user owns this like
        if instance.user == user:
            instance.delete()
        else:
            pass


class AgoraCommentLikedSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgoraCommentLiked
        fields = '__all__'

    def destroy(self, validated_data):
        instance = self.instance
        user = self.context['request'].user

        # Check if the user owns this like
        if instance.user == user:
            instance.delete()
        else:
            pass


class TipCommentLikedSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipCommentLiked
        fields = '__all__'

    def destroy(self, validated_data):
        instance = self.instance
        user = self.context['request'].user

        # Check if the user owns this like
        if instance.user == user:
            instance.delete()
        else:
            pass
