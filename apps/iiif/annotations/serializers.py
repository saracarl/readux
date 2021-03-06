from .models import Annotation
from rest_framework import serializers
import json


class AnnotationSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Annotation
        fields = ('oa_annotation',)
