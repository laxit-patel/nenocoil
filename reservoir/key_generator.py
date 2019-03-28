# This Module Generates Next key based on previous value from database along with its creation time and  initials
# This Module Presumes that you have Chosen Database entity name With Capital Letter And Literal Names like for clients = Client and not client_table, client_details or anything
import datetime
from reservoir.date_generator import date_generator
from client.models import Client
from order.models import Order
from invoice.models import Invoice
from product.models import Product
from design.models import Design
from drawing.models import Drawing
from producttype.models import ProductType


def key_generator(entity):

    if entity == "Client":
        if Client.objects.count() == 0:
            counter = str('0000')
            initial = "CLNT"
        else:
            initial = "CLNT"
            last_row = Client.objects.latest("Client_Id")
            prev_counter = str(last_row).split("_")[2][0:4]
            new_counter = int(prev_counter, 16) + 1
            counter = hex(new_counter)[2:6].zfill(4).upper()
    elif entity == "Order":
        if Order.objects.count() == 0:
            counter = str('0000')
            initial = "ORDR"
        else:
            initial = "ORDR"
            last_row = Order.objects.latest("Order_Id")
            prev_counter = str(last_row).split("_")[2][0:4]
            new_counter = int(prev_counter, 16) + 1
            counter = hex(new_counter)[2:6].zfill(4).upper()
    elif entity == "Invoice":
        if Invoice.objects.count() == 0:
            counter = str('0000')
            initial = "INVC"
        else:
            initial = "INVC"
            last_row = Invoice.objects.latest("Invoice_Id")
            prev_counter = str(last_row).split("_")[2][0:4]
            new_counter = int(prev_counter, 16) + 1
            counter = hex(new_counter)[2:6].zfill(4).upper()
    elif entity == "Product":
        if Product.objects.count() == 0:
            counter = str('0000')
            initial = "PRDC"
        else:
            initial = "PRDC"
            last_row = Product.objects.latest("Product_Id")
            prev_counter = str(last_row).split("_")[2][0:4]
            new_counter = int(prev_counter, 16) + 1
            counter = hex(new_counter)[2:6].zfill(4).upper()
    elif entity == "Design":
        if Design.objects.count() == 0:
            counter = str('0000')
            initial = "DSGN"
        else:
            initial = "DSGN"
            last_row = Design.objects.latest("Design_Id")
            prev_counter = str(last_row).split("_")[2][0:4]
            new_counter = int(prev_counter, 16) + 1
            counter = hex(new_counter)[2:6].zfill(4).upper()
    elif entity == "Drawing":
        if Drawing.objects.count() == 0:
            counter = str('0000')
            initial = "DRAW"
        else:
            initial = "DRAW"
            last_row = Drawing.objects.latest("Drawing_Id")
            prev_counter = str(last_row).split("_")[2][0:4]
            new_counter = int(prev_counter, 16) + 1
            counter = hex(new_counter)[2:6].zfill(4).upper()
    elif entity == "ProductType":
        if ProductType.objects.count() == 0:
            counter = str('0000')
            initial = "PTYP"
        else:
            initial = "PTYP"
            last_row = ProductType.objects.latest("ProductType_Id")
            prev_counter = str(last_row).split("_")[2][0:4]
            new_counter = int(prev_counter, 16) + 1
            counter = hex(new_counter)[2:6].zfill(4).upper()
    else:
        entity = "Invalid Entity"

    if entity == "Invalid Entity":
        return "Invalid Entity"
    else:
        date = date_generator()
        key = date + "_" + initial + "_" + counter
        return key
