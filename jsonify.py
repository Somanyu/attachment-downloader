import json
import os
import uuid


def ticket_json():
    count = 0

    ticketJSON = None
    jsonify = None
    ticket = {"ticket": []}

    directory = 'C:/Users/somanyu/Desktop/destination/Text/destination/'
    for filename in os.listdir(directory):
        file_txt = os.path.join(directory, filename)

        fp = open(file_txt, 'r')
        textFile = fp.readlines()

        airline = textFile[-1][2:11].strip()
        Airline = None
        AirlineEmail = None
        if airline == "destination":
            Airline = airline
            AirlineEmail = "order@destination.com"

        confirmation_no = textFile[1][28:].strip()

        passenger_name = textFile[4].strip()

        flight = textFile[7].split('(')
        flight_number = flight[1][:-2].strip()

        """
        ################################################
        Finding origin and destination of the passenger
        ################################################
        """
        string1 = "Airport"
        index1 = 0
        for line1 in textFile:
            index1 += 1
            if string1 in line1:
                break
        airport = textFile[index1-1].split("Airport")
        origin = airport[0].strip()
        destination = airport[1].strip()

        if origin.startswith("Netaji"):
            origin = "Netaji Subhas Chandra Bose International"
            destination = "Dubai International"

        """
        ####################################
        Finding Booking Total of the ticket
        ####################################
        """
        string2 = "Booking total"
        index2 = 0

        for line2 in textFile:
            index2 += 1
            if string2 in line2:
                break

        booking_price = textFile[index2-1].split("Booking total")
        try:
            btotal = booking_price[1].split(" ")
            booking_total = btotal[2].strip().replace(",", "")
        except:
            booking_total = None

        count += 1

        """
        ######################################
        Finding Passenger Total of the ticket
        ######################################
        """
        string3 = "Passenger total"
        index3 = 0

        for line3 in textFile:
            index3 += 1
            if string3 in line3:
                break

        passenger_price = textFile[index3-1].split("Passenger total")
        try:
            ptotal = passenger_price[1].split(" ")
            passenger_total = ptotal[2].strip().replace(",", "")
        except:
            passenger_total = None

        """
        ######################################
        Finding Transaction Fee of the ticket
        ######################################
        """
        string4 = "Transaction fee"
        index4 = 0

        for line4 in textFile:
            index4 += 1
            if string4 in line4:
                break

        transc_fee = textFile[index4-1].split("Transaction fee")
        try:
            tfee = transc_fee[1].split(" ")
            transaciton_fee = tfee[2].strip().replace(",", "")
        except:
            transaciton_fee = None

        """
        #################################
        Finding Taxes/fees of the ticket
        #################################
        """
        string5 = "Taxes/fees"
        index5 = 0
        for line5 in textFile:
            index5 += 1
            if string5 in line5:
                break

        Taxes = []

        try:
            tax = textFile[index5-1] + textFile[index5]
            taxes = tax.split(";")

            tax_code = ['PZ', 'I8', 'I2', 'OM', 'LB', 'H4', 'JB', 'JA', 'GE', 'JL', 'AE ', 'F6', 'TP',
                        'QA', 'ZR', 'K3', 'WO', 'IN', 'P2', 'NY', 'N5', 'YD', 'SP', 'RG']

            for i in tax_code:
                if tax.find(i, 10) != -1:
                    #print(i , " = ", tax.find(i, 10))
                    e = tax.find(i, 10)
                    f = tax[e+6:e+12].split(";")
                    x = {"Code": tax[e:e+2], "Amount": f[0]}
                    # print(x)
                    Taxes.append(x)

        except:
            pass

        Origin = {"Name": origin, "City": "", "Country": ""}
        Destination = {"Name": destination, "City": "", "Country": ""}
        BaseFare = {"Amount": passenger_total, "Currency": "AED"}
        PassengerTotal = {"Amount": passenger_total,
                          "Currency": "AED"}
        TransactionTotal = {"Amount": transaciton_fee, "Currency": "AED"}
        BookingTotal = {"Amount": booking_total, "Currency": "AED"}

        Passenger = {
            "PassengerName": passenger_name,
            "PassengerTotal": PassengerTotal,
            "BaseFare": BaseFare,
            "TransactionTotal": TransactionTotal,
            "BookingTotal": BookingTotal,
            "Taxes": Taxes}

        ticketJSON = {
            "Id": str(uuid.uuid4()),
            "Airline": Airline,
            "AirlineEmail": AirlineEmail,
            "Count": count,
            "BookingNumber": confirmation_no,
            "FlightNumber": flight_number,
            "Origin": Origin,
            "Destination": Destination,
            "Passengers": [Passenger]
        }

        jsonify = json.dumps(ticketJSON, indent=4)
        # print(jsonify)
        yield(jsonify)

        ticket["ticket"].append(ticketJSON)
    final = json.dumps(ticket, indent=4)
    # print(final)
    

    jsonFile = open('xen.json', 'w')
    jsonFile.write(final)
    jsonFile.close()


# ticket_json()
# print(ticket_json())
# for j in ticket_json():
#     print(j)
