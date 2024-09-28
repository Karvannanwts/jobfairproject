from django.shortcuts import render,redirect
import random
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib import messages
import re
from django.core.files.storage import FileSystemStorage
from .models import *
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import check_password
from django.db import IntegrityError
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException


# def send_otp(phone_number):
#     try:
#         otp = random.randint(1000, 9999)  # Generate a 4-digit OTP
#         SID = 'ACccff6c0361e1eb11e65d6999d77bee81'  # Your Twilio SID
#         token = 'da062c1f1e551261e52f2ad94cd97ea9'  # Your Twilio Auth Token
#         client = Client(SID, token)

#         # Add the country code +91 for India
#         full_phone_number = f"+91{8270860729}"

#         # Send OTP message
#         message = client.messages.create(
#             body=f"Your OTP is {otp}",
#             from_='+16062688896',  # Your Twilio verified phone number
#             to=full_phone_number  # Phone number to send the OTP
#         )

#         return otp

#     except TwilioRestException as e:
#         print(f"Error sending OTP: {e}")
#         return None

# if __name__ == "__main__":
#     phone_number = '8270860729'  # Example phone number (without country code)
#     otp_sent = send_otp(phone_number)
    
#     if otp_sent:
#         print(f"OTP sent successfully: {otp_sent}")
#     else:
#         print("Failed to send OTP.")

#def send_otp_view(request):
    # if request.method == 'POST':
    #     phone_number = request.POST.get('phone_number')
        
    #     if phone_number:  # Validate phone number
    #         otp = send_otp(phone_number)
            
    #         # Save the OTP and phone number in the session or database for verification
    #         request.session['otp'] = otp
    #         request.session['phone_number'] = phone_number
            
    #         return JsonResponse({'status': 'success', 'message': 'OTP sent successfully'})
    #     else:
    #         return JsonResponse({'status': 'error', 'message': 'Invalid phone number'})

    # return render(request, 'send_otp.html')

# # views.py

# def verify_otp_view(request):
    # if request.method == 'POST':
    #     user_otp = request.POST.get('otp')
    #     session_otp = request.session.get('otp')

    #     if str(user_otp) == str(session_otp):
    #         return JsonResponse({'status': 'success', 'message': 'OTP verified successfully'})
    #     else:
    #         return JsonResponse({'status': 'error', 'message': 'Invalid OTP'})

    # return render(request, 'verify_otp.html')


def mailsend(mail_id):
    global otp
    otp = random.randint(1111,9999)
    subject = 'Otp verification'
    message = f'Your OTP for verification is: {otp}'
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [mail_id]

    send_mail(
        subject,
        message,
        from_email,
        recipient_list,
        otp,
    )

# def name_validation(fullname):
#     name_pattern = re.compile(r"^[A-Za-zÀ-ÖØ-öø-ÿ' -]{3,}$")
#     if name_pattern.match(fullname):
#         return fullname
#     else:
#         return JsonResponse({'status': 'error', 'message': 'Incorrect Name. Please try again.'})

# def phone_validation(phone):
#     phone_pattern = re.compile(r"^(\?\d{3}\?[-\s]?)?\d{3}[-\s]?\d{4}$")
#     if phone_pattern.match(phone):
#         return phone
#     else:
#         return JsonResponse({'status': 'error', 'message': 'Incorrect Phone Number. Please try again.'})

# def address_validation(address):
#     address_pattern = re.compile(r"^[A-Za-z0-9À-ÖØ-öø-ÿ'.,#\-/\s]{5,}$")
#     if address_pattern.match(address):
#         return address
#     else:
#         return JsonResponse({'status': 'error', 'message': 'Incorrect Address. Please try again.'})

def home_view(request):
    return render(request,'index.html')

# def login(request):
#     if request.method == 'POST':
#         username = request.POST.get('Name')
#         qualification = request.POST.get('qualification')
#         phone = request.POST.get('mobile')
        

#         # Username validation using regex (at least 4 letters, no numbers)
#         if not re.match(r'^[A-Za-z\s]{3,}$', username):
#             return HttpResponse("Invalid username: Must be at least 3 letters long and contain no numbers.")

