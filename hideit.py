#!/usr/bin/env python3

from sys import argv
from os import path, getcwd

class hideit():
    def __init__(self) -> None:      
        #colors
        self.Y = "\033[93m"
        self.R = "\033[91m"
        self.W = "\033[97m"
        self.G = "\033[92m"
        self.Res = "\033[0m"
    
    # Display the help menu.
    def help(self):
        print(f"""usage: {argv[0]} <FILENAME.py>\n """)
   
   
    # Encodes a visible string into a sequence of invisible Unicode tag characters.
    def encodeToInvisible(self, visible: str) -> str:
        try:        
            invisible = ""
            for char in visible:
                invisible_char = chr(0xE0000 + ord(char))
                invisible += invisible_char
        
            return invisible
        except Exception as e:
            print(f"{self.R}[!] - Error: \n{str(e)}{self.Res}")


    # Construct the finale payload and save it to a '.py' file.
    def constructPayload(self, invisible: str,original_filename: str) -> None:
        stub = f"""''.join([chr(ord(char) - 0xE0000) for char in '{invisible}'])"""
        payload = f"""exec({stub})"""
        try:
            with open(f"invisible_{original_filename}", 'w') as outputfile:
                outputfile.write(payload)
            cwd = getcwd()
            print(f"[{self.G}+{self.Res}] - Payload successfully saved as {cwd}/invisible_{original_filename}")
        except Exception as e:
            print(f"{self.R}[!] - Error: \n{str(e)}{self.Res}")
    
    # main     
    def main(self):
        if not len(argv) > 1:
            self.help()
            exit(1)
        
        file_to_process = argv[1]

        if not path.isfile(file_to_process):
            print(f"[{self.R}!{self.Res}] - Please specify a valid python file.")
            exit(1)
        
        with open(file_to_process,'r') as inputfile:
            visible_code = inputfile.read()
        

        invisible_code = self.encodeToInvisible(visible_code)
        # constructing the final payload
        self.constructPayload(invisible_code,file_to_process)

        
if __name__ == "__main__":
    Main = hideit()
    Main.main()
    
    
