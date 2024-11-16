# serializers.py
from rest_framework import serializers
from .models import NaukriJobs

class NaukriJobsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NaukriJobs
        fields = '__all__'
