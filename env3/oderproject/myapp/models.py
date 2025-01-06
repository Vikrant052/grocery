

from django.db import models
from django.conf import settings 

class Order(models.Model):
  
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,  
        related_name='orders'
    )

    total_price = models.DecimalField(max_digits=20, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=50,
        choices=[('Pending', 'Pending'), ('Completed', 'Completed')],
        default='Pending'
    )

    def __str__(self):
        return f"Order #{self.id} - {self.status}"




