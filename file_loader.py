import magic

def identify_file_type(file_path):
    mime = magic.Magic(mime=True)
    file_type = mime.from_file(file_path)
    return file_type

file_path = 'path_to_your_file'
file_type = identify_file_type(file_path)
print("File type:", file_type)
