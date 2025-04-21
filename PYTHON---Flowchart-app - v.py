import tkinter as tk
from tkinter import simpledialog
from diagrams import Diagram, Edge
from diagrams.programming.flowchart import StartEnd, Process, Decision


# Function to create a styled flowchart
def create_flowchart(title):
    graph_attr = {
        "fontsize": "20",
        "bgcolor": "#F9F9F9",  # Light background
        "rankdir": "TB",  # Top-Bottom direction
        "splines": "ortho"  # Clean lines
    }

    node_attr = {
        "fontsize": "16",
        "fontcolor": "#333333",
        "color": "#333366",
        "style": "filled",
        "fillcolor": "#E6F0FA",
        "shape": "box"
    }

    edge_attr = {
        "fontsize": "12",
        "fontcolor": "#333333",
        "color": "#888888"
    }

    with Diagram(title, show=True, graph_attr=graph_attr, node_attr=node_attr, edge_attr=edge_attr):
        start = StartEnd("🚀 Start")
        process1 = Process("📥 Step 1: Input Data")
        decision = Decision("🧐 Is Data Valid?")
        process2 = Process("⚙️ Step 2: Process Data")
        end = StartEnd("🏁 End")
        error = StartEnd("❌ Error Handling")

        start >> Edge(label="begin") >> process1
        process1 >> Edge(label="check") >> decision
        decision >> Edge(label="Yes ✅", color="green") >> process2
        process2 >> Edge(label="done") >> end
        decision >> Edge(label="No ❌", color="red", style="dashed") >> error


# Function to get user settings
def get_settings():
    root = tk.Tk()
    root.withdraw()  # Hide main window
    title = simpledialog.askstring("Input", "Enter flowchart title:", parent=root)
    if title:
        create_flowchart(title)


if __name__ == "__main__":
    get_settings()
