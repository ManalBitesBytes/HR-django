from rest_framework import serializers
from .models import Employee, PerformanceReview

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class PerformanceReviewSerializer(serializers.Serializer):
    employee_id = serializers.IntegerField()
    review_date = serializers.DateField()
    reviewer = serializers.CharField(max_length=100)
    rating = serializers.IntegerField(min_value=1, max_value=5)
    comments = serializers.CharField()
    goals = serializers.DictField()

    def create(self, validated_data):
        return PerformanceReview(**validated_data).save()

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance
