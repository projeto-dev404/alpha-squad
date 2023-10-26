from django.db import models

# Create your models here.



class Stacks(models.Model):

    STACK_CHOICES = [
    ('PYTHON','PYTHON'),
    ('JAVA','JAVA'),
    ('JAVASCRIPT','JAVASCRIPT'),
    ('PHP','PHP'),
    ('RUBY ON RAILS','RUBY ON RAILS'),
    ('UX/UI','UX/UI'),
    ('DEVOPS','DEVOPS'),
    ('BIG DATA','BIG DATA'),
    ('C#/.NET','C#/.NET'),
    ('FLUTTER','FLUTTER'),
    ('RUST','RUST'),
    ('ANDROID','ANDROID'),
    ('IOS','IOS'),
    ('CLOUD (AWS/AZURE)','CLOUD (AWS/AZURE)'),
    ('IA','IA'),
    
]

    id = models.AutoField(primary_key=True,)
    escolha = models.CharField(max_length=30,choices=STACK_CHOICES, default="DEFAULT VALUE",)
   

    def __str__(self):
        return f'{self.escolha}' ' - ' f'{self.id}'