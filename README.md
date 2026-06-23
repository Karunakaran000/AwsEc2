# AWS Highly Available Web Application using ALB and Auto Scaling Group

## Objective

Deploy a highly available web application in AWS using private EC2 instances behind an Application Load Balancer (ALB), with Auto Scaling Group (ASG) for automatic scaling and NAT Gateway for outbound internet access.

---

## Architecture

Internet Users
↓
Application Load Balancer (Public Subnets)
↓
Target Group
↓
Auto Scaling Group
↓
EC2 Instances (Private Subnets)
↓
NAT Gateway
↓
Internet

---

## VPC Configuration

### VPC

* Name: aws-vpc

### Subnets

#### Public Subnets

* Public Subnet A (ap-south-1a)
* Public Subnet B (ap-south-1b)

#### Private Application Subnets

* Private App Subnet A1
* Private App Subnet B1

#### Private Database Subnets

* Private DB Subnet A2
* Private DB Subnet B2

Total Subnets: 6

---

## Route Tables

### Public Route Table

Routes:

* VPC CIDR → local
* 0.0.0.0/0 → Internet Gateway

Associated with:

* Public Subnet A
* Public Subnet B

### Private Route Table A

Routes:

* VPC CIDR → local
* 0.0.0.0/0 → NAT Gateway

Associated with:

* Private App Subnet A1
* Private DB Subnet A2

### Private Route Table B

Routes:

* VPC CIDR → local
* 0.0.0.0/0 → NAT Gateway

Associated with:

* Private App Subnet B1
* Private DB Subnet B2

---

## Internet Connectivity

### Internet Gateway

Attached to VPC.

Purpose:

* Public internet access for ALB and NAT Gateway.

### NAT Gateway

* Deployed in Public Subnet.
* Elastic IP attached.

Purpose:

* Allows private EC2 instances to access the internet.
* Supports package installation and updates.
* Blocks inbound internet access to private instances.

Verified by:

* apt update
* apt install apache2-utils

from private EC2 instances.

---

## Security Groups

### ALB Security Group

Inbound:

* HTTP (80) from Anywhere
* HTTPS (443) from Anywhere

Outbound:

* All traffic

### Application Security Group

Inbound:

* TCP 3002 from ALB Security Group

Outbound:

* All traffic

### Database Security Group

Inbound:

* Database port from Application Security Group only

Outbound:

* Restricted as required

---

## Application Deployment

### Application

* Flask Application

Listening Port:

* 3002

### User Data

Responsibilities:

* Update packages
* Install Python
* Install dependencies
* Deploy application
* Start application automatically

Logging enabled:

```bash
exec > >(tee /var/log/user-data.log)
exec 2>&1
```

Purpose:

* Capture user data execution logs.

---

## Launch Template

Configured:

* Ubuntu AMI
* Instance Type
* EBS Volume
* Security Group
* IAM Role
* User Data Script

Not Configured:

* Key Pair

Reason:

* Access provided through AWS Systems Manager (SSM).

---

## IAM Role

Attached Policies:

* AmazonSSMManagedInstanceCore

Purpose:

* Session Manager access
* Secure administration without SSH

---

## Load Balancer

### Application Load Balancer

Deployed in:

* Public Subnet A
* Public Subnet B

Listener:

* HTTP 80

---

## Target Group

Target Type:

* Instance

Protocol:

* HTTP

Port:

* 3002

Health Check Path:

* /

Issue Encountered:

Health Check Path initially configured as:

/health

Result:

404 returned

Targets marked unhealthy.

Resolution:

Changed health check path to:

/

Targets became healthy.

---

## Auto Scaling Group

Configuration:

* Minimum Capacity = 2
* Desired Capacity = 2
* Maximum Capacity = 6

Health Check Type:

* ELB

Instances launched in:

* Private App Subnets

---

## Scaling Policy

Target Tracking Policy

Metric:

* Average CPU Utilization

Target:

* 60%

---

## Validation Performed

### Load Balancer Validation

Verified:

* Application accessible using ALB DNS Name.

### Health Check Validation

Verified:

* Targets healthy.

### Auto Scaling Validation

Generated load using ApacheBench:

```bash
ab -n 100000 -c 100 http://ALB-DNS/
```

Observed:

* Scale Out from 2 instances to 5 instances.

After stopping load:

Observed:

* Scale In from 5 instances back to 2 instances.

### NAT Gateway Validation

Verified:

```bash
sudo apt update
sudo apt install apache2-utils
```

from private EC2 instances.

Confirmed outbound internet access through NAT Gateway.

---

## Challenges Faced

### Unhealthy Targets

Issue:

* Health checks failing.

Cause:

* Incorrect health check path.

Fix:

* Changed health check path to valid endpoint.

### Intermittent 502 Errors

Cause:

* Targets transitioning between healthy and unhealthy states during testing.

Resolved after correcting health checks.

### Auto Scaling Not Triggering Initially

Cause:

* CPU utilization did not exceed target threshold.

Resolved after generating sufficient traffic.

---

## Current Status

Working Successfully:

* VPC
* Public and Private Subnets
* Route Tables
* Internet Gateway
* NAT Gateway
* Security Groups
* SSM Access
* Launch Template
* Application Load Balancer
* Target Group
* Auto Scaling Group
* Health Checks
* Scale Out
* Scale In

---

## Future Enhancements

Not Yet Implemented:

* RDS Database
* Multi-AZ RDS
* ACM SSL Certificate
* HTTPS Listener
* Route 53
* CloudWatch Dashboard
* CloudWatch Alarms
* VPC Endpoints
* WAF
* CI/CD Pipeline
* Infrastructure as Code (Terraform / CloudFormation)
* Containerization (Docker)
* ECS / EKS
