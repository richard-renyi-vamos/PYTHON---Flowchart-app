import tkinter as tk
from tkinter import simpledialog
from diagrams import Diagram
from diagrams.programming.flowchart import StartEnd, Process, Decision

# Function to create a flowchart
def create_flowchart(title):
    with Diagram(title, show=True):
        start = StartEnd("Start")
        process1 = Process("Step 1: Input Data")
        decision = Decision("Is Data Valid?")
        process2 = Process("Step 2: Process Data")
        end = StartEnd("End")
        
        start >> process1 >> decision
        decision >> process2 >> end
        decision >> StartEnd("Error Handling")

# Function to get user settings
def get_settings():
    root = tk.Tk()
    root.withdraw()  # Hide main window
    title = simpledialog.askstring("Input", "Enter flowchart title:", parent=root)
    if title:
        create_flowchart(title)

if __name__ == "__main__":
    get_settings()
