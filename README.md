# local-event-finder-aws-serverless
A serverless web application built using AWS Amplify, Amazon API Gateway, and AWS Lambda that helps users discover local events based on their location and interests. The app integrates with public event APIs and web scraping to populate an events database.
📌 Abstract
This project presents a Local Event Finder Web Application that allows users to discover nearby events such as concerts, workshops, meetups, and festivals based on their location and interests.
The application is built using AWS Amplify for frontend hosting, Amazon API Gateway and AWS Lambda for backend APIs, and integrates public event APIs and web scraping to populate event data.
📌 Problem Statement
Users often struggle to find local events happening around them across multiple platforms. Existing solutions are fragmented and not personalized.
📌 Solution
The proposed system provides a centralized platform where users can discover relevant local events based on location and interest preferences.
📌 Technologies Used
AWS Amplify
Amazon API Gateway
AWS Lambda
DynamoDB
Public Event APIs (Eventbrite / Ticketmaster – conceptual)
Python (Backend)
JavaScript / React (Frontend)
📌 System Architecture
Frontend (AWS Amplify)
        ↓
API Gateway
        ↓
AWS Lambda
        ↓
DynamoDB
        ↑
Public Event APIs + Web Scraper
📌 Advantages
Serverless & scalable
Location-based event discovery
Real-time event updates
Low operational cost
📌 Future Enhancements
User authentication (Cognito)
Event bookmarking
Notification alerts
Mobile app version
📍 Local Event Finder – Serverless Web Application
📖 Overview
Local Event Finder is a serverless web application that helps users discover nearby events based on their location and interests.
The application uses AWS Amplify for frontend hosting, API Gateway and AWS Lambda for backend services, and integrates with public event APIs and web scraping to fetch event data.
🛠️ Tech Stack
AWS Amplify (Frontend Hosting)
Amazon API Gateway
AWS Lambda
Amazon DynamoDB
Public Event APIs
Python
JavaScript (React)
🏗️ Architecture
User Browser
     ↓
AWS Amplify (Frontend)
     ↓
API Gateway
     ↓
AWS Lambda
     ↓
DynamoDB
     ↑
Public Event APIs / Scraper
🚀 Features
Location-based event discovery
Interest-based filtering
Serverless backend APIs
Public event API integration
Event data scraping support
📂 Repository Structure
local-event-finder-aws-serverless/
│
├── README.md
│
├── frontend/
│   ├── index.html
│   ├── app.js
│   └── styles.css
│
├── lambda/
│   ├── get_events.py
│   └── scrape_events.py
│
├── api/
│   └── api-definition.yaml
│
├── database/
│   └── dynamodb-schema.json
│
├── architecture/
│   └── architecture-diagram.png
│
├── report/
│   └── project-report.md
│
└── docs/
    ├── setup-guide.md
    └── workflow.md
    ⚙️ Setup Overview
Deploy frontend using AWS Amplify
Create API Gateway endpoints
Deploy Lambda functions
Create DynamoDB table
Integrate public event APIs
✅ Outcome
Fully serverless event discovery app
Scalable and cost-effective solution
Real-world cloud application
Developed a serverless Local Event Finder web application using AWS Amplify,
API Gateway, and AWS Lambda to provide location-based and interest-based
event discovery with public API integration.
Interview One-Line Explanation
“The frontend is hosted on AWS Amplify, backend APIs are handled by Lambda through API Gateway, and event data is fetched from public APIs and stored in DynamoDB.”
