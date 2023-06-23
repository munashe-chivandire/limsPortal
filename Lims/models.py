from django.db import models
# Create your models here.

class Province(models.Model):
    name            = models.CharField(max_length=1000, null=True,blank=True)
    code            = models.CharField(max_length=1000, null=True,blank=True)
    date_created    = models.DateTimeField('date created', auto_now_add=True, null=True, blank = True)
    date_update     = models.DateTimeField('date updated', auto_now=True, null=True, blank = True)


    def __str__(self):
        return str(self.name)
    
    class Meta:
        ordering = ('-date_created',)

class District(models.Model):
    name        = models.CharField(max_length=1000, null=True,blank=True)
    code        = models.CharField(max_length=1000, null=True,blank=True)
    province    = models.ForeignKey(Province, on_delete=models.CASCADE, null=True, blank=True)
    date_created    = models.DateTimeField('date created', auto_now_add=True, null=True, blank = True)
    date_update     = models.DateTimeField('date updated', auto_now=True, null=True, blank = True)

    def __str__(self):
        return str(self.name)
    
    class Meta:
        ordering = ('-date_created',)


class conpi_reasons(models.Model):
    name        = models.CharField(max_length=1000, null=True,blank=True)
    code        = models.CharField(max_length=1000, null=True,blank=True)
    date_created    = models.DateTimeField('date created', auto_now_add=True, null=True, blank = True)
    date_update     = models.DateTimeField('date updated', auto_now=True, null=True, blank = True)

    def __str__(self):
        return str(self.name)
    
    class Meta:
        ordering = ('-date_created',)



class conpi_stages(models.Model):
    name            = models.CharField(max_length=1000, null=True,blank=True)
    code            = models.CharField(max_length=1000, null=True,blank=True)
    date_created    = models.DateTimeField('date created', auto_now_add=True, null=True, blank = True)
    date_update     = models.DateTimeField('date updated', auto_now=True, null=True, blank = True)

    def __str__(self):
        return str(self.name)
    
    class Meta:
        ordering = ('-date_created',)



class conpi(models.Model):
    farm_name           = models.CharField(max_length=5000, null=True, blank= True)
    district            = models.ForeignKey(District, on_delete=models.CASCADE, null=True, blank= True)
    title_deed_number   = models.CharField(max_length=5000, null=True,  blank= True)
    farm_category       = models.CharField(max_length=5000, null=True,  blank= True)
    farm_owner_name     = models.CharField(max_length=5000, null=True,  blank= True)
    name_of_applicant   = models.CharField(max_length=5000, null=True,  blank= True)
    contact_details     = models.CharField(max_length=5000, null=True,  blank= True)
    reason_for_applying = models.ForeignKey(conpi_reasons, on_delete=models.CASCADE, null=True, blank=True )
    settlers            = models.BooleanField(null=True, blank=True)
    number_of_settlers  = models.IntegerField(null=True,blank=True)
    reasons_for_conpi   = models.TextField(null=True, blank=True)
    status              = models.ForeignKey(conpi_stages, on_delete=models.CASCADE, null=True, blank=True)
    interestinterest            = models.BooleanField(null=True, blank=True)
    signatue            = models.FileField(upload_to='signature', null =True, blank =True)
    other               = models.FileField(upload_to='other_conpi_documents', null =True, blank =True)
    date_created        = models.DateTimeField('date created', auto_now_add=True, null=True, blank = True)
    date_update         = models.DateTimeField('date updated', auto_now=True, null=True, blank = True)

    def __str__(self):
        return str(self.farm_name)
    
    class Meta:
        ordering = ('-date_created',)

