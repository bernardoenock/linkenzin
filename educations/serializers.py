from rest_framework import serializers

from .models import Education

class EducationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Education
        fields = [
            "institution_name",
            "course",
            "start_date",
            "end_date",
            "certificate",
            "curriculum"
            ]
        

        