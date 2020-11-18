from rest_framework import serializers
from django.contrib.auth.models import  User

from .models import Article, Reporter, Publication


class ReporterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reporter
        fields = '__all__'
       
class ArticleSerializer(serializers.ModelSerializer):
    # Reporter= ReporterSerializer()
    class Meta:
        model = Article
        fields = [
            'id',
            'headline',
            'Reporter',
            'picture'
        ]
class PublicationSerialzation(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = '__all__'

class ReporterAndArticleSerializer(serializers.ModelSerializer):
    Reporter= ReporterSerializer()
    class Meta:
        model = Article
        fields = [
            'headline',
            'Reporter',
            'picture'
        ] 
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email'
        ]