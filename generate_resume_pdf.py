from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from datetime import datetime

pdf_path = 'static/resume/resume.pdf'
doc = SimpleDocTemplate(pdf_path, pagesize=letter, topMargin=0.5*inch, bottomMargin=0.5*inch)
story = []

styles = getSampleStyleSheet()
title_style = ParagraphStyle(
    'CustomTitle',
    parent=styles['Heading1'],
    fontSize=24,
    textColor=colors.HexColor('#4F46E5'),
    spaceAfter=6,
    alignment=TA_CENTER,
    fontName='Helvetica-Bold'
)

subtitle_style = ParagraphStyle(
    'CustomSubtitle',
    parent=styles['Normal'],
    fontSize=11,
    textColor=colors.HexColor('#666666'),
    alignment=TA_CENTER,
    spaceAfter=3,
    fontName='Helvetica'
)

section_style = ParagraphStyle(
    'SectionHeading',
    parent=styles['Heading2'],
    fontSize=12,
    textColor=colors.HexColor('#4F46E5'),
    spaceAfter=8,
    spaceBefore=8,
    fontName='Helvetica-Bold',
    borderPadding=5,
    borderColor=colors.HexColor('#A855F7'),
    borderWidth=0,
    textTransform='uppercase',
)

normal_style = ParagraphStyle(
    'CustomNormal',
    parent=styles['Normal'],
    fontSize=10,
    textColor=colors.HexColor('#333333'),
    spaceAfter=4,
    leading=12
)

story.append(Paragraph("NAVEEN VARMA PANDETI", title_style))
story.append(Paragraph("Software Developer | Python | AWS | SDET", subtitle_style))
story.append(Paragraph("📧 varmanaveen66@gmail.com | 🔗 <a href='https://github.com/Varma06'>GitHub</a> | 💼 <a href='https://linkedin.com/in/naveen-varma-pandeti-3527a1204/'>LinkedIn</a>", subtitle_style))
story.append(Spacer(1, 0.15*inch))

story.append(Paragraph("PROFESSIONAL SUMMARY", section_style))
summary_text = "Experienced Software Developer with 4+ years of expertise in building scalable backend systems, cloud-native applications, and AI-driven automation solutions. Proven track record in Python development, AWS cloud infrastructure, and end-to-end test automation. Passionate about designing reliable systems that meet real-world business needs and solving complex technical challenges."
story.append(Paragraph(summary_text, normal_style))
story.append(Spacer(1, 0.1*inch))

story.append(Paragraph("PROFESSIONAL EXPERIENCE", section_style))

exp_data = [
    {
        'title': 'Software Development Engineer in Test (SDET)',
        'company': 'Comcast',
        'duration': 'August 2025 - Present',
        'location': 'Philadelphia, PA',
        'bullets': [
            'Developing full-stack solutions combining backend development and comprehensive testing strategies',
            'Building AI Automation tools that reduce manual effort and organizational costs'
        ]
    },
    {
        'title': 'Software Engineer',
        'company': 'Charles Schwab',
        'duration': 'July 2024 - July 2025',
        'location': 'Irving, Texas',
        'bullets': [
            'Engineered scalable backend services using Python and FastAPI',
            'Refactored legacy Java services into modular Python microservices with Docker and Kubernetes'
        ]
    },
    {
        'title': 'Software Engineer',
        'company': 'Accenture',
        'duration': 'January 2021 - November 2022',
        'location': 'Bengaluru, India',
        'bullets': [
            'Led development of cloud-native APIs using Python and Flask for banking systems',
            'Designed microservices architecture with PostgreSQL, Elasticsearch, and Pytest'
        ]
    }
]

for exp in exp_data:
    header = f"<b>{exp['title']}</b> | {exp['company']} | {exp['duration']}"
    story.append(Paragraph(header, normal_style))
    story.append(Paragraph(f"<i>{exp['location']}</i>", normal_style))
    for bullet in exp['bullets']:
        story.append(Paragraph(f"• {bullet}", normal_style))
    story.append(Spacer(1, 0.08*inch))

story.append(Spacer(1, 0.1*inch))

story.append(Paragraph("KEY PROJECTS", section_style))

projects = [
    {
        'title': 'Access Networks - E2E API Automation Framework',
        'tech': 'Python, Robot Framework, Bruno, Jenkins, GitHub Actions',
        'desc': 'Architected API testing automation with auto-generated test cases, CI/CD integration, 80% manual testing reduction'
    },
    {
        'title': 'Real-time Customer Usage Pipeline - AWS',
        'tech': 'AWS Step Functions, Lambda, S3, SNS, SQS, Kinesis',
        'desc': 'Real-time data processing pipeline with automated validation and device performance monitoring'
    },
    {
        'title': 'Sentiment Analysis of Yelp - Data Engineering',
        'tech': 'AWS S3, EMR, Glue, Athena, Redshift, Spark',
        'desc': 'Transformed 9GB+ JSON data into 15 normalized tables, analytics-ready warehouse'
    }
]

for proj in projects:
    story.append(Paragraph(f"<b>{proj['title']}</b>", normal_style))
    story.append(Paragraph(f"<i>{proj['tech']}</i>", normal_style))
    story.append(Paragraph(proj['desc'], normal_style))
    story.append(Spacer(1, 0.08*inch))

story.append(Spacer(1, 0.1*inch))

story.append(Paragraph("TECHNICAL SKILLS", section_style))

skills_text = """
<b>Languages:</b> Python, Java, JavaScript, TypeScript<br/>
<b>Backend:</b> Django, Flask, FastAPI, Spring Boot, Node.js<br/>
<b>Databases:</b> PostgreSQL, MySQL, MongoDB, DynamoDB, Redis<br/>
<b>Cloud:</b> AWS (EC2, Lambda, S3, RDS, ECS, Kinesis, SNS, SQS), Docker, Kubernetes<br/>
<b>Testing:</b> TDD, BDD, Unit Testing, E2E Testing, Robot Framework, Selenium, Pytest<br/>
<b>DevOps:</b> Jenkins, Git, GitHub, Terraform, Ansible<br/>
<b>Tools:</b> IntelliJ IDEA, VS Code, Linux/Unix, CloudWatch, Grafana, ELK
"""
story.append(Paragraph(skills_text, normal_style))

# Build PDF
doc.build(story)
print(f"✅ Resume PDF generated: {pdf_path}")
