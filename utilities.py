from imports import *

def getURL(fileID):
    URLlinkObj = bot.get_file(fileID)
    fileURL = f'https://api.telegram.org/file/bot{API_TOKEN}/{URLlinkObj.file_path}'
    return fileURL


def getFilename(file):
    split = os.path.splitext(file)
    return split
