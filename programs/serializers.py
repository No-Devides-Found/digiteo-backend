from rest_framework import serializers
from .models import Program, Category, Contents, Quiz, Assignment, Tag, Program_Tag_Map

class Program_Tag_MapSerializer(serializers.ModelSerializer):
	program_id = serializers.StringRelatedField()
	tag_id = serializers.StringRelatedField
	
	def create(self, validated_data):
		program_tag_map = Program_Tag_Map.objects.create(**validated_data)
		return program_tag_map
	
	class Meta:
		model = Program_Tag_Map
		fields = '__all__'

class ProgramSerializer(serializers.ModelSerializer):
	category_id = serializers.StringRelatedField()
	Tag = Program_Tag_MapSerializer(many=True, allow_null=True)
	
	def create(self, validated_data):
		program = Program.objects.create(**validated_data)
		return program
	
	class Meta:
		model = Program
		fields = '__all__'



class CategorySerializer(serializers.ModelSerializer):
	programs = ProgramSerializer(many=True, read_only=True)
	
	def create(self, validated_data):
		program = Program.objects.create(**validated_data)
		return program

	class Meta:
		model = Category
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


class TagSerializer(serializers.ModelSerializer):
	
	def create(self, validated_data):
		tag = Tag.objects.create(**validated_data)
		return tag
	
	class Meta:
		model = Tag
		fields = '__all__'