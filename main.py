from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Social media links
    social_links = {
        'linkedin': 'https://www.linkedin.com/in/emilniclas/',
        'github': 'https://github.com/emilorisit',
        'x': 'https://x.com/your-handle',  # X/Twitter handle not provided yet
        'instagram': 'https://www.instagram.com/emilorisit/',
        'email': 'contact.scheming298@passinbox.com'
    }

    # LinkedIn profile picture URL
    profile_pic = "https://media.licdn.com/dms/image/v2/D4D03AQFVRy2rQSrzWw/profile-displayphoto-shrink_400_400/B4DZOX8YQOHoAk-/0/1733421009251?e=1746057600&v=beta&t=Q_imaNsiec-U7CdO-G45vFt2RpQ3KHUwGRaDrsHdpYg"

    return render_template('index.html', 
                         social_links=social_links,
                         profile_pic=profile_pic)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)