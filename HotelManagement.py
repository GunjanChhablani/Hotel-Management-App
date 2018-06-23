import pickle
import random
import sys
from Tkinter import *
import tkMessageBox
import tkFont
from PIL import ImageTk,Image
WINDOW=Tk()
WINDOW.resizable(width=FALSE, height=FALSE)
WINDOW.geometry('450x450+300+150')
WINDOW.title('Hotel Management')
MainFrame=Frame(WINDOW)
MainFrame.place(x=0,y=0,relwidth=1,relheight=1)
FNentry=Entry()
FNbut=Button()
LNentry=Entry()
LNbut=Button()
listbox1=Listbox()
FinalCostLabel=Label()
NewFrame=Frame()
CustomerIDEntry1=Entry()
CustomerIDEntry=Entry()
CheckOutDateEntry=Entry()
CheckOutButton=Button()
GetDetailsButton=Button()
Spinbox1=Spinbox()
LFrame=Frame()
scrollbar1=Scrollbar()
Newlabel=Label()
gobutton=Button()
RoomtypeOptions=Button()
CheckInDateEntry=Entry()
CheckInDateLabel=Label()
SelectRoomNoLabel=Label()
SelectRoomTypeLabel=Label()
WrongCheckInEntryLabel=Label()
FinaliseButton=Button()
PrintCustomerIDLabel={}
ka1=Label()
ka2=Label()
ka3=Label()
ka4=Label()
ka5=Label()
ka6=Label()
ka7=Label()
CheckinDoneNameLabel=Label()
CheckinDoneIDLabel=Label()
BackButton=Button()
newbut=Button()
image2=Image.open('bg.gif')
image1=ImageTk.PhotoImage(image2)
h1=image1.height()
w1=image1.width()
background_label = Label(MainFrame,image=image1,height=h1,width=w1)
background_label.place(x=0, y=0)
fhini=open('HotelData.log','a')
fhini.close()
fhini=open('HotelCustomerData2.log','a')
fhini.close()
fhi=open("HotelData.log",'r')
k=fhi.readline()
CreditsLabel=Label(MainFrame,bg="#CE9CC0",text="Made By - \n Tanmay Jain \n Shreyasi Barman \n Gunjan Chhablani")
CreditsLabel.place(x=350,y=350)
def getHotelName():
    global HotelN
    global Namebut
    HotelName=ent1.get()
    fhin=open("HotelData.log",'a')
    fhin.write("Hotel Name:"+HotelName+"\n")
    fhin.close()
    HotelN.grid_forget()
    Namebut.grid_forget()
    return HotelName
def getHotelRate():
    global HotelR
    global Ratebut
    HotelRate=ent2.get()
    fhin=open("HotelData.log",'a')
    fhin.write("Hotel Rating:"+HotelRate+"\n")
    HotelR.grid_forget()
    Ratebut.grid_forget()
    fhin.close()
    return HotelRate
if "Hotel Name" not in k:
    global HotelN
    global Namebut
    global Ratebut
    global HotelR
    ent1=StringVar()
    ent2=StringVar()
    HotelN=Entry(MainFrame,textvariable=ent1)
    HotelN.grid(row=0,column=0)
    ent1.set('Enter Hotel Name')
    Namebut=Button(MainFrame,text="Enter",command=getHotelName)
    Namebut.grid(row=0,column=1)
    ent2.set('Enter Hotel Rate')    
    HotelR=Entry(MainFrame,textvariable=ent2)
    HotelR.grid(row=1,column=0)
    Ratebut=Button(MainFrame,text="Enter",command=getHotelRate)
    Ratebut.grid(row=1,column=1)
    fhi.close()
else:
    fhi.close()
