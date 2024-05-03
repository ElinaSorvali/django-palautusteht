from django.db import models
    
class Autot(models.Model):
    merkki = models.CharField(max_length= 50, default="auto")
    malli = models.CharField(max_length= 50, default="auto")
    vuosi = models.CharField(max_length= 4, default="auto")
    väri = models.CharField(max_length= 20, default="auto")
    moottori = models.DecimalField(max_digits=8, decimal_places=2, default=1.00)
    hinta = models.DecimalField(max_digits=8, decimal_places=2, default=1.00)

    def __str__(self):
        return f"{self.merkki}"

class Osat(models.Model):
    tuotenimi = models.CharField(max_length= 50, default="varaosat")
    auto = models.ForeignKey(Autot, on_delete=models.CASCADE)
    paino = models.CharField(max_length= 20, default="varaosat")
    määrä = models.CharField(max_length= 50, default="varaosat")
    hinta = models.DecimalField(max_digits=8, decimal_places=2, default=1.00)

    def __str__(self):
        return f"{self.tuotenimi}"