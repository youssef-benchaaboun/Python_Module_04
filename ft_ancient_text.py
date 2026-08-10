import sys
import typing

def read_file(atgumts:list)->None:
    try:
        if len(argumts) !=1:
            raise Exception("Usage: ft_ancient_text.py <file>")
    except Exception as error:
        print(error)
        return
    try:
        file=open(argumts[0])
    except (FileExistsError,FileNotFoundError) as error:
        print(f"Error opening file '{argumts[0]}': {error}")
        return
    content=file.read()
    print(content)

if __name__=="__main__":
    argumts=sys.argv[1:]
    read_file(argumts)