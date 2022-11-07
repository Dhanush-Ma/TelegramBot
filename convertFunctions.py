from imports import *


def convertPNGtoJPG(fileURL, chatID, filename, requiredEXT, messageID):
    response = requests.get(fileURL)
    image = Image.open(BytesIO(response.content)).convert("RGB")
    image.save(f'{filename}.{requiredEXT}', "jpeg")
    bot.send_document(chat_id=chatID,
                      reply_to_message_id=messageID,
                      document=open(f'{filename}.{requiredEXT}', 'rb'))


def convertJPGtoPNG(fileURL, chatID, filename, messageID):
    response = requests.get(fileURL)
    image = Image.open(BytesIO(response.content)).convert("RGBA")
    image.save(f'{filename}.png', "png")
    bot.send_document(chat_id=chatID,
                      reply_to_message_id=messageID,
                      document=open(f'{filename}.png', 'rb'))


def imageToPDF(fileURL, chatID, filename, messageID):
    response = requests.get(fileURL)
    image = Image.open(BytesIO(response.content)).convert("RGB")
    image.save(f'{filename}.pdf', "pdf")
    bot.send_document(chat_id=chatID,
                      reply_to_message_id=messageID,
                      document=open(f'{filename}.pdf', 'rb'))


def convertWEBPtoImage(fileURL, chatID, filename, extension, messageID):
    response = requests.get(fileURL)
    image = Image.open(BytesIO(response.content)).convert("RGB")
    if extension == ".jpg" or ".jpeg":
        image.save(f'{filename}.{extension}', "jpeg")
    else:
        image.save(f'{filename}.{extension}', "png")
    bot.send_document(chat_id=chatID,
                      reply_to_message_id=messageID,
                      document=open(f'{filename}{extension}', 'rb'))


def imageToWEBP(fileURL, chatID, filename, messageID):
    response = requests.get(fileURL)
    image = Image.open(BytesIO(response.content)).convert("RGB")
    image.save(f'{filename}.webp', "webp")
    bot.send_document(chat_id=chatID,
                      reply_to_message_id=messageID,
                      document=open(f'{filename}.webp', 'rb'))
