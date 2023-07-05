from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Product
from user.models import User

# Function in charge of notifying updates
@receiver(post_save, sender=Product)
def send_notification(sender, instance, **kwargs):
    subject = f"Cambio en el producto: {instance.name}"
    message = f"Se ha realizado un cambio en el producto {instance.name}."
    from_email = "quiquejesus94@gmail.com"  #  dirección de correo electrónico
    admin_emails = [admin.email for admin in User.objects.all()]  # Obtén los correos de los administradores
    print(admin_emails)
    send_mail(subject, message, from_email, admin_emails, fail_silently=True)

# Function in charge of notifying deletes 
@receiver(post_delete, sender=Product)
def send_deleted_notification(sender, instance, **kwargs):
    subject = f"Producto eliminado: {instance.name}"
    message = f"El producto {instance.name} ha sido eliminado."
    from_email = "quiquejesus94@gmail.com"  # dirección de correo electrónico
    admin_emails = [admin.email for admin in User.objects.all()]  # Obtén los correos de los administradores
    send_mail(subject, message, from_email, admin_emails, fail_silently=True)