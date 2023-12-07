from rest_framework import serializers

from .models import Course, Curriculum, Subject


class CurriculumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curriculum
        fields = (
            "id",
            "short_name",
            "name",
        )


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = (
            "id",
            "name",
        )


class ReadCourseSerializer(serializers.ModelSerializer):
    curriculum = CurriculumSerializer()
    subject = SubjectSerializer()

    class Meta:
        model = Course
        fields = "__all__"


class CreateCourseSerializer(serializers.ModelSerializer):
    curriculum = serializers.SlugRelatedField(
        slug_field="short_name", queryset=Curriculum.objects.all()
    )
    subject = serializers.CharField()

    class Meta:
        model = Course
        fields = (
            "title",
            "description",
            "curriculum",
            "subject",
            "year",
            "price",
            "enrollment_type",
        )

    def create(self, validated_data):
        subject_name = validated_data.pop("subject")
        subject, created = Subject.objects.get_or_create(name=subject_name)
        course = Course.objects.create(subject=subject, **validated_data)
        return course

    def update(self, instance, validated_data):
        if validated_data.get("subject"):
            subject_name = validated_data.pop("subject")
            subject, created = Subject.objects.get_or_create(name=subject_name)
            instance.subject = subject
            instance.save()
        return super().update(instance, validated_data)
