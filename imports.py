from PIL import Image
from io import BytesIO
from telebot.types import File, InlineKeyboardButton, InlineKeyboardMarkup
import telebot
import requests
import os

# unique API token
API_TOKEN = "5651760970:AAE7pebd11gWgpOC4X5IOd9zTz43MwJ6PbM"

# establishing the connection of API
bot = telebot.TeleBot(API_TOKEN, parse_mode=None)
