from flask import Flask, render_template, request, jsonify
from datetime import datetime
import json
import os
from pathlib import Path

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

ACADEMIC_PROJECTS = [
    {
        "id": 1,
        "title": "Sentiment Analysis of Yelp - 3NF Data Engineering",
        "description": "Built a scalable AWS-based data engineering pipeline to process and analyze the Yelp Open Dataset. Transformed 9GB+ nested JSON data into 15 normalized relational tables using 3NF normalization.",
        "tech_stack": ["AWS S3", "AWS EMR", "AWS Glue", "Amazon Athena", "Amazon Redshift", "Python", "Spark", "SQL"],
        "github": "https://github.com/Varma06/YELP-3NF",
        "demo": None,
        "highlights": "9GB+ JSON → 15 normalized tables, Analytics-ready warehouse"
    },
    {
        "id": 2,
        "title": "Data Analysis - Netflix & IPL Datasets",
        "description": "Performed comprehensive Exploratory Data Analysis on Netflix and IPL datasets. Implemented web scraping for live data collection and built predictive dashboards for real-time tracking.",
        "tech_stack": ["Python", "Pandas", "NumPy", "Web Scraping", "Data Visualization", "Dashboards"],
        "github": "https://github.com/Varma06/Netflix-Netflix-TV-Shows-and-Movies-",
        "demo": None,
        "highlights": "Live predictive tracking dashboards"
    },
    {
        "id": 3,
        "title": "Traffic Prediction for Intelligent Transportation System",
        "description": "Developed a real-time traffic prediction system using deep learning (YOLO, CNN) for vehicle detection and counting. Implemented dynamic traffic signal optimization based on vehicle density.",
        "tech_stack": ["Python", "Flask", "YOLO", "CNN", "OpenCV", "MySQL"],
        "github": "https://github.com/Varma06/TRAFFIC-PREDICTION-FOR-INTELLIGENT-TRANSPORTATION-SYSTEM-USING-DEEP-LEARNING",
        "demo": None,
        "highlights": "Real-time vehicle detection & adaptive signal control"
    }
]

PROFESSIONAL_PROJECTS = [
    {
        "id": 4,
        "title": "Access Networks - E2E API Automation Framework",
        "description": "Architected and implemented comprehensive API testing automation for Access Networks. Created intelligent test suite using Python + Robot Framework that auto-generates test cases from API specifications, covering all HTTP methods and back-office field mappings. Integrated with CI/CD pipelines (Jenkins, Concourse, GitHub Actions) for production validation across QA, staging, preprod, and prod environments.",
        "tech_stack": ["Python", "Robot Framework", "Bruno", "Jenkins", "Concourse", "GitHub Actions", "REST APIs", "Schema Validation"],
        "github": None,
        "demo": None,
        "highlights": "Live APIs for Xumo, Xfinity, Rogers | Reduced manual testing by 80% | Automated Slack/Email reporting"
    },
    {
        "id": 5,
        "title": "Real-time Customer Usage Pipeline - AWS",
        "description": "Engineered real-time data processing pipeline to handle customer usage records. Leveraged AWS Step Functions for orchestration, S3 for data storage, and SNS/SQS/Kinesis streams for event-driven processing. Implemented automated validation of back-office data transformations with intelligent alarm triggers for device performance monitoring.",
        "tech_stack": ["AWS Step Functions", "AWS S3", "AWS Lambda", "SNS", "SQS", "Kinesis Streams", "CloudWatch", "Python"],
        "github": None,
        "demo": None,
        "highlights": "Real-time stream processing | Automated device status alerts | End-to-end data validation"
    }
]

PROJECTS = PROFESSIONAL_PROJECTS + ACADEMIC_PROJECTS