#         # Qualification validation using regex (at least 4 letters, no numbers)
#         if not re.match(r'^[A-Za-z\s]{4,}$', qualification):
#             return HttpResponse("Invalid qualification: Must be at least 4 letters long and contain no numbers.")
        
#         # Phone Number Validation (exactly 10 digits)
#         if not re.match(r'^[6-9]{1}\d{9}$', phone):
#             return JsonResponse({'error': 'start with 6-9 Phone number must be exactly 10 digits.'}, status=400)

#         # Email validation using Django's validate_email
#         # try:
#         #     validate_email(email)
#         # except ValidationError:
#         #     return HttpResponse("Invalid email format.")

#         # # Check if the email already exists in the database
#         # if UserProfile.objects.filter(email=email).exists():
#         #     return HttpResponse("The email address is already in use. Please use a different email address.")

#         # Create a new UserProfile instance and save it to the database
#         # try:
#         #     user_profile = UserProfile(username=username, qualification=qualification, email=email)
#         #     user_profile.save()
#         #     return HttpResponse("Form successfully submitted and data saved to the database.")
#         # except Exception as e:
#         #     return HttpResponse(f"An error occurred: {str(e)}")

#     return render(request,'reg_login.html')

# def signin(request):

#     return render(request,'register1.html')

# def register(request):
#     category = request.GET.get('category', None)
    
#     if request.method == "POST":
#         mail_id = request.POST.get('email')
#         otp = random.randint(1111, 9999)
#         mailsend(mail_id, otp)
        
#         # Store OTP, email, and it_bps in the session
#         request.session['otp'] = otp
#         request.session['it_bps'] = category
#         request.session['email'] = mail_id

#         return redirect('email_otp')

#     return render(request, 'register_email.html')

# def otp(request):
    #otp = request.session.get('otp')
    if request.method=="POST":
        one_time_pass = request.POST.get('otp')
        if str(otp) == one_time_pass:
            return JsonResponse({'status': 'success', 'message': 'OTP verified successfully!'})

        else:
            return JsonResponse({'status': 'error', 'message': 'Incorrect OTP. Please try again.'})
            
    return render(request,'email_otp.html',{'otp': otp})

# def aadhar(request):
#     # Retrieve the values from the session
#     it_bps = request.session.get('it_bps')
#     email = request.session.get('email')
    
#     if not it_bps or not email:
#         # Handle the case if values are missing (e.g., redirect or error)
#         return redirect('email_otp')

#     if request.method == "POST":
#         aadhar = request.POST.get('aadhar')
#         firstName = request.POST.get('firstName')
#         middleName = request.POST.get('middleName')
#         lastName = request.POST.get('lastName')
#         day = request.POST.get('day')
#         month = request.POST.get('month')
#         year = request.POST.get('year')
        
#         errors = {}

#         # Validate Aadhar (must be 4 digits)
#         if not aadhar.isdigit() or len(aadhar) != 4:
#             errors['aadhar'] = "Aadhar number must be exactly 4 digits."

#         # Validate First Name (at least 4 characters and no numbers)
#         if len(firstName) < 3 or not firstName.isalpha():
#             errors['first_name'] = "First name must be at least 3 letters and contain only letters."

#         # Validate Last Name (at least 1 character and no numbers)
#         if len(lastName) < 1 or not lastName.isalpha():
#             errors['last_name'] = "Last name must be at least 1 letter and contain only letters."

#         # Validate Date of Birth (basic check for valid date)
#         if not day or not month or not year:
#             errors['dob'] = "Please provide a valid date of birth."

#         # If there are any validation errors, return JSON response for AJAX
#         if errors:
#             return JsonResponse({'status': 'error', 'message': 'Validation failed.', 'errors': errors})

#         try:
#             PrimaryTable.objects.create(
#                 it_bps=it_bps,
#                 email=email,
#                 aadhar=aadhar,
#                 firstname=firstName,
#                 middleName=middleName,
#                 lastname=lastName,
#                 day=day,
#                 month=month,
#                 year=year,
#             )

#             # Return a success response
#             return JsonResponse({'status': 'success', 'message': 'Data successfully submitted!'})
#         except IntegrityError:
#             return JsonResponse({'status': 'error', 'message': 'This email is already registered.'})
#     # For GET requests, render the form template
#     return render(request, 'aadhar.html')