class Booking(object):
    def __init__(self):
        self.lname=''
        self.fname=''
        self.record={}
        ent3=StringVar()
        ent3.set('Enter First Name')
        ent4=StringVar()
        ent4.set('Enter Last Name')
        global NewFrame
        NewFrame=Frame(MainFrame)
        NewFrame.configure(bg='#6E7EB1',bd=2)
        NewFrame.place(x=10,y=100)
        def FirstName():
            global FNbut
            self.fname=((ent3.get()).lower()).capitalize()
            self.record['fname']=self.fname
            FNbut.grid_forget()
        global FNentry
        global FNbut
        
        FNentry=Entry(NewFrame,textvariable=ent3)
        FNentry.grid(row=2,column=2)
      
        FNbut=Button(NewFrame,text="Enter",command=FirstName)
        FNbut.grid(row=2,column=3)
            

        def LastName():
            global LNbut
            self.lname=((ent4.get()).lower()).capitalize()
            self.record['lname']=self.lname
            LNbut.grid_forget()
        self.cost=0
        self.record['cost']=self.cost
        global LNentry
        global LNbut
        LNentry=Entry(NewFrame,textvariable=ent4)
        LNentry.grid(row=3,column=2)
        LNbut=Button(NewFrame,text="Enter",command=LastName)
        LNbut.grid(row=3,column=3)
