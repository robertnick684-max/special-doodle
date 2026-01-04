from flask import Flask, request, jsonify
import yt_dlp

app = Flask(__name__)

@app.route('/get_video', methods=['POST'])
def get_video():
    url = request.json.get('url')
    ydl_opts = {'format': 'best'}
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        # Returns title, thumbnail, and direct download URL
        return jsonify({
            'title': info.get('title'),
            'thumbnail': info.get('thumbnail'),
            'url': info.get('url')
        })

if __name__ == '__main__':
    app.run(debug=True)