def personal_1(request):

    # # Fetch primary_table entry for the logged-in user
    # try:
    #     primary_table = PrimaryTable.objects.get(email=email)
    # except PrimaryTable.DoesNotExist:
    #     return JsonResponse({'status': 'error', 'message': 'Primary table entry does not exist.'})

    # Handle POST request for form submission
    if request.method == "POST":
        # Retrieve form data
        res_mr_mrs = request.POST.get('name')
        father_name = request.POST.get('fatherName')
        gender = request.POST.get('gender')
        house_no = request.POST.get('houseNo')
        street_name = request.POST.get('street')
        landmark = request.POST.get('area')
        country = request.POST.get('country')
        state = request.POST.get('state')
        city = request.POST.get('city')
        pincode = request.POST.get('pincode')
        alt_email = request.POST.get('altEmail')
        mobile = request.POST.get('mobilePhone')
        alt_mobile = request.POST.get('altPhone')

        # Validation
        errors = []
        
        if not mobile or len(mobile) != 10:
            errors.append("Please enter a valid 10-digit mobile number.")
        if not father_name:
            errors.append("Father's name is required.")
        if not house_no:
            errors.append("House No. is required.")
        if not street_name:
            errors.append("Street name is required.")
        if not pincode or len(pincode) != 6 or not pincode.isdigit():
            errors.append("Please enter a valid 6-digit pincode.")
        if not city:
            errors.append("City is required.")
        if not country:
            errors.append("Country is required.")
        
        # If there are validation errors, return them as JSON
        if errors:
            return JsonResponse({'status': 'error', 'message': 'Validation failed.', 'errors': errors})
        
        # If validation passes, save the form data to the PersonalDetails model
        PersonalDetails.objects.create(
            # primary_table=primary_table,
            res_mr_mrs=res_mr_mrs,
            father_name=father_name,
            gender=gender,
            house_no=house_no,
            street_name=street_name,
            landmark=landmark,
            country=country,
            state=state,
            city=city,
            pincode=pincode,
            alt_email=alt_email,
            mobile=mobile,
            alt_mobile=alt_mobile
        )

        # Return success response
        return JsonResponse({'status': 'success', 'message': 'Personal details saved successfully!'})

    # Prepare the day, month, and year variables for the template
    # day = primary_table.day
    # month = primary_table.month
    # year = primary_table.year

    # Pass primary_table data and date_of_birth details to the template
    return render(request, 'personal_1.html', {
        # 'primary_table': primary_table,
        # 'day': day,
        # 'month': month,
        # 'year': year,
    })
    
def academic(request):
    # Redirect to a success page after saving

    return render(request,'academic.html')

# def register_details(request):
#     # if request.method=="POST":
#     #     fullname = request.POST.get('fullName')
#     #     name = name_validation(fullname)
#     #     dob = request.POST.get('dob')
#     #     gender = request.POST.get('gender')
#     #     department =request.POST.get('department')
#     #     collegename =request.POST.get('collegeName')
#     #     passedout =request.POST.get('passedout')
#     #     address =request.POST.get('address')
#     #     address_home = address_validation(address)
#     #     countryCode =request.POST.get('countryCode')
#     #     phone =request.POST.get('phone')
#     #     phone_no = phone_validation(phone)

#     #      # Validate the data
#     #     errors = []
#     #     if not name:
#     #         errors.append('Full name is required.')
#     #     if not dob:
#     #         errors.append('Date of birth is required.')
#     #     else:
#     #         try:
#     #             dob = datetime.strptime(dob, '%Y-%m-%d').date()
#     #         except ValueError:
#     #             errors.append('Invalid date format.')
#     #     if not gender in ['Male', 'Female', 'Other']:
#     #         errors.append('Invalid gender.')
#     #     if not department:
#     #         errors.append('Department is required.')
#     #     if not collegename:
#     #         errors.append('College name is required.')
#     #     if not passedout:
#     #         errors.append('Year of passing is required.')
#     #     if not address:
#     #         errors.append('Address is required.')
#     #     if not countryCode:
#     #         errors.append('Country code is required.')
#     #     if not phone or not phone.isdigit():
#     #         errors.append('Phone number is required and must be digits.')


