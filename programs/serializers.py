from rest_framework import serializers
from .models import Program, Category
# ,Assignment

class ProgramSerializer(serializers.ModelSerializer):
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


# class AssignmentSerializer(serializers.ModelSerializer):
# 	programs = ProgramSerializer(many=True, read_only=True)
	
# 	class Meta: 
# 		model = Assignment
# 		fields = '__all__'