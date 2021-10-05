import xml.etree.ElementTree as ET
import networkx as nx

isTrim = True

tree = ET.parse('test.xml')
root = tree.getroot()

word_mapping_whole = {}
edges = []
previous_whole = ""
current_whole = ""
parent = root
hasChild = True 
   
while(hasChild == True): 
    for child in parent:
        print(child.tag)
        parent = child
    