#     #     # Save the data if valid
#     #     try:
#     #         Registration.objects.create(
#     #             full_name=name,
#     #             dob=dob,
#     #             gender=gender,
#     #             department=department,
#     #             college_name=collegename,
#     #             passed_out=passedout,
#     #             address=address,
#     #             country_code=countryCode,
#     #             phone=phone
#     #         )
#     #         return redirect('success')
#     #     except ValidationError as e:
#     #         return HttpResponse(f"Error: {e}")

#     #     print(name,dob,gender,department,collegename,passedout,address_home,countryCode,phone_no)
#     return redirect('register_details2')

# def register_details2(request):
#     if request.method == 'POST':
#         pass
#     return render(request,'captcha.html')

def student_corner(request):
    return render(request, 'studentscorner.html')

# def existing_student_query(request):
#     # if request.method == 'POST':
#     #     query = StudentRegistration(  # Adjust this to the correct model
#     #         user_name=request.POST.get('userName'),
#     #         user_id=request.POST.get('userId'),
#     #         user_dept=request.POST.get('userDept'),
#     #         user_college=request.POST.get('userCollege'),
#     #         user_query=request.POST.get('userQuery'),
#     #         user_file=request.FILES.get('userFile')
#     #     )
#     #     query.save()
#     #     return redirect('home')
#     return render(request, 'studentscorner.html')

def college_registration(request):
    return render(request, 'college_register.html')

# def register_new_college(request):
    # print("kar")
    # if request.method == 'POST':
    #     # Fetch form data from POST request
    #     user_id = request.POST.get('userId')
    #     password = request.POST.get('password')
    #     principal_name = request.POST.get('principalName')
    #     principal_number = request.POST.get('principalNumber')
    #     principal_email = request.POST.get('principalMail')
    #     placement_officer_name = request.POST.get('placementOfficerName')
    #     placement_officer_number = request.POST.get('placementOfficerNumber')
    #     placement_officer_email = request.POST.get('placementOfficerMail')
        

    #     # Save the form data into the database
    #     new_college = CollegeRegistration.objects.create(
    #         user_id=user_id,
    #         principal_name=principal_name,
    #         principal_number=principal_number,
    #         principal_email=principal_email,
    #         placement_officer_name=placement_officer_name,
    #         placement_officer_num=placement_officer_number,
    #         placement_officer_email=placement_officer_email,
    #         password=password
    #     )
    #     new_college.save()

        #return JsonResponse({'message': 'New College Registered Successfully!'})

# def registered_college_login(request):
#     if request.method == 'POST':
#         user_id = request.POST.get('userId')
#         password = request.POST.get('password')

#         # Authenticate the user manually
       
# def submit_college_details(request):
    print("kar")
    if request.method == 'POST':
        user_id = request.POST.get('userId')
        college_name = request.POST.get('collegeName')
        stream = request.POST.get('stream')
        district = request.POST.get('district')
        address = request.POST.get('address')
        contact_type = request.POST.get('contactType')
        number_of_dept = request.POST.get('departments')
        ug_students = request.POST.get('totalStudentsUG')
        pg_students = request.POST.get('totalStudentsPG')

# def admin_login(request):
#     # if request.method == 'POST':
#     #     email = request.POST.get('email')
#     #     password = request.POST.get('password')
#     #     try:
#     #         # Query the database for a user with the matching username
#     #         user = admin_user_login.objects.get(username=email)
#     #         password_admin = admin_user_login.objects.get(password=password)
#     #         print(user.username,password_admin.password)
            
#     #         if email == user.username:
#     #             if password == password_admin.password:
#     #                 print("Login successful")
#     #                 return JsonResponse({'status': 'success', 'message': 'Admin Login successfully'})
                    
#     #             else:
#     #                 print('invalid password')
#     #                 return JsonResponse({'status': 'error', 'message': 'Password is Incorrect'})
#     #         else:
#     #             return JsonResponse({'status': 'error', 'message': 'Username not found. Please try again.'})
                

#     #     except admin_user_login.DoesNotExist:
#     #         print("Username not found")
#     #         return JsonResponse({'status': 'error', 'message': 'Username or Password incorrect. Please try again.'})
#     return render(request,'admin.html') 

# def personal_details(request):
#     return render(request,'personal_details.html') 

