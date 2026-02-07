from evening.models import *

sol = Soldiers.objects.all()
for s in sol:
    staff = Staff()
    staff.slug = s.slug
    staff.position_name = s.position_name
    staff.mil_prof = s.mil_prof
    staff.position_rank = s.position_rank
    staff.soldier = s.pk
    staff.save()
