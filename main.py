from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Social media links
    social_links = {
        'linkedin': 'https://linkedin.com/in/your-profile',
        'github': 'https://github.com/your-username',
        'twitter': 'https://twitter.com/your-handle',
    }
    
    # LinkedIn profile picture URL (replace with actual URL)
    profile_pic = "https://via.placeholder.com/150"
    
    return render_template('index.html', 
                         social_links=social_links,
                         profile_pic=profile_pic)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
