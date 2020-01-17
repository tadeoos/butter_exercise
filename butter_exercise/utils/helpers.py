from django.utils import timezone


def aware_today():
    return timezone.now().date()
