# Create a class called scheme with scheme_id, scheme_name,outgoing_rate, and message_charge.
# Derive customer class form scheme and include cust_id, name and mobile_no data.
# Define necessary functions to read and display data

class scheme():
    def __init__(self, scheme_id, scheme_name, outgoing_rate, message_charge):
        self.scheme_id = scheme_id
        self.scheme_name = scheme_name
        self.outgoing_rate = outgoing_rate
        self.message_charge = message_charge


class customer(scheme):
    def __init__(self, scheme_id, scheme_name, outgoing_rate, message_charge, cust_id, name, mobile_no):
        scheme.__init__(self, scheme_id, scheme_name,
                        outgoing_rate, message_charge)
        self.cust_id = cust_id
        self.name = name
        self.mobile_no = mobile_no
        print(self.scheme_id, self.scheme_name, self.outgoing_rate,
              self.message_charge, self.cust_id, self.name, self.mobile_no)


scheme_id = int(input("Enter Scheme id: "))
scheme_name = input("Enter Scheme Name: ")
outgoing_rate = float(input("Enter Outgoing Rate: "))
message_charge = float(input("Enter Message Charge: "))
cust_id = int(input("Enter Customer id: "))
name = input("Enter Customer Name: ")
mobile_no = input("Enter mobile no: ")
obj = customer(scheme_id, scheme_name, outgoing_rate,
               message_charge, cust_id, name, mobile_no)
