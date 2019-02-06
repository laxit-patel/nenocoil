# This Module Generates Next key based on previous value from database along with its creation time and  initials
# This Module Presumes that you have Chosen Database entity name With Capital
import datetime
from client.models import Client
from order.models import Order


def key_generator(entity):

    if entity == "Client":
        initial = "clnt"
        if Client.objects.count() == 0:
            counter = str('0000')
        else:
            last_row = Client.objects.latest("Client_Id")
            prev_counter = str(last_row).split("_")[2][0:4]
            new_counter = int(prev_counter) + 1
            counter = str(new_counter).zfill(4)
    elif entity == "Order":
        initial = "ordr"
        last_row = Order.objects.latest("Order_Id")
        prev_counter = str(last_row).split("_")[2][0:4]
        new_counter = int(prev_counter) + 1
        counter = str(new_counter).zfill(4)
    else:
        initial = "Invalid Entity"

    if entity == "Invalid Entity":
        return "Invalid Entity"
    else:
        date = datetime.datetime.now().strftime("%m%y")
        key = date + "_" + initial + "_" + counter
        return key