def academic_qualification(request):
    
    if request.method == "POST":
        

        # Get the primary key (email) of the PrimaryTable from the form or session
        email = request.session.get('email')

        try:
            primary_table_instance = PrimaryTable.objects.get(email=email)
        except PrimaryTable.DoesNotExist:
            return redirect('home')  # Redirect to an error page if the primary_table instance is not found
        
        # Extract form data
        institute_name = request.POST.get('institute_name')
        high_qualification = request.POST.get('highest-qualification')
        stream = request.POST.get('stream')
        passed_out = request.POST.get('year_of_passing')
        # Create a new AcademicDetails instance
        AcademicDetails.objects.create(
            primary_table=primary_table_instance,
            institute_name=institute_name,
            high_qualification=high_qualification,
            stream=stream,
            passed_out=passed_out,
        )

        try:
            # Assume form validation and saving logic here
            return JsonResponse({"status": "success", "message": "Your data has been saved."})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)})
    
    return render(request,'academic_qualification.html')

def academic_graduate(request):
    if request.method == "POST":
        # Extract form data
        course_name = request.POST.get('course_name')
        course_duration_start = request.POST.get('course_duration_start')
        course_duration_end = request.POST.get('course_duration_end')
        course_type = request.POST.get('course_type')
        university_college_name = request.POST.get('university_college_name')
        department = request.POST.get('specializations')
        grading_system = request.POST.get('grading_system')

        # Handle CGPA and Percentage if present
        cgpa = request.POST.get('cgpa')
        percentage = request.POST.get('percentage')

        # Ensure `grading_system` is valid
        if grading_system == 'cgpa' and not cgpa:
            # Handle missing CGPA
            return render(request, 'your_template.html', {'error': 'CGPA is required.'})

        if grading_system == 'percentage' and not percentage:
            # Handle missing Percentage
            return render(request, 'your_template.html', {'error': 'Percentage is required.'})

        # Get the PrimaryTable instance
        email = request.session.get('email')
        try:
            primary_table_instance = PrimaryTable.objects.get(email=email)
        except PrimaryTable.DoesNotExist:
            return redirect('home')

        # Create a new CourseDetails instance
        CourseDetails.objects.create(
            primary_table=primary_table_instance,
            course_name=course_name,
            course_duration_start=course_duration_start,
            course_duration_end=course_duration_end,
            course_type=course_type,
            university_college_name=university_college_name,
            department=department,
            grading_system=grading_system,
        )

        return JsonResponse({'status': 'success', 'message': 'Data submitted successfully!'})
    
    return render(request,'academic_graduate.html')

def academic_xii_grade(request):
    if request.method == "POST":
        # Get the primary key (id) o f the PrimaryTable from the session or other method
        primary_table_id = request.session.get('email')  # or any other method you use to get it
        
        # Check if primary_table_id exists
        if not primary_table_id:
            return redirect('error_page')  # Redirect to an error page if primary_table_id is not found
        
        try:
            primary_table_instance = PrimaryTable.objects.get(email=primary_table_id)
        except PrimaryTable.DoesNotExist:
            return redirect('error_page')  # Redirect to an error page if PrimaryTable instance is not found
        
        # Extract form data
        course = request.POST.get('course')
        
        if course == '12thGrade':
            specialization = request.POST.get('specialization12th')
            print(specialization)
            university = request.POST.get('university12th')
            board_of_education = request.POST.get('boardSelection')
            duration_start = request.POST.get('durationFrom12th')
            duration_end = request.POST.get('durationTo12th')
            course_type = request.POST.get('courseType12th')
            grading_system = request.POST.get('gradingSystem12th')
            
            # Create a new XIIAndDiploma instance for 12th Grade
            XIIAndDiploma.objects.create(
                primary_table=primary_table_instance,
                specialization=specialization,
                university=university,
                board_of_education=board_of_education,
                duration_start=duration_start,
                duration_end=duration_end,
                course_type=course_type,
                grading_system=grading_system
            )
        
        elif course == 'equivalentDiploma':
            specialization = request.POST.get('specializationDiploma')
            university = request.POST.get('universityDiploma')
            duration_start = request.POST.get('durationFromDiploma')
            duration_end = request.POST.get('durationToDiploma')
            course_type = request.POST.get('courseTypeDiploma')
            grading_system = request.POST.get('gradingSystemDiploma')
            
            # Create a new XIIAndDiploma instance for Equivalent Diploma
            XIIAndDiploma.objects.create(
                primary_table=primary_table_instance,
                specialization=specialization,
                university=university,
                board_of_education='',  # Not applicable for Equivalent Diploma
                duration_start=duration_start,
                duration_end=duration_end,
                course_type=course_type,
                grading_system=grading_system
            )
        
        return JsonResponse({'status': 'success', 'message': 'Data submitted successfully!'})
    
    return render(request,'academic_xii_grade.html')

