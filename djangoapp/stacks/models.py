from django.db import models





class Participantes(models.Model):
    nome = models.CharField(max_length=120,unique=True)



class Stack(models.Model):

    nome  = models.CharField(max_length=30,primary_key=True,unique=True)


    choices = (
        ('DEFAULT','DEFAUT'),
        ('PYTHON','PYTHON'),
        ('JAVA','JAVA'),
    )

    choice_stacks = models.CharField(max_length=30,choices=choices,default='DEFAULT')
    
    pessoas = models.ManyToManyField("Participantes",blank=True)

    def __str__(self):
        return f'{self.choice_stacks}'' 'f'{self.nome}' 
    
    

