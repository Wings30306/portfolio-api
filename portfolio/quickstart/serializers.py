from django.contrib.auth.models import User, Group
from rest_framework import serializers

# From own apps
from codeprojects.models import Language, Project, ProjectLanguage


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ["url", "title", "live_link", "code_link", "preview_img", "languages"]

        
class LanguageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Language
        fields = ["url", "name", "link", "logo", "projects"]
        

class ProjectLanguageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProjectLanguage
        fields = ["url", "project", "language"]
        
