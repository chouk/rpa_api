from django.db import models

# Create your models here.
class Application(models.Model):
    code = models.CharField(max_length=10)
    date_soumise = models.DateField(auto_now=True)

    class Meta:
        ordering = ('-date_soumise',)

    def __str__(self):
        return self.code


class Client(models.Model):
    provinces = (
       ('NB', 'New Brunswick'),
       ('NL', 'Newfoundland and Labrador'),
       ('NS', 'Nova Scotia'),
       ('ON', 'Ontario'),
       ('PE', 'Prince Edward Island'),
       ('QC', 'Québec'),
    )
    types_client = (
    ('MAPL','Apllicant principale'),
    ('JAPL','Apllicant conjoint'),
    ('COAP1','Co-Apllicant1'),
    ('COAP2','Co-Applicant2'),)


    code_demande = models.ForeignKey(Application, related_name='clients', on_delete=models.CASCADE)
    type_client = models.CharField( "Type: ", max_length=5, choices=types_client, default='MAPL')
    nom = models.CharField( "Nom: ", max_length=100)
    prenom = models.CharField("Prénom: ", max_length=100)
    no_civique = models.CharField("Numéro civique: ", max_length=20)
    addresse_civique = models.CharField("Adresse: ", max_length=100)
    code_postale = models.CharField("Code postale: ", max_length=7)
    province = models.CharField( "Province: ", max_length=2, choices=provinces)
    nas = models.IntegerField("Numéro d'assurance sociale: ")
    date_de_naissance = models.DateField("Date de naissance: ", auto_now=False, auto_now_add=False)
    employeur = models.CharField("Employeur: ", max_length=100)
    salaire = models.DecimalField("Salaire: ",max_digits=8, decimal_places=2)

    class Meta:
        unique_together = ['code_demande', 'type_client']
    def __str__(self):
        return self.nom + ' ' + self.prenom