class Hotel(Booking):
    room_price={'Penthouse':1000,'King Deluxe Bedroom':700,'Queen Deluxe Bedroom': 600,'King Standard Bedroom':450,'Queen Standard Bedroom':350}
    hotel_roomall={'Penthouse':[str(100+x) for x in range(1,11)],'King Deluxe Bedroom':[str(200+x) for x in range(1,21)],'Queen Deluxe Bedroom':[str(300+x) for x in range(1,21)],'King Standard Bedroom':[str(400+x) for x in range(1,21)],'Queen Standard Bedroom':[str(500+x) for x in range(1,51)]}
    def __init__(self):
        global NewFrame,gobutton,RoomtypeOptions,CheckInDateLabel,CheckInDateEntry,SelectRoomNoLabel,SelectRoomTypeLabel,FinaliseButton,CheckinDoneNameLabel,BackButton,CheckinDoneIDLabel,Newlabel,Spinbox1
        self.coutd=''
        CheckinDoneIDLabel.grid_forget()
        CheckinDoneNameLabel.grid_forget()
        Booking.__init__(self)
        self.record['checkoutdate']=self.coutd
        k=Hotel.hotel_roomall.keys()
        var1=StringVar()
        SelectRoomTypeLabel=Label(NewFrame,text="Select Room Type")
        SelectRoomTypeLabel.configure(bg='#6E7EB1',bd=2,fg='white')
        SelectRoomTypeLabel.grid(row=5,column=2)
        RoomtypeOptions=OptionMenu(NewFrame,var1,*k)
        RoomtypeOptions.configure(bg='#6E7EB1',bd=2,fg='white')
        RoomtypeOptions.grid(row=5,column=3)
        var2=StringVar()
        CheckInDateLabel=Label(NewFrame,text="Type Date as dd/mm/yy",fg='black')
        CheckInDateLabel.configure(bg='#6E7EB1',bd=2,fg='white')
        CheckInDateLabel.grid(row=4,column=2)
        CheckInDateEntry=Entry(NewFrame,textvariable=var2)
        CheckInDateEntry.grid(row=4,column=3)
        Newlabel=Label(NewFrame,text="Select No of Rooms")
        Newlabel.configure(bg='#6E7EB1',bd=2,fg='white')
        Newlabel.grid(row=6,column=2)
        spinboxvariable=IntVar()
        Spinbox1=Spinbox(NewFrame,from_=1,to=10,textvariable=spinboxvariable)
        Spinbox1.grid(row=6,column=3)       
        SelectRoomNoLabel=Label(NewFrame,text="Select Room Number(s)")
        SelectRoomNoLabel.configure(bg='#6E7EB1',bd=2,fg='white')
        SelectRoomNoLabel.grid(row=7,column=2)       
        def Roomnumbers():
            global LFrame,listofava
            LFrame=Frame(MainFrame)
            self.roomtype=getroomtype()
            print getroomtype()
            if getroomtype():
                RoomAvailable=Hotel.hotel_roomavailable()
                listofava=RoomAvailable[self.roomtype]
                global listbox1,scrollbar1
                scrollbar1=Scrollbar(LFrame, orient=VERTICAL)
                listbox1=Listbox(LFrame,selectmode='multiple',yscrollcommand=scrollbar1.set)
                for i in range(len(listofava)):
                    listbox1.insert(i," "+str(listofava[i]))                
                scrollbar1.config(command=listbox1.yview)
                scrollbar1.pack(side=RIGHT, fill=Y)
                scrollbar1.pack()
                LFrame.config(bg='#6E7EB1')
                listbox1.pack(fill=BOTH)
                LFrame.place(x=155,y=240)
                
                
                
                
        def getroomtype():
            roomtypegot=var1.get()
            self.roomtype=roomtypegot
            self.record['roomtype']=self.roomtype
            return roomtypegot
        gobutton=Button(NewFrame,text="GO",command=Roomnumbers)
        gobutton.grid(row=6,column=4)
        while True:
            allottingid=1000+random.randint(1,10000)
            if allottingid not in Hotel.ids():
                self.id=allottingid
                break
        alpha=False
        self.record['cost']=self.cost
        self.record['id']=self.id
        def finalise():
            global CheckinDoneNameLabel,BackButton,CheckinDoneIDLabel,newbut,FinaliseButton,NewFrame,scrollbar1,listofava,listbox1
            
            self.noofrooms=spinboxvariable.get()
            listget=[]
            for i in listbox1.curselection():
                listget.append(listofava[int(i)])
            if self.fname!='Enter first name' and bool(self.fname) and bool(self.lname) and  self.lname!='Enter last name'  and len(getcindate())==8 and len(listget)==self.noofrooms:
                Hotel.removeallcheckin()
                getroomtype()
                self.cind=getcindate()
                self.record['checkindate']=self.cind
                self.rooms=listget
                self.record['rooms']=self.rooms
                print self.rooms
                self.cost+=Hotel.room_price[self.roomtype]
                self.dumptofile()
                CheckinDoneNameLabel=Label(NewFrame,text=self.record['fname']+" "+self.record['lname']+" entered")
                CheckinDoneIDLabel=Label(NewFrame,text=str(self.id)+"is the ID")
                CheckinDoneNameLabel.grid(row=10,column=9)
                CheckinDoneIDLabel.grid(row=11,column=9)
                newbut=Button(NewFrame,text="New Entry",command=checkin)
                newbut.grid(row=13,column=0)
                BackButton=Button(MainFrame,text="Back",command=back)
                BackButton.grid(row=13,column=13)
                FinaliseButton.grid_forget()
            else:
                Hotel.removeallcheckin()
                FinaliseButton.grid_forget()
                WrongCheckInEntryLabel=Label(NewFrame, text= "WRONG ENTRY.")
                WrongCheckInEntryLabel.grid(row=13,column=0)
                newbut=Button(NewFrame,text="Try Again",command=checkin)
                newbut.grid(row=14,column=0)
        def getcindate():
            cindate=var2.get()
            return cindate
        FinaliseButton=Button(NewFrame,text="FINALISE",command=finalise)
        FinaliseButton.grid(row=9,column=9)
        BackButton=Button(MainFrame,text="Back",command=back)
        BackButton.grid(row=13,column=13)
    @staticmethod
    def hotel_roomavailable():
        hotel_roomavailable=Hotel.hotel_roomall
        l=Hotel.getcustomerlist()
        for j in l:
            for k in Hotel.hotel_roomall.keys():
                if j.coutd=='':
                    for insiderooms in j.rooms:
                        if insiderooms in Hotel.hotel_roomall[k]:
                            hotel_roomavailable[k].remove(insiderooms)
        return hotel_roomavailable
    @staticmethod
    def removeallcheckin():
        global FNentry,FNbut,LNentry,LNbut,BackButton,gobutton,RoomtypeOptions,CheckInDateLabel,CheckInDateEntry,SelectRoomNoLabel,SelectRoomTypeLabel,scrollbar1,Spinbox1,listbox1,Newlabel,LFrame
        FNbut.grid_forget()
        BackButton.grid_forget()
        LNentry.grid_forget()
        LNbut.grid_forget()
        listbox1.pack_forget()
        scrollbar1.pack_forget()
        Spinbox1.grid_forget()
        Newlabel.grid_forget()
        LFrame.place_forget()        
        gobutton.grid_forget()
        CheckInDateLabel.grid_forget()
        CheckInDateEntry.grid_forget()
        SelectRoomNoLabel.grid_forget()
        SelectRoomTypeLabel.grid_forget()          
        RoomtypeOptions.grid_forget()
        gobutton.grid_forget()
        FNentry.grid_forget()
    @staticmethod
    def ids():
        idlist=[]
        for i in Hotel.getcustomerlist():
            idlist.append(i.id)
        return idlist
    @staticmethod   
    def checkout(cid,coutd):
        global FinalCostLabel
        s1=Hotel.getcustomer(cid)
        if s1.coutd=='':
            s1.coutd=coutd
            s1.record['checkoutdate']=coutd        
            a=s1.cind
            b=s1.coutd
            print a
            print b
            l1=a.split('/')
            l2=b.split('/')
            if l2>l1:
                days=((int(l2[0])-int(l1[0])+1)+(int(l2[1])-int(l1[1]))*30+(int(l2[2])-int(l1[2]))*365)-1
                s1.payment_left=int(s1.cost+(days*Hotel.room_price[s1.roomtype]*0.8))*s1.noofrooms
                s1.record['cost']=s1.payment_left
                s1.Finalcost()
                FinalCostLabel=Label(MainFrame,text="The Final Cost is "+str(s1.record['cost']))
                FinalCostLabel.pack()
                print "CHECKOUT DONE"
                Hotel.delcustomer(cid)
                print s1.fname," checked out"
                s1.dumptofile()
            else:
                print "INVALID CHECKOUT DATE"
        else:
            print "Already checked out"
    @staticmethod
    def getcustomerlist():
        l=[]
        fhopen=open('HotelCustomerData2.log','rb')
        while True:
            try:
                l.append(pickle.load(fhopen))
            except(EOFError):
                break
        fhopen.close()
        return l
    @staticmethod      
    def delcustomer(cid):
        l=Hotel.getcustomerlist()
        TemporaryOpen=open('temp.log','wb')
        for j in l:
            if j.id!=int(cid):
                pickle.dump(j,TemporaryOpen)
            else:
                continue
        TemporaryOpen.close()
        import os
        os.remove('HotelCustomerData2.log')
        os.rename('temp.log','HotelCustomerData2.log')
    @staticmethod
    def get_id(finame,laname):
        me=Hotel.getcustomerlist()
        l=[]
        for i in me:
            if i.fname==(finame.lower()).capitalize() and i.lname==(laname.lower()).capitalize():
                l.append(i.id)
        return l
    
                
    @staticmethod               
    def customerdetails(cid):
        m=Hotel.getcustomer(cid)
        for a,b in m.record.items():
            print a,":",b
    @staticmethod
    def getcustomer(cid):
        l=Hotel.getcustomerlist()
        for j in l:
            if j.id==cid:
                return j
    def Finalcost(self):
        print self.record['cost']
    def dumptofile(self):
        fenter=open('HotelCustomerData2.log','ab')
        pickle.dump(self,fenter)
        fenter.close()
