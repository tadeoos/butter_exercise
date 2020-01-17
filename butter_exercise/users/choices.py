from django.utils.translation import gettext_lazy as _

from butter_exercise.utils.enums import TextChoices


class AgreementCategories(TextChoices):
    TERMS_AND_SERVICES = 'terms_and_services', _('Terms and Services')
