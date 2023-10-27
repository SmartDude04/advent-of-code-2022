# Use list comprehension to open the file and parse through
lines = [line.strip() for line in open("day-7/day7-snippet.txt", "r")]

# Global folder array, stores every folder found as an object
folders = []
class Folder:
    
    size = 0
    parent_folder = "/"
    files = []
    folders = []
    
    # Init function, also compute size of the folder
    def __init__(self, parent_folder, files, folders) -> None:
        self.parent_folder = parent_folder
        self.files = files
        self.folders = folders
        
    # Return the size of the folder
    def get_size(self) -> int:
        return self.size
    
    # Get the index in the folder array of the parent folder so a lookup can be performed
    def find_parent_folder_index(self) -> int:
        for i, v in enumerate(folders):
            if v == self.parent_folder:
                return i

        return -1
    


#def build_folder(command_line_num):

tester = Folder("var", 3, 5)