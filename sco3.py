
users = {}
import random
import string
from datetime import datetime
import mysql.connector
import matplotlib.pyplot as plt  

def generate_captcha():
    characters = string.ascii_uppercase + string.digits
    captcha = ''.join(random.choices(characters, k=6))
    return captcha

def verify_captcha():
    while True:
        captcha_code = generate_captcha()
        print("\n=== VERIFICATION CHECK ===")
        print(f"Please enter this code: {captcha_code}")
        print("(Case sensitive)")
        
        attempts = 3
        while attempts > 0:
            user_input = input("Enter the code: ")
            if user_input == captcha_code:
                print("Verification successful!")
                return True
            else:
                attempts -= 1
                if attempts > 0:
                    print(f"Incorrect code. {attempts} attempts remaining.")
                else:
                    print("Verification failed. Please try again with a new code.")
                    break

def get_department():
    """Function to get user's department"""
    while True:
        print("\n=== SELECT DEPARTMENT ===")
        print("1. Technical (Degree)")
        print("2. Medical")
        print("3. Technical (Diploma)")
        dept_choice = input("Enter your department choice (1-3): ")
        if dept_choice == '1': return "Technical (Degree)"
        elif dept_choice == '2': return "Medical"
        elif dept_choice == '3': return "Technical (Diploma)"
        else: print("Invalid choice! Please try again.")

def get_board():
    """Function to get user's educational board"""
    while True:
        print("\n=== SELECT BOARD ===")
        print("1. Gujarat Board")
        print("2. CBSE")
        print("3. ICSE")
        board_choice = input("Enter your board choice (1-3): ")
        if board_choice == '1': return "Gujarat Board"
        elif board_choice == '2': return "CBSE"
        elif board_choice == '3': return "ICSE"
        else: print("Invalid choice! Please try again.")

def get_education_level():
    """Function to get user's education level"""
    while True:
        print("\n=== SELECT EDUCATION LEVEL ===")
        print("1. After 10th (SSC)")
        print("2. After 12th (HSC)")
        print("3. After Diploma")
        edu_choice = input("Enter your education level choice (1-3): ")
        if edu_choice == '1': return "After 10th (SSC)"
        elif edu_choice == '2': return "After 12th (HSC)"
        elif edu_choice == '3': return "After Diploma"
        else: print("Invalid choice! Please try again.")

def get_year(prompt, min_year=2000, max_year=2024):
    while True:
        try:
            year = int(input(prompt))
            if min_year <= year <= max_year:
                return year
            print(f"Please enter a valid year between {min_year} and {max_year}")
        except ValueError:
            print("Please enter a valid year!")

def get_seat_number():
    print("\n=== ENTER BOARD SEAT NUMBER ===")
    seat_number = input("Seat Number (as shown on your marksheet): ").upper()
    while not seat_number:
        print("Seat number cannot be empty!")
        seat_number = input("Seat Number: ").upper()
    return seat_number

def get_category():
    """Function to get user's category"""
    while True:
        print("\n=== SELECT CATEGORY ===")
        print("1. General")
        print("2. OBC")
        print("3. SC")
        print("4. ST")
        print("5. Open")
        category_choice = input("Enter your category choice (1-5): ")
        if category_choice == '1': return "General"
        elif category_choice == '2': return "OBC"
        elif category_choice == '3': return "SC"
        elif category_choice == '4': return "ST"
        elif category_choice == '5': return "Open"
        else: print("Invalid choice! Please try again.")

def get_address():
    print("\n=== ENTER ADDRESS DETAILS ===")
    address_line1 = input("Address Line 1 (House/Flat No., Street): ").strip()
    while not address_line1:
        print("Address Line 1 cannot be empty!")
        address_line1 = input("Address Line 1: ").strip()
    address_line2 = input("Address Line 2 (Area/Locality): ").strip()
    city = input("City: ").strip().title()
    while not city:
        print("City cannot be empty!")
        city = input("City: ").strip().title()
    state = input("State: ").strip().title()
    while not state:
        print("State cannot be empty!")
        state = input("State: ").strip().title()
    pincode = input("Pincode: ").strip()
    while not (pincode.isdigit() and len(pincode) == 6):
        print("Please enter a valid 6-digit pincode!")
        pincode = input("Pincode: ").strip()
    full_address = f"{address_line1}\n{address_line2}\n{city}, {state} - {pincode}"
    return full_address

