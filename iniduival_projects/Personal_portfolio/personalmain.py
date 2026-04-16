"""
Student Portfolio - Python Class Projects
==========================================
Fully class-based architecture.
Replace placeholder project data and run() methods with your real content.
"""

import tkinter as tk
from tkinter import scrolledtext
import personallibrary,simple_morsecopy,Random_password_generator,classmain


# ─────────────────────────────────────────────
#  BASE PROJECT CLASS
# ─────────────────────────────────────────────

class Project:
    """
    Base class for every portfolio project.

    Subclass this for each of your 4 projects and override:
      - title, description, learned, challenge  (class attributes)
      - run(self)  →  put your project code here; use self.output() to print

    The GUI calls run() automatically after showing the description.
    """

    title       = "Untitled Project"
    description = "No description provided."
    learned     = ["No learning points listed."]
    challenge   = "No challenge listed."

    def __init__(self):
        self._output_widget = None

    def set_output_widget(self, widget: scrolledtext.ScrolledText) -> None:
        """Called by the GUI to wire up the output box before run() is invoked."""
        self._output_widget = widget

    def output(self, text: str = "") -> None:
        """Use this instead of print() inside your run() method."""
        if self._output_widget:
            self._output_widget.config(state="normal")
            self._output_widget.insert(tk.END, str(text) + "\n")
            self._output_widget.see(tk.END)
            self._output_widget.config(state="disabled")

    def run(self) -> None:
        """Override this method with your project's code."""
        self.output("(No run() method defined for this project yet.)")


# ─────────────────────────────────────────────
#  YOUR 4 PROJECTS  ← Edit these classes
# ─────────────────────────────────────────────

class Radom_password_generator(Project):
    title       = "Project 1: Number Guessing Game"
    description = (
        "A text-based game where the computer picks a random number "
        "and the player guesses until they find it."
    )
    learned = [
        "How to use while loops and conditional logic to control game flow.",
        "How to generate random numbers with the random module.",
    ]
    challenge = (
        "Figuring out how to give 'too high' / 'too low' hints "
        "without revealing the answer too early."
    )

    def run(self):
        import random
        secret = random.randint(1, 20)
        self.output("=== Number Guessing Game ===")
        self.output(f"(Demo) Secret number is {secret}.")
        self.output("Simulating 3 guesses...")
        for guess in [10, secret - 1, secret]:
            if guess < secret:
                self.output(f"  Guess {guess} → Too low!")
            elif guess > secret:
                self.output(f"  Guess {guess} → Too high!")
            else:
                self.output(f"  Guess {guess} → Correct!")
        # ↓ Paste your real project code below ↓
        Random_password_generator() 

    


class SimpleMorse(Project):
    title       = "Project 2: Simple Calculator"
    description = (
        "A command-line calculator that performs addition, subtraction, "
        "multiplication, and division based on user input."
    )
    learned = [
        "How to use functions to organize repeated logic.",
        "How to handle invalid input with try/except blocks.",
    ]
    challenge = "Preventing crashes when the user attempts to divide by zero."

    def run(self):
        self.output("=== Simple Calculator ===")
        examples = [(10, "+", 5), (9, "-", 4), (6, "*", 7), (20, "/", 4), (5, "/", 0)]
        for a, op, b in examples:
            try:
                result = self._calculate(a, op, b)
                self.output(f"  {a} {op} {b} = {result}")
            except ValueError as e:
                self.output(f"  {a} {op} {b} → Error: {e}")
        # ↓ Paste your real project code below ↓
        simple_morsecopy() 
                        


class classmain(Project):
    title       = "Project 3: To-Do List"
    description = (
        "A program that lets users add, view, and remove tasks, "
        "saving the list to a text file between sessions."
    )
    learned = [
        "How to read from and write to files using open() and file methods.",
        "How to work with lists to store and modify data at runtime.",
    ]
    challenge = (
        "Keeping the saved file in sync with the in-memory list "
        "after every add or delete operation."
    )

    def __init__(self):
        super().__init__()
        self._tasks = []

    def add_task(self, task: str):
        self._tasks.append(task)

    def remove_task(self, index: int):
        if 0 <= index < len(self._tasks):
            self._tasks.pop(index)

    def run(self):
        self.output("=== To-Do List ===")
        for task in ["Buy groceries", "Finish homework", "Walk the dog"]:
            self.add_task(task)
        self.output("Tasks after adding three items:")
        for i, t in enumerate(self._tasks, 1):
            self.output(f"  {i}. {t}")
        self.remove_task(1)
        self.output("\nTasks after removing item 2:")
        for i, t in enumerate(self._tasks, 1):
            self.output(f"  {i}. {t}")
        self.output("\n(Demo: real version saves tasks to a .txt file)")
        # ↓ Paste your real project code below ↓
        classmain()


class personallibrary       (Project):
    title       = "Project 4: Word Frequency Counter"
    description = (
        "Reads any text file and prints a ranked list of the most "
        "common words along with how many times each appears."
    )
    learned = [
        "How to use dictionaries to count and look up values efficiently.",
        "How to sort dictionary items by value using sorted() and lambda.",
    ]
    challenge = (
        "Stripping punctuation and normalizing capitalization so that "
        "'Hello', 'hello,' and 'HELLO' all count as the same word."
    )

    def run(self):
        import string
        self.output("=== Word Frequency Counter ===")
        sample = (
            "The quick brown fox jumps over the lazy dog. "
            "The fox ran quickly, and the dog barked."
        )
        self.output(f"Sample text:\n  \"{sample}\"\n")
        freq = self._count(sample)
        self.output("Top 6 words:")
        for word, count in sorted(freq.items(), key=lambda x: -x[1])[:6]:
            self.output(f"  '{word}': {count}")
        # ↓ Paste your real project code below ↓

    def _count(self, text: str) -> dict:
        import string
        words = text.lower().translate(
            str.maketrans("", "", string.punctuation)
        ).split()
        freq = {}
        for word in words:
            freq[word] = freq.get(word, 0) + 1
        return freq


