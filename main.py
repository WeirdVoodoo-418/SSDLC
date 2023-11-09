import psutil
import os
import json
import xml.etree.ElementTree as ET

def system_info():
    # This function will print the logical drives, names, volume label, size and file system type
    # NOTE: This functionality is platform-dependent and works on Windows.
    print("Logical Drive Information:")
    for partition in psutil.disk_partitions():
        try:
            usage = psutil.disk_usage(partition.mountpoint)
        except PermissionError:
            # this can be caught due to the disk that isn't ready
            continue
        print(f"  Drive: {partition.device}")
        print(f"  File system type: {partition.fstype}")
        try:
            drive = psutil.disk_usage(partition.mountpoint)
            print(f"  Total Size: {round(drive.total / (1024 * 1024 * 1024))} GB")
            print(f"  Used: {round(drive.used / (1024 * 1024 * 1024))} GB")
            print(f"  Free: {round(drive.free / (1024 * 1024 * 1024))} GB")
        except PermissionError:
            print("  Access Denied.")
        print()

# system_info()

class FileManager:
    def __init__(self, file_name):
        self.file_name = file_name

    def create_file(self):
        with open(self.file_name, 'w') as _:
            pass
        return f"File '{self.file_name}' created."

    def write_to_file(self, content):
        with open(self.file_name, 'w') as file:
            file.write(content)
        return f"Content written to '{self.file_name}'."

    def read_file(self):
        with open(self.file_name, 'r') as file:
            content = file.read()
        return f"Content of '{self.file_name}':\n{content}"

    def delete_file(self):
        os.remove(self.file_name)
        return f"File '{self.file_name}' deleted."

# file_manager = FileManager('demo_file.txt')
# print(file_manager.create_file())
# print(file_manager.write_to_file('Hello SSDLC!'))
# print(file_manager.read_file())
# print(file_manager.delete_file())



class JSONFileManager:
    def __init__(self, file_name):
        self.file_name = file_name

    def create_and_write_json(self, data):
        with open(self.file_name, 'w') as json_file:
            json.dump(data, json_file, indent=4)
        return f"JSON file '{self.file_name}' created and data written."

    def read_json(self):
        with open(self.file_name, 'r') as json_file:
            data = json.load(json_file)
        return f"Content of '{self.file_name}':\n{json.dumps(data, indent=4)}"

    def delete_file(self):
        os.remove(self.file_name)
        return f"JSON file '{self.file_name}' deleted."


# json_data = {
#     "username": "root",
#     "permissions": "root",
#     "importance_level": 777,
#     "text": "I'm just a simple data, uwu :3",
# }
# json_file_manager = JSONFileManager('example_data\data.json')
# print(json_file_manager.create_and_write_json(json_data))
# print(json_file_manager.read_json())
# print(json_file_manager.delete_file())

class XMLFileManager:
    def __init__(self, file_name):
        self.file_name = file_name

    def create_and_write_xml(self, data):
        root = ET.Element("root")
        for key, value in data.items():
            ET.SubElement(root, key).text = value
        tree = ET.ElementTree(root)
        tree.write(self.file_name)
        return f"XML file '{self.file_name}' created and data written."

    def read_xml(self):
        tree = ET.parse(self.file_name)
        root = tree.getroot()
        xml_str = ET.tostring(root, encoding='unicode', method='xml')
        return f"Content of '{self.file_name}':\n{xml_str}"

    def delete_file(self):
        os.remove(self.file_name)
        return f"XML file '{self.file_name}' deleted."


# Example usage:
xml_data = {
    "username": "root",
    "permissions": "root",
    "importance_level": "777",
    "text": "I'm just a simple data, uwu :3",
}
xml_file_manager = XMLFileManager('example_data\data.xml')
print(xml_file_manager.create_and_write_xml(xml_data))
print(xml_file_manager.read_xml())
print(xml_file_manager.delete_file())
