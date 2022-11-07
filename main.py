from imports import *
from utilities import *
from convertFunctions import convertJPGtoPNG,convertPNGtoJPG,convertWEBPtoImage,imageToPDF,imageToWEBP


# supported formats at the moment
overall_supported_formats = [".png", ".webp", ".jpg", ".jpeg"]

# inline buttons of what the bot does with the file.
png = InlineKeyboardButton("PNG", callback_data="png")
jpg = InlineKeyboardButton("JPG", callback_data="jpg")
jpeg = InlineKeyboardButton("JPEG", callback_data="jpeg")
pdf = InlineKeyboardButton("PDF", callback_data="pdf")
webp = InlineKeyboardButton("WEBP", callback_data="webp")
inlineKeysForImages = [png, jpg, jpeg, pdf, webp]


# message handler for commands
# /start
@bot.message_handler(commands=['start'])
def send_info(message):
    bot.send_message(chat_id=message.chat.id,
                     text="Hi! Convert Bot at your service!\nWith me you can convert files from one format to other.Try to send files only as a file and not as a photo.Send me a file to convert.\n\nType /help to see formats accepted at the moment.")

# /help


@bot.message_handler(commands=['help'])
def send_info(message):
    bot.send_message(chat_id=message.chat.id,
                     text=f"Accepted formats:\n\n📸Images({len(overall_supported_formats)})\n{',  '.join(overall_supported_formats)}")

# message handle for document type files


@ bot.message_handler(content_types='document')
def handle_docs(message):
    fileID = message.document.file_id
    fileURL = getURL(fileID)
    filename, extension = getFilename(fileURL)
    if extension in overall_supported_formats:
        supported_formats = []
        if extension == '.png' or '.jpg' or '.jpeg' or '.webp':
            supported_formats.clear()
            for i in inlineKeysForImages:
                if (f'.{i.callback_data}' == extension):
                    pass
                else:
                    supported_formats.append(i)

        markup = InlineKeyboardMarkup()
        markup.row_width = 2
        markup.add(
            supported_formats[0], supported_formats[1],
            supported_formats[2], supported_formats[3], row_width=2)

        bot.reply_to(
            message, f'You have entered a photo of type *{extension.upper()}* Below are the possible type of conversions available at the moment.',
            reply_markup=markup, parse_mode="Markdown")
        # program goes to markup (ie) inline message handlers

    else:
        msg = "\n".join(overall_supported_formats)
        bot.reply_to(
            message, f'*You have entered an invalid file format.\nThe list of supported formats accepted at the moment are:\n\n {msg.upper()}*',
            parse_mode="Markdown")


@ bot.message_handler(content_types=['photo', 'image'])
def handle_photos(message):
    bot.send_message(chat_id=message.chat.id,
                     text=f"*Try sending the photo as a document file for more clear conversion rate and without compression.* ", parse_mode="Markdown")
    bot.send_document(chat_id=message.chat.id,
                      document=open('info.webp', 'rb'))


@ bot.callback_query_handler(func=lambda message: True)
def callback_query(call):
    if call.data == "png":
        bot.answer_callback_query(call.id, "png")
        fileID = call.message.reply_to_message.document.file_id
        chatID = call.message.reply_to_message.chat.id
        file = call.message.reply_to_message.document.file_name
        messageID = call.message.reply_to_message.message_id
        filename, ext = getFilename(file)
        url = getURL(fileID)
        providedEXT = ext
        if providedEXT == ".jpg" or ".jpeg":
            bot.send_message(
                chat_id=chatID, text="_Processing..._", parse_mode="Markdown")
            convertJPGtoPNG(url, chatID, filename, messageID)
        if providedEXT == ".webp":
            bot.send_message(
                chat_id=chatID, text="_Processing..._", parse_mode="Markdown")
            convertWEBPtoImage(url, chatID, filename, ext, messageID)

    if call.data == "jpg":
        bot.answer_callback_query(call.id, "jpg")
        fileID = call.message.reply_to_message.document.file_id
        chatID = call.message.reply_to_message.chat.id
        messageID = call.message.reply_to_message.message_id
        file = call.message.reply_to_message.document.file_name
        filename, ext = getFilename(file)
        url = getURL(fileID)
        providedEXT = ext
        requiredEXT = call.data
        if providedEXT == ".png" or ".jpeg":
            bot.send_message(
                chat_id=chatID, text="_Processing..._", parse_mode="Markdown")
            convertPNGtoJPG(url, chatID, filename, requiredEXT, messageID)
        if providedEXT == ".webp":
            bot.send_message(
                chat_id=chatID, text="_Processing..._", parse_mode="Markdown")
            convertWEBPtoImage(url, chatID, filename, ext, messageID)

    if call.data == "jpeg":
        bot.answer_callback_query(call.id, "jpeg")
        fileID = call.message.reply_to_message.document.file_id
        chatID = call.message.reply_to_message.chat.id
        file = call.message.reply_to_message.document.file_name
        messageID = call.message.reply_to_message.message_id
        filename, ext = getFilename(file)
        url = getURL(fileID)
        providedEXT = ext
        requiredEXT = call.data
        if providedEXT == ".png" or ".jpg":
            bot.send_message(
                chat_id=chatID, text="_Processing..._", parse_mode="Markdown")
            convertPNGtoJPG(url, chatID, filename, requiredEXT, messageID)
        if providedEXT == ".webp":
            bot.send_message(
                chat_id=chatID, text="_Processing..._", parse_mode="Markdown")
            convertWEBPtoImage(url, chatID, filename, ext, messageID)

    if call.data == "pdf":
        bot.answer_callback_query(call.id, "pdf")
        fileID = call.message.reply_to_message.document.file_id
        chatID = call.message.reply_to_message.chat.id
        file = call.message.reply_to_message.document.file_name
        messageID = call.message.reply_to_message.message_id
        filename, ext = getFilename(file)
        url = getURL(fileID)
        providedEXT = ext
        if providedEXT == ".png" or ".jpg" or ".jpeg":
            bot.send_message(
                chat_id=chatID, text="_Processing..._", parse_mode="Markdown")
            imageToPDF(url, chatID, filename, messageID)

    if call.data == "webp":
        bot.answer_callback_query(call.id, "webp")
        fileID = call.message.reply_to_message.document.file_id
        chatID = call.message.reply_to_message.chat.id
        file = call.message.reply_to_message.document.file_name
        messageID = call.message.reply_to_message.message_id
        filename, ext = getFilename(file)
        url = getURL(fileID)
        bot.send_message(
            chat_id=chatID, text="_Processing..._", parse_mode="Markdown")
        imageToWEBP(url, chatID, filename, messageID)


bot.infinity_polling()
