import xml.etree.ElementTree as etree
tree = etree.parse('feed.xml')
root = tree.getroot()
print(root.tag)
print(len(root))
for child in root:
    print(child)
print(root.attrib)
print(root.findall('{http://www.w3.org/2005/Atom}entry'))
print(tree.findall('//{http://www.w3.org/2005/Atom}author'))