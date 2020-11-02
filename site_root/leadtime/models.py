from django.db import models

class Inventory(models.Model):
    item = models.TextField()
    sku = models.TextField()
    shipper = models.TextField()
    ship_loc = models.TextField()
    ship_intransit = models.TextField()
    ship_backorder = models.TextField()
    ship_perweek = models.TextField()
    leadtime_core = models.TextField()
    leadtime_growth = models.TextField()