def get_college_type():
    """Function to get college type"""
    while True:
        print("\n=== SELECT COLLEGE TYPE ===")
        print("1. Government")
        print("2. Private")
        type_choice = input("Enter college type (1-2): ")
        if type_choice == '1': return "Government"
        elif type_choice == '2': return "Private"
        else: print("Invalid choice! Please try again.")

def get_stream():
    """Function to get user's stream"""
    while True:
        print("\n=== SELECT STREAM ===")
        print("1. Science")
        print("2. General")
        stream_choice = input("Enter your stream choice (1-2): ")
        if stream_choice == '1': return "Science"
        elif stream_choice == '2': return "General"
        else: print("Invalid choice! Please try again.")

def validate_mobile(mobile):
    """Validate mobile number format"""
    mobile = mobile.replace(" ", "")
    return len(mobile) == 10 and mobile.isdigit()

def get_gender():
    """Function to get user's gender"""
    while True:
        print("\n=== SELECT GENDER ===")
        print("1. Male")
        print("2. Female")
        print("3. Other")
        gender_choice = input("Enter your choice (1-3): ")
        if gender_choice == '1': return "Male"
        elif gender_choice == '2': return "Female"
        elif gender_choice == '3': return "Other"
        else: print("Invalid choice! Please try again.")

