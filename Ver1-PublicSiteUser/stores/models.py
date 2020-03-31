from django.db import models
from tenant_schemas.models import TenantMixin


class Client(TenantMixin):

    name = models.CharField(max_length=255, unique=True, null=False)
    description = models.TextField(blank=True)
    expire_date = models.DateField()
    created_on = models.DateField(auto_now_add=True)

    auto_create_schema = True

    def __str__(self):
        return self.domain_url





