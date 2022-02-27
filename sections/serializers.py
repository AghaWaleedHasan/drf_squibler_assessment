from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField
from .models import Section

class SectionSerializer(serializers.ModelSerializer):
    children = RecursiveField(many=True,default='')
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    lookup_field='slug'
    # url = serializers.HyperlinkedIdentityField(view_name='sections-detail')
    # extra_kwargs = {'url': {'lookup_field':'slug'}}

    class Meta:
        model = Section
        fields = ('id','title','content','parent','children','user','slug')
        read_only_fields = ('children',)
        write_only_fields = ('parent',)

class SectionCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Section
        fields = ('title','content','parent','user')