def removeallmain():
    global Checkinbut,Checkoutbut,Custdetbut,Quitbut,WelcomeLabel,GETIDbut
    Checkinbut.place_forget()
    GETIDbut.place_forget()
    Checkoutbut.place_forget()
    Custdetbut.place_forget()
    Quitbut.place_forget()
    WelcomeLabel.grid_forget()
def checkin():
    removeallmain()
    s1=Hotel()
def forcheckoutbut():
    global CheckOutButton,CustomerIDEntry1,CheckOutDateEntry,BackButton1,NewFrame
    NewFrame=Frame(MainFrame)
    NewFrame.configure(bg='#6E7EB1',bd=2)
    NewFrame.place(x=150,y=200)
    removeallmain()
    DateVariable=StringVar()    
    custinp2=StringVar()
    custinp2.set("Enter id here")
    DateVariable.set("Enter Date Here")
    def customdeta1():
        custid=int(custinp2.get())
        return custid
    CustomerIDEntry1=Entry(NewFrame,textvariable=custinp2)
    CustomerIDEntry1.grid(row=13,column=12)
    def checkoutfin():
        IDvalforcheckout=customdeta1()
        Datevalforcheckout=str(DateVariable.get())
        Hotel.checkout(IDvalforcheckout,Datevalforcheckout)  
    CheckOutDateEntry=Entry(NewFrame,textvariable=DateVariable)
    CheckOutDateEntry.grid(row=14,column=12)
    CheckOutButton=Button(NewFrame,text="Check Out",command=checkoutfin)
    CheckOutButton.grid(row=15,column=12)
    BackButton1=Button(NewFrame,text="Back",command=back)
    BackButton1.grid(row=16,column=13)
