from django.db import models

CHOICE_STACKS = [
    ('DEFAULT','DEFAUT'),
    ('PYTHON','PYTHON'),
    ('JAVA','JAVA'),

]

class Stack(models.Model):
    id = models.AutoField(primary_key=True, default='DEFAULT')
    nome = models.CharField(max_length=30)

    
   
    
    

