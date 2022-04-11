from codify_exam.main.models import Customer, VIPCustomer
from main.models import Worker, Document, Project
from datetime import date

aigulya = Customer.objects.create(fullname="Aigulya", birth_date = date(1988, 10, 25), address = "Bishkek", phone_number = 73834746)
tahir = Customer.objects.create(fullname="Tahir", birth_date = date(2004, 7, 19), address = "Bishkek", phone_number = 37374748)
dolat = Customer.objects.create(fullname="Dolatbek", birth_date = date(2003, 10, 11), address ="Osh", phone_number = 65738398)

nurbek = VIPCustomer(name="Nurbek", birth_date=(1980, 1, 25), address="Bishkek", phone_number= 996550587711, vip_status_start = date(2022, 3, 8), donation_amount = 5000)

aika = Worker.objects.create(fullname="Aikanysh", birth_date = date(1988, 8, 25), work_position="administrator", work_experience=date(2000, 1,1))
kamila = Worker.objects.create(fullname="Kamila", birth_date = date(1992, 11, 12), work_position="analyst", work_experience=date(2002,12,1))
salavat = Worker.objects.create(fullname="Salavat", birth_date = date(2003, 7, 20), work_position="editor", work_experience=date(2004,10,1))

p1 = Document(worker=aika, inn="12367486", id_card = "P1264748383")
p2 = Document(worker=kamila, inn = "26365733", id_card = "P2736488379")
p3 = Document(worker=salavat, inn = "28483938", id_card = "P2849504847")

p3 = Document.objects.get(id=3)
p3.delete()

codify = Project.objects.create(project_name = "Codify")
codify.members.set([aika, kamila, salavat], through_defaults={'date_joined':date(2022, 4, 5)})

all_workers = Worker.objects.all()
print(all_workers)

for worker in all_workers:
    print(worker.fullname)
    print(worker.document.inn)
    print(worker.document.card_id)

all_work_projects = Project.objects.all()
print(all_work_projects)

target_employee = Project.objects.get(Worker.fullname == "Aikanysh")
print(target_employee)