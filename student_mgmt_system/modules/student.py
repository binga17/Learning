#handles all CRUD

def add_student(cur, conn, name, age, gpa):
    cur.execute("INSERT INTO students (name, age, gpa) VALUES (?, ?, ?)", (name, age, gpa))
    conn.commit()
    print(f"Student '{name}' added successfully!")

def view_students(cur):
    #displays all the students from the database
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()
    
    if not rows:
        print("No student records found")
        return
    
    print("\n STUDENT LIST:")
    print("-" * 40)
    for r in rows:
        print(f"ID: {r[0]} | Name: {r[1]} | Age: {r[2]} | GPA: {r[3]}")
    print("_" * 40)
    
def update_student(cur, conn, name, new_gpa):
        #updates a student's GPA
        cur.execute("UPDATE students SET gpa = ? WHERE name = ?", (new_gpa, name))
        if cur.rowcount == 0:
            print(f"No student found with name '{name}'.")
        else:
            conn.commit()
            print(f"GPA updated for '{name}' to {new_gpa}.")
def delete_student(cur, conn, name):
    #deletes a student by name
    cur.execute ("DELETE FROM students WHERE name = ?", (name, ))
    if cur.rowcount == 0:
        print(f"No student found with name '{name}'.")
    else:
        conn.commit()
        print(f"Student '{name}' deleted successfully!")
        