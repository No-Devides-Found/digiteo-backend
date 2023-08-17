from rest_framework import serializers
from .models import Program, Category, Contents, Quiz, Assignment, Tag, Program_Tag_Map, Program_User_Map
from posts.models.evaluation import Evaluation


class ProgramSerializer(serializers.ModelSerializer):
    tag = serializers.SerializerMethodField(read_only=True)
    participants_cnt = serializers.SerializerMethodField(read_only=True)
    score = serializers.SerializerMethodField(read_only=True)

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
