CHATGPT CONVERSATION

******************

ChatGPT said:
Here's a Python script that generates flowcharts using the diagrams library. It creates a simple flowchart as an example.

Flowchart Generator
This script generates a simple flowchart with a start node, a decision point, and process steps. You need to install the diagrams library before running it:

bash
Copy
Edit
pip install diagrams
Let me know if you need a more complex version! 🚀






You said:
add a GUI for settings
ChatGPT said:
Edited
I've added a GUI for settings using Tkinter. Now, when you run the script, it will prompt you to enter a title for the flowchart. Let me know if you want additional settings! 🚀

******************


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
