


import shutil
from rest_framework import serializers
from .models import *

class FileSerializer(serializers.ModelSerializer):
    model= File
    field = '__all__'


class FolderSerializer(serializers.ModelSerializer):
    model= Folder
    field = '__all__'

class FileListSerializer(serializers.Serializer):
    files= serializers.ListField(
        child= serializers.FileField( max_length=100000, allow_empty_file=False, use_url=False)
    )
    folder= serializers.CharField(required= False)



    def zips(self, folder):
        shutil.make_archive(f'static/media/zip/{folder}','zip',f'static/{folder}')


    def create(self, validated_data):
        folder= Folder.objects.create()
        files= validated_data.pop('files')
        file_objs=[]
        for file in files:
            file_obj= File.objects.create(file=file , folder=folder) 
            file_objs.append(file_obj)
        return {'files':{}, 'folder': str(folder.uid)} 

        self.zips(folder.uid)




    