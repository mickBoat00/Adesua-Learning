from rest_framework.serializers import ModelSerializer

from .models import Curriculum


class CurriculumSerializer(ModelSerializer):
    class Meta:
        model = Curriculum
        fields = ("short_name", "name")
