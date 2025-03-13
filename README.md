# AI Mood Translator

## Overview
AI Model Translator is a deep learning-based language translation tool that leverages transformer models to provide accurate and efficient translations between multiple languages. It supports text-based translation and can be integrated into various applications.

## Features
- Supports multiple languages
- Uses state-of-the-art transformer models
- Can be fine-tuned for specific domains
- REST API for easy integration
- Optimized for efficiency and speed
- Auto-detects input language
- Determines user's default language based on IP location
- Supports both offline (pyttsx3) and online (gTTS) text-to-speech

## Installation

### Prerequisites
- Python 3.8+
- pip
- Virtual environment (optional but recommended)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ai-model-translator.git
   cd ai-model-translator
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Translator
Start the translation service using:
```bash
python translator.py
```

### Functionality
1. **User Input**: Enter the text to be translated.
2. **Language Detection**: The tool automatically detects the input language.
3. **User Location Detection**: Determines the default translation language based on the user's IP address.
4. **Translation**: The text is translated into the target language (default or user-specified).
5. **Speech Output**: The translated text can be spoken using:
   - **Offline Mode**: Uses `pyttsx3` for local text-to-speech.
   - **Online Mode**: Uses `gTTS` (Google Text-to-Speech) for better pronunciation.

### Example Usage
#### Translating Text
```bash
Enter text to translate: Hello, how are you?
Detected Language: en
Detected Country: IN
Default Target Language: ta
Translated Text (ta): ஹலோ, எப்படி இருக்கிறீர்கள்?
```

#### Speech Output
```bash
Do you want to hear the translated text? (yes/no): yes
Choose speech mode - 'offline' or 'online' (default: offline): online
```

## Model Training (Optional)
To train a custom model, prepare your dataset and run:
```bash
python train.py --data path/to/dataset --epochs 10
```

## Technologies Used
- Python
- Transformers (Hugging Face)
- Flask (API)
- TensorFlow / PyTorch
- `deep_translator` for translation
- `langdetect` for automatic language detection
- `pyttsx3` for offline text-to-speech
- `gTTS` for online text-to-speech

## License
This project is licensed under the MIT License.
