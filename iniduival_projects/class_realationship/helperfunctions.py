# ============================================================
# helper.py
# Contains everything the gradebook needs:
#   - Student class
#   - GradeBook class (with CSV save/load)
#   - UI helper functions  (headers, pause, input validation)
#   - Menu action functions (one per menu option)
#
# main.py imports from here and only runs the loop.
# ============================================================

import csv
import os

CSV_FILE = "gradebook.csv"   # Single source-of-truth filename


# ══════════════════════════════════════════════════════════
# STUDENT CLASS
# Represents one student and all grade-related logic
# ══════════════════════════════════════════════════════════
class Student:
    def __init__(self, name, student_id):
        """
        Create a Student.
        Attributes:
            name (str)       : Full name
            student_id (str) : Unique ID (primary key in the CSV)
            grades (list)    : Float grades in the range [0, 100]
        """
        self.name       = name
        self.student_id = student_id
        self.grades     = []          # Populated via add_grade()

    # ── Grade helpers ──────────────────────────────────────

    def add_grade(self, grade):
        """Append one validated grade (float 0-100) to this student."""
        self.grades.append(grade)

    def calculate_average(self):
        """
        Return the mean of all grades as a float.
        Returns None when the grade list is empty.
        """
        if not self.grades:
            return None
        return sum(self.grades) / len(self.grades)

    def get_letter_grade(self):
        """
        Map the numerical average to a letter grade.
        A=90+, B=80-89, C=70-79, D=60-69, F=<60
        Returns 'N/A' when there are no grades yet.
        """
        avg = self.calculate_average()
        if avg is None:
            return "N/A"
        if avg >= 90:   return "A"
        elif avg >= 80: return "B"
        elif avg >= 70: return "C"
        elif avg >= 60: return "D"
        else:           return "F"

    # ── Display ────────────────────────────────────────────

    def display_info(self):
        """Print a formatted record card for this one student."""
        avg        = self.calculate_average()
        avg_str    = f"{avg:.2f}" if avg is not None else "N/A"
        letter     = self.get_letter_grade()
        grade_disp = self.grades if self.grades else ["None yet"]

        print(f"   {'Name':<12}: {self.name}")
        print(f"   {'ID':<12}: {self.student_id}")
        print(f"   {'Grades':<12}: {grade_disp}")
        print(f"   {'Average':<12}: {avg_str}")
        print(f"   {'Letter':<12}: {letter}")

    # ── CSV serialisation ──────────────────────────────────

    def to_csv_row(self):
        """
        Return this student as a single CSV row (list of strings).
        Format: name, student_id, grade1, grade2, ...
        Grades are spread across extra columns so one student = one row.
        """
        return [self.name, self.student_id] + [str(g) for g in self.grades]

    @classmethod
    def from_csv_row(cls, row):
        """
        Reconstruct a Student from one CSV row (list of strings).
        Expects: [name, student_id, grade1, grade2, ...]
        Silently skips any value that cannot be converted to float.
        """
        student = cls(row[0], row[1])
        for value in row[2:]:
            try:
                student.grades.append(float(value))
            except ValueError:
                pass   # Ignore blank or corrupted grade cells
        return student



# GRADEBOOK CLASS
# Manages the roster; owns all CSV read/write operations.
# Composed of Student objects (composition pattern).

