from flask import Flask, render_template, request, redirect, url_for
import os
from utils.extract_audio import extract_audio
from utils.transcribe_audio import transcribe_audio
from utils.summarize_text import summarize_text
from utils.parse_resume import parse_resume

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

# Route for the homepage with file upload forms
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        video_file = request.files.get('video')
        resume_file = request.files.get('resume')
        
        if video_file and resume_file:
            video_path = os.path.join(app.config['UPLOAD_FOLDER'], video_file.filename)
            resume_path = os.path.join(app.config['UPLOAD_FOLDER'], resume_file.filename)
            video_file.save(video_path)
            resume_file.save(resume_path)
            
            # Extract, transcribe, and summarize the video cover letter
            audio_path = extract_audio(video_path)
            transcribed_text = transcribe_audio(audio_path)
            summarized_text = summarize_text(transcribed_text)

            # Parse the resume for contact details and skills
            resume_data = parse_resume(resume_path)

            # Render results on a separate page
            return render_template("result.html", transcribed_text=transcribed_text, summarized_text=summarized_text, resume_data=resume_data)
        
    return render_template('index.html')

# Route to display results
@app.route('/result')
def result():
    return render_template('result.html')

if __name__ == '__main__':
    app.run(debug=True)
