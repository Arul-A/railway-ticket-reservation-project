from tabulate import tabulate
class Railway:
    def __init__(self):
        self.passenger_id = 0
        self.passenger = {}
        self.canceled_berth = ""
        self.canceled_ticket = ""
        self.seat_number = ""
        self.canceled_seat_number = ""
        self.passenger_list = []
        self.ticket = ""
        self.lower_berth = [" " for _ in range(21)]
        self.middle_berth = [" " for _ in range(21)]
        self.upper_berth = [" " for _ in range(21)]
        self.rac = [" " for _ in range(10)]
        self.wl = [" " for _ in range(10)]
        self.options = ["Ticket Booking", "Cancel Ticket", "Show Available Ticket",
                        "Booked Tickets", "Exit"]

    def show_options(self):
        print("    Railway Ticket Booking")
        print("*" * 30)
        for i in range(len(self.options)):
            print(f"{i+1}.{self.options[i]}")

    def get_passenger(self):
        self.passenger_id += 1
        name = input("Enter Name:").upper()
        age = int(input("Enter Age:"))
        gender = input("Enter Gender(M/F):").upper()
        berth = input("Enter the berth preference(L/M/U):").upper()
        self.passenger = {"id":self.passenger_id, "name":name, "age":age, "gender":gender, "berth":berth}

    def is_ticket_available(self):
        count_l = 0
        for i in range(len(self.lower_berth)):
            if self.lower_berth[i] == " ":
                count_l += 1
        print(f"Available tickets in Lower Berth:{count_l}")
        count_m = 0
        for j in range(len(self.middle_berth)):
            if self.middle_berth[j] == " ":
                count_m += 1
        print(f"Available tickets in Middle Berth:{count_m}")
        count_u = 0
        for k in range(len(self.middle_berth)):
            if self.upper_berth[k] == " ":
                count_u += 1
        print(f"Available tickets in Upper Berth:{count_u}")
        count_r = 0
        for l in range(len(self.rac)):
            if self.rac[l] == " ":
                count_r += 1
        print(f"Available tickets in RAC:{count_r}")
        count_w = 0
        for m in range(len(self.wl)):
            if self.wl[m] == " ":
                count_w += 1
        print(f"Available tickets in Waiting list:{count_w}")

    def ticket_booking(self):
        if self.passenger['berth'] == 'L':
            if " " in self.lower_berth:
                for i in range(len(self.lower_berth)):
                    if self.lower_berth[i] == " ":
                        print("Lower Berth is Given, Booked Successfully")
                        self.seat_number = str(i+1)+"L"
                        self.passenger['seat_no'] = self.seat_number
                        self.passenger_list.append(self.passenger)
                        self.lower_berth[i] = self.seat_number
                        return
            elif " " in self.middle_berth:
                for j in range(len(self.middle_berth)):
                    if self.middle_berth[j] == " ":
                        print("Middle Berth is Given, Booked Successfully")
                        self.seat_number = str(j + 1) + "M"
                        self.passenger['seat_no'] = self.seat_number
                        self.passenger_list.append(self.passenger)
                        self.middle_berth[j] = self.seat_number
                        return
            elif " " in self.upper_berth:
                for k in range(len(self.upper_berth)):
                    if self.upper_berth[k] == " ":
                        print("Upper Berth is Given, Booked Successfully")
                        self.seat_number = str(k + 1) + "U"
                        self.passenger['seat_no'] = self.seat_number
                        self.passenger_list.append(self.passenger)
                        self.upper_berth[k] = self.seat_number
                        return
            else:
                if " " in self.rac:
                    for i in range(len(self.rac)):
                        if self.rac[i] == " ":
                            print("Added to RAC")
                            self.seat_number = str(i + 1) + "RAC"
                            self.passenger['seat_no'] = self.seat_number
                            self.passenger_list.append(self.passenger)
                            self.rac[i] = self.seat_number
                            return
                elif " " in self.wl:
                    for j in range(len(self.wl)):
                        if self.wl[j] == " ":
                            print("Added to Waiting List")
                            self.seat_number = str(j + 1) + "WL"
                            self.passenger['seat_no'] = self.seat_number
                            self.passenger_list.append(self.passenger)
                            self.wl[j] = self.seat_number
                            return
                else:
                    print("No tickets Available")
        elif self.passenger['berth'] == 'M':
            if " " in self.middle_berth:
                for j in range(len(self.middle_berth)):
                    if self.middle_berth[j] == " ":
                        print("Middle Berth is Given, Booked Successfully")
                        self.seat_number = str(j + 1) + "M"
                        self.passenger['seat_no'] = self.seat_number
                        self.passenger_list.append(self.passenger)
                        self.middle_berth[j] = self.seat_number
                        return
            elif " " in self.lower_berth:
                for i in range(len(self.lower_berth)):
                    if self.lower_berth[i] == " ":
                        print("Lower Berth is Given, Booked Successfully")
                        self.seat_number = str(i + 1) + "L"
                        self.passenger['seat_no'] = self.seat_number
                        self.passenger_list.append(self.passenger)
                        self.lower_berth[i] = self.seat_number
                        return
            elif " " in self.upper_berth:
                for k in range(len(self.upper_berth)):
                    if self.upper_berth[k] == " ":
                        print("Upper Berth is Given, Booked Successfully")
                        self.seat_number = str(k + 1) + "U"
                        self.passenger['seat_no'] = self.seat_number
                        self.passenger_list.append(self.passenger)
                        self.upper_berth[k] = self.seat_number
                        return
            else:
                if " " in self.rac:
                    for i in range(len(self.rac)):
                        if self.rac[i] == " ":
                            print("Added to RAC")
                            self.seat_number = str(i + 1) + "RAC"
                            self.passenger['seat_no'] = self.seat_number
                            self.passenger_list.append(self.passenger)
                            self.rac[i] = self.seat_number
                            return
                elif " " in self.wl:
                    for j in range(len(self.wl)):
                        if self.wl[j] == " ":
                            print("Added to Waiting List")
                            self.seat_number = str(j + 1) + "WL"
                            self.passenger['seat_no'] = self.seat_number
                            self.passenger_list.append(self.passenger)
                            self.wl[j] = self.seat_number
                            return
                else:
                    print("No tickets Available")
        elif self.passenger['berth'] == 'U':
            if " " in self.upper_berth:
                for k in range(len(self.upper_berth)):
                    if self.upper_berth[k] == " ":
                        print("Upper Berth is Given, Booked Successfully")
                        self.seat_number = str(k + 1) + "U"
                        self.passenger['seat_no'] = self.seat_number
                        self.passenger_list.append(self.passenger)
                        self.upper_berth[k] = self.seat_number
                        return
            elif " " in self.lower_berth:
                for i in range(len(self.lower_berth)):
                    if self.lower_berth[i] == " ":
                        print("Lower Berth is Given, Booked Successfully")
                        self.seat_number = str(i + 1) + "L"
                        self.passenger['seat_no'] = self.seat_number
                        self.passenger_list.append(self.passenger)
                        self.lower_berth[i] = self.seat_number
                        return
            elif " " in self.middle_berth:
                for j in range(len(self.middle_berth)):
                    if self.middle_berth[j] == " ":
                        print("Middle Berth is Given, Booked Successfully")
                        self.seat_number = str(j + 1) + "M"
                        self.passenger['seat_no'] = self.seat_number
                        self.passenger_list.append(self.passenger)
                        self.middle_berth[j] = self.seat_number
                        return
            else:

                if " " in self.rac:
                    for i in range(len(self.rac)):
                        if self.rac[i] == " ":
                            print("Added to RAC")
                            self.seat_number = str(i + 1) + "RAC"
                            self.passenger['seat_no'] = self.seat_number
                            self.passenger_list.append(self.passenger)
                            self.rac[i] = self.seat_number
                            return
                elif " " in self.wl:
                    for j in range(len(self.wl)):
                        if self.wl[j] == " ":
                            print("Added to Waiting List")
                            self.seat_number = str(j + 1) + "WL"
                            self.passenger['seat_no'] = self.seat_number
                            self.passenger_list.append(self.passenger)
                            self.wl[j] = self.seat_number
                            return
                else:
                    print("No tickets Available")

    def moving_rac_tickets(self):
        # if tickets cancelled moving the rac ticket to confirm ticket
        for i in range(len(self.rac)):
            if self.rac[i] != " ":
                if self.canceled_berth == "L":
                    index = int(self.canceled_seat_number[0]) - 1
                    self.lower_berth[index] = self.canceled_seat_number
                    for j in range(len(self.passenger_list)):
                        if self.passenger_list[j]['seat_no'] == self.rac[i]:
                            self.passenger_list[j]['seat_no'] = self.canceled_seat_number
                            self.rac[i] = " "
                            return

                elif self.canceled_berth == "U":
                    index = int(self.canceled_seat_number[0]) - 1
                    self.upper_berth[index] = self.canceled_seat_number
                    for j in range(len(self.passenger_list)):
                        if self.passenger_list[j]['seat_no'] == self.rac[i]:
                            self.passenger_list[j]['seat_no'] = self.canceled_seat_number
                            self.rac[i] = " "
                            return
                elif self.canceled_berth == "M":
                    index = int(self.canceled_seat_number[0]) - 1
                    self.middle_berth[index] = self.canceled_seat_number
                    for j in range(len(self.passenger_list)):
                        if self.passenger_list[j]['seat_no'] == self.rac[i]:
                            self.passenger_list[j]['seat_no'] = self.canceled_seat_number
                            self.rac[i] = " "
                            return
                else:
                    pass

    def sort_rac(self):
        for i in range(len(self.rac)-1):
            if self.rac[i] == " ":
                temp = self.rac[i]
                self.rac[i] = self.rac[i+1]
                for j in range(len(self.passenger_list)):
                    if self.passenger_list[j]['seat_no'] == self.rac[i]:
                        self.rac[i] = str(i+1)+"RAC"
                        self.passenger_list[j]['seat_no'] = self.rac[i]
                        self.rac[i+1] = temp
                        return

    def moving_wl_tickets(self):
        # after moving rac ticket to confirm ticket then moving waiting list to rac
        for i in range(len(self.rac)):
            if self.rac[i] == " ":
                for j in range(len(self.wl)):
                    if self.wl[j] != " ":
                        for k in range(len(self.passenger_list)):
                            if self.passenger_list[k]['seat_no'] == self.wl[j]:
                                self.passenger_list[k]['seat_no'] = str(i+1)+"RAC"
                                self.rac[i] = str(i+1)+"RAC"
                                self.wl[j] = " "
                                return

    def sort_wl(self):
        for i in range(len(self.wl)-1):
            if self.wl[i] == " ":
                temp = self.wl[i]
                self.wl[i] = self.wl[i+1]
                for j in range(len(self.passenger_list)):
                    if self.passenger_list[j]['seat_no'] == self.wl[i]:
                        self.wl[i] = str(i + 1) + "WL"
                        self.passenger_list[j]['seat_no'] = self.wl[i]
                        self.wl[i + 1] = temp
                        return

    def cancel_ticket(self):
        c_id = int(input("Enter passenger_id to cancel the ticket:"))
        for i in range(len(self.passenger_list)):
            if self.passenger_list[i]['id'] == c_id:
                self.canceled_ticket = self.passenger_list[i]
                self.passenger_list.pop(i)
                self.canceled_seat_number = self.canceled_ticket['seat_no']
                self.canceled_berth = self.canceled_seat_number[1]
                break
        if self.canceled_berth == "L":
            for i in range(len(self.lower_berth)):
                if self.lower_berth[i] == self.canceled_seat_number:
                    self.lower_berth[i] = " "
        elif self.canceled_berth == "U":
            for i in range(len(self.lower_berth)):
                if self.upper_berth[i] == self.canceled_seat_number:
                    self.upper_berth[i] = " "
        elif self.canceled_berth == "M":
            for i in range(len(self.middle_berth)):
                if self.middle_berth[i] == self.canceled_seat_number:
                    self.middle_berth[i] = " "
        elif self.canceled_berth == "R":
            for i in range(len(self.rac)):
                if self.rac[i] == self.canceled_seat_number:
                    self.rac[i] = " "
        else:
            for i in range(len(self.wl)):
                if self.wl[i] == self.canceled_seat_number:
                    self.wl[i] = " "
        self.moving_rac_tickets()
        self.sort_rac()
        self.moving_wl_tickets()
        self.sort_wl()

    def passengers_details(self):
        for i in range(len(rail.passenger_list)):
            print(f"Passenger_id:{rail.passenger_list[i]['id']}")
            print(f"Name:{rail.passenger_list[i]['name']}")
            print(f"Age:{rail.passenger_list[i]['age']}")
            print(f"Gender:{rail.passenger_list[i]['gender']}")
            print(f"Seat_Number:{rail.passenger_list[i]['seat_no']}")
            print("-"*20)
            result = (tabulate(self.passenger_list[i], headers=["ID","NAME","AGE","GENDER","SEAT NUMBER"]))
            print(result)


rail = Railway()
while True:
    rail.show_options()
    option = int(input("Enter Your Option:"))
    if option == 1:
        rail.get_passenger()
        rail.ticket_booking()
    elif option == 2:
        rail.cancel_ticket()
    elif option == 3:
        rail.is_ticket_available()
    elif option == 4:
        rail.passengers_details()
    if option == 5:
        print("Exited")
        break




