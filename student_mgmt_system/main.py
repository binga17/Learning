#runs Command-Line Interface and ties everything together

from modules.database import get_connection, initialize_db
from modules.student import add_student, view_students, update_student, delete_student

def menu():
    #displays the main menu and handles user input
    conn, cur = get_connection()
    
    while True:
        print("\n STUDENT MANAGEMENT SYSTEM")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update GPA")
        print("4. Delete Student")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter name: ").strip()
            age = int(input("Enter age: "))
            gpa = float(input("Enter GPA: "))
            add_student(cur, conn, name, age, gpa)
            
        elif choice == '2':
            view_students(cur)
            
        elif choice == '3':
            name = input("Enter name to update: ").strip()
            new_gpa = float(input("Enter new GPA: "))
            update_student(cur, conn, name, new_gpa)
        
        elif choice == '4':
            name = input("Enter name to delete: ").strip()
            delete_student(cur, conn,name)
            
        elif choice == '5':
            print("Exiting the system. Goodboye!")
            break
        
        else:
            print("Invalid option. Please try again")
            
    conn.close()
    
if __name__ == "__main__":
    initialize_db()
    menu()
    
                        