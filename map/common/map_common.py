__author__ = 'kelvin Guerrero'
from map.models import Map
from datetime import date

def dar_semestre():
    map = Map.objects.first()