A mini computer vision project that decodes Morse Code based on eye blinks in real-time. Designed to assist users in communicating through simple eye gestures.
# Morse Code Eye Blink Decoder

## Features
- Detect eye blinks via webcam using MediaPipe and OpenCV in python.
- Decodes Morse Code based on eye-blink duration.
- Sends decoded messages in real-time to a C# WinForms app.
- Displays the doecoded message live in the desktop app.
- support special morse code for deleting the last character (--.--).

## Requirements
- Python 3.8+ with dependencies in `requirements.txt`.
- .NET Framework for the C# desktop app.
- Python Virtual Environment.

## Setup
### Python
1. Create and activate a python virtual environment in the `pythonApp` folder:
```bash
python -m venv venv
source venv/bin/activate  #linux/macOS
venv\scripts\activate     # Windows
```
2. Install required python packages:
```bash
pip install -r requirements.txt
```
3. Run the python code independently to verify it works:
```bash
python main.py
```

## C# Desktop App
1. OPen the soltion in Visual Studio
2. Ensure that the Python interpreter and script path are correctly set in `Form1.cs`.
3. Build and run the C# App.
4. Click the "Start" button to launch the python process and start decoding.

## How it Works
- Python Detect the blinks and interpret them into Morse Code.
- Ocne a character is detected, python prints the decoded message with a prefix `[MSG]`.
- The C# App reads the python output, extract the decoded message, and displays it live.

## Project Structure

morseCodeDecoder/  
│  
├── morseCodeDecoder/  
│   ├── assests/  
│   │     └─ (icons and pngs)  
│   ├── pythonApp/  
│   │   ├─ `constants.py`  
│   │   ├─ `main.py`  
│   │   ├─ `requirements.txt`  
│   │   └─ `utils.py`  
│   └── `Form1.cs`  
└── `morseCodeDecoder.sln`  

## Troubleshooting
-  Insure Python and dependencies are installed successfully.
-  Verify Python interpreter path in your C# app matches your system.
- Check webcam access premissions.
- Use the console outputs to debug any issues.
