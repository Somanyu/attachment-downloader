import os
import mariadb


def ticket_details():
    try:
        conn = mariadb.connect(
            user="root",
            password="",
            host="localhost",
            port=3306,
            database="destination",
        )
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB {e}")

    cur = conn.cursor()

    count = 0

    directory = "C:/Users/somanyu/Desktop/destination/Text/destination/"
    for filename in os.listdir(directory):
        file_txt = os.path.join(directory, filename)

        fp = open(file_txt, "r")
        textFile = fp.readlines()

        conifrmation_no = textFile[1][28:].strip()

        passenger_name = textFile[4].strip()

        flight = textFile[7].split("(")
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
        airport = textFile[index1 - 1].split("Airport")
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

        booking_price = textFile[index2 - 1].split("Booking total")
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

        passenger_price = textFile[index3 - 1].split("Passenger total")
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

        transc_fee = textFile[index4 - 1].split("Transaction fee")
        try:
            tfee = transc_fee[1].split(" ")
            transaciton_fee = tfee[2].strip().replace(",", "")
        except:
            transaciton_fee = None

        print("\nCount:", count)
        print("Booking Number:", conifrmation_no)
        print("Passenger Name:", passenger_name)
        print("Flight Number:", flight_number)
        print("Origin:", origin)
        print("Destination:", destination)
        print("Booking Total: ", booking_total)
        print("Passenger Total: ", passenger_total)
        print("Transaction Fee: ", transaciton_fee)

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

        try:
            tax = textFile[index5 - 1] + textFile[index5]
            taxes = tax.split(";")

            tax_code = [
                "PZ",
                "LB",
                "H4",
                "JB",
                "JA",
                "GE",
                "JL",
                "AE ",
                "F6",
                "TP",
                "QA",
                "ZR",
                "K3",
                "WO",
                "IN",
                "P2",
                "NY",
                "N5",
                "YD",
                "SP",
                "RG",
            ]

            print("Taxes : ")
            for i in tax_code:
                if tax.find(i, 10) != -1:
                    # print(i , " = ", tax.find(i, 10))
                    e = tax.find(i, 10)
                    f = tax[e + 6 : e + 12].split(";")

                    print(tax[e : e + 2], ": ", f[0])

        except:
            print("Unexpected Error")
        print("\nTaxes/fees: ", tax)
        print("\n########################################################\n")

        sql = "INSERT IGNORE INTO `customer_details`(`id`, `booking_number`, `passenger_name`, `flight_number`, `origin`, `destination`, `booking_total`, `passenger_total`, `transaction_fee`) VALUES (%d, %s, %s, %s ,%s ,%s , %d, %d, %d)"
        val = (
            count,
            conifrmation_no,
            passenger_name,
            flight_number,
            origin,
            destination,
            booking_total,
            passenger_total,
            transaciton_fee,
        )
        try:
            cur.execute(sql, val)
        except mariadb.Error as e:
            print(f"Error: {e}")

        conn.commit()
        if cur.lastrowid == None:
            print("Aready Inserted")
        else:
            print(f"last inserted ID: {cur.lastrowid}")
    # print(f"Total {count} rows added in the database.")


ticket_details()
