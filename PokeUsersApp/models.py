from django.db import models

class Pokemon(models.Model):
    poke_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class User(models.Model):
    username = models.CharField(max_length = 50)
    password = models.CharField(max_length = 100)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    pokemon_captured = models.ManyToManyField(
        Pokemon,
        related_name = 'captured_by'
    )