from rest_framework import serializers
from .models import Program, Contents, Quiz, Assignment, Tag, Program_Tag_Map, Program_User_Map
from posts.models.evaluation import Evaluation
from posts.serializers import EvaluationSerializer


class ProgramSerializer(serializers.ModelSerializer):
    tag = serializers.SerializerMethodField(read_only=True)
    participants_cnt = serializers.SerializerMethodField(read_only=True)
    score = serializers.SerializerMethodField(read_only=True)
    reviews = serializers.SerializerMethodField(read_only=True)
    progress = serializers.SerializerMethodField(read_only=True)

    def get_participants_cnt(self, obj):
        program_user_maps = Program_User_Map.objects.filter(
            program=obj.id).filter(participate=True)
        return len(program_user_maps)

    def get_tag(self, obj):
        program_tag_map = Program_Tag_Map.objects.filter(program=obj.id)
        tag_list = []
        for program_tag in program_tag_map:
            tag_list.append(program_tag.tag.name)
        return tag_list

    def get_score(self, obj):
        program_user_maps = Program_User_Map.objects.filter(program=obj.id)
        total_score = 0
        total_evaluations = 0  # eval 갯수

        for program_user_map in program_user_maps:
            evaluation = program_user_map.evaluation
            if evaluation:
                total_score += evaluation.score
                total_evaluations += 1

        if total_evaluations == 0:
            return None

        average_score = total_score / total_evaluations
        return round(average_score, 1)
    
    def get_progress(self, obj):
        user = self.context['request'].user
        total_progress = Contents.objects.filter(program=obj.id).count()
        if total_progress == 0:
            return None

        if user.is_authenticated:
            program_user_map = Program_User_Map.objects.filter(program=obj.id, user=user).first()

            if program_user_map:
                last_content = program_user_map.last_content

            else:
                last_content = 0
        else:
            last_content = 0
    
        return last_content / total_progress

    def get_reviews(self, obj):
        program_user_maps = list(
            Program_User_Map.objects.filter(program=obj).values())
        evaluations = []
        for item in program_user_maps:
            # print(item)
            evaluation = Evaluation.objects.filter(
                id=item['evaluation_id']).first()
            if evaluation is None:
                continue
            eval_serializer = EvaluationSerializer(evaluation, many=False)
            evaluations.append(eval_serializer.data)

        return evaluations

    def create(self, validated_data):
        program = Program.objects.create(**validated_data)
        return program

    class Meta:
        model = Program
        fields = '__all__'


class ContentsSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        contents = Contents.objects.create(**validated_data)
        return contents

    class Meta:
        model = Contents
        fields = '__all__'


class QuizSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        quiz = Quiz.objects.create(**validated_data)
        return quiz

    class Meta:
        model = Quiz
        fields = '__all__'


class AssignmentSerializer(serializers.ModelSerializer):
    programs = ProgramSerializer(many=True, read_only=True)

    def create(self, validated_data):
        assignment = Assignment.objects.create(**validated_data)
        return assignment

    class Meta:
        model = Assignment
        fields = '__all__'



class ProgramUserMapSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        program_user_map = Program_User_Map.objects.create(**validated_data)
        return program_user_map

    class Meta:
        model = Program_User_Map
        fields = '__all__'