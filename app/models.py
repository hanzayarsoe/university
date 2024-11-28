from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.urls import reverse
from tinymce.models import HTMLField
# Create your models here.


class GeneralInfo(models.Model):
    university_name = models.CharField(max_length=255, unique=True,
                                       blank=False, null=False, default="University")
    short_name = models.CharField(max_length=255, blank=True, null=True)
    establishment_year = models.IntegerField(blank=True, null=True)
    total_staffs = models.IntegerField(blank=True, null=True)
    total_students = models.IntegerField(blank=True, null=True)
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    location = models.TextField()
    postal = models.IntegerField(null=True, blank=True)
    location_url = models.CharField(max_length=255, null=True, blank=True)
    logo_url = models.URLField(unique=True, blank=True, null=True)
    facebook_url = models.URLField(null=True, blank=True)
    instagram_url = models.URLField(null=True, blank=True)
    viber_url = models.URLField(null=True, blank=True)
    youtube_url = models.URLField(null=True, blank=True)
    about_us = models.TextField(
        null=True, blank=True, default="About University")
    about_us_image = models.URLField(null=True, blank=True)
    short_description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.university_name


class Gallery(models.Model):
    image_name = models.CharField(
        max_length=255, null=True, blank=True, default="Gallery")
    image_url_1 = models.URLField(max_length=255, null=True, blank=True)
    image_url_2 = models.URLField(max_length=255, null=True, blank=True)
    image_url_3 = models.URLField(max_length=255, null=True, blank=True)
    image_url_4 = models.URLField(max_length=255, null=True, blank=True)
    image_url_5 = models.URLField(max_length=255, null=True, blank=True)
    image_url_6 = models.URLField(max_length=255, null=True, blank=True)

    def __str__(self) -> str:
        return self.image_name


class ImageShowcase(models.Model):
    image_name = models.CharField(max_length=255, blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.image_name


class ServiceSection(models.Model):
    icon = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(
        max_length=255, unique=True, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.title


class Position(models.Model):
    name = models.CharField(max_length=255, unique=True,)

    def __str__(self):
        return self.name


class AcademicDepartment(models.Model):
    name = models.CharField(max_length=255, unique=True, blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    department_type = models.CharField(max_length=50, default='academic')

    def get_absolute_url(self):
        return reverse(
            'department',
            kwargs={'department_type': self.department_type, 'slug': self.slug}
        )

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class AcademicMember(models.Model):
    name = models.CharField(max_length=255, unique=True)
    position = models.ForeignKey(
        'Position', on_delete=models.SET_NULL, null=True, blank=True)
    academic_department = models.ForeignKey(
        'AcademicDepartment', on_delete=models.SET_NULL, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    degrees = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    biography = models.TextField(blank=True, null=True)
    image_url = models.URLField()
    facebook_url = models.URLField(blank=True, null=True)
    viber_url = models.URLField(blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order']


class ManagementDepartment(models.Model):
    name = models.CharField(max_length=255, unique=True, blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    department_type = models.CharField(max_length=50, default='management')

    def get_absolute_url(self):
        return reverse(
            'department',
            kwargs={'department_type': self.department_type, 'slug': self.slug}
        )

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class ManagementMember(models.Model):
    name = models.CharField(max_length=255, unique=True)
    position = models.ForeignKey(
        'Position', on_delete=models.SET_NULL, null=True, blank=True)
    management_department = models.ForeignKey(
        'ManagementDepartment', on_delete=models.SET_NULL, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    degrees = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    biography = models.TextField(blank=True, null=True)
    image_url = models.URLField()
    facebook_url = models.URLField(blank=True, null=True)
    viber_url = models.URLField(blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order']


class Publication(models.Model):
    member = models.ForeignKey(
        AcademicMember, on_delete=models.CASCADE, related_name='publications', blank=True, null=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self) -> str:
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "Blog Categories"


class Blog(models.Model):
    image_url = models.URLField(null=True, blank=True)
    title = models.CharField(max_length=255)
    category = models.ForeignKey(
        'Category', on_delete=models.SET_NULL, null=True, blank=True)
    content = HTMLField(blank=True, null=True)
    author = models.ForeignKey(
        'Author', on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse('blog_detail', args=[str(self.id)])


class Testimonial(models.Model):
    image_url = models.URLField(blank=True, null=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    position = models.CharField(max_length=50, null=True, blank=True)
    feedback = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.name


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.name} - {self.subject}"


class CourseCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Course Categories"
        ordering = ['name']

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=200, unique=True)
    code = models.CharField(max_length=10, unique=True)  # e.g., "CS101"
    description = models.TextField(blank=True, null=True)
    img_url = models.URLField(blank=True, null=True)
    credits = models.PositiveIntegerField(blank=True, null=True)
    duration = models.CharField(max_length=50)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    is_popular = models.BooleanField(default=True)

    # New category field, linking Course to Category
    category = models.ForeignKey(
        CourseCategory, on_delete=models.SET_NULL, null=True, related_name="courses")

    instructor = models.CharField(max_length=100, blank=True, null=True)
    syllabus_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['code']  # Orders courses by code by default

    def __str__(self):
        return f"{self.code} - {self.name}"

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('course_detail', args=[str(self.id)])
