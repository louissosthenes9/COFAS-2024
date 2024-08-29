from django.db import models

# Create your models here.

class User(models.Model):
    """
    Custom User model.

    This model represents a user in the system, with fields for first name, middle name, last name, role, status, gender, and foreign keys to Profile and FieldPlacement.

    Args:
        first_name (str): The user's first name.
        middle_name (str, optional): The user's middle name. Defaults to None.
        last_name (str): The user's last name.
        role (str): The user's role, either 'applicant' or 'admin'. Defaults to 'applicant'.
        status (str): The user's status, either 'pending', 'accepted', or 'rejected'. Defaults to 'pending'.
        gender (str): The user's gender.
        field_placement (FieldPlacement): The user's field placement.
        profile (Profile): The user's profile.

    Example:
        >>> user = User(first_name='John', last_name='Doe', role='applicant', status='pending', gender='male', field_placement=FieldPlacement.objects.get(id=1), profile=Profile.objects.get(id=1))
    """
    
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
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50)
    role = models.CharField(max_length=30, choices=ROLE_CHOICES, default='applicant')
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='pending')
    gender = models.CharField(max_length=10)
    field_placement = models.ForeignKey('FieldPlacement', on_delete=models.CASCADE)
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.role}"



class Profile(models.Model):
    """
    Profile model.

    This model represents a user's profile, with fields for email, hashed password, academic year, course, phone number, university name, and a foreign key to Document.

    Args:
        email (str): The user's email address.
        hashed_password (str): The user's hashed password.
        academic_year (str): The user's academic year.
        course (str): The user's course.
        phone_number (int): The user's phone number.
        university_name (str): The user's university name.
        document (Document): The user's document.

    Example:
        >>> profile = Profile(email='johndoe@example.com', hashed_password='hashed_password', academic_year='2022', course='Computer Science', phone_number=1234567890, university_name='University of Example', document=Document.objects.get(id=1))
    """
    profile_id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=50, unique=True)
    hashed_password = models.CharField(max_length=255)
    academic_year = models.CharField(max_length=50)
    course = models.CharField(max_length=100)
    phone_number = models.BigIntegerField()
    university_name = models.CharField(max_length=255)
    document = models.ForeignKey('Document', on_delete=models.CASCADE)

    def __str__(self):
        return self.email



class Document(models.Model):
    """
    Document model.

    This model represents a user's document, with fields for university ID path, reference letter path, transcript path, resume/CV path, and profile picture path.

    Args:
        university_id_path (str): The path to the user's university ID document.
        reference_letter_path (str): The path to the user's reference letter document.
        transcript_path (str): The path to the user's transcript document.
        resume_cv_path (str): The path to the user's resume/CV document.
        profile_pic_path (str): The path to the user's profile picture.

    Example:
        >>> document = Document(university_id_path='path/to/university_id', reference_letter_path='path/to/reference_letter', transcript_path='path/to/transcript', resume_cv_path='path/to/resume_cv', profile_pic_path='path/to/profile_pic')
    """
    document_id = models.AutoField(primary_key=True)
    university_id_path = models.CharField(max_length=255)
    reference_letter_path = models.CharField(max_length=255)
    transcript_path = models.CharField(max_length=255)
    resume_cv_path = models.CharField(max_length=255)
    profile_pic_path = models.CharField(max_length=255)

    def __str__(self):
        return self.title



class FieldPlacement(models.Model):
    """
    Field Placement model.

    This model represents a field placement, with fields for title, description, unit, department, level, location, duration, and deadline.

    Args:
        title (str): The title of the field placement.
        description (str): The description of the field placement.
        unit (str): The unit of the field placement.
        department (str): The department of the field placement.
        level (str): The level of the field placement.
        location (str): The location of the field placement.
        duration (str): The duration of the field placement.
        deadline (date): The deadline of the field placement.

    Example:
        >>> field_placement = FieldPlacement(
                title='Web development',
                description='Skilled in Django',
                unit='ICT',
                department='Software Engineering',
                level='Undergraduate',
                location='HQ-DSM',
                duration='3 months',
                deadline='2025-01-01'
            )
    """

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
