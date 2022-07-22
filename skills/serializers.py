from rest_framework.serializers import ModelSerializer

from .models import Skill

from accounts.models import Account


class UsersSkillsSerializer(ModelSerializer):
    class Meta:
        model = Account
        fields = "email"

class SkillSerializer(ModelSerializer):
    skills_users = UsersSkillsSerializer(many=True, read_only=True)

    class Meta:
        model = Skill
        fields = "__all__"

        

class SkillsUsersSerializer(ModelSerializer):
    class Meta:
        model = Skill
        fields = "__all__"