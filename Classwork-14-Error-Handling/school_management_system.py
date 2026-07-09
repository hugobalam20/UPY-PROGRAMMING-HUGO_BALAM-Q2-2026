# ==========================================
# INPUT
# ==========================================
users = {
    'jperez': {'password': '1234', 'rol': 'student', 'name': 'Juan Pérez'},
    'dromo': {'password': '1234', 'rol': 'student', 'name': 'Daniela Romo'},
    'mjuarez': {'password': '1234', 'rol': 'student', 'name': 'Mauricio Juárez'},
    'mlopez': {'password': '1234', 'rol': 'student', 'name': 'María López'},
    'euc': {'password': '1234', 'rol': 'student', 'name': 'Ernesto Uc'},
    'cbalam': {'password': '1234', 'rol': 'student', 'name': 'Carlos Balam'},
    'jpedrozo': {'password': '1234', 'rol': 'professor', 'name': 'Jorge Pedrozo'},
    'dgamboa': {'password': '1234', 'rol': 'coordinator', 'name': 'Didier Gamboa'}
}

subjects = (
    "Discrete Mathematics",
    "Programming",
    "English II",
    "Differential Calculus",
    "Probability and Statistics",
    "Computer and Server Architecture",
    "Socio-Emotional Skills and Conflict Management"
)

notes = {
    'jperez': {'Discrete Mathematics': 8.5, 'Programming': 9.2, 'English II': 9.0, 'Differential Calculus': 7.8, 'Probability and Statistics': 8.3, 'Computer and Server Architecture': 6.8, 'Socio-Emotional Skills and Conflict Management': 9.5},
    'dromo': {'Discrete Mathematics': 9.0, 'Programming': 6.7, 'English II': 9.4, 'Differential Calculus': 6.2, 'Probability and Statistics': 9.1, 'Computer and Server Architecture': 6.5, 'Socio-Emotional Skills and Conflict Management': 9.8},
    'mjuarez': {'Discrete Mathematics': 7.5, 'Programming': 8.0, 'English II': 8.5, 'Differential Calculus': 7.0, 'Probability and Statistics': 7.8, 'Computer and Server Architecture': 6.2, 'Socio-Emotional Skills and Conflict Management': 8.9},
    'mlopez': {'Discrete Mathematics': 9.5, 'Programming': 9.8, 'English II': 9.2, 'Differential Calculus': 9.0, 'Probability and Statistics': 9.6, 'Computer and Server Architecture': 9.4, 'Socio-Emotional Skills and Conflict Management': 10.0},
    'euc': {'Discrete Mathematics': 8.2, 'Programming': 6.9, 'English II': 8.8, 'Differential Calculus': 6.0, 'Probability and Statistics': 6.4, 'Computer and Server Architecture': 8.1, 'Socio-Emotional Skills and Conflict Management': 9.0},
    'cbalam': {'Discrete Mathematics': 8.8, 'Programming': 9.0, 'English II': 8.5, 'Differential Calculus': 6.6, 'Probability and Statistics': 8.9, 'Computer and Server Architecture': 8.7, 'Socio-Emotional Skills and Conflict Management': 9.2}
}

program_active = True
while program_active:
    current_user = ""
    current_role = ""
    current_name = ""
    authenticated = False
    
    print("\n" + "="*55)
    print("         SCHOOL MANAGEMENT SYSTEM LOGIN")
    print("="*55)
    print("(Type 'shutdown' in username to turn off the program)")
    
    while not authenticated:
        try:
            username_input = input("Username: ").strip()
            if username_input.lower() == 'shutdown':
                print("\nShutting down the system. Goodbye!")
                authenticated = True
                program_active = False
                break
                
            password_input = input("Password: ").strip()
            
            if username_input in users and users[username_input]['password'] == password_input:
                current_user = username_input
                current_role = users[username_input]['rol']
                current_name = users[username_input]['name']
                print(f"\n[OK] Welcome, {current_name} ({current_role})\n")
                authenticated = True
            else:
                raise ValueError("Incorrect username or password. Try again.\n")
        except ValueError as login_err:
            print(f"[X] {login_err}")

    if not program_active:
        break

