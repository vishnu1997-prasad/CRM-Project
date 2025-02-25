import uuid
from .models import Students
import random,string
# LM_100101

def get_admission_num():

    pattern = str(uuid.uuid4().int)[:7]

    adm_num = f"LM-{pattern}"

    if not Students.objects.filter(adm_num=adm_num).exists():

        return adm_num


def get_password() :

    password = ''.join(random.choices(string.ascii_letters+string.digits,k=8))

    return password