def other_details(request):
    if request.method == "POST":
        # Get the primary key (id) of the PrimaryTable from the session
        # primary_table_id = request.session.get('email')
        
        # # Check if the primary_table_id exists
        # if not primary_table_id:
        #     return redirect('error_page')  # Redirect to an error page if primary_table_id is not found

        # try:
        #     primary_table_instance = PrimaryTable.objects.get(email=primary_table_id)
        # except PrimaryTable.DoesNotExist:
        #     return redirect('error_page')  # Redirect if the PrimaryTable instance is not found

        # Get nationality from the form
        nationality = request.POST.get('nationality')

        # Get languages and their details
        languages = request.POST.getlist('language')
        speaks = request.POST.getlist('speak')
        reads = request.POST.getlist('read')
        writes = request.POST.getlist('write')
        mother_tongue = request.POST.getlist('mother-tongue')

        # Loop through the languages and create instances
        for i, language in enumerate(languages):
            # Safely access the checkboxes, ensure no out-of-range error
            speak = speaks[i] == 'on' if i < len(speaks) else False
            read = reads[i] == 'on' if i < len(reads) else False
            write = writes[i] == 'on' if i < len(writes) else False
            is_mother_tongue = mother_tongue[i] == 'on' if i < len(mother_tongue) else False

            OtherDetails.objects.create(
                # primary_table=primary_table_instance,
                nationality=nationality,
                language=language,
                speak=speak,
                read=read,
                write=write,
                mother_tongue=language if is_mother_tongue else ''
            )

        try:
            # Assume form validation and saving logic here
            return JsonResponse({"status": "success", "message": "Your data has been saved."})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)})
    return render(request,'other_details.html')

def other_qualificaion(request):
    if request.method == "POST":
        # Get the primary key (id) of the PrimaryTable from the session or other method
        primary_table_id = request.session.get('email')  # Adjust this according to your session handling

        # Check if primary_table_id exists
        if not primary_table_id:
            return redirect('error_page')  # Redirect to an error page if primary_table_id is not found
        
        try:
            primary_table_instance = PrimaryTable.objects.get(email=primary_table_id)
        except PrimaryTable.DoesNotExist:
            return redirect('error_page')  # Redirect to an error page if PrimaryTable instance is not found

        # Extract form data
        any_other_course = request.POST.get('other_course')
        if any_other_course == 'yes':
            course_name = request.POST.get('course_name')
            specialization = request.POST.get('specialization')
            university = request.POST.get('university')
            duration_start = request.POST.get('duration_start')
            duration_end = request.POST.get('duration_end')
            course_type = request.POST.get('course_type')
            grading_system = request.POST.get('grading_system')

            # Determine grading system specifics
            if grading_system == 'cgpa':
                cgpa = request.POST.get('cgpa')
                percentage = None
            elif grading_system == 'percentage':
                cgpa = None
                percentage = request.POST.get('percentage')
            else:
                cgpa = None
                percentage = None

            # Create a new OtherQualification instance
            OtherQualification.objects.create(
                primary_table=primary_table_instance,
                any_other_course=any_other_course,
                course_name=course_name,
                specialization=specialization,
                university=university,
                duration_start=duration_start,
                duration_end=duration_end,
                course_type=course_type,
                grading_system=grading_system
                # Note: Add cgpa and percentage fields if needed
            )

        return JsonResponse({'status': 'success', 'message': 'Data submitted successfully!'})
    return render(request,'other_qualification.html')

