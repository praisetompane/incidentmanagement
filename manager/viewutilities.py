from django.core.mail import send_mail
from django.utils.crypto import get_random_string

def generateReferenceNumber():
    return get_random_string(length=10)


def sendAcknowledgementEmail(maintenaceType, referenceNumber, recipients):
    send_mail(
        'Maintenance Request for' + maintenaceType,
        'Thank you for logging you request, your reference number is:' + referenceNumber,
        'simplemaintenances@gmail.com',
        recipients,
        fail_silently=False)