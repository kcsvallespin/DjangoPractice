from django.db import models

class TestTable(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    
    class Meta:
        db_table = 'testtable' 
        managed = False 

    def __str__(self):
        return self.name