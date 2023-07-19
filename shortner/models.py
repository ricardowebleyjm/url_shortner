from django.db import models

class URL(models.Model):
    original_url = models.URLField(max_length=255)
    shortened_url = models.CharField(max_length=30, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    click_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.shortened_url

class Click(models.Model):
    url = models.ForeignKey(URL, on_delete=models.CASCADE)
    clicked_at = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField()

    def __str__(self):
        return f"Clicked at: {self.clicked_at}, IP: {self.ip_address}"