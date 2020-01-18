from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import JSONField
from django.core.serializers.json import DjangoJSONEncoder
from django.db import models
from django.template import Template, Context
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from butter_exercise.users.choices import AgreementCategories
from butter_exercise.utils.helpers import aware_today


class User(AbstractUser):
    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_("Name of User"), blank=True, max_length=255)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})


class Agreement(models.Model):
    category = models.CharField(
        max_length=255, choices=AgreementCategories.choices, default=AgreementCategories.TERMS_AND_SERVICES
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=aware_today, help_text=_("The date agreement was signed"))
    data = JSONField(encoder=DjangoJSONEncoder, help_text=_("Data agreement was signed with"))
    html = models.TextField()

    @staticmethod
    def get_required_data_keys() -> set:
        # this can be made much smarter during future development
        return {'first_name', 'last_name', 'street', 'post_code'}

    @staticmethod
    def get_template():
        template_string = """
        <div style="font-size: 20px; text-align: center;">
            <p>Some agreement template</p>
            <p style="font-size: 15px;">
                {{first_name}} - {{last_name}}
            </p>
            <p>
                {{street}} - {{post_code}}
            </p>
            <p style="font-size: 15px;">
                Dated: {{date}}
            </p>
        </div>
        """
        return Template(template_string)

    def save(self, *args, **kwargs):
        if not self.html:
            self.html = self._get_html()
        return super().save(*args, **kwargs)

    def _get_html(self) -> str:
        data = self.data.copy()
        data['date'] = self.date
        context = Context(data)
        return self.get_template().render(context)
