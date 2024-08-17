'''creating a class train for booking,registration status,ticket number,name'''

class train:

    company="indian railways pvt ltd"

    def __init__(self,name,ticket_no,reg_status):
        self.ticket_no=ticket_no
        self.name=name
        self.reg_status=reg_status


arpit=train("arpit",100,"booked successfully")
print(arpit.name,arpit.reg_status,arpit.ticket_no)

akhil=train("akhil",101,"booked successfully")
print(akhil.name,akhil.reg_status,akhil.ticket_no)

harry=train("harry",102,"under process")
print(harry.name,harry.reg_status,harry.ticket_no)

