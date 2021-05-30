import os

import django


os.environ['DJANGO_SETTINGS_MODULE'] = 'joblist.settings'
django.setup()


from vacancies.models import Specialty, Company, Vacancy

import vacancies.data as data

if __name__ == '__main__':
    for spec in data.specialties:
        Specialty.objects.create(
            title = spec["title"],
            code=spec["code"]
        )
        print(spec["title"])

    for comp in data.companies:
        Company.objects.create(
            id = comp["id"],
            name = comp["title"],
            location = comp["location"],
            description = comp["description"],
            employee_count = comp["employee_count"]
        )
        print(comp["title"])

    for job in data.jobs:
        comp = Company.objects.get(id=job["company"])
        spec = Specialty.objects.get(code=job["specialty"])
        Vacancy.objects.create(
            title=job["title"],
            specialty = spec,
            company = comp,
            skills = job["skills"],
            description = job["description"],
            salary_min = job["salary_from"],
            salary_max = job["salary_to"],
            published_at = job["posted"]
        )
        print(job["title"])
