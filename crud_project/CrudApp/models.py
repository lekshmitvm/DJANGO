from djongo import models

# Create your models here.
class VehicleModel(models.Model):
    vehicle_number = models.CharField(max_length=200, primary_key=True, db_index=True)
    vehicle_model = models.CharField(max_length=200, null=True)
    CHOICES = ( ("Two wheeler", "Two wheeler"),
                ("Two wheeler", "Three wheeler"),
                ("Two wheeler", "Four wheeler"),
    )
    vehicle_type = models.CharField(max_length=100, choices=CHOICES, null=True)
    vehicle_description = models.CharField(max_length=1000, null=True)

    
    def __str__(self):
        return self.vehicle_number

    class Meta:
        db_table = "vehicle_col"