# ─────────────────────────────────────────────
#  PROJECT DETAIL WINDOW
# ─────────────────────────────────────────────

class ProjectWindow(tk.Toplevel):
    """
    Opens when the user clicks a project button.
    Shows the description FIRST, then runs the project on demand.
    """

    def __init__(self, parent, project: Project):
        super().__init__(parent)
        self.title(project.title)
        self.resizable(True, True)
        self._project = project
        self._build_ui()

    def _build_ui(self):
        p = self._project

        # ── Description card (visible BEFORE run) ──
        info = tk.LabelFrame(self, text="Project Description", padx=10, pady=8)
        info.pack(fill="x", padx=16, pady=10)

        tk.Label(info, text="What it does:",
                 font=("TkDefaultFont", 10, "bold")).pack(anchor="w")
        tk.Label(info, text=p.description,
                 wraplength=500, justify="left").pack(anchor="w", pady=(2, 8))

        tk.Label(info, text="What I learned:",
                 font=("TkDefaultFont", 10, "bold")).pack(anchor="w")
        for point in p.learned:
            tk.Label(info, text=f"  \u2022  {point}",
                     wraplength=500, justify="left").pack(anchor="w")

        tk.Label(info, text="\nProgramming challenge I overcame:",
                 font=("TkDefaultFont", 10, "bold")).pack(anchor="w")
        tk.Label(info, text=f"  \u2022  {p.challenge}",
                 wraplength=500, justify="left").pack(anchor="w", pady=(2, 6))

        # ── Output area ──
        out_frame = tk.LabelFrame(self, text="Output", padx=10, pady=6)
        out_frame.pack(fill="both", expand=True, padx=16, pady=(0, 6))

        self._output_box = scrolledtext.ScrolledText(
            out_frame, height=10, state="disabled", font=("TkFixedFont", 10)
        )
        self._output_box.pack(fill="both", expand=True)
        self._project.set_output_widget(self._output_box)

        # ── Buttons ──
        btn_frame = tk.Frame(self)
        btn_frame.pack(pady=8)

        tk.Button(btn_frame, text="▶  Run Project",
                  font=("TkDefaultFont", 11, "bold"), width=16,
                  command=self._run).grid(row=0, column=0, padx=8)

        tk.Button(btn_frame, text="Clear Output", width=12,
                  command=self._clear).grid(row=0, column=1, padx=8)

        tk.Button(btn_frame, text="Close", width=10,
                  command=self.destroy).grid(row=0, column=2, padx=8)

    def _run(self):
        self._clear()
        try:
            self._project.run()
        except Exception as exc:
            self._project.output(f"[Error] {exc}")

    def _clear(self):
        box = self._output_box
        box.config(state="normal")
        box.delete("1.0", tk.END)
        box.config(state="disabled")


# ─────────────────────────────────────────────
#  MAIN PORTFOLIO WINDOW
# ─────────────────────────────────────────────

class PortfolioApp(tk.Tk):
    """
    Main application window.
    Holds the intro section and one button per project.
    Add or remove entries from PROJECT_CLASSES to change what appears.
    """

    PROJECT_CLASSES = [
        SimpleMorse,
        personallibrary,
        Radom_password_generator,
        classmain,
    ]

    def __init__(self):
        super().__init__()
        self.title("My Python Portfolio")
        self.resizable(True, True)
        self._projects = [cls() for cls in self.PROJECT_CLASSES]
        self._build_ui()

    def _build_ui(self):
        # ── Title ──
        tk.Label(
            self,
            text="My Python Class Portfolio",
            font=("TkDefaultFont", 18, "bold"),
            pady=12,
        ).pack()

        # ── Introduction ──
        intro = tk.LabelFrame(self, text="Introduction", padx=10, pady=8)
        intro.pack(fill="x", padx=20, pady=(0, 10))

        tk.Label(
            intro,
            text=(
                "Welcome to my portfolio! This application showcases four projects "
                "I built during this Python class, each demonstrating a different "
                "set of programming skills.\n\n"
                "How to navigate: Click any project button below to open a detail "
                "window. Read the description and learning notes first, then click "
                "\"Run Project\" to execute the code and see the output."
            ),
            wraplength=560,
            justify="left",
        ).pack(anchor="w")

        # ── Project buttons ──
        proj = tk.LabelFrame(self, text="Projects", padx=10, pady=8)
        proj.pack(fill="both", expand=True, padx=20, pady=(0, 10))

        for project in self._projects:
            tk.Button(
                proj,
                text=f"  {project.title}  ",
                font=("TkDefaultFont", 11),
                width=48,
                command=lambda p=project: ProjectWindow(self, p),
            ).pack(pady=5)

        # ── Footer ──
        tk.Label(
            self,
            text="Select a project above to view its description and run it.",
            fg="gray",
        ).pack(pady=(0, 12))


# ─────────────────────────────────────────────
#  Entry point
# ─────────────────────────────────────────────

if __name__ == "__main__":
    app = PortfolioApp()
    app.mainloop()
