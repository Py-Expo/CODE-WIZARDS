**Speech-to-Text Medical Transcription Server**


This project is a Speech-to-Text Medical Transcription Server built using Python. It transcribes medical audio recordings, performs text generation, corrects spelling mistakes, and saves the transcribed text into a database.

Features:
Speech-to-Text Transcription: Utilizes a pre-trained model to transcribe medical audio recordings into text format.

Text Generation: Generates additional medical text based on the transcribed audio using a pre-trained model.

Spelling Correction: Corrects spelling mistakes in the generated text.

Database Integration: Stores the transcribed text in a MySQL database.

User Authentication: Provides user authentication for accessing the transcription server.

Prerequisites:

Python 3.x
transformers library
pymysql library
spellchecker library
flask library
Installation:

Clone the repository:

```
git clone <repository-url>
cd <repository-directory>
```

Install dependencies:

```
pip install transformers pymysql spellchecker flask
```

Set up MySQL:

Ensure you have MySQL installed and running.
Create a database and a user with appropriate privileges.
Update the database connection configuration in the code (DB_HOST, DB_USER, DB_PASSWORD, DB_NAME).

Usage:

Run the Flask server:

```
python app.py
```

Access the application via a web browser:

```
Open http://localhost:5000 in your web browser.
```

Login or register a new user.

Authenticate using your credentials.

Once authenticated, the server will start running at http://localhost:8000.

The client-side will automatically open in your default web browser.

Provide the required audio input for transcription.