def forcustdbut():
    removeallmain()
    global CustomerIDEntry,GetDetailsButton,ka1,ka2,ka3,ka4,ka5,BackButton,ka6,ka7,NewFrame
    NewFrame=Frame(MainFrame)
    NewFrame.configure(bg='#6E7EB1',bd=2)
    NewFrame.place(x=150,y=200)
    ka1.grid_forget()
    ka2.grid_forget()
    ka3.grid_forget()
    ka4.grid_forget()
    ka5.grid_forget()
    ka6.grid_forget()
    ka7.grid_forget()
    custinp=StringVar()
    custinp.set("Enter id here")
    def customdeta():
        custid=int(custinp.get())
        return custid
    CustomerIDEntry=Entry(NewFrame,textvariable=custinp)
    CustomerIDEntry.grid(row=13,column=12)
    def getdetails():
        global ka1,ka2,ka3,ka4,ka5,ka6,ka7,NewFrame
        am=0
        m=Hotel.getcustomer(customdeta())
        ka1=Label(NewFrame,text="FirstName: "+m.record['fname'])
        ka2=Label(NewFrame,text="LastName: "+m.record['lname'])
        ka3=Label(NewFrame,text="RoomNo(s): "+str(m.record['rooms']))
        ka4=Label(NewFrame,text="ID: "+str(m.record['id']))
        ka5=Label(NewFrame,text="CheckInDate: "+m.record['checkindate'])
        ka6=Label(NewFrame,text="CheckOutDate: "+m.record['checkoutdate'])
        ka7=Label(NewFrame,text="Roomtype: "+m.record['roomtype'])
        ka1.grid(row=15,column=12)
        ka2.grid(row=16,column=12)
        ka3.grid(row=17,column=12)
        ka4.grid(row=18,column=12)
        ka5.grid(row=19,column=12)
        ka6.grid(row=20,column=12)
        ka7.grid(row=21,column=12)
    GetDetailsButton=Button(NewFrame,text="Get Details",command=getdetails)
    GetDetailsButton.grid(row=14,column=12)
    BackButton=Button(NewFrame,text="Back",command=back)
    BackButton.grid(row=13,column=13)
def GETIDfunc():
    removeallmain()
    global CheckOutButton,CustomerIDEntry1,CheckOutDateEntry,BackButton,NewFrame
    NewFrame=Frame(MainFrame)
    NewFrame.configure(bg='#6E7EB1',bd=2)
    NewFrame.place(x=150,y=200)
    var35=StringVar()    
    custinp4=StringVar()
    custinp4.set("Enter First Name")
    var35.set("Enter Last Name")
    def customdeta2():
        custid=custinp4.get()
        return custid
    CustomerIDEntry1=Entry(NewFrame,textvariable=custinp4)
    CustomerIDEntry1.grid(row=13,column=12)
    def checkoutfin():
        global PrintCustomerIDLabel
        IDvalforcheckout=customdeta2()
        Datevalforcheckout=str(var35.get())
        A=Hotel.get_id(IDvalforcheckout,Datevalforcheckout)
        PrintCustomerIDLabel={}
        for i in range(len(A)):
            PrintCustomerIDLabel[i]=Label(NewFrame,text=str(A[i]))
            PrintCustomerIDLabel[i].grid(row=16+i,column=12)
    CheckOutDateEntry=Entry(NewFrame,textvariable=var35)
    CheckOutDateEntry.grid(row=14,column=12)
    CheckOutButton=Button(NewFrame,text="GET ID",command=checkoutfin)
    CheckOutButton.grid(row=15,column=12)
    BackButton=Button(NewFrame,text="Back",command=back)
    BackButton.grid(row=16,column=13)
