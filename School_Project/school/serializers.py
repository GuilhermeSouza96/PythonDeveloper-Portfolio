from rest_framework import serializers
from school.models import Student, Course, Enrollment
from school.validators import invalid_cpf, invalid_phone, invalid_name

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

    def validate(self, data):
        if invalid_cpf(data['cpf']):
            raise serializers.ValidationError({'cpf': 'CPF must be valid!'})
        if invalid_name(data['name']):
             raise serializers.ValidationError({'name': 'Name must have only letters!'})
        if invalid_phone(data['phone']):
            raise serializers.ValidationError({'phone': 'Phone must be like: 55 99999-9999 (including spaces and dashes)'})
        
        return data

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = '__all__'

class ListEnrollmentsStudentSerializer(serializers.ModelSerializer):
    course = serializers.ReadOnlyField(source='course.description')
    period = serializers.SerializerMethodField()
    class Meta:
        model = Enrollment
        fields = ['course', 'period']

    def get_period(self, obj):
        return obj.get_period_display()
    
class ListEnrollmentsCourseSerializer(serializers.ModelSerializer):
    student_name = serializers.ReadOnlyField(source='student.name')
    class Meta:
        model = Enrollment
        fields = ['student_name']

class StudentSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = Student
        exclude = ['birth_date', 'cpf']