def create_user_file(username, user_info):
    filename = f"{username}_details.txt"
    try:
        with open(filename, 'w') as file:
            file.write("=" * 50 + "\n")
            file.write(f"STUDENT DETAILS - {username.upper()}\n")
            file.write("=" * 50 + "\n\n")
            file.write("BASIC INFORMATION\n")
            file.write("-" * 20 + "\n")
            file.write(f"Mobile Number: {user_info.get('mobile', 'Not provided')}\n")
            file.write(f"Gender: {user_info.get('gender', 'Not provided')}\n")
            file.write(f"Stream: {user_info.get('stream', 'Not provided')}\n")
            file.write(f"Department: {user_info.get('department', 'Not provided')}\n")
            file.write(f"Education Level: {user_info.get('education_level', 'Not provided')}\n")
            file.write(f"Board: {user_info.get('board', 'Not provided')}\n")
            file.write(f"Seat Number: {user_info.get('seat_number', 'Not provided')}\n")
            file.write(f"Passing Year: {user_info.get('passing_year', 'Not provided')}\n")
            file.write(f"Admission Year: {user_info.get('admission_year', 'Not provided')}\n\n")
            if 'scholarship_status' in user_info:
                file.write("SCHOLARSHIP DETAILS\n")
                file.write("-" * 20 + "\n")
                file.write(f"Application Date: {user_info['scholarship_applied_date']}\n")
                file.write(f"College Name: {user_info['college_name']}\n")
                file.write(f"College Location: {user_info['college_location']}\n")
                file.write(f"College Type: {user_info['college_type']}\n")
                file.write(f"Annual Fees: Rs. {user_info['college_fees']:,.2f}\n")
                file.write(f"Category: {user_info['category']}\n\n")
                file.write("Personal Details:\n")
                file.write(f"Date of Birth: {user_info['date_of_birth']}\n")
                file.write(f"Aadhar Number: {user_info['aadhar_number']}\n\n")
                file.write("Family Information:\n")
                file.write(f"Father's Name: {user_info['father_name']}\n")
                file.write(f"Father's Occupation: {user_info['father_occupation']}\n")
                file.write(f"Mother's Name: {user_info['mother_name']}\n")
                file.write(f"Mother's Occupation: {user_info['mother_occupation']}\n")
                file.write(f"Family Income: Rs. {user_info['family_income']:,.2f}\n\n")
                file.write("Address:\n")
                file.write(f"{user_info['address']}\n\n")
                file.write("Academic & Application Status:\n")
                file.write(f"Academic Percentage: {user_info['academic_percentage']}%\n")
                file.write(f"Scholarship Status: {user_info['scholarship_status']}\n")
                if user_info['scholarship_status'] == 'Cancelled - Income Exceeds Limit':
                    file.write("\nNote: Application cancelled due to family income exceeding Rs. 1,50,000\n")
                elif user_info['scholarship_status'] == 'Cancelled - Low Academic Performance':
                    file.write("\nNote: Application cancelled due to academic percentage below 40%\n")
            file.write("\n" + "=" * 50 + "\n")
            file.write(f"File generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"\nDetailed information has been saved to {filename}")
        return True
    except Exception as e:
        print(f"Error creating file: {str(e)}")
        return False

def sign_up(db):
    print("\n=== SIGN UP ===")
    username = input("Create username: ")
    
    if username in users:
        print("Username already taken! Please try another one.")
        return
    
    password = input("Create password: ")
    
    admin_data = {
        'UserName': username,
        'Passward': password
    }
    
    if not db.add_admin(admin_data):
        print("Failed to create admin account in database!")
        return
    
    while True:
        mobile = input("\nEnter your mobile number (10 digits): ")
        if validate_mobile(mobile):
            break
        print("Invalid mobile number! Please enter a valid 10-digit ")
    
    gender = get_gender()
    stream = get_stream()
    department = get_department()
    education_level = get_education_level()
    board = get_board()
    seat_number = get_seat_number()
    
    
    passing_year = get_year("\nEnter your passing year (e.g., 2023): ")
    while True:
        admission_year = get_year("\nEnter your admission year (e.g., 2024): ", min_year=passing_year)
        if admission_year >= passing_year:
            break
        print("Admission year must be after passing year!")
    
    if not verify_captcha():
        print("Registration cancelled due to failed verification.")
        return
    
    users[username] = {
        'password': password,
        'mobile': mobile,
        'gender': gender,
        'stream': stream,
        'department': department,
        'education_level': education_level,
        'board': board,
        'seat_number': seat_number,
        'passing_year': passing_year,
        'admission_year': admission_year
    }
    
    student_data = {
        'Student_name': username,
        'Department': department,
        'board': board,
        'Category': 'General',
        'College_type': 'Government',
        'Stream': stream
    }
    
    if not db.add_student(student_data):
        print("Failed to add student to database!")
        return

  
    create_user_file(username, users[username])

def validate_aadhar(aadhar):
    aadhar = aadhar.replace(" ", "")
    return len(aadhar) == 12 and aadhar.isdigit()

def get_date_of_birth():
    while True:
        try:
            print("\nEnter your date of birth:")
            day = int(input("Day : "))
            month = int(input("Month : "))
            year = int(input("Year :"))
            if not (1 <= day <= 31 and 1 <= month <= 12 and 1990 <= year <= 2010):
                print("Please enter a valid date within reasonable range")
                continue
            return f"{year}-{month:02d}-{day:02d}"
        except ValueError:
            print("Please enter valid numbers!")

def apply_scholarship(username, db):
    print("\n=== SCHOLARSHIP APPLICATION ===")
    
    if 'scholarship_status' in users[username]:
        print(f"You have already applied for scholarship!")
        print(f"Current status: {users[username]['scholarship_status']}")
        return
    
    college_name = input("\nCollege Name: ").strip().title()
    while not college_name:
        print("College name cannot be empty!")
        college_name = input("College Name: ").strip().title()
    
    college_location = input("College Location (City, State): ").strip().title()
    while not college_location:
        print("College location cannot be empty!")
        college_location = input("College Location (City, State): ").strip().title()
    
    college_type = get_college_type()
    while True:
        try:
            college_fees = float(input("\nCollege Annual Fees (in Rs.): "))
            if college_fees > 0:
                break
            print("Please enter a valid amount greater than 0")
        except ValueError:
            print("Please enter a valid number!")
    
    category = get_category()
    address = get_address()
    father_name = input("\nFather's Name: ").title()
    while not father_name:
        print("Father's name cannot be empty!")
        father_name = input("Father's Name: ").title()
    
    father_occupation = input("Father's Occupation: ").strip().title()
    while not father_occupation:
        print("Father's occupation cannot be empty!")
        father_occupation = input("Father's Occupation: ").strip().title()
    
    mother_name = input("\nMother's Name: ").title()
    while not mother_name:
        print("Mother's name cannot be empty!")
        mother_name = input("Mother's Name: ").title()
    
    mother_occupation = input("Mother's Occupation: ").strip().title()
    while not mother_occupation:
        print("Mother's occupation cannot be empty!")
        mother_occupation = input("Mother's Occupation: ").strip().title()
    
    dob = get_date_of_birth()
    while True:
        aadhar = input("\nAadhar Card Number (12 digits): ")
        if validate_aadhar(aadhar):
            break
        print("Invalid Aadhar number! Please enter 12 digits only.")
    
    while True:
        try:
            percentage = float(input("\nPrevious Year Academic Percentage: "))
            if 0 <= percentage <= 100:
                break
            print("Please enter a valid percentage between 0 and 100")
        except ValueError:
            print("Please enter a valid number!")
    
    while True:
        try:
            income = float(input("\nAnnual Family Income (in Rs.): "))
            if income >= 0:
                break
            print("Please enter a valid income (must be 0 or greater)")
        except ValueError:
            print("Please enter a valid number!")
    
    status = 'Pending Review'
    if percentage < 40:
        status = 'Cancelled - Low Academic Performance'
        print("\n=== Application Status ===")
        print("Your scholarship application has been cancelled.")
        print("Reason: Academic percentage below minimum requirement of 40%")
    elif income > 150000:
        status = 'Cancelled - Income Exceeds Limit'
        print("\n=== Application Status ===")
        print("Your scholarship application has been cancelled.")
        print("Reason: Family income exceeds the maximum limit of Rs. 1,50,000")
    
    users[username].update({
        'scholarship_applied_date': str(datetime.now().date()),
        'college_name': college_name,
        'college_location': college_location,
        'college_type': college_type,
        'college_fees': college_fees,
        'category': category,
        'address': address,
        'father_name': father_name,
        'father_occupation': father_occupation,
        'mother_name': mother_name,
        'mother_occupation': mother_occupation,
        'date_of_birth': dob,
        'aadhar_number': aadhar,
        'academic_percentage': percentage,
        'family_income': income,
        'scholarship_status': status
    })
    
    scholarship_details = {
        'Name': username,
        'Amount': college_fees,
        'Eligibility': 'Eligible' if status == 'Pending Review' else 'Not Eligible',
        'ApplyDate': datetime.now().date(),
        'Year': users[username]['admission_year']
    }
    db.add_student_details(scholarship_details)
    
    updates = {
        'Collage_type': college_type,
        'Category': category
    }
    
    if status == 'Pending Review':
        print("\n=== Application Submitted Successfully ===")
        print("Your application will be reviewed shortly.")
    print("You can check your application status in the Student Status section.")
    
    create_user_file(username, users[username])

def view_student_status(username, db):
    """Function to view student status and details from database"""
    user_info = users[username]
    
    print("\nWould you like to generate/update your detailed information file?")
    choice = input("Enter 'Y' for Yes, any other key to skip: ")
    if choice.upper() == 'Y':
        create_user_file(username, users[username])

def user_menu(username, db):
    """Function to handle user menu after login"""
    while True:
        print("\n=== STUDENT MENU ===")
        print("1. Apply for Scholarship")
        print("2. View Student Status")
        print("3. Logout")
        choice = input("Enter your choice (1-3): ")
        if choice == '1': apply_scholarship(username, db)
        elif choice == '2': view_student_status(username, db)
        elif choice == '3':
            print("Logging out... Goodbye!")
            break
        else: print("Invalid choice! Please try again.")

def login(db):
    """Function to handle user login"""
    print("\n=== LOGIN ===")
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    if username in users and users[username]['password'] == password:
        print("\nLogin successful!")
        print(f"Welcome back, {username}!")
        user_menu(username, db)
    else:
        print("Invalid username or password!")

def plot_scholarship_statuses():
    """Function to plot scholarship status distribution"""
    if not users:
        print("No data available to plot.")
        return
    
    status_counts = {
        'Pending Review': 0,
        'Cancelled - Low Academic Performance': 0,
        'Cancelled - Income Exceeds Limit': 0,
        'Not Applied': 0
    }
    
    for user_info in users.values():
        status = user_info.get('scholarship_status', 'Not Applied')
        status_counts[status] = status_counts.get(status, 0) + 1
    
    statuses = list(status_counts.keys())
    counts = list(status_counts.values())
    
    plt.figure(figsize=(10, 6))
    plt.bar(statuses, counts, color=['#4CAF50', '#FF5733', '#C70039', '#3498DB'])
    plt.xlabel('Scholarship Status')
    plt.ylabel('Number of Students')
    plt.title('Distribution of Scholarship Application Statuses')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    
    plt.show()

def main():
    """Main function to run the program"""
    db = DatabaseConnection()
    while True:
        print("\n=== MAIN MENU ===")
        print("1. Sign Up")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")
        if choice == '1': sign_up(db)
        elif choice == '2': login(db)
        elif choice == '3':
            print("Thank you for using our system. Goodbye!")
            db.close()
            plot_scholarship_statuses()  
            break
        else: print("Invalid choice! Please try again.")






class DatabaseConnection:
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="scoler"
            )
            self.cursor = self.connection.cursor(dictionary=True)
            print(" Connected to database successfully!")
        except mysql.connector.Error as err:
            print(f"Database Connection Error: {err}")
            exit(1)

    def add_admin(self, admin_data):
        try:
            if self.username_exists(admin_data['UserName']):
                print(f"Error: Username '{admin_data['UserName']}' already exists!")
                return False
            query = "INSERT INTO admin (UserName, Passward) VALUES (%s, %s)"
            values = (admin_data['UserName'], admin_data['Passward'])
            self.cursor.execute(query, values)
            self.connection.commit()
            print("Admin added successfully!")
            return True
        except mysql.connector.Error as err:
            print(f"Error adding admin: {err}")
            return False

    def add_student(self, student_data):
        try:
            query = "INSERT INTO student (Student_name, Department, Borad, Category, Collage_type, Stream) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (
                student_data['Student_name'],
                student_data['Department'],
                student_data['board'],
                student_data['Category'],
                student_data['College_type'],
                student_data['Stream']
            )
            self.cursor.execute(query, values)
            self.connection.commit()
            print("Student added successfully!")
            return True
        except mysql.connector.Error as err:
            print(f"Error adding student: {err}")
            return False

    def add_student_details(self, details):
        try:
            query = "INSERT INTO student_details (Name, Amount, Eligibility, ApplyDate, Year) VALUES (%s, %s, %s, %s, %s)"
            values = (details['Name'], details['Amount'], details['Eligibility'], details['ApplyDate'], details['Year'])
            self.cursor.execute(query, values)
            self.connection.commit()
            print("Student details added successfully!")
            return True
        except mysql.connector.Error as err:
            print(f"Error adding student details: {err}")
            return False

    def username_exists(self, username):
        try:
            query = "SELECT COUNT(*) as count FROM admin WHERE UserName = %s"
            self.cursor.execute(query, (username,))
            result = self.cursor.fetchone()
            return result['count'] > 0
        except mysql.connector.Error as err:
            print(f"Error checking username: {err}")
            return False

    def verify_admin(self, username, password):
        try:
            query = "SELECT * FROM admin WHERE UserName = %s AND Passward = %s"
            self.cursor.execute(query, (username, password))
            result = self.cursor.fetchone()
            return result is not None
        except mysql.connector.Error as err:
            print(f"Error verifying admin: {err}")
            return False

    def _clear_unread_results(self):
        """Clear any unread results from the cursor"""
        while self.connection.unread_result:
            self.cursor.fetchall()  

    def close(self):
        """Close database connection safely"""
        try:
            self._clear_unread_results()  
            self.cursor.close()
            self.connection.close()
            print("Database connection closed.")
        except mysql.connector.Error as err:
            print(f"Error closing database connection: {err}")

def login(db):
    print("\n=== LOGIN ===")
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    if db.verify_admin(username, password):
        print("\nLogin successful!")
        print(f"Welcome back, {username}!")
        user_menu(username, db)
    else:
        print("Invalid username or password!")

def main():
    db = DatabaseConnection()
    while True:
        print("\n=== MAIN MENU ===")
        print("1. Sign Up")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")
        if choice == '1':
            sign_up(db)
        elif choice == '2':
            login(db)
        elif choice == '3':
            print("Thank you for using our system. Goodbye!")
            db.close()
            plot_scholarship_statuses()
            break
        else:
            print("Invalid choice! Please try again.")






if __name__ == "__main__":
    main()