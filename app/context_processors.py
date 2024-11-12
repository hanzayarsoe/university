from .models import GeneralInfo, AcademicDepartment, ManagementDepartment


def general_info(request):
    general_info = GeneralInfo.objects.first()
    academic_departments = AcademicDepartment.objects.all()
    management_departments = ManagementDepartment.objects.all()
    return {'general_info': general_info, 'academic_departments': academic_departments, 'management_departments': management_departments}
