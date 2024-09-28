from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

"""
class admin_user_login(models.Model):
    username = models.EmailField(unique=True)
    password = models.TextField(validators=[MinLengthValidator(8)])


class CollegeRegistration(models.Model):
    user_id = models.CharField(max_length=50, unique=True)
    principal_name = models.CharField(max_length=255, null=True)
    principal_number = models.CharField(max_length=50, null=True)
    principal_email = models.EmailField(unique=True, null=True)
    placement_officer_name = models.CharField(max_length=255, null=True)
    placement_officer_num = models.CharField(max_length=50)
    placement_officer_email = models.EmailField(unique=True)
    password = models.CharField(max_length=250)
    stream = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    contact_type = models.CharField(max_length=50)
    number_of_dept = models.PositiveIntegerField()
    ug_students = models.CharField(max_length=50)
    pg_students = models.CharField(max_length=50)


class StudentRegistration(models.Model):
    student_name = models.CharField(max_length=50)
    college_name = models.CharField(max_length=50)
    student_ug_pg = models.CharField(max_length=50)
    student_stream = models.CharField(max_length=50)
    student_dept = models.CharField(max_length=50)
    student_sem = models.PositiveIntegerField()
    student_10_mark = models.PositiveIntegerField()
    student_12_mark = models.PositiveIntegerField()
    student_aadhar_num = models.CharField(max_length=50)
    student_pan_num = models.CharField(max_length=50)
    student_cgpa = models.CharField(max_length=50)
    student_email = models.EmailField(max_length=254, unique=True)
    student_phone_num = models.CharField(max_length=50, unique=True)
    student_alter_num = models.CharField(max_length=50, blank=True)
    student_address = models.CharField(max_length=250)
    student_resume = models.FileField(upload_to='resumes/', max_length=100)
    password = models.TextField(validators=[MinLengthValidator(8)])

    def __str__(self):
        return f"{self.student_name} - {self.college_name}"


class adminchanges(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=50)
    small_title = models.CharField(max_length=50)
    small_content = models.CharField(max_length=50)
    job_images = models.ImageField(upload_to=None)

class Registration(models.Model):
    full_name = models.CharField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(max_length=20)
    department = models.CharField(max_length=20)
    college_name = models.CharField(max_length=100)
    passed_out = models.CharField(max_length=4)
    address = models.TextField()
    country_code = models.CharField(max_length=5)
    phone = models.CharField(max_length=20)
"""

# 1st Table (Primary Table)
class PrimaryTable(models.Model):
    it_bps = models.CharField(max_length=50)
    email = models.EmailField(primary_key=True)
    aadhar = models.CharField(max_length=12)
    firstname = models.CharField(max_length=100)
    middleName = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    day = models.IntegerField()
    month = models.CharField(max_length=20)
    year = models.IntegerField()

    def __str__(self):
        return self.firstname + " " + self.lastname



# 2nd Table (Reference to Primary Table)
class PersonalDetails(models.Model):
    primary_table = models.ForeignKey(PrimaryTable, on_delete=models.CASCADE)
    res_mr_mrs = models.CharField(max_length=10)
    father_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    house_no = models.CharField(max_length=50)
    street_name = models.CharField(max_length=100)
    landmark = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    pincode = models.CharField(max_length=10)
    alt_email = models.EmailField()
    mobile = models.CharField(max_length=15)
    alt_mobile = models.CharField(max_length=15, blank=True)


# 3rd Table
class AcademicDetails(models.Model):
    primary_table = models.ForeignKey(PrimaryTable, on_delete=models.CASCADE)
    institute_name = models.CharField(max_length=200)
    high_qualification = models.CharField(max_length=100)
    stream = models.CharField(max_length=100)
    passed_out = models.CharField(max_length=4)

# 5th Table
class CourseDetails(models.Model):
    primary_table = models.ForeignKey(PrimaryTable, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=100)
    course_duration_start = models.DateField()
    course_duration_end = models.DateField()
    course_type = models.CharField(max_length=50)
    university_college_name = models.CharField(max_length=200)
    department = models.CharField(max_length=100)
    grading_system = models.CharField(max_length=50)

# 6th Table (xii and diploma)
class XIIAndDiploma(models.Model):
    primary_table = models.ForeignKey(PrimaryTable, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100)
    university = models.CharField(max_length=200)
    board_of_education = models.CharField(max_length=100)
    duration_start = models.DateField()
    duration_end = models.DateField()
    course_type = models.CharField(max_length=50)
    grading_system = models.CharField(max_length=50)
    

# 7th Table (xth)
class XthDetails(models.Model):
    primary_table = models.ForeignKey(PrimaryTable, on_delete=models.CASCADE)
    roll_no = models.CharField(max_length=50)
    university = models.CharField(max_length=200)
    board_of_education = models.CharField(max_length=100)
    duration_start = models.DateField()
    duration_end = models.DateField()
    grading_system = models.CharField(max_length=50)


# 8th Table (Other Qualification)
class OtherQualification(models.Model):
    primary_table = models.ForeignKey(PrimaryTable, on_delete=models.CASCADE)
    any_other_course = models.CharField(max_length=100)
    course_name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    university = models.CharField(max_length=200)
    duration_start = models.DateField()
    duration_end = models.DateField()
    course_type = models.CharField(max_length=50)
    grading_system = models.CharField(max_length=50)

# 9th Table (Work Experience)
class WorkExperience(models.Model):
    primary_table = models.ForeignKey(PrimaryTable, on_delete=models.CASCADE)
    experience = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    employee_type = models.CharField(max_length=100)
    duration_from = models.DateField()
    duration_to = models.DateField()
    designation = models.CharField(max_length=100)
    annual_salary = models.DecimalField(max_digits=10, decimal_places=2)

class ArrearDetails(models.Model):
    primary_table = models.ForeignKey(PrimaryTable, on_delete=models.CASCADE)
    arrears = models.CharField(max_length=3, choices=[('yes', 'Yes'), ('no', 'No')], default='no')
    arrear_count = models.IntegerField(null=True, blank=True)


# 10th Table (Others)
class OtherDetails(models.Model):
    primary_table = models.ForeignKey(PrimaryTable, on_delete=models.CASCADE)
    nationality = models.CharField(max_length=50)
    language = models.CharField(max_length=50)
    speak = models.BooleanField(default=False)
    read = models.BooleanField(default=False)
    write = models.BooleanField(default=False)
    mother_tongue = models.CharField(max_length=50)

# 11th Table (Photo/CV)
class PhotoCV(models.Model):
    primary_table = models.ForeignKey(PrimaryTable, on_delete=models.CASCADE)
    blood_group = models.CharField(max_length=3)
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/')
    cv = models.FileField(upload_to='cvs/')
