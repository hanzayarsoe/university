from typing import Any
from django.contrib import admin
from django.http import HttpRequest
from app.models import (GeneralInfo, ImageShowcase, CourseCategory, Course,
                        Position, AcademicMember, Publication,
                        ServiceSection, Gallery, AcademicDepartment, ManagementDepartment, ManagementMember,
                        Author, Category, Blog, Testimonial, ContactMessage)
from adminsortable2.admin import SortableAdminMixin
# Register your models here.


@admin.register(GeneralInfo)
class GeneralInfoAdmin(admin.ModelAdmin):
    list_display = [
        'university_name',
        'short_name',
        'establishment_year',
        'phone',
        'email'
    ]
    readonly_fields = ['created_at', 'updated_at']

    def has_add_permission(self, request):
        count = GeneralInfo.objects.count()
        if count >= 1:
            return False
        return super().has_add_permission(request)


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = [
        'image_name'
    ]

    def has_add_permission(self, request):
        count = Gallery.objects.count()
        if count >= 1:
            return False
        return super().has_add_permission(request)


@admin.register(ImageShowcase)
class ImageShowcaseAdmin(admin.ModelAdmin):
    list_display = [
        'image_name',
        'uploaded_at'
    ]


@admin.register(ServiceSection)
class ServiceSectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']


class PublicationInline(admin.TabularInline):
    model = Publication
    extra = 1


@admin.register(AcademicDepartment)
class AcademicDepartmentAdmin(admin.ModelAdmin):
    list_display = ['name']
    readonly_fields = ['slug']


@admin.register(ManagementDepartment)
class ManagementDepartmentAdmin(admin.ModelAdmin):
    list_display = ['name']
    readonly_fields = ['slug']


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(AcademicMember)
class AcademicMemberAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['name', 'position', 'academic_department', 'order']
    list_editable = ['order']
    list_filter = ['academic_department', 'position']
    search_fields = ['name', 'academic_department__name', 'position__name']
    ordering = ['order']

    class Meta:
        model = AcademicMember


@admin.register(ManagementMember)
class ManagementMemberAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['name', 'position', 'management_department', 'order']
    list_editable = ['order']
    list_filter = ['management_department', 'position']
    search_fields = ['name', 'management_department__name', 'position__name']
    ordering = ['order']

    class Meta:
        model = AcademicMember


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'created_at']


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'feedback']


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at']
    list_filter = ['created_at']

    def has_add_permission(self, request: HttpRequest) -> bool:
        return False

    def has_change_permission(self, request: HttpRequest, obj: Any | None = ...) -> bool:
        return False

    def has_delete_permission(self, request: HttpRequest, obj: Any | None = ...) -> bool:
        return False


@admin.register(CourseCategory)
class CourseCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'duration', 'instructor', 'category']
    list_filter = ['code', 'instructor', 'category']
