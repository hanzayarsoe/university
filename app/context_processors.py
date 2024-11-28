from .models import GeneralInfo, Gallery, AcademicDepartment, ManagementDepartment


def general_info(request):
    general_info = GeneralInfo.objects.first()
    gallery = Gallery.objects.first()
    academic_departments = AcademicDepartment.objects.all()
    management_departments = ManagementDepartment.objects.all()
    academic_urls = [dept.get_absolute_url() for dept in academic_departments]
    management_urls = [dept.get_absolute_url()
                       for dept in management_departments]
    return {'general_info': general_info, 'gallery': gallery, 'academic_departments': academic_departments, 'management_departments': management_departments, 'academic_urls': academic_urls,
            'management_urls': management_urls, }
