from django.contrib.auth.models import UserManager

class CustomeUserManager(UserManager):

    def create_user(self, phone,password =None, **extra_fields):

        if not phone :
            raise ValueError("Phone number required")
        
        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user
        
    
    def create_superuser(self, phone, password=None, **extra_fields):

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(phone, password, **extra_fields)