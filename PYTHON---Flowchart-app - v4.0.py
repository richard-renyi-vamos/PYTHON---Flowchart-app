import tkinter as tk
from tkinter import simpledialog, messagebox
from diagrams import Diagram, Edge
from diagrams.programming.flowchart import StartEnd, Process, Decision
import os


def create_flowchart(title, steps, direction):
    graph_attr = {
        "fontsize": "20",
        "bgcolor": "#F9F9F9",
        "rankdir": direction,  # Now user-defined!
        "splines": "ortho"
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

    file_name = title.lower().replace(" ", "_")

    with Diagram(title, filename=file_name, show=True, graph_attr=graph_attr, node_attr=node_attr, edge_attr=edge_attr):
        start = StartEnd("🚀 Start")
        prev_node = start

        nodes = []

        # Create custom steps
        for i, step in enumerate(steps):
            if "decision" in step.lower():
                node = Decision(f"🧐 {step}")
            else:
                node = Process(f"⚙️ {step}")
            prev_node >> Edge(label=f"step {i+1}") >> node
            prev_node = node
            nodes.append(node)

        end = StartEnd("🏁 End")
        prev_node >> Edge(label="done") >> end


def get_settings():
    root = tk.Tk()
    root.withdraw()

    title = simpledialog.askstring("Flowchart Title", "Enter flowchart title:", parent=root)
    direction = simpledialog.askstring("Layout", "Direction? TB (Top-Bottom) or LR (Left-Right):", parent=root)

    if not title or direction not in ("TB", "LR"):
        messagebox.showerror("Error", "Invalid input. Please try again.")
        return

    steps = []
    while True:
        step = simpledialog.askstring("Add Step", "Enter a step (or click Cancel to finish):", parent=root)
        if not step:
            break
        steps.append(step)

    if steps:
        create_flowchart(title, steps, direction)
    else:
        messagebox.showinfo("No Steps", "No steps were added. Flowchart cancelled.")


if __name__ == "__main__":
    get_settings()
