from rest_framework import serializers
from .models import Application
from .models import Client
import clients.views

class ApplicationSerializer(serializers.HyperlinkedModelSerializer):
    clients = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='client-detail'
    )

    class Meta:
        model = Application
        fields = (
                'url',
                'pk',
                'code',
                'clients')


class ClientSerializer(serializers.HyperlinkedModelSerializer):
    code_demande = serializers.SlugRelatedField(queryset=Application.objects.all(), slug_field='code')

    class Meta:
        model = Client
        fields = (
            'url',
            'code_demande',
            'nom',
            'prenom',
            'no_civique',
            'addresse_civique',
            'code_postale',
            'province',
            'nas',
            'date_de_naissance',
            'salaire',)