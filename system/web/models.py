from django.db import models

# Create your models here.
class Data(models.Model):
	id = models.AutoField(primary_key=True)
	url = models.CharField(max_length=100, verbose_name="Url")

	def __str__(self):
		row = "Url: " + self.url
		return row