class GradeBook:
    def __init__(self):
        """Start with an empty roster. Call load_from_csv() to restore data."""
        self.students = []

    # ── Roster management ──────────────────────────────────

    def add_student(self, name, student_id):
        """
        Add a new Student to the roster.
        Returns False on duplicate ID, True on success.
        """
        if self.find_by_id(student_id):
            return False
        self.students.append(Student(name, student_id))
        return True

    def find_by_id(self, student_id):
        """Return the Student whose ID matches, or None."""
        for s in self.students:
            if s.student_id == student_id:
                return s
        return None

    def find_by_name(self, name):
        """Return the Student whose name matches (case-insensitive), or None."""
        for s in self.students:
            if s.name.lower() == name.lower():
                return s
        return None

    # ── Statistics ─────────────────────────────────────────

    def get_class_average(self):
        """
        Compute the overall average across every grade in the gradebook.
        Returns None when no grades have been entered anywhere.
        """
        all_grades = [g for s in self.students for g in s.grades]
        if not all_grades:
            return None
        return sum(all_grades) / len(all_grades)

    @staticmethod
    def letter_from_avg(avg):
   
        #Static helper: convert any float average to a letter grade string.
        #Used for the class-wide average in the summary screen.
      
        if avg is None:     return "N/A"
        if avg >= 90:       return "A"
        elif avg >= 80:     return "B"
        elif avg >= 70:     return "C"
        elif avg >= 60:     return "D"
        else:               return "F"

    # ── CSV persistence ────────────────────────────────────

    def save_to_csv(self):
   
        #Write every student and their grades to CSV_FILE.

        #CSV layout (one student per row):
            #name, student_id, grade1, grade2, ...

        #Overwrites the file completely so it always mirrors memory.
        #Returns (True, success_message) or (False, error_message).
       
        try:
            with open(CSV_FILE, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["name", "student_id", "grades..."])  # header
                for student in self.students:
                    writer.writerow(student.to_csv_row())
            return True, f"Saved {len(self.students)} student(s) to '{CSV_FILE}'."
        except IOError as e:
            return False, f"Could not save file: {e}"

    def load_from_csv(self):
        """
        Read students and their grades from CSV_FILE.

        - Skips the header row automatically.
        - Skips rows with missing name or ID.
        - Skips rows whose ID is already in the roster (no duplicates).

        Returns (True, success_message) or (False, error_message).
        """
        if not os.path.exists(CSV_FILE):
            return False, f"No file named '{CSV_FILE}' found."

        try:
            loaded = skipped = 0
            with open(CSV_FILE, "r", newline="") as f:
                reader = csv.reader(f)
                next(reader, None)          # skip header
                for row in reader:
                    if len(row) < 2 or not row[0].strip() or not row[1].strip():
                        skipped += 1
                        continue
                    if self.find_by_id(row[1]):   # duplicate guard
                        skipped += 1
                        continue
                    self.students.append(Student.from_csv_row(row))
                    loaded += 1

            msg = f"Loaded {loaded} student(s) from '{CSV_FILE}'."
            if skipped:
                msg += f" ({skipped} row(s) skipped — duplicate or incomplete.)"
            return True, msg
        except IOError as e:
            return False, f"Could not read file: {e}"


# ══════════════════════════════════════════════════════════
# UI HELPER FUNCTIONS
# Small utilities shared across menu action functions
# ══════════════════════════════════════════════════════════

def print_header(title):
    print(f"  {title}")
 
def pause():
    """Hold the screen until the user presses Enter."""
    input("\n  Press Enter to continue...")

def print_main_menu():
    """Render the main menu with all seven options."""
    print_header("SIMPLE GRADE BOOK ")
    print("  Welcome to the Class Grade Book!\n")
    print(" MAIN MENU:")
    print("     [1]  Add New Student")
    print("     [2]  Add Grade to Student")
    print("     [3]  View Student Record")
    print("     [4]  View All Students")
    print("     [5]  Class Summary")
    print("     [6]  Save  /  Load")
    print("     [7]  Exit")

def get_valid_choice():
    """
    Keep prompting until the user enters a digit 1–7.
    Core input-validation loop for menu navigation.
    """
    while True:
        choice = input("\n  Enter your choice (1-7): ").strip()
        if choice in ("1", "2", "3", "4", "5", "6", "7"):
            return choice
        print(" Invalid choice — please enter a number between 1 and 7.")

def get_valid_grade():
    """
    Prompt until the user enters a float in [0, 100].
    Handles non-numeric input with a helpful error message.
    """
    while True:
        raw = input("  Enter grade (0-100): ").strip()
        try:
            grade = float(raw)
            if 0 <= grade <= 100:
                return grade
            print("  Grade must be between 0 and 100.")
        except ValueError:
            print("  Please enter a valid number (e.g. 85 or 91.5).")


# ══════════════════════════════════════════════════════════
# MENU ACTION FUNCTIONS
# One function per menu option — each receives the gradebook
# ══════════════════════════════════════════════════════════

def menu_add_student(gradebook):
    """
    Option 1 — Collect name and ID, then add a new Student.
    Rejects empty fields and duplicate IDs.
    """
    print_header("ADD NEW STUDENT")

    name = input("  Enter student name : ").strip()
    if not name:
        print("  Name cannot be empty.")
        pause()
        return

    student_id = input("  Enter student ID   : ").strip()
    if not student_id:
        print("  Student ID cannot be empty.")
        pause()
        return

    if gradebook.add_student(name, student_id):
        print("\nStudent added successfully!")
        gradebook.find_by_id(student_id).display_info()
    else:
        print(f" ID '{student_id}' is already in the gradebook.")

    pause()


def menu_add_grade(gradebook):
    """
    Option 2 — Look up a student by ID and append a validated grade.
    Lists the current roster first so the user can see available IDs.
    """
    print_header(" ADD GRADE")

    if not gradebook.students:
        print("    No students yet — add a student first (option 1).")
        pause()
        return

    print("  Current Students:")
    for s in gradebook.students:
        print(f"     • {s.name} (ID: {s.student_id})")

    student_id = input("\n  Enter student ID: ").strip()
    student    = gradebook.find_by_id(student_id)

    if not student:
        print(f"  No student found with ID '{student_id}'.")
        pause()
        return

    grade  = get_valid_grade()
    student.add_grade(grade)

    avg    = student.calculate_average()
    letter = student.get_letter_grade()

    print(f"\nGrade added!")
    print(f"     {student.name} now has {len(student.grades)} grade(s).")
    print(f"     Current average : {avg:.2f} ({letter})")
    pause()


