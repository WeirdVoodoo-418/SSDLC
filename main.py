import psutil
import os
import json
import xml.etree.ElementTree as ET
import zipfile

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

class ZipFileManager:
    def __init__(self, zip_file_name):
        self.zip_file_name = zip_file_name

    def create_zip_archive(self):
        with zipfile.ZipFile(self.zip_file_name, 'w') as _:
            pass
        return f"Zip archive '{self.zip_file_name}' created."

    def add_file_to_zip(self, file_name):
        with zipfile.ZipFile(self.zip_file_name, 'a') as zipf:
            zipf.write(file_name)
        return f"File '{file_name}' added to the zip archive '{self.zip_file_name}'."

    def extract_and_display_info(self):
        with zipfile.ZipFile(self.zip_file_name, 'r') as zipf:
            zipf.extractall("extracted")
            info = zipf.infolist()
            extracted_info = [(file.filename, file.file_size) for file in info]
        return f"Extracted files: {extracted_info}"

    def delete_files_and_archive(self, file_name):
        if(file_name != ''):
            os.remove(file_name)
        os.remove(self.zip_file_name)
        return f"File '{file_name}' and archive '{self.zip_file_name}' deleted."

def main():
    while True:
        operation = input("What do you want to do: [system, file, json, xml, zip, exit]: ").lower()
        
        if operation == 'exit':
            break

        if operation == 'system':
            system_info()
        elif operation == 'file':
            file_name = input("Enter the filename: ")
            file_manager = FileManager(file_name)
            file_action = input("What do you want to do: [create, write, read, delete]: ").lower()
            if file_action == 'create':
                print(file_manager.create_file())
            elif file_action == 'write':
                content = input("Enter content to write in the file: ")
                print(file_manager.write_to_file(content))
            elif file_action == 'read':
                print(file_manager.read_file())
            elif file_action == 'delete':
                print(file_manager.delete_file())
        elif operation == 'json':
            file_name = input("Enter the JSON filename: ")
            json_file_manager = JSONFileManager(file_name)
            json_action = input("What do you want to do: [create and write, read, delete]: ").lower()
            if json_action == 'create and write':
                json_data = input("Enter JSON data (in dictionary format): ")
                json_data_dict = json.loads(json_data)
                print(json_file_manager.create_and_write_json(json_data_dict))
            elif json_action == 'read':
                print(json_file_manager.read_json())
            elif json_action == 'delete':
                print(json_file_manager.delete_file())
        elif operation == 'xml':
            file_name = input("Enter the XML filename: ")
            xml_file_manager = XMLFileManager(file_name)
            xml_action = input("What do you want to do: [create and write, read, delete]: ").lower()
            if xml_action == 'create and write':
                xml_data = input("Enter XML data (in dictionary format): ")
                xml_data_dict = json.loads(xml_data)
                print(xml_file_manager.create_and_write_xml(xml_data_dict))
            elif xml_action == 'read':
                print(xml_file_manager.read_xml())
            elif xml_action == 'delete':
                print(xml_file_manager.delete_file())
        elif operation == 'zip':
            zip_file_name = input("Enter the zip filename: ")
            zip_manager = ZipFileManager(zip_file_name)
            zip_action = input("What do you want to do: [create, add file, extract and display, delete]: ").lower()
            if zip_action == 'create':
                print(zip_manager.create_zip_archive())
            elif zip_action == 'add file':
                file_name = input("Enter the name of the file to add to the zip archive: ")
                print(zip_manager.add_file_to_zip(file_name))
            elif zip_action == 'extract and display':
                print(zip_manager.extract_and_display_info())
            elif zip_action == 'delete':
                file_name = input("Enter the name of the file to delete along with the archive: ")
                print(zip_manager.delete_files_and_archive(file_name))

        else:
            print("Invalid operation. Please try again.")

if __name__ == '__main__':
    main()
