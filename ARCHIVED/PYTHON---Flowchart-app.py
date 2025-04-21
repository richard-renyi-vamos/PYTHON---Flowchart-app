from graphviz import Digraph

def create_flowchart():
    # Create a new directed graph
    dot = Digraph(comment='The Flowchart')

    # Adding nodes (steps in the flowchart)
    dot.node('A', 'Start')
    dot.node('B', 'Step 1')
    dot.node('C', 'Step 2')
    dot.node('D', 'End')

    # Connecting nodes with edges
    dot.edge('A', 'B', 'action 1')
    dot.edge('B', 'C', 'action 2')
    dot.edge('C', 'D', 'action 3')

    # Print the generated source code
    print(dot.source)

    # Save and render the image
    filename = dot.render(filename='flowchart', format='png', cleanup=True)
    print(f'Flowchart saved as {filename}')

create_flowchart()
