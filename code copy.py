import pickle
from datetime import datetime
 
def CreateFile():
   F = open('Stock', "wb")
   Rec = []
   while True:
       Ino = int(input("Item No:"))
       Iname = input("Name:")
       Qty = int(input("Qty:"))
       Expiry_date = input("Expiry Date (YYYY-MM-DD):")
       Rec.append([Ino, Iname, Qty, Expiry_date])
       Ch = input("More Items (Y/N):")
       if Ch in "nN":
           break
   pickle.dump(Rec, F)
   F.close()
 
def Addatend():
   F = open("Stock", "rb+")
   Rec = pickle.load(F)
   while True:
       Ino = int(input("Item No:"))
       Iname = input("Name:")
       Qty = int(input("Qty:"))
       Expiry_date = input("Expiry Date (YYYY-MM-DD):")
       Rec.append([Ino, Iname, Qty, Expiry_date])
       Ch = input("More Items (Y/N):")
       if Ch in "nN":
           break
   F.seek(0)
   pickle.dump(Rec, F)
   F.close()
 
def Procure():
   try:
       F = open("Stock", "rb+")
       Rec = pickle.load(F)
       Ino = int(input("Item No:"))
       for I in range(len(Rec)):
           if Rec[I][0] == Ino:
               Qty = int(input("Qty:"))
               Rec[I][2] += Qty
               F.seek(0)
               pickle.dump(Rec, F)
               break
       else:
           print("Item not found")
       F.close()
   except:
       print("File not found")
 
def Issue():
   try:
       F = open("Stock", "rb+")
       Rec = pickle.load(F)
       Ino = int(input("Item No:"))
       for I in range(len(Rec)):
           if Rec[I][0] == Ino:
               Qty = int(input("Qty:"))
               if Rec[I][2] >= Qty:
                   Rec[I][2] -= Qty
                   F.seek(0)
                   pickle.dump(Rec, F)
               else:
                   print("Insufficient Stock")
               break
       else:
           print("Item not found")
       F.close()
   except:
       print("File not found")
 
def SortFile():
   F = open("Stock", "rb+")
   Rec = pickle.load(F)
   Rec.sort()
   F.seek(0)
   pickle.dump(Rec, F)
   F.close()
 
def ReadFile():
    try:
        F = open("Stock", "rb")
        Rec = pickle.load(F)
        print("INo.Name Qty Expiry Date")	
        for R in Rec:
            print(R[0], R[1], R[2], R[3])  
        F.close()
    except:
        print("File not found")
 
def InoSearch():
    try:
        F = open("Stock", "rb")
        Rec = pickle.load(F)
        Inos = int(input("Item Number to be searched:"))
        for R in Rec:
           if R[0] == Inos:
               print(R[0], R[1], R[2], R[3])                 
               break
        else:
            print("Item not found")
        F.close()
    except:
        print("File not found")
 
def NameSearch():
    try:
       F = open("Stock", "rb")
       Rec = pickle.load(F)
       Inames = input("Item Name to be searched:")
       Found = 0
       for R in Rec:
           if R[1].upper() == Inames.upper():
               print(R[0], R[1], R[2], R[3])                
               Found += 1
       print(Inames, "found", Found, "times...")
       F.close()
    except:
       print("File not found")
 
def Overflowstock():
    try:
       F = open("Stock", "rb")
       Rec = pickle.load(F)
       Found = 0
       for R in Rec:
           if R[2] > 400:
               print(R[0], R[1], R[2], R[3])                 
               Found += 1
       print(Found, "items are at overflow situation")
       F.close()
    except:
       print("File not found")
 
def Reorder():
    try:
       F = open("Stock", "rb")
       Rec = pickle.load(F)
       today = datetime.now()
       Found = 0
       for R in Rec:
           item_date = datetime.strptime(R[3], "%Y-%m-%d")
           days_left = (item_date - today).days
           if days_left < 0:
               print(f"Item {R[1]} with Item No {R[0]} has expired. Please reorder.")
               Found += 1
           elif days_left <= 30:  # Example threshold for low stock reminder
               print(f"Item {R[1]} with Item No {R[0]} has {days_left} days left before it expires. Consider reordering soon.")
               Found += 1
       if Found == 0:
           print("No items need reordering.")
       F.close()
    except:
       print("File not found")
 
print("Hello, this is an Inventory Management System")
Pass = input("To begin, please enter the password: ")
if Pass == "123456CBSE":
   print("User Authenticated")
 
while True:
    Q = input("C:Create D:Display A:Addatend S:Sort IS:InoSearch N:NameSearch O:Overflow IE:Issue P:Procure R:Reorder Q:Quit ")
    if Q in "cC":
        CreateFile()
    elif Q in "dD":
        ReadFile()
    elif Q in "aA":
        Addatend()
    elif Q in "sS":
        SortFile()
    elif Q in "nN":
        NameSearch()
    elif Q in "oO":
        Overflowstock()
    elif Q in ["IS", "is", "Is", "iS"]:
        InoSearch()
    elif Q in ["IE", "ie", "Ie", "iE"]:
        Issue()
    elif Q in "pP":
        Procure()
    elif Q in "rR":
        Reorder()
    elif Q in "qQ":
        break
    else:
        print("Invalid Option!!!")
else:
    print("Invalid User")
