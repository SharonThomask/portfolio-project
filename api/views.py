from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse

# Create your views here.
class AboutView(View):
    def get(self,request):
        data={
        "ID" : 1234,
        "Full Name" : "SHARON THOMAS",
        "PROFFESSIONAL TITLE" : "PYTHON DEVELOPER",
        "BIO" : "I AM SHARON THOMAS,LIVING AT KOCHI",
        "EMAIL" : "sharonkallarakkal91@gmail.com",
        "CONTACT" : "6231654789",
        "DOB" : "12-12-1991",
        "GITHUB" : "https://github.com/?utm_source=chatgpt.com",
        "LINKEDIN URL" : "https://www.linkedin.com/?utm_source=chatgpt.com",
        }

        return JsonResponse(data)
class EducationView(View):
    def get(self,request):
        data1 = {
            "ID"            : "1235",
            "Institution"   : "Aquinas",
            "Degree/Course" : "B.Sc",
            "University"    : "MG University",
            "Location"      : "Kochi",
            "Start Year"    : "2021",
            "End Year"      : "2025",
            "Grade or CGPA" : "8.00",
            "Description"   : "Active and passionate"
        }
        return JsonResponse(data1)

class ProjectView(View):

    def get(self, request):

        data2 = [
            {
                "id": "12345",
                "title": "Employee Management System",
                "short_description": "Employee record management application.",
                "long_description": "A CRUD application for managing employee details.",
                "technologies_used": "Python, Django, MySQL",
                "live_url": "https://example.com",
                "github_url": "https://github.com/username/employee-management",
                "image_url": "https://example.com/employee.jpg",
                "featured": True
            },

            {
                "id": "12346",
                "title": "Student Management System",
                "short_description": "Application for managing student information.",
                "long_description": "A system to manage student details, courses, marks, and records.",
                "technologies_used": "Python, Django, MySQL, HTML, CSS",
                "live_url": "https://example.com",
                "github_url": "https://github.com/username/student-management",
                "image_url": "https://example.com/student.jpg",
                "featured": True
            },

            {
                "id": "12347",
                "title": "Online Food Ordering System",
                "short_description": "A web application for ordering food online.",
                "long_description": "This project allows customers to browse food items, add products to a cart, place orders, and manage their orders.",
                "technologies_used": "Python, Django, MySQL, HTML, CSS, JavaScript",
                "live_url": "https://example.com",
                "github_url": "https://github.com/username/food-ordering-system",
                "image_url": "https://example.com/food-ordering.jpg",
                "featured": True
            }
        ]

        return JsonResponse(data2, safe=False)

class SkillsView(View):
    def get(self,request):
        data3=[
            {
        "id": "1",
        "skill_name": "Python",
        "category": "Programming",
        "proficiency_level": "Advanced",
        "years_of_experience": 2
    },
    {
        "id": "2",
        "skill_name": "Django",
        "category": "Web Development",
        "proficiency_level": "Intermediate",
        "years_of_experience": 1
    },
    {
        "id": "3",
        "skill_name": "MySQL",
        "category": "Database",
        "proficiency_level": "Intermediate",
        "years_of_experience": 1
    }
        ]
        return JsonResponse(data3,safe=False)

class ExperienceView(View):
    def get(self,request):
        data3 = [
    {
        "id": "1",
        "job_title": "Python Django Developer",
        "company_name": "ABC Technologies",
        "location": "Kochi, Kerala",
        "employment_type": "Full Time",
        "start_date": "2025-06-01",
        "end_date": None,
        "currently_working": True,
        "description": "Developing web applications using Python, Django, MySQL, HTML, CSS, and JavaScript."
    },
    {
        "id": "2",
        "job_title": "Python Developer Intern",
        "company_name": "XYZ Solutions",
        "location": "Kochi, Kerala",
        "employment_type": "Internship",
        "start_date": "2024-06-01",
        "end_date": "2025-05-31",
        "currently_working": False,
        "description": "Worked on Python programming, database management, CRUD operations, and Django web development."
    }
        ]
        return JsonResponse(data3,safe=False)

class CertificationView(View):
    def get(self,request):
        data4 = [
            {
                "id": "1",
        "certification_name": "Python Programming Certification",
        "organisation_name": "Luminar Technolab",
        "issued_year": 2026
    },
    {
        "id": "2",
        "certification_name": "Django Web Development Certification",
        "organisation_name": "Luminar Technolab",
        "issued_year": 2026
    },
    {
        "id": "3",
        "certification_name": "MySQL Database Certification",
        "organisation_name": "Coursera",
        "issued_year": 2025
    }
        ]
        return JsonResponse(data4,safe=False)

class ServiceView(View):
    def get(self,request):
        data5=[
            {
                "id": "1",
        "service_name": "Web Development",
        "description": "Design and development of modern, responsive websites and web applications.",
        "technologies": "Python, Django, HTML, CSS, JavaScript",
        "contact_information": "contact@example.com"
    },
    {
        "id": "2",
        "service_name": "Software Development",
        "description": "Custom software solutions designed to meet business requirements.",
        "technologies": "Python, Django, MySQL",
        "contact_information": "contact@example.com"
    },
    {
        "id": "3",
        "service_name": "Database Management",
        "description": "Database design, development, maintenance, and optimization services.",
        "technologies": "MySQL, SQL, Python",
        "contact_information": "contact@example.com"
    },
            
        ]
        return JsonResponse(data5,safe=False)

