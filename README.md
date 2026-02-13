# Naveen Varma Pandeti - Premium Portfolio Website

A modern, production-ready personal portfolio website built with Flask, Tailwind CSS, and modern UI/UX principles. Designed to showcase Python backend engineering, AWS cloud architecture, SDET expertise, and AI automation solutions.

## 🎨 Features

✅ **Modern Design**
- Dark theme with animated gradients (blue/purple tech aesthetic)
- Smooth scroll animations and transitions
- Fully responsive (mobile-first approach)
- Premium SaaS-like design inspiration (Stripe, Vercel, Notion)

✅ **Interactive Sections**
- Full-screen hero with animated background
- About me with highlight cards
- Categorized skills with hover effects
- Dynamic project showcase with tech stack badges
- Professional experience timeline
- Contact form with validation
- Footer with social links

✅ **Performance & SEO**
- SEO meta tags and structured data
- Fast load times with optimized assets
- Clean HTML/CSS/JavaScript
- Favicon support
- Smooth scrolling behavior

✅ **Backend**
- Flask-based API routes
- Contact form submission with validation
- Dynamic content loading from Python lists
- Error handling and logging
- Production-ready structure

## 📁 Project Structure

```
portfolio/
├── app.py                          # Flask application & routes
├── requirements.txt                # Python dependencies
├── README.md                       # This file
├── static/
│   ├── css/
│   │   └── style.css               # Custom animations & styles
│   ├── images/                     # Profile pics, project screenshots
│   └── resume/
│       └── resume.pdf              # Downloadable resume (add yours)
└── templates/
    ├── base.html                   # Base template with navigation
    └── index.html                  # Main portfolio page
```

## 🚀 Quick Start (Local Development)

### Prerequisites
- Python 3.8+
- pip (Python package manager)
- Git (optional)

### Installation Steps

1. **Clone or create the project directory**
   ```bash
   cd ~/Desktop
   mkdir portfolio && cd portfolio
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Add your resume**
   - Place your resume PDF in `static/resume/resume.pdf`

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Access the portfolio**
   - Open browser to `http://localhost:5000`
   - Hot reload enabled for development

### Development Tips

- **Edit content**: Modify `PROJECTS`, `EXPERIENCE`, `SKILLS` in `app.py`
- **Customize styling**: Update `static/css/style.css`
- **Add social links**: Update footer in `templates/index.html`
- **Contact emails**: Update contact form handler in `app.py`

## 📝 Customization Guide

### Update Personal Information

**In `app.py`:**
- Update `PROJECTS` list with your projects
- Update `EXPERIENCE` list with your work history
- Update `SKILLS` dictionary with your technical skills

**In `templates/index.html`:**
- Footer contact info (email, LinkedIn, GitHub)
- About me content
- Any personal branding

### Modify Colors & Styling

**Primary colors**: Edit `static/css/style.css`
- Primary: Indigo (`#4f46e5`)
- Secondary: Purple (`#a855f7`)
- Accent: Cyan (`#06b6d4`)

Or use Tailwind's built-in color utilities directly in HTML.

### Add Favicon

Replace the inline favicon SVG in `templates/base.html`:
```html
<link rel="icon" type="image/x-icon" href="static/images/favicon.ico">
```

## 🌐 Deployment Guide

### Option 1: Render.com (Recommended - Free tier available)

1. **Push to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial portfolio"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/portfolio.git
   git push -u origin main
   ```

2. **Create account at render.com**
   - Sign up with GitHub

3. **Create New Web Service**
   - Connect your GitHub repository
   - Runtime: Python 3.11
   - Build command: `pip install -r requirements.txt`
   - Start command: `gunicorn app:app`
   - Environment variables: None needed for basic setup

4. **Deploy**
   - Click "Deploy"
   - Wait for deployment to complete (~2-5 min)
   - Your portfolio is live! 🎉

**Live URL**: `https://your-portfolio.onrender.com`

### Option 2: Railway.app

1. **Connect GitHub repository**
   - Sign in at railway.app
   - Click "New Project" → "Deploy from GitHub repo"

2. **Configuration**
   - Railway auto-detects Flask + Python
   - Build: `pip install -r requirements.txt`
   - Start: `gunicorn app:app`

3. **Environment Variables**
   - No required variables for basic setup

4. **Deploy**
   - Railway automatically deploys on push
   - Access via provided Railway domain

### Option 3: AWS EC2

#### Setup EC2 Instance (Ubuntu 22.04 LTS - Free t2.micro)

1. **Launch Instance**
   ```bash
   # Connect via SSH and run:
   sudo apt update && sudo apt upgrade -y
   sudo apt install python3-pip python3-venv nginx git -y
   ```

2. **Clone your repository**
   ```bash
   cd /var/www
   sudo git clone https://github.com/YOUR_USERNAME/portfolio.git
   cd portfolio
   sudo python3 -m venv venv
   source venv/bin/activate
   sudo pip install -r requirements.txt
   ```