def end():
    WINDOW.destroy()
def back():
    global Checkinbut,Checkoutbut,NewFrame,Custdetbut,Quitbut,BackButton,CheckinDoneNameLabel,CheckinDoneIDLabel,newbut,CustomerIDEntry,GetDetailsButton,ka1,ka2,ka3,ka4,ka5,ka6,ka7,WrongCheckInEntryLabel,FinalCostLabel,CheckOutButton,CustomerIDEntry1,CheckOutDateEntry,FinaliseButton,GETIDbut,listbox1,WelcomeLabel,PrintCustomerIDLabel,listbox1,LFrame,scrollbar1
    listbox1.pack_forget()
    scrollbar1.pack_forget
    LFrame.place_forget()
    Hotel.removeallcheckin()
    WrongCheckInEntryLabel.grid_forget()
    for i in PrintCustomerIDLabel.keys():
        PrintCustomerIDLabel[i].grid_forget()
    NewFrame.place_forget()
    FinalCostLabel.pack_forget()
    FNentry.grid_forget()
    FNbut.grid_forget()
    LNentry.grid_forget()
    LNbut.grid_forget()
    gobutton.grid_forget()
    RoomtypeOptions.grid_forget()
    CheckInDateEntry.grid_forget()
    CheckInDateLabel.grid_forget()
    SelectRoomNoLabel.grid_forget()
    SelectRoomTypeLabel.grid_forget()
    FinaliseButton.grid_forget()
    CustomerIDEntry1.grid_forget()
    CheckOutDateEntry.grid_forget()
    CheckOutButton.grid_forget()
    ka1.grid_forget()
    ka2.grid_forget()
    ka3.grid_forget()
    ka4.grid_forget()
    ka5.grid_forget()
    ka6.grid_forget()
    ka7.grid_forget()
    CustomerIDEntry.grid_forget()
    GetDetailsButton.grid_forget()
    CheckinDoneNameLabel.grid_forget()
    CheckinDoneIDLabel.grid_forget()
    BackButton.grid_forget()
    newbut.grid_forget()
    Checkinbut=Button(MainFrame,text="Checkin",command=checkin)
    Checkinbut.config(bg='#6E7EB1',fg='white',height=2,width=14,borderwidth=2)
    Checkinbut.place(x=170,y=40)
    WelcomeLabel=Label(MainFrame,text='Welcome')
    WelcomeLabel.grid()
    Checkoutbut=Button(MainFrame,text="Checkout",command=forcheckoutbut)
    Checkoutbut.config(bg='#6E7EB1',fg='white',height=2,width=14,borderwidth=2)
    Checkoutbut.place(x=170,y=125)
    Custdetbut=Button(MainFrame,text="CustomerDetails",command=forcustdbut)
    Custdetbut.config(bg='#6E7EB1',fg='white',height=2,width=14,borderwidth=2)
    Custdetbut.place(x=170,y=210)
    GETIDbut=Button(MainFrame,text="Get customer's ID",command=GETIDfunc)
    GETIDbut.config(bg='#6E7EB1',fg='white',height=2,width=14,borderwidth=2)
    GETIDbut.place(x=170,y=295)
    Quitbut=Button(MainFrame,text="Quit",command=end)
    Quitbut.config(bg='#6E7EB1',fg='white',height=2,width=14,borderwidth=2)
    Quitbut.place(x=170,y=380)
back()
MainFrame.mainloop()

     
