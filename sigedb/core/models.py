from django.db import models


class District(models.Model):
    id_district = models.AutoField(primary_key=True)
    district_name = models.CharField(max_length=100)
    district_code = models.CharField(max_length=3)


class Subdistrict(models.Model):
    id_subdistrict = models.AutoField(primary_key=True)
    subdistrict_name = models.CharField(max_length=100)
    subdistrict_code = models.CharField(max_length=3)
    district_id = models.ForeignKey(District, on_delete=models.CASCADE)


class Contractor(models.Model):
    id_contractor = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    director = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    telephone = models.CharField(max_length=11)
    district_id = models.ForeignKey(District, on_delete=models.CASCADE)
    subdistrict_id = models.ForeignKey(Subdistrict, on_delete=models.CASCADE)


class Typeworks(models.Model):
    id_typeworks = models.AutoField(primary_key=True)
    typeworks_description = models.CharField(max_length=100)
    typeworks_code = models.CharField(max_length=2)


class Fundsource(models.Model):
    id_fundsource = models.AutoField(primary_key=True)
    fundsource_description = models.CharField(max_length=100)
    fundsource_code = models.CharField(max_length=2)


class Contract(models.Model):
    id_contract = models.AutoField(primary_key=True)
    contract_description = models.CharField(max_length=200)
    contract_year_cycle = models.IntegerField()
    contract_value = models.DecimalField(max_digits=9, decimal_places=2)
    contract_cost = models.DecimalField(max_digits=9, decimal_places=2)
    contract_code = models.CharField(max_length=20)
    contract_length_original = models.IntegerField()
    contract_length_actual = models.IntegerField()
    contractor_id = models.ForeignKey(Contractor, on_delete=models.CASCADE)
    typeworks_id = models.ForeignKey(Typeworks, on_delete=models.CASCADE)
    fundsource_id = models.ForeignKey(Fundsource, on_delete=models.CASCADE)



