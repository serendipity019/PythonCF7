import os

def read_file(file_path):
    if not os.path.isfile(file_path):
        print(f"Error: {file_path} doesn't exits")
        return
    
    try:
        with open(file_path, 'r') as f:
            # Display file metadata
            print(f"Filename: {f.name}") # Just to have it as knowledge
            print(f"closed: {f.closed}") # Just to have it as knowledge
            print(f"Opening mode: {f.mode}") # Just to have it as knowledge

            contents = f.read()
            print("Contents:", contents)
    except FileNotFoundError:
        print(f"Error, {file_path} not found.")
    except IOError as e:
        print(f"Error reading file {file_path}: {e}")

    print(f"File closed after with-block: {f.closed}")

def read_file_contents(file_path): # This is the same like try- with resource in Java
            if not os.path.isfile(file_path):
                print(f"Error: {file_path} doesn't exits")
                return
            
            try:
                 with open(file_path, 'r') as f:
                      return f.read()
            except FileNotFoundError:
                 print(f"Error, {file_path} not found.")
            except IOError as e:
                print(f"Error reading file {file_path}: {e}")
            return None        
    
def create_file(file_path, content):
        try:
            with open(file_path, 'w') as f:
                f.write(content)
                print(f"File {file_path} created!")
        except IOError as e:
            print(f"Error creating file {file_path}: {e}")    
            return

def update_file(file_path, content):
     if not os.path.isfile(file_path):
                print(f"Error: {file_path} doesn't exits")
                return None
     
     try:
          with open(file_path, 'a') as f:
               f.write(content)
               print(f"File {file_path} updated with new content.")
     except IOError as e:
            print(f"Error creating file {file_path}: {e}")    
            return
     
def delete_file(file_path):
    if not os.path.isfile(file_path):
                print(f"Error: {file_path} doesn't exits")
                return None

    try:
          os.remove(file_path)
          print(f"File {file_path} removed.")
    except IOError as e:
            print(f"Error creating file {file_path}: {e}")    
            return            
          
def main():
    # create_file("example.txt", "Hello Coding Factory 7")
    # print()

    print("Reading my file")
    read_file_contents("example.txt")
    
    update_file("example.txt", ". Hello World!")
    read_file("example.txt")

    #delete_file("example.txt")

if __name__ == "__main__":
    main()  
