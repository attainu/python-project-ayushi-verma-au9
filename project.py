class ParkingLot:
    def add_space(self, total_space):
        self.my_lot = {}
        self.total_cark_parked = 0
        for i in range(1, int(total_space)+1):
            self.my_lot[i] = []
        print("Created a parking lot with", total_space, "slots")

    def park_new_car(self, regno, color, entry_time):
        for slot in self.my_lot:
            if self.my_lot[slot] and self.my_lot[slot][0] == regno:
                print("Sorry, duplicate Registration No. are not allowed")
                return
        for slot, values in self.my_lot.items():
            if not values:
                values.append(regno)
                values.append(color)
                values.append(entry_time)
                self.total_cark_parked += 1
                print("Allocated slot number: ", slot)
                return
        print("Sorry, parking lot is full")

    def leave_park_car(self, slot):
        if self.my_lot[slot]:
            start = self.my_lot[slot][2]
            end = datetime.now().time()
            t1 = timedelta(hours=start.hour,
                           minutes=start.minute, seconds=start.second)
            t2 = timedelta(
                hours=end.hour, minutes=end.minute, seconds=end.second)
            time_duration = t2 - t1
            minutes = (time_duration.seconds // 60) % 60
            hours = time_duration.seconds//3600
            self.my_lot[slot] = []
            self.total_cark_parked -= 1
            print("Slot number", slot, "is free")
            print("Parking Time :", hours, "hr", minutes, "min")
            print("Bill =", minutes * 10, "rs")
        else:
            print("Slot number", slot, "is already free")

    def status_check(self):
        if self.total_cark_parked:
            print("Slot No. Registration No Colour")
            for slot, values in self.my_lot.items():
                if values:
                    print(slot, values[0], values[1])
        else:
            print("Parking Slot is Empty")

    def find_reg_by_color(self, color):
        no_car = True
        for slot in self.my_lot:
            if self.my_lot[slot] and self.my_lot[slot][1] == color:
                if no_car:
                    print(self.my_lot[slot][0], end="")
                    no_car = False
                else:
                    print(",", self.my_lot[slot][0])
        if no_car:
            print("Not found")

    def find_slot_by_color(self, color):
        no_car = True
        for slot in self.my_lot:
            if self.my_lot[slot] and self.my_lot[slot][1] == color:
                if no_car:
                    print(slot, end="")
                    no_car = False
                else:
                    print(",", slot)
        if no_car:
            print("Not found")

    def find_slot_by_reg(self, regno):
        for slot, values in self.my_lot.items():
            if values and values[0] == regno:
                print(slot)
                return
        print("Not found")


if __name__ == "__main__":
    from datetime import datetime, timedelta
    my_parking = ParkingLot()
    a = int(input("Press 1 for Interative commands & 2 for File : \t"))
    if a == 1:
        while(True):
            ask_input = input().split(" ")
            if ask_input[0] == 'create_parking_lot':
                my_parking.add_space(ask_input[1])

            elif ask_input[0] == 'park':
                entry_time = datetime.now().time()
                my_parking.park_new_car(
                    ask_input[1], ask_input[2], entry_time)

            elif ask_input[0] == 'leave':
                my_parking.leave_park_car(int(ask_input[1]))

            elif ask_input[0] == 'status':
                my_parking.status_check()

            elif ask_input[0] == 'registration_numbers_for_cars_with_colour':
                my_parking.find_reg_by_color(ask_input[1])

            elif ask_input[0] == 'slot_numbers_for_cars_with_colour':
                my_parking.find_slot_by_color(ask_input[1])

            elif ask_input[0] == 'slot_number_for_registration_number':
                my_parking.find_slot_by_reg(ask_input[1])

            elif ask_input[0] == 'exit':
                break

            else:
                print("Wrong input")
    elif a == 2:
        input_file = open(
            "D:/Technical Stuffs/Attainu Course/Ayushi Project/input_doc.txt", "r")
        reading_all_line = input_file.readlines()
        for single_line in reading_all_line:
            single_line = single_line.lower().replace('\n', '')
            ask_input = single_line.split(" ")
            if ask_input[0] == 'create_parking_lot':
                my_parking.add_space(ask_input[1])

            elif ask_input[0] == 'park':
                entry_time = datetime.now().time()
                my_parking.park_new_car(
                    ask_input[1], ask_input[2], entry_time)

            elif ask_input[0] == 'leave':
                my_parking.leave_park_car(int(ask_input[1]))

            elif ask_input[0] == 'status':
                my_parking.status_check()

            elif ask_input[0] == 'registration_numbers_for_cars_with_colour':
                my_parking.find_reg_by_color(ask_input[1])

            elif ask_input[0] == 'slot_numbers_for_cars_with_colour':
                my_parking.find_slot_by_color(ask_input[1])

            elif ask_input[0] == 'slot_number_for_registration_number':
                my_parking.find_slot_by_reg(ask_input[1])

            elif ask_input[0] == 'exit' or ask_input[0] == '':
                break

            else:
                print("Wrong input")
        input_file.close()
    else:
        print("Choose from 2 options only")
