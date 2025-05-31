import base64
import os
from google import genai
from google.genai import types
import json
import wikipediaapi as wiki
import webbrowser as wb
import gen
import web
import article
import pyautogui as pg
import time

with open("config.json" , 'r') as file:
    config = json.load(file)

API_KEY = config["API"]
