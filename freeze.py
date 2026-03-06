from flask_frozen import Freezer
from app import app
import os
import shutil

# GitHub Pages expects deployment in the root or a dedicated branch
# We will generate static files into the 'build' directory
app.config['FREEZER_DESTINATION'] = 'build'
# Helps generate relative links for GitHub pages where base path is repo name
app.config['FREEZER_RELATIVE_URLS'] = True

freezer = Freezer(app)

if __name__ == '__main__':
    # Build the static site
    freezer.freeze()
    print("Static site built successfully in the 'build/' directory.")

    # CNAME handling (if any custom domain is used in future)
    # with open('build/CNAME', 'w') as f:
    #     f.write('yourdomain.com')
    
    # We should also copy over the resume PDF specifically as Frozen-Flask 
    # might miss static files not directly linked via url_for() in a certain way
    if not os.path.exists('build/static/resume'):
        os.makedirs('build/static/resume', exist_ok=True)
    if os.path.exists('static/resume/resume.pdf'):
        shutil.copy('static/resume/resume.pdf', 'build/static/resume/resume.pdf')
    if os.path.exists('static/resume/resume.html'):
        shutil.copy('static/resume/resume.html', 'build/static/resume/resume.html')