EXPERIENCE = [
    {
        "company": "Comcast",
        "position": "SDET (Software Development Engineer in Test)",
        "duration": "August 2025 - Present",
        "location": "Philadelphia, PA",
        "bullets": [
            "Developing software solutions combining backend development and comprehensive testing strategies",
            "Built AI Automation tools that reduce manual effort and organizational costs by streamlining operational workflows"
        ]
    },
    {
        "company": "Charles Schwab",
        "position": "Software Engineer",
        "duration": "July 2024 - July 2025",
        "location": "Irving, Texas",
        "bullets": [
            "Engineered scalable backend services using Python and FastAPI with focus on secure APIs and real-time data pipelines",
            "Refactored legacy Java services into modular Python microservices deployed via Docker and Kubernetes"
        ]
    },
    {
        "company": "Accenture",
        "position": "Software Engineer",
        "duration": "January 2021 - November 2022",
        "location": "Bengaluru, India",
        "bullets": [
            "Led development of cloud-native APIs using Python and Flask for banking systems with AWS deployment",
            "Designed and implemented microservices architecture with PostgreSQL, Elasticsearch, and automated testing using Pytest"
        ]
    }
]

SKILLS = {
    "Programming Languages": ["Python", "Java", "JavaScript", "TypeScript"],
    "Backend Frameworks": ["Django", "Flask", "FastAPI", "Spring Boot", "Node.js"],
    "Frontend Frameworks": ["React", "Angular", "HTML", "CSS"],
    "Databases": ["PostgreSQL", "MySQL", "MongoDB", "DynamoDB", "Redis"],
    "Cloud & Containerization": ["AWS (EC2, Lambda, S3, RDS, ECS, Kinesis, SNS, SQS)", "Docker", "Kubernetes", "Azure", "GCP"],
    "Monitoring & Observability": ["Grafana", "ELK (Elasticsearch)", "CloudWatch Logs", "Splunk", "Prometheus"],
    "API & Messaging": ["REST APIs", "gRPC", "SOAP", "Kafka", "JSON", "XML"],
    "CI/CD & Automation": ["Jenkins", "Git", "GitHub", "Terraform", "Ansible", "Selenium", "Pytest"],
    "Testing & SDLC": ["TDD", "BDD", "Unit Testing", "Functional Testing", "Regression Testing", "Integration Testing", "E2E Testing", "CI/CD"],
    "Tools & IDEs": ["IntelliJ IDEA", "Eclipse", "Visual Studio Code", "Linux/Unix", "Windows"]
}

@app.route('/')
def index():
    return render_template('index.html', 
                         projects=PROJECTS,
                         experience=EXPERIENCE,
                         skills=SKILLS)

@app.route('/api/contact', methods=['POST'])
def contact():
    try:
        data = request.get_json()
        
        name = data.get('name', '').strip()
        email = data.get('email', '').strip()
        message = data.get('message', '').strip()
        
        if not all([name, email, message]):
            return jsonify({
                'success': False,
                'error': 'Please fill in all fields'
            }), 400
        
        if '@' not in email or '.' not in email:
            return jsonify({
                'success': False,
                'error': 'Please enter a valid email address'
            }), 400
        
        if len(message) < 10:
            return jsonify({
                'success': False,
                'error': 'Message must be at least 10 characters long'
            }), 400
        
        contact_log = {
            'timestamp': datetime.now().isoformat(),
            'name': name,
            'email': email,
            'message': message
        }
        
        logs_dir = Path('logs')
        logs_dir.mkdir(exist_ok=True)
        
        with open(logs_dir / 'contacts.log', 'a') as f:
            f.write(json.dumps(contact_log) + '\n')
        
        return jsonify({
            'success': True,
            'message': 'Thank you! I\'ll get back to you soon.'
        }), 200
        
    except Exception as e:
        print(f"Error processing contact form: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'An error occurred. Please try again later.'
        }), 500

@app.route('/api/projects', methods=['GET'])
def get_projects():
    return jsonify({
        'success': True,
        'projects': PROJECTS
    }), 200

@app.route('/api/resume-download', methods=['GET'])
def resume_download():
    resume_path = Path('static/resume/resume.pdf')
    if resume_path.exists():
        return jsonify({
            'success': True,
            'download_path': '/static/resume/resume.pdf'
        }), 200
    else:
        return jsonify({
            'success': False,
            'error': 'Resume file not found'
        }), 404

@app.errorhandler(404)
def page_not_found(e):
    return render_template('base.html'), 404

@app.errorhandler(500)
def internal_error(e):
    print(f"Internal server error: {str(e)}")
    return jsonify({
        'success': False,
        'error': 'Internal server error'
    }), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
