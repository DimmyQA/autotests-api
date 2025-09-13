import xml.etree.ElementTree as ET

xml_data = """
<user>
    <id>1</id>
    <first_name>Dima</first_name>
    <last_name>Litvinov</last_name>
    <email>dima.litv@example.com</email>
    <age>34</age>
</user>
"""

root = ET.fromstring(xml_data)

print(root.find('first_name').text)