def academic_x_grade(request):
    if request.method == 'POST':
        # Get the primary key (email) of the PrimaryTable from the session or another method
        primary_table_id = request.session.get('email')  # Assumed you're storing 'email' in the session
        
        # Check if primary_table_id exists in the session
        if not primary_table_id:
            return redirect('error_page')  # Redirect to an error page if primary_table_id is not found
        
        # Get the PrimaryTable instance by email
        try:
            primary_table_instance = PrimaryTable.objects.get(email=primary_table_id)
        except PrimaryTable.DoesNotExist:
            return redirect('error_page')  # Redirect to an error page if the PrimaryTable instance is not found
        
        # Extract form data
        course = request.POST.get('course')
        
        # If the form is for the 10th Grade (assuming `course == 'XthGrade'`)
        if course == 'XthGrade':
            roll_no = request.POST.get('roll_no')
            university = request.POST.get('university')
            board_of_education = request.POST.get('board_of_education')
            duration_start = request.POST.get('duration_start')
            duration_end = request.POST.get('duration_end')
            grading_system = request.POST.get('grading_system')
            
            print(roll_no,university)
            # Create a new XthDetails instance for 10th Grade
            XthDetails.objects.create(
                primary_table=primary_table_instance,
                roll_no=roll_no,
                university=university,
                board_of_education=board_of_education,
                duration_start=duration_start,
                duration_end=duration_end,
                grading_system=grading_system
            )
        
        # Handle other course types (if needed)
        # Example: Equivalent Diploma
        elif course == 'equivalentDiploma':
            roll_no = request.POST.get('roll_no')
            university = request.POST.get('university')
            duration_start = request.POST.get('duration_start')
            duration_end = request.POST.get('duration_end')
            grading_system = request.POST.get('grading_system')
            
            # Create a new XthDetails instance for Equivalent Diploma (no board_of_education)
            XthDetails.objects.create(
                primary_table=primary_table_instance,
                roll_no=roll_no,
                university=university,
                board_of_education='',  # Not applicable for Equivalent Diploma
                duration_start=duration_start,
                duration_end=duration_end,
                grading_system=grading_system
            )
        
        # After saving the form, redirect to the next page (or success page)
        return JsonResponse({'status': 'success', 'message': 'Data submitted successfully!'})

    return render(request,'academic_x_grade.html')

def work_exp(request):
    if request.method == "POST":
        # Get the primary key (email) of the PrimaryTable from the session or other method
        primary_table_id = request.session.get('email')  # Adjust according to session handling

        # Check if primary_table_id exists
        if not primary_table_id:
            return redirect('error_page')  # Redirect to an error page if primary_table_id is not found
        
        try:
            primary_table_instance = PrimaryTable.objects.get(email=primary_table_id)
        except PrimaryTable.DoesNotExist:
            return redirect('error_page')  # Redirect to an error page if PrimaryTable instance is not found

        # Extract form data for WorkExperience
        employer_name = request.POST.get('name')
        employment_type = request.POST.get('employee_type')
        duration_from = request.POST.get('duration_from')
        duration_to = request.POST.get('duration_to')
        designation = request.POST.get('designation')
        gross_salary = request.POST.get('annual_salary')

        # Create a new WorkExperience instance
        WorkExperience.objects.create(
            primary_table=primary_table_instance,
            name=employer_name,
            employee_type=employment_type,
            duration_from=duration_from,
            duration_to=duration_to,
            designation=designation,
            annual_salary=gross_salary
        )

         # Process the form data
        try:
            # Assume form validation and saving logic here
            return JsonResponse({"status": "success", "message": "Your data has been saved."})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)})
    return render(request,'work_exp.html')

def arrear(request):
    if request.method == "POST":
        primary_table_id = request.session.get('email')
        
        if not primary_table_id:
            return redirect('error_page')
        
        try:
            primary_table_instance = PrimaryTable.objects.get(email=primary_table_id)
        except PrimaryTable.DoesNotExist:
            return redirect('error_page')
        
        arrears = request.POST.get('relevant-course')
        arrear_count = request.POST.get('arrearcount')
        
        if arrears == 'no':
            arrear_count = None
        
        # ArrearDetails.objects.create(
        #     primary_table=primary_table_instance,
        #     arrears=arrears,
        #     arrear_count=arrear_count
        # )
        
        return JsonResponse({'status': 'success', 'message': 'Data submitted successfully!'})

    return render(request,'arrear.html')

