# ☁️ AWS Serverless Cloud Resume

A fully functional, serverless portfolio website hosted on AWS. This project demonstrates my ability to design and implement a decoupled cloud architecture using industry best practices.

## 🔗 [View Live Portfolio](http://chills-cloud-resume-2026.s3-website-us-east-1.amazonaws.com)

---

## 🏗️ The Architecture
The project follows a serverless "Event-Driven" pattern:
- **Frontend**: **Amazon S3** (Static Hosting) + **CloudFront** (Global Delivery).
- **API**: **Amazon API Gateway** acting as a secure bridge.
- **Compute**: **AWS Lambda** (Python/Boto3) processing visitor logic.
- **Database**: **Amazon DynamoDB** for persistent visitor tracking.
- **Security**: **IAM Roles** with Least Privilege access.

---

## 📸 Project Journey

### 1. The Design Phase
I started with a simple HTML site. During the initial S3 hosting, I successfully resolved a **403 Forbidden Access** error by implementing a JSON Bucket Policy.
![S3 Error Fix](./screenshots/error.png)

### 2. The Backend Integration
I built a RESTful API to communicate with my Python Lambda function. Below is the JSON response verifying that the database is updating correctly.
![Backend Verification](./screenshots/backend.png)

### 3. The Final Result
The result is a professional, high-performance portfolio with a live visitor counter.
![Final Site](./screenshots/final_site.png)

---

## 🧠 Key Learnings
- **CORS Management**: Handled Cross-Origin Resource Sharing (CORS) between different AWS domains.
- **Python Boto3**: Used the AWS SDK for Python to interact with DynamoDB.
- **Cloud Security**: Implemented IAM policies for secure service-to-service communication.
