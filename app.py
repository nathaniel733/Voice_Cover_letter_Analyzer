from flask import Flask, render_template, request
import os
from utils.extract_audio import extract_audio
from utils.transcribe_audio import transcribe_audio
from utils.summarize_text import summarize_text
from utils.parse_resume import parse_resume
from utils.text_analysis import analyze_text

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

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
            
            # Process video
            audio_path = extract_audio(video_path)
            transcribed_text = transcribe_audio(audio_path)
            summarized_text = summarize_text(transcribed_text)

            # Analyze text
            analysis_results, key_phrases = analyze_text(transcribed_text)

            # Process resume
            resume_data = parse_resume(resume_path)

            # Render results
            return render_template(
                "result.html",
                transcribed_text=transcribed_text,
                summarized_text=summarized_text,
                analysis_results=analysis_results,
                key_phrases=key_phrases,
                resume_data=resume_data
            )
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
