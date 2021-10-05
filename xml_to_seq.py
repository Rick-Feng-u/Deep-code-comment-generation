import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
import networkx as nx
import json
from networkx.drawing.nx_pydot import graphviz_layout

def xml_to_prufer(xml_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()
    
    word_mapping_whole = {}
    edges = []
    previous_whole = ""
    current_whole = ""
    
    queue = []     #Initialize a queue
    
    queue.append(root)
    
    while queue:
        elem = queue.pop(0)
        #print(elem.tag, elem.attrib)
        if(bool(elem.attrib)):
            previous_whole = elem.tag + " " + json.dumps(elem.attrib)
        else:
            previous_whole = elem.tag + " " + elem.text
        if(previous_whole not in word_mapping_whole):
            word_mapping_whole[previous_whole] = len(word_mapping_whole)
            
        
        for neighbour in elem:
            queue.append(neighbour)
            #print(neighbour.tag, neighbour.attrib)
            if(bool(neighbour.attrib)):
                current_whole = neighbour.tag + " " + json.dumps(neighbour.attrib)
            else:
                current_whole = neighbour.tag + " " + neighbour.text
            if(current_whole not in word_mapping_whole):
                word_mapping_whole[current_whole] = len(word_mapping_whole)
            elif(current_whole in word_mapping_whole):
                continue
            edges.append((int(word_mapping_whole[previous_whole]), int(word_mapping_whole[current_whole])))
            
    print(edges)
    nx_tree = nx.Graph(edges)
    pos = pos = graphviz_layout(nx_tree, prog="dot")
    nx.draw(nx_tree, pos)
    plt.show()
    
    sequence = nx.to_prufer_sequence(nx_tree)
    print(sequence)

    output_sequence = []

    for item in sequence:
        output_sequence.append(list(word_mapping_whole.keys())[list(word_mapping_whole.values()).index(int(item))])
    
    print(output_sequence)
    return output_sequence

if __name__ == '__main__':
    xml_to_prufer('test.xml')