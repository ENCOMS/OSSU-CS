"""
App: extensions.py

Description:
In a file called extensions.py, implement a program that prompts the user for the name of a file and then outputs
that file’s media type if the file’s name ends, case-insensitively, in any of these suffixes:

* .gif
* .jpg
* .jpeg
* .png
* .pdf
* .txt
* .zip

"""



def main():
    fileType = input("File name: ").lower().strip()
    print(extConvert(fileType))


def extConvert(e):
    if e.endswith(".gif"):
        return "image/gif"
    elif e.endswith(".jpg") or e.endswith(".jpeg"):
        return "image/jpeg"
    elif e.endswith(".png"):
        return "image/png"
    elif e.endswith(".pdf"):
        return "application/pdf"
    elif e.endswith(".txt"):
        return "text/plain"
    elif e.endswith(".zip"):
        return "application/zip"
    else:
        return "application/octet-stream"


main()