def menu_view_student(gradebook):
    """
    Option 3 — Display the full record for one student.
    Accepts either a student ID or a name as the search term.
    """
    print_header("  VIEW STUDENT RECORD  ")

    if not gradebook.students:
        print("    No students in the gradebook yet.")
        pause()
        return

    search  = input("  Enter student ID or name: ").strip()
    student = gradebook.find_by_id(search) or gradebook.find_by_name(search)

    if not student:
        print(f"  ❌  No student found matching '{search}'.")
        pause()
        return

    print(f"\n  ── Record for {student.name} ──")
    student.display_info()
    pause()


def menu_view_all(gradebook):
    """
    Option 4 — Render a formatted table of every student
    with their ID, name, average, and letter grade.
    """
    print_header("👥  ALL STUDENTS  👥")

    if not gradebook.students:
        print("  No students in the gradebook yet.")
        pause()
        return

    top    = "  ┌─────────┬──────────────────────┬────────┬───────┐"
    mid    = "  ├─────────┼──────────────────────┼────────┼───────┤"
    bottom = "  └─────────┴──────────────────────┴────────┴───────┘"
    header = "  │ {:<7} │ {:<20} │ {:<6} │ {:<5} │".format(
                 "ID", "Name", "Avg", "Grade")

    print(top)
    print(header)
    print(mid)

    for s in gradebook.students:
        avg    = s.calculate_average()
        avg_s  = f"{avg:.1f}" if avg is not None else "N/A"
        letter = s.get_letter_grade()
        print("  │ {:<7} │ {:<20} │ {:<6} │ {:<5} │".format(
            s.student_id, s.name[:20], avg_s, letter))

    print(bottom)
    print(f"\n  Total Students: {len(gradebook.students)}")
    pause()


def menu_class_summary(gradebook):
    """
    Option 5 — Print every student's name, grades, and individual average,
    then show the overall class average computed from all recorded grades.
    """
    print_header(" CLASS SUMMARY")

    if not gradebook.students:
        print("   No students in the gradebook yet.")
        pause()
        return

    print(f"  {'Student':<22} {'ID':<10} {'Grades':<30} {'Avg':>6}  {'Ltr':>3}")
    print("  " + "─" * 74)

    for s in gradebook.students:
        avg    = s.calculate_average()
        avg_s  = f"{avg:.2f}" if avg is not None else "N/A"
        letter = s.get_letter_grade()
        g_disp = str(s.grades) if s.grades else "None yet"
        if len(g_disp) > 28:
            g_disp = g_disp[:25] + "..."
        print(f"  {s.name:<22} {s.student_id:<10} {g_disp:<30} {avg_s:>6}  {letter:>3}")

    print("  " + "─" * 74)
    class_avg = gradebook.get_class_average()
    if class_avg is not None:
        cl = GradeBook.letter_from_avg(class_avg)
        print(f"\n  📌  Overall Class Average : {class_avg:.2f} ({cl})")
    else:
        print("\n  Overall Class Average : N/A (no grades entered yet)")

    print(f"  📌  Total Students        : {len(gradebook.students)}")
    pause()


def menu_save_load(gradebook):
    """
    Option 6 — Sub-menu to save the current gradebook to CSV
    or load a previously saved CSV into the current session.

    Save  : Writes all students + grades, overwrites the file.
    Load  : Appends new students from the file (skips duplicates).
    """
    print_header("SAVE / LOAD")
    print("  [1]  Save gradebook to CSV")
    print("  [2]  Load gradebook from CSV")
    print("  [3]  Back to main menu")

    while True:
        sub = input("\n  Enter your choice (1-3): ").strip()
        if sub in ("1", "2", "3"):
            break
        print("Please enter 1, 2, or 3.")

    if sub == "1":

        if not gradebook.students:
            print(" Nothing to save — gradebook is empty.")
        else:
            ok, msg = gradebook.save_to_csv()
            print(f"\n  { if ok else}  {msg}")

    elif sub == "2":
        # Warn the user if data already exists in the session
        if gradebook.students:
            confirm = input(
                f"\n Roster already has {len(gradebook.students)} student(s).\n"
                "  Loading will ADD records from the CSV (duplicates skipped).\n"
                "  Continue? (y/n): "
            ).strip().lower()
            if confirm != "y":
                print("  Load cancelled.")
                pause()
                return

        ok, msg = gradebook.load_from_csv()
        print(f"\n  { if ok else}  {msg}")

    # sub == "3" — fall through back to main menu
    pause()

