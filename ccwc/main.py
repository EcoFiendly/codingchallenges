import os
import sys

def ccwc(filename:str) -> dict:
    """
    Function takes a file and counts the number of bytes, lines, words and characters in the file

    filename: name of file
    """
    results = {
        "-c": 0,
        "-l": 0,
        "-w": 0,
        "-m": 0,
    }
    
    line = 0
    word = 0
    char = 0
    
    try:
        byte = os.path.getsize(filename)
        with open(filename) as fh:
            for l in fh:
                line += 1
                word += len(l.split())
                char += len(l)

        results["-c"] = byte
        results["-l"] = line
        results["-w"] = word
        results["-m"] = char
        
    except Exception as err:
        print(err)
    return results

if __name__ == '__main__':
    if len(sys.argv) < 1:
        exit(f"Usage: {sys.argv[0]} option FILENAMEs")

    if len(sys.argv[1]) == 2:
        results = wc(sys.argv[2])
        print(results[sys.argv[1]])
    else:
        results = wc(sys.argv[1])
        print(f"{results['-l']}   {results['-w']}   {results['-c']}   {sys.argv[1]}")