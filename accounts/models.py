from django.db import models

# Create your models here.

# User Table
class User(models.Model):
    ROLE_CHOICES = [
        ('applicant', 'Applicant'),
        ('admin', 'Admin'),
    ]
    
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]

    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default='applicant')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    gender = models.CharField(max_length=10)
    field_placement = models.ForeignKey('FieldPlacement', on_delete=models.CASCADE)
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.role}"

# Profile Table
class Profile(models.Model):
    profile_id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    hashed_password = models.CharField(max_length=255)
    academic_year = models.CharField(max_length=50)
    course = models.CharField(max_length=100)
    phone_number = models.BigIntegerField()
    university_name = models.CharField(max_length=255)
    document = models.ForeignKey('Document', on_delete=models.CASCADE)

    def __str__(self):
        return self.email

# Documents Table
class Document(models.Model):
    document_id = models.AutoField(primary_key=True)
    university_id_path = models.CharField(max_length=255)
    reference_letter_path = models.CharField(max_length=255)
    transcript_path = models.CharField(max_length=255)
    resume_cv_path = models.CharField(max_length=255)
    profile_pic_path = models.CharField(max_length=255)

    def __str__(self):
        return f"Document {self.document_id}"

# Field Placement Table
class FieldPlacement(models.Model):
    field_placement_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    unit = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    level = models.CharField(max_length=50)
    location = models.CharField(max_length=255)
    duration = models.CharField(max_length=50)
    deadline = models.DateField()

    def __str__(self):
        return self.title