def resume(request):
    primary_table_id = request.session.get('email')  # Get the primary key (email) of the PrimaryTable from the session

    # Check if primary_table_id exists
    if not primary_table_id:
        return redirect('error_page')  # Redirect to an error page if primary_table_id is not found

    try:
        primary_table_instance = PrimaryTable.objects.get(email=primary_table_id)
    except PrimaryTable.DoesNotExist:
        return redirect('error_page')  # Redirect if PrimaryTable instance is not found

    print(primary_table_instance)  # Check this in your console
    print(f"First Name: {primary_table_instance.firstname}, Last Name: {primary_table_instance.lastname}")


    if request.method == "POST":
        # Get form fields for name and blood group
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        blood_group = request.POST.get('blood_group')

        # Ensure that files are uploaded correctly
        photo = request.FILES.get('photo')
        cv = request.FILES.get('cv')

        if photo and cv:  # Check if both files are uploaded
            # Save the files in the respective directories (static/photos/ and static/cvs/)
            fs_photo = FileSystemStorage(location='static/photos/')
            photo_filename = fs_photo.save(photo.name, photo)

            fs_cv = FileSystemStorage(location='static/resumes/')
            cv_filename = fs_cv.save(cv.name, cv)

            # Save the form data in the PhotoCV model
            PhotoCV.objects.create(
                primary_table=primary_table_instance,
                name=f"{first_name} {last_name}",
                blood_group=blood_group,
                photo=photo_filename,
                cv=cv_filename
            )
            
            return redirect('preview')  # Redirect to a success page after saving the data
        else:
            # Handle the case where files were not uploaded
            return render(request, 'resume.html', {'error': 'Please upload both a photo and CV.'})
    
    return render(request, 'resume.html', {'primary_table': primary_table_instance})

def preview(request):

    users = PrimaryTable.objects.all()
    user_details = []

    for user in users:
        try:
            personal_details = PersonalDetails.objects.get(primary_table=user)
            academic_details = AcademicDetails.objects.filter(primary_table=user)
            course_details = CourseDetails.objects.filter(primary_table=user)
            xii_and_diploma = XIIAndDiploma.objects.filter(primary_table=user)
            xth_details = XthDetails.objects.filter(primary_table=user)
            other_qualifications = OtherQualification.objects.filter(primary_table=user)
            work_experience = WorkExperience.objects.filter(primary_table=user)
            arrear_details = ArrearDetails.objects.get(primary_table=user)
            other_details = OtherDetails.objects.get(primary_table=user)
            photo_cv = PhotoCV.objects.get(primary_table=user)

            user_details.append({
                'user': user,
                'personal_details': personal_details,
                'academic_details': academic_details,
                'course_details': course_details,
                'xii_and_diploma': xii_and_diploma,
                'xth_details': xth_details,
                'other_qualifications': other_qualifications,
                'work_experience': work_experience,
                'arrear_details': arrear_details,
                'other_details': other_details,
                'photo_cv': photo_cv,
            })
        except Exception as e:
            print(f"Error loading data for {user.email}: {e}")
    
    context = {
        'user_details': user_details
    }

    return render(request, 'preview.html', context)

def reg(request):

    if request.method == 'POST':
        name = request.POST.get('Name').capitalize()
        aadhaar = request.POST.get('aadhar')
        pan = request.POST.get('pan').upper()
        email = request.POST.get('email')
        print("kar")
        mailsend(email)

        return redirect('reg_otp')

    # If the request is GET or other type, render the form page
    return render(request, 'reg.html')

def reg_login(request):
    if request.method == 'POST':
        return redirect('payment')
    return render(request,'reg_login.html')

def reg_otp(request):
    if request.method=="POST":
        one_time_pass1 = request.POST.get('otp1')
        one_time_pass2 = request.POST.get('otp2')
        one_time_pass3 = request.POST.get('otp3')
        one_time_pass4 = request.POST.get('otp4')
        one_time_pass = one_time_pass1 + one_time_pass2 + one_time_pass3 + one_time_pass4
        if str(otp) == one_time_pass:
            return JsonResponse({'status': 'success', 'message': 'OTP verified successfully!'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Incorrect OTP. Please try again.'})
    return render(request,'reg_otp.html',{'otp': otp})

def payment(request):
    return render(request,'payment.html')

def college_preview(request):
    return render(request,'college_preview.html')

def student_preview(request):
    return render(request,'student_preview.html')
