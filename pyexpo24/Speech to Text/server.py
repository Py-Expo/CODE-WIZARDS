import json
import pymysql
from http.server import BaseHTTPRequestHandler, HTTPServer
from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer

# Database connection configuration
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "Gokul@sgr123"
DB_NAME = "firstproject"

def connect_db():
    return pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME)

class CORSRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open(r'C:\Users\Gokul Ramm\Desktop\pyexpo24\Speech to Text\templates\index.html', 'rb') as file:
                self.wfile.write(file.read())
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data.decode('utf-8'))
        transcribed_text = data['transcribedText']
        user_id = data['userId']  # Assuming you'll send the userId from the frontend

        # Load medical-specific model and tokenizer
        model_name = "emilyalsentzer/Bio_ClinicalBERT"
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForCausalLM.from_pretrained(model_name)
        medical_pipeline = pipeline("text-generation", model=model, tokenizer=tokenizer)

        # Generate text based on the transcribed audio
        generated_text = medical_pipeline(transcribed_text, max_length=100)[0]["generated_text"]

        # Save the transcribed text in the database
        db = connect_db()
        cursor = db.cursor()
        cursor.execute("INSERT INTO transcriptions (user_id, transcribed_text) VALUES (%s, %s)", (user_id, generated_text))
        db.commit()
        db.close()

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps({'generatedText': generated_text}).encode('utf-8'))

def run_server():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, CORSRequestHandler)
    print('Server running at http://localhost:8000/')
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()