# ==========================================
# PROCESS & OUTPUT
# ==========================================
    try:
        if current_role == 'student':
            print(f"--- REPORT CARD: {current_name} ---")
            aprobadas = set()
            for subject in subjects:
                grade = notes[current_user][subject]
                print(f" * {subject}: {grade}")
                if grade >= 7.0:
                    aprobadas.add(subject)
            all_subjects = set(subjects)
            pendientes = all_subjects - aprobadas
            print(f"\nPassed subjects (aprobadas): {aprobadas}")
            print(f"Pending subjects (pendientes): {pendientes}")
            input("\nPress Enter to log out and return to Login...")

        elif current_role == 'professor':
            print("--- List of Registered Students ---")
            for usr, info in users.items():
                if info['rol'] == 'student':
                    print(f"Username: {usr} | Name: {info['name']}")
            
            menu_professor_active = True
            while menu_professor_active:
                print("\n--- Grade Modification Menu ---")
                print("(Type 'logout' in student username to close professor session)")
                student_selec = input("Student (username): ").strip()
                
                if student_selec.lower() == 'logout':
                    print("Logging out from professor session...")
                    menu_professor_active = False
                elif student_selec in users and users[student_selec]['rol'] == 'student':
                    print("\nAvailable subjects to grade:")
                    for s in subjects:
                        print(f" * {s}")
                    subject_selec = input("\nSelect Subject: ").strip()
                    
                    if subject_selec in subjects:
                        grade_confirmed = False
                        while not grade_confirmed:
                            try:
                                new_grade_input = input("New Grade: ").strip()
                                new_grade = float(new_grade_input)
                                
                                if new_grade < 0.0 or new_grade > 10.0:
                                    raise ValueError("Grade must be between 0.0 and 10.0.")
                                    
                                print(f"Are you sure you want to change {subject_selec} grade to {new_grade}? (s/n): ", end="")
                                confirmation = input().strip().lower()
                                
                                if confirmation == 's':
                                    notes[student_selec][subject_selec] = new_grade
                                    print("\nGrade updated successfully!")
                                    student_name = users[student_selec]['name']
                                    print(f"\n--- Updated Report Card for {student_name} ({student_selec}) ---")
                                    for s in subjects:
                                        print(f" * {s}: {notes[student_selec][s]}")
                                    grade_confirmed = True
                                else:
                                    print("\n[Correction] Re-entering the grade for the same student and subject...\n")
                            except ValueError as num_err:
                                print(f"[Error] Invalid numeric grade entry: {num_err}. Try again.")
                    else:
                        print("[Error] The entered subject is not valid. Try again.")
                else:
                    print("[Error] User does not exist or is not a student. Try again.")

        elif current_role == 'coordinator':
            print("=======================================")
            print("        GLOBAL REPORT (READ-ONLY)")
            print("=======================================\n")
            print("1. LIST OF PROFESSORS:")
            for usr, info in users.items():
                if info['rol'] == 'professor':
                    print(f" * {info['name']}")
            print("\n2. LIST OF SUBJECTS:")
            for subject in subjects:
                print(f" * {subject}")
            print("\n3. STUDENT GRADES REPORT:")
            for student, subj_notes in notes.items():
                student_name = users[student]['name']
                print(f"\nStudent: {student_name} ({student})")
                for s in subjects:
                    print(f" * {s}: {subj_notes[s]}")
            print("\n" + "="*55)
            input("Press Enter to log out and return to Login...")
        else:
            print(" [X] Role not recognized in the system.")
            
    except KeyError as key_err:
        print(f"System Error: Missing reference value {key_err}")
