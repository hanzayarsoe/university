from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.contrib import messages
from django.conf import settings
from django.core.paginator import Paginator
from app.models import ImageShowcase, ServiceSection, AcademicMember, AcademicDepartment, ManagementMember, ManagementDepartment, Blog, Testimonial, ContactMessage, Course, CourseCategory

# Create your views here.


def index(request):
    images = ImageShowcase.objects.all()
    service_sections = ServiceSection.objects.all()
    try:
        department = AcademicDepartment.objects.get(name="Executive")
    except AcademicDepartment.DoesNotExist:
        department = None
    members = AcademicMember.objects.filter(
        academic_department__name="Executive").order_by('order')
    blogs = Blog.objects.all().order_by('-created_at')[:3]
    testimonials = Testimonial.objects.all()

    for index, blog in enumerate(blogs):
        blog.delay = index * 0.2

    for index, service_section in enumerate(service_sections):
        service_section.delay = index * 0.2

    for index, academic_member in enumerate(members):
        academic_member.delay = index * 0.2

    context = {
        "images": images,
        "service_sections": service_sections,
        'department': department,
        'all_members': members,
        "blogs": blogs,
        "testimonials": testimonials
    }

    return render(request, "index.html", context)


def about(request):
    service_sections = ServiceSection.objects.all()
    for index, service_section in enumerate(service_sections):
        service_section.delay = index * 0.2
    context = {
        "service_sections": service_sections
    }
    return render(request, "about.html", context)


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        context = {
            "name": name,
            "email": email,
            "subject": subject,
            "message": message
        }

        email_html = render_to_string('contact_email.html', context)

        email_message = EmailMessage(
            subject=subject,
            body=email_html,
            from_email=settings.EMAIL_HOST_USER,
            to=[settings.EMAIL_HOST_USER],
        )
        email_message.content_subtype = "html"

        try:
            email_message.send()
            messages.success(
                request, "Your message has been sent successfully!")

            # Save to the database if email was sent successfully
            ContactMessage.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )
        except Exception as e:
            messages.error(
                request, "Failed to send your message. Please try again later.")

        return redirect("contact")

    return render(request, "contact.html")


def courses(request):
    popular_courses = Course.objects.filter(is_popular=True)
    testimonials = Testimonial.objects.all()
    context = {
        "testimonials": testimonials,
        "popular_courses": popular_courses
    }
    return render(request, "courses.html", context)


def testimonial(request):
    testimonials = Testimonial.objects.all()
    context = {
        "testimonials": testimonials
    }
    return render(request, "testimonial.html", context)


def notfound(request):
    context = {}
    return render(request, "404.html", context)


def department(request, department_type, slug):
    if department_type == "academic":
        department = get_object_or_404(AcademicDepartment, slug=slug)
        members = AcademicMember.objects.filter(
            academic_department=department).order_by('order')
    elif department_type == "management":
        department = get_object_or_404(ManagementDepartment, slug=slug)
        members = ManagementMember.objects.filter(
            management_department=department).order_by('order')
    else:
        # Handle invalid department type, possibly with a 404
        return render(request, '404.html')  # Customize as needed

    # Add animation delay to each member
    for index, member in enumerate(members):
        member.delay = index * 0.2

    # Prepare context
    context = {
        'department': department,
        'all_members': members,
    }
    return render(request, 'department.html', context)


def blogs(request):
    all_blogs = Blog.objects.all().order_by('-created_at')
    paginator = Paginator(all_blogs, 3)

    page_number = request.GET.get('page')
    blogs = paginator.get_page(page_number)

    for index, blog in enumerate(all_blogs):
        blog.delay = index * 0.2

    context = {
        "blogs": blogs
    }
    return render(request, 'blogs.html', context)


def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    recent_blogs = Blog.objects.all().exclude(
        id=blog.id).order_by('-created_at')[:4]
    context = {
        "blog": blog,
        "recent_blogs": recent_blogs
    }
    return render(request, 'blog_detail.html', context)
