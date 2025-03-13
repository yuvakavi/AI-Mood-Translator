import requests
import pyttsx3  # Offline TTS
from gtts import gTTS  # Online TTS
from deep_translator import GoogleTranslator
from langdetect import detect
from textblob import TextBlob  # Sentiment Analysis
import os
import time

# Function to get the user's country based on IP
def get_user_location():
    try:
        response = requests.get("https://ipinfo.io/json")
        data = response.json()
        country = data.get("country", "Unknown")
        return country
    except Exception as e:
        print("Could not retrieve location. Error:", e)
        return "Unknown"

# Mapping country codes to default language codes
country_language_map = {
    "US": "en", "IN": "ta", "FR": "fr", "ES": "es", "DE": "de",
    "CN": "zh-CN", "JP": "ja", "BR": "pt", "RU": "ru"
}

# Function to analyze sentiment
def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity  # -1 (negative) to +1 (positive)
    
    if polarity > 0.2:
        return "positive"
    elif polarity < -0.2:
        return "negative"
    else:
        return "neutral"

# Function to speak text using pyttsx3 (offline)
def speak_text_offline(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Function to speak text using gTTS (online)
def speak_text_online(text, lang="ta"):
    try:
        tts = gTTS(text=text, lang=lang)
        filename = "temp_audio.mp3"
        tts.save(filename)
        os.system(f"start {filename}")  # Use "afplay" for macOS, "mpg321" for Linux
        time.sleep(3)
        os.remove(filename)
    except Exception as e:
        print("Error in speech output:", e)

# Get user input
text = input("Enter text to translate: ").strip()

# Auto-detect input language
detected_lang = detect(text)
print(f"Detected Language: {detected_lang}")

# Identify user location
user_country = get_user_location()
print(f"Detected Country: {user_country}")

# Set default target language based on location
default_target_lang = country_language_map.get(user_country, "ta")
print(f"Default Target Language: {default_target_lang}")

# Ask user for target language (or use default)
target_lang = input(f"Enter target language code (Press Enter for default '{default_target_lang}'): ").strip()
if not target_lang:
    target_lang = default_target_lang

# Analyze sentiment
mood = analyze_sentiment(text)
print(f"Detected Mood: {mood}")

# Change translation style based on mood
if mood == "positive":
    text += " 😊"
elif mood == "negative":
    text = "I need help! " + text
elif mood == "neutral":
    text += " 🤔"

try:
    # Translate text
    translated_text = GoogleTranslator(source=detected_lang, target=target_lang).translate(text)
    print(f"Translated Text ({target_lang}): {translated_text}")

    # Ask user if they want to hear the translated text
    speak_choice = input("Do you want to hear the translated text? (yes/no): ").strip().lower()
    if speak_choice == "yes":
        speak_mode = input("Choose speech mode - 'offline' or 'online' (default: offline): ").strip().lower()
        if speak_mode == "online":
            speak_text_online(translated_text, target_lang)
        else:
            speak_text_offline(translated_text)

except Exception as e:
    print("Translation failed. Please check the language code and try again.")
    print("Error:", e)
