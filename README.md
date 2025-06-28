# Auror Moody's Magical Cybersecurity Classroom

A Harry Potter themed chatbot interface for learning about cybersecurity concepts with guidance from the famous Auror, Mad-Eye Moody.

## 🔮 Features

- **Magical Interface**: Hogwarts-inspired dark theme GUI
- **Character-Driven Experience**: Interact with Auror Moody, known for his "CONSTANT VIGILANCE!"
- **Wizarding Terminology**: Cybersecurity concepts explained with Harry Potter analogies
- **Easy to Use**: Simple chat interface with magical command buttons

## 📋 Requirements

- Python 3.7+
- Required packages (install with `pip`):
  - tkinter (usually comes with Python)
  - google-genai (for the Gemini API)
  - pillow (for icon generation)
  - python-dotenv (for environment variables)

## 🧙‍♂️ Setup

1. Install the required packages:
   ```
   pip install google-genai pillow python-dotenv
   ```

2. Create a `.env` file in the root directory with your Google Gemini API key:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

3. Generate the icon (optional):
   ```
   python moody_icon.py
   ```

4. Run the application:
   ```
   python front.py
   ```

## 🪄 Usage

1. Type your cybersecurity question in the input field
2. Click "Cast Inquiry" or press Enter to send your message
3. Auror Moody will respond with cybersecurity advice in his characteristic style
4. Type "exit", "quit", or "disapparate" to close the application

## ⚡ About Auror Moody

Alastor "Mad-Eye" Moody is a renowned Auror (dark wizard catcher) in the Harry Potter universe, known for his magical eye, paranoia, and constant reminders for "CONSTANT VIGILANCE!" In this application, he takes on the role of a cybersecurity expert, using wizarding analogies to explain digital security concepts.

---

*"Dark wizards and cyber criminals have a lot in common. Both rely on secrecy and fear. The best defense against both? Knowledge and vigilance!" - Auror Moody* 