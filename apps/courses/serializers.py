from rest_framework import serializers

from .models import Course, Curriculum, Lesson, Subject


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
            "cover_image",
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


class ReadLessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        exclude = ["video"]
        read_only_fields = ["__all__"]


class EnrolledStudentLessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"
        read_only_field = [fields]


class CreateLessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"

    def __init__(self, instance=None, data=..., **kwargs):
        super().__init__(instance, data, **kwargs)
        self.fields["course"].queryset = self.context.get("request").user.courses.all()


class ListCourseSerializer(serializers.ModelSerializer):
    curriculum = CurriculumSerializer()
    subject = SubjectSerializer()
    lessons_number = serializers.SerializerMethodField()
    students = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = "__all__"
        read_only_fields = [fields]

    def get_lessons_number(self, obj) -> int:
        return obj.lessons.count()

    def get_students(self, obj) -> int:
        return obj.students.count()


class DetailCourseSerializer(ListCourseSerializer):
    lessons = EnrolledStudentLessonSerializer(many=True)


class EnrollStudentWithoutInitSerializer(serializers.Serializer):
    course = serializers.PrimaryKeyRelatedField(
        label="Course ID", queryset=Course.objects.all()
    )
    student = serializers.HiddenField(default=serializers.CurrentUserDefault())


class EnrollStudentSerializer(serializers.Serializer):
    course = serializers.PrimaryKeyRelatedField(
        label="Course ID", queryset=Course.objects.all()
    )
    student = serializers.HiddenField(default=serializers.CurrentUserDefault())

    # def __init__(self, instance=None, data=..., **kwargs):
    #     super().__init__(instance, data, **kwargs)
    #     user = self.context.get("request").user
    # self.fields["course"].queryset = Course.objects.exclude(Q(instructor=user) | Q(students=user))

    def validate_course(self, value):
        print(dir(self))
        print(self.context)
        raise serializers.ValidationError("Cannot enroll in course")
        # return False


class PayForCourseSerializer(serializers.Serializer):
    mobile_number = serializers.CharField()

    def validate_mobile_number(self, data):
        if data != "0551234987":
            raise serializers.ValidationError(
                "For testing purpose, Please use the Paystack test number '0551234987' "
            )
        return data
