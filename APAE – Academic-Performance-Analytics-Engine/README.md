# APAE – Academic Performance Analytics Engine

## Project Overview
APAE (Academic Performance Analytics Engine) is a Python & SQLite based academic data analysis system designed to go beyond basic record management.  
While traditional student management systems focus mainly on CRUD operations, APAE emphasizes **data analysis, performance insights, and decision support** for academic institutions.

This project allows users to store student academic data and generate meaningful analytics such as rankings, performance summaries, risk identification, and course-wise insights.

---

## Motivation
After building a basic Student Management System and an advanced Academic Records Management System (ARMS), this project was developed to explore **analytics-driven academic systems**.

The goal was to move away from only menu-based CRUD logic and focus more on:
- analyzing stored data
- comparing student performance
- generating academic insights
- simulating real-world academic decision-making

APAE represents a more analytical and insight-oriented approach to academic data handling.

---

## Features

### Core Data Management
- Add new student records
- Update existing student details
- Delete a student record
- View all students in a structured format
- Search students by ID or name
- Persistent data storage using SQLite

### Analytics & Insights Module
- Generate top-performing students based on marks
- Identify students at academic risk
- Course-wise average performance analysis
- Ranking system for students
- Performance comparison across multiple students
- Summary insights based on stored academic data

---

## Tech Stack
- Programming Language: Python
- Database: SQLite (sqlite3)
- Interface: Console-based (CLI)
- Storage: Relational database with permanent persistence

---

## Concepts Used
- SQL CRUD operations
- Python–SQL integration
- Data aggregation and comparison
- Conditional analysis
- Modular programming structure
- Input validation and exception-safe database handling

---

## Database Schema

**Table Name:** records

| Field Name   | Description |
|-------------|------------|
| student_id  | Primary key (Auto Increment) |
| name        | Student name |
| age         | Student age |
| course      | Enrolled course |
| marks       | Academic score |

---

## How This Project Is Different
Unlike traditional student management systems, APAE focuses on **academic performance analytics** rather than only data storage.  
It provides insights that can help identify trends, risks, and top performers, making it more aligned with real academic evaluation systems.

---

## Author
**SHREYANSH PATEL**

---

## Future Enhancements
- Export analytics reports
- Grade-based classification
- Graphical visualization of performance data
- Role-based access (admin / faculty)
- Web or GUI-based interface