3. **Setup Gunicorn**
   ```bash
   # Create systemd service file
   sudo nano /etc/systemd/system/portfolio.service
   ```

   Add:
   ```
   [Unit]
   Description=Portfolio Flask App
   After=network.target

   [Service]
   User=ubuntu
   WorkingDirectory=/var/www/portfolio
   ExecStart=/var/www/portfolio/venv/bin/gunicorn -w 4 -b 127.0.0.1:5000 app:app
   Restart=always

   [Install]
   WantedBy=multi-user.target
   ```

4. **Start Service**
   ```bash
   sudo systemctl daemon-reload
   sudo systemctl start portfolio
   sudo systemctl enable portfolio
   ```

5. **Configure Nginx** (Reverse proxy)
   ```bash
   sudo nano /etc/nginx/sites-available/portfolio
   ```

   Add:
   ```nginx
   server {
       listen 80;
       server_name your-domain.com;

       location / {
           proxy_pass http://127.0.0.1:5000;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
       }
   }
   ```

6. **Enable Nginx site**
   ```bash
   sudo ln -s /etc/nginx/sites-available/portfolio /etc/nginx/sites-enabled/
   sudo nginx -t
   sudo systemctl restart nginx
   ```

7. **Setup SSL with Let's Encrypt**
   ```bash
   sudo apt install certbot python3-certbot-nginx -y
   sudo certbot --nginx -d your-domain.com
   ```

## 🌍 Custom Domain Setup

### For Render.com

1. Go to Render Dashboard → Select your service
2. Settings → Custom Domain
3. Add your domain (e.g., `portfolio.naveenvp.dev`)
4. Follow DNS configuration steps
5. Point your domain provider DNS to Render nameservers

### For AWS EC2

1. Go to Route 53 or your DNS provider
2. Create A record pointing to your EC2 Elastic IP
3. Update Nginx server_name with your domain
4. Test with `curl http://your-domain.com`

### For Railway.app

1. Settings → Custom Domain
2. Add your domain
3. Update DNS A record to Railway IP address

## 📊 Environment Variables (Production)

Create `.env` file for production:
```
FLASK_ENV=production
FLASK_DEBUG=False
SECRET_KEY=your-secret-key-here
```

Load in `app.py`:
```python
from dotenv import load_dotenv
import os

load_dotenv()
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-key')
```

## 📧 Email Integration (Optional)

To enable email notifications for contact form:

1. **Install Flask-Mail**
   ```bash
   pip install Flask-Mail
   ```

2. **Update `app.py`**
   ```python
   from flask_mail import Mail, Message

   app.config['MAIL_SERVER'] = 'smtp.gmail.com'
   app.config['MAIL_PORT'] = 587
   app.config['MAIL_USE_TLS'] = True
   app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
   app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
   mail = Mail(app)
   ```

3. **Update contact route** to send email

## 🔍 SEO Optimization

The portfolio includes:
- ✅ Meta tags and OG tags
- ✅ Semantic HTML structure
- ✅ Mobile responsiveness
- ✅ Fast load times
- ✅ Clean URL structure
- ✅ Favicon

Submit to search engines:
- [Google Search Console](https://search.google.com/search-console)
- [Bing Webmaster Tools](https://www.bing.com/webmasters)

## 🎯 Performance Tips

1. **Compress images**
   - Use tools like TinyPNG for project screenshots
   - Convert to WebP format

2. **Cache headers**
   ```python
   @app.after_request
   def set_cache_headers(response):
       response.cache_control.max_age = 3600  # 1 hour
       return response
   ```

3. **CDN**
   - Images served from Cloudinary or similar
   - Static files from CDN network

4. **Database** (Future upgrades)
   - Connect to PostgreSQL for projects/experience data
   - Implement caching with Redis

## 📱 Social Media Integration

Update links in `templates/index.html`:
- GitHub: `https://github.com/YOUR_USERNAME`
- LinkedIn: `https://linkedin.com/in/YOUR_PROFILE`
- Twitter: `https://twitter.com/YOUR_HANDLE`
- Email: `mailto:your@email.com`

## 🐛 Troubleshooting

**Issue: 404 errors on routes**
- Ensure Flask is running (`python app.py`)
- Check file structure matches project layout
- Clear browser cache

**Issue: Styles not loading**
- Verify `style.css` path is correct
- Check Tailwind CDN is accessible
- Open browser DevTools console

**Issue: Contact form not submitting**
- Check browser console for JS errors
- Verify `/api/contact` route in Flask app
- Check network tab in DevTools

**Issue: Resume not downloading**
- Ensure `resume.pdf` exists in `static/resume/`
- Check file permissions
- Try different browser

## 📈 Analytics (Optional)

Add Google Analytics:
```html
<!-- In base.html, before </head> -->
<script async src="https://www.googletagmanager.com/gtag/js?id=YOUR_GA_ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'YOUR_GA_ID');
</script>
```

## 🎓 Learning Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Tailwind CSS](https://tailwindcss.com/docs)
- [Jinja2 Templates](https://jinja.palletsprojects.com/)
- [Python Best Practices](https://pep8.org/)

## 📄 License

Free to use and modify for personal use.

## 🙌 Support

For issues or questions:
1. Check troubleshooting section
2. Review code comments
3. Consult Flask/Tailwind documentation
4. Contact: naveen@example.com

---

**Built with ❤️ using Python, Flask & Tailwind CSS**

Last Updated: February 12, 2026
