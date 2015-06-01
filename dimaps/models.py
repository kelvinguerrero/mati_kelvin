from django.db import models
from django.utils.timezone import now

# Create your models here.


class Service(models.Model):
    identifier = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=200)
    discovery_method = models.CharField(max_length=200)
    business_function = models.TextField()
    service_providers = models.TextField()
    security = models.TextField()
    created_at = models.DateTimeField(

        default=now(),
        editable=False,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        default=now(),
        editable=False,
    )

    @models.permalink
    def get_absolute_url(self):
        return 'dimaps_service_detail', (), {'pk': self.pk}

    def __unicode__(self):
        return self.identifier


class TechnicalData(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    service = models.ForeignKey('Service')
    created_at = models.DateTimeField(

        default=now(),
        editable=False,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        default=now(),
        editable=False,
    )

    @models.permalink
    def get_absolute_url(self):
        return 'dimaps_technicaldata_detail', (), {'pk': self.pk}

    def __unicode__(self):
        return self.name


class ServiceConsumer(models.Model):
    name = models.CharField(max_length=200)
    objective = models.TextField()
    service = models.ForeignKey('Service')
    created_at = models.DateTimeField(

        default=now(),
        editable=False,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        default=now(),
        editable=False,
    )

    @models.permalink
    def get_absolute_url(self):
        return 'dimaps_serviceconsumer_detail', (), {'pk': self.pk}

    def __unicode__(self):
        return self.name


class Operation(models.Model):
    name = models.CharField(max_length=200)
    preconditions = models.TextField()
    postconditions = models.TextField()
    details = models.TextField()
    http_call = models.CharField(max_length=10)
    url_operation = models.CharField(max_length=200)
    service = models.ForeignKey('Service')
    created_at = models.DateTimeField(

        default=now(),
        editable=False,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        default=now(),
        editable=False,
    )

    @models.permalink
    def get_absolute_url(self):
        return 'dimaps_operation_detail', (), {'pk': self.pk}

    def __unicode__(self):
        return self.name


class Input(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    mandatory = models.BooleanField(default=False)
    observation = models.TextField()
    operation = models.ForeignKey('Operation')
    created_at = models.DateTimeField(

        default=now(),
        editable=False,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        default=now(),
        editable=False,
    )

    @models.permalink
    def get_absolute_url(self):
        return 'dimaps_input_detail', (), {'pk': self.pk}

    def __unicode__(self):
        return self.name


class Output(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    mandatory = models.BooleanField(default=False)
    observation = models.TextField()
    operation = models.ForeignKey('Operation')
    created_at = models.DateTimeField(

        default=now(),
        editable=False,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        default=now(),
        editable=False,
    )

    @models.permalink
    def get_absolute_url(self):
        return 'dimaps_output_detail', (), {'pk': self.pk}

    def __unicode__(self):
        return self.name