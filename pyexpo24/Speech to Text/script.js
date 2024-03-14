function startRecognition() {
    recognition = new webkitSpeechRecognition() || new SpeechRecognition();
    recognition.continuous = true;
    recognition.interimResults = true;
    recognition.lang = 'en-US'; // Change the language code as needed

    let processedTranscript = ''; // Variable to store processed transcript

    recognition.onresult = function(event) {
        let interimTranscript = '';
        for (let i = event.resultIndex; i < event.results.length; i++) {
            if (event.results[i].isFinal) {
                interimTranscript += event.results[i][0].transcript + ' ';
            }
        }
        if (interimTranscript !== '') {
            // Process the transcript for special commands
            interimTranscript = processSpecialCommands(interimTranscript);
            processedTranscript += interimTranscript;
            // Append transcribed text separately from the "Diagnosis:" label
            output.innerHTML += '<p><strong>Transcribed Text:</strong> Diagnosis: ' + processedTranscript + '</p>';
            fetch('/generate_text', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({transcribedText: processedTranscript})
            })
            .then(response => response.json())
            .then(data => {
                output.innerHTML += '<p><strong>Generated Text:</strong> ' + data.generatedText + '</p>';
                outputContainer.scrollTop = outputContainer.scrollHeight;
            })
            .catch(error => console.error('Error:', error));
        }
    };

    recognition.onstart = function() {
        startBtn.textContent = 'Stop Recording';
    };

    recognition.onend = function() {
        startBtn.textContent = 'Start Recording';
    };

    recognition.start();
}
