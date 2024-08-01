from django.db import models

# Create your models here.


class my_menu(models.Model):
     name_menu = models.CharField(max_length=30)
     name = models.CharField(max_length=30)
     description = models.TextField('Описание')

     class Meta:
         verbose_name = 'Меню'
         verbose_name_plural = 'Меню'

     def __str__(self):
         return self.name


class submenu(models.Model):
    parent = models.ForeignKey(my_menu, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=500)
    url_link = models.TextField(max_length=1000,  verbose_name='Внешний URL-адрес статьи',)
    selfparent = models.ForeignKey('self', on_delete=models.SET_DEFAULT, verbose_name='Вложить в', default=0, null=True, blank=True,)

    class Meta:
        verbose_name = 'Вложение меню'
        verbose_name_plural = 'Вложения меню'

    def __str__(self):
        return self.name
