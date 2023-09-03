import os
import shutil

def organize_downloads():
    downloads_folder = os.path.join(os.path.expanduser('~'), 'Downloads')
    image_extensions = ['.jpeg', '.jpg', '.png', '.gif']
    document_extensions = ['.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx']
    installation_extensions = ['.dmg', '.zip']
    
    # create the folders if they don't exist
    if not os.path.exists(os.path.join(downloads_folder, 'Images')):
        os.makedirs(os.path.join(downloads_folder, 'Images'))
    if not os.path.exists(os.path.join(downloads_folder, 'Documents')):
        os.makedirs(os.path.join(downloads_folder, 'Documents'))
    if not os.path.exists(os.path.join(downloads_folder, 'Installations')):
        os.makedirs(os.path.join(downloads_folder, 'Installations'))
        
    for filename in os.listdir(downloads_folder):
        file_path = os.path.join(downloads_folder, filename)
        if os.path.isfile(file_path):
            extension = os.path.splitext(filename)[1].lower()
            if extension in image_extensions:
                shutil.move(file_path, os.path.join(downloads_folder, 'Images', filename))
            elif extension in document_extensions:
                shutil.move(file_path, os.path.join(downloads_folder, 'Documents', filename))
            elif extension in installation_extensions:
                shutil.move(file_path, os.path.join(downloads_folder, 'Installations', filename))

if __name__ == '__main__':
    organize_downloads()

print("Finished")
