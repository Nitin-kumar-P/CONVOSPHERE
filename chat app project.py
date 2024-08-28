from tkinter import *
from tkinter import messagebox as mg
import openai as bot
import mysql.connector as cc
import smtplib as mail

"""
online database data:
    Host: sql12.freesqldatabase.com
Database name: sql12664932
Database user: sql12664932
Database password: yBwbZKJHW2
Port number: 3306
"""

"""created login credentials so far for test purpose you may create new 
 username, password
 'nitin', 'ngtnitin007'
  'test',  'test123'
  'nitin','nitinkumar007'
"""

con= cc.connect(host="sql12.freesqldatabase.com",user="sql12664932",password="yBwbZKJHW2",database="sql12664932",port="3306")#online host
cur=con.cursor()
#created username = nitin and password= ngtnitin007
def control():
    name= ent.get()
    password=ent2.get()
    passc=ent_c.get()
    sure=mg.askquestion("confirmation","are you sure")
    if sure=="yes":
        if password!=passc:
            mg.showerror("error","please check your password")
        elif password==passc:
            if name=="" or passc=="" or password =="":
                mg.showerror("error","fields cannot be blank")
            else:
                inserting="insert into users(user_name,password) values('{}','{}')".format(name,passc)
                cur.execute(inserting)
                con.commit()
                cur.execute("select * from users")
                a=cur.fetchall()
                k = True
                if k==True:
                    mg.showinfo("restart","all done sucessfully pls restart your programe \n THANKS FOR USING")
                    res.destroy()




def reg():
    global ent,ent2,ent_c,res
    root.destroy()
    res=Tk()
    res.title("REGISTRATION")
    res.maxsize(320,400)
    res.geometry("320x400")
    res.minsize(320,400)
    res.config(bg="#121212") # or I can use res["background"]="#121212" as I did below
    l1=Label(res,text="CONVO SPHERE",font="impact",pady=2,padx=70,bg="yellow")
    l1.place(x=50,y=40)
    your_name=Label(res,text="Your Name",font=("impact",12,"italic"),bg="#121212",fg="yellow")
    your_name.place(x=30,y=88)
    ent=Entry(res,width=45)
    ent.place(x=30,y=125)
    your_pass = Label(res, text="Your password", font=("impact", 12, "italic"), bg="#121212", fg="yellow")
    your_pass.place(x=30, y=162)
    ent2 = Entry(res, width=45)
    ent2.place(x=30, y=200)
    confirm_pass = Label(res, text="Confirm Your Password", font=("impact", 12, "italic"), bg="#121212", fg="yellow")
    confirm_pass.place(x=30, y=230)
    ent_c = Entry(res, width=45)
    ent_c.place(x=30, y=265)
    ent_c.config(show="*")
    sub=Button(res,text="SUBMIT",padx=10,font="impact",bg="yellow",activebackground="#121212",activeforeground="white",
               command=control)
    sub.place(x=120,y=300)



def gpt():
    user_data=user_entry.get("1.0","end")
    print(user_data)
    f=open("api key.txt","r")
    key=f.read()
    bot.api_key=key
    bot_answer=bot.ChatCompletion.create(model="gpt-3.5-turbo",messages=[{"role":"user","content":user_data}])
    response=bot_answer.choices[0].message.content.strip()
    print(response)
    bot_entry.config(state="normal")
    bot_entry.insert(0.0,response)
    bot_entry.config(state="disabled")

def check():
    #HOME BUTTON FUNTION
    def main():
        global user_entry, bot_entry, k5, root2
        try:
            root3.destroy()
        except:
            pass
        root2 = Tk()
        root2.title("CONVO SPHERE screen")
        root2.geometry("740x440")
        root2.maxsize(740, 440)
        root2.minsize(740, 440)
        root2["background"] = "#121212"
        # main program start
        user_input = Label(text="START YOUR CHAT BELOW:", fg="yellow", font=("impact", 12, "italic"), bg="#121212")
        user_input.place(x=150, y=250)
        # bot reply start
        bot_entry = Text(root2, width=60, height=7, font=("impact", 12),state="disabled")
        bot_entry.place(x=150, y=80)

        # bot reply end
        # user entry start

        user_entry = Text(root2, width=60, height=7, font=("impact", 12))
        user_entry.place(x=150, y=280)
        # user entry end

        submit_button = Button(root2,text="SUBMIT", font=("Impact", 12), pady=2, padx=2, bg="yellow", fg="black",
                               activebackground="#121212",
                               activeforeground="white",command=lambda :gpt())
        submit_button.place(x=5, y=300)
        labelT = Label(root2, text="CONVO SPHERE", bg="yellow", fg="black", font="impact", padx=2, pady=2)
        labelT.place(x=50, y=35, width=645)
        home = Button(root2, text="HOME", font="impact", bg="yellow", fg="black", activeforeground="white",
                      activebackground="#121212")
        home.place(x=5, y=85, width=110)
        about = Button(root2, text="ABOUT", font="impact", bg="yellow", fg="black", activeforeground="white",
                       activebackground="#121212", command=lambda :info())
        about.place(x=5, y=135, width=109)
        contact = Button(root2, text="CONTACT", font="impact", bg="yellow", fg="black", activeforeground="white",
                         activebackground="#121212",command=lambda: con())
        contact.place(x=5, y=185, width=107)
    #ABOUT BUTTON FUNCTION
    def info():
        global root3
        try:
            root2.destroy()
        except:
            pass
        root3 = Tk()
        root3.title("CONVO SPHERE screen")
        root3.geometry("740x440")
        root3.maxsize(740, 440)
        root3.minsize(740, 440)
        root3["background"] = "#121212"
        labela = Label(root3, text="", font=("arial", 15, "bold"), padx=5,
                       pady=5,
                       bg="#121212",
                       fg="white")
        labela.place(x=235, y=80)
        labelT = Label(root3, text="ABOUT THE PROJECT", bg="yellow", fg="black", font="impact", padx=2, pady=2)
        labelT.place(x=50, y=35, width=645)
        home = Button(root3, text="HOME", font="impact", bg="yellow", fg="black", activeforeground="white",
                      activebackground="#121212", command=lambda : main())
        home.place(x=5, y=85, width=110)
        about = Button(root3, text="ABOUT", font="impact", bg="yellow", fg="black", activeforeground="white",
                       activebackground="#121212")
        about.place(x=5, y=135, width=109)
        contact = Button(root3, text="CONTACT", font="impact", bg="yellow", fg="black", activeforeground="white",
                         activebackground="#121212",command= lambda :con())
        contact.place(x=5, y=185, width=107)

        information=Text(root3,width=61,height=17,fg="yellow",font="impact",bg="#121212")
        information.place(x=140,y=85)
        information.insert("1.0","Welcome to  CONVO SPHERE, where advanced artificial intelligence technology"
                                 " meets seamless communication. IAM  pleased to present an unparalleled chat experience "
                                 "\nthat transcends traditional messaging, affording a unique opportunity "
                                 "for human \n interaction with cutting-edge AI technology.The AI chat app has been designed"
                                 " to \nrevolutionize how you interact and communicate with others. "
                                 "It is powered by \nstate-of-the-art technology similar to the renowned ChatGPT. "
                                 "This technology \nenables the app to offer a personalized and dynamic conversation "
                                 "that adapts to \nyour unique style, preferences, and needs.CONVO SPHERE brings "
                                 "the power of \nadvanced language models to your fingertips, "
                                 "providing a chat experience that is \nboth engaging and informative."
                                 " Whether you seek information, companionship, or \nsimply a bit of fun banter,"
                                 "  \nCONVO SPHERE is here to elevate your chat experience."
                                 
                                 "Come with me on the frontier \nof artificial intelligence and human interaction,"
                                 " where every conversation is an \nexploration of limitless possibilities. "
                                 "Let the convo sphere be your virtual companion, guide, and conversational ally."
                                 " Immerse yourself in a world where technology meets warmth, where innovation "
                                 "meets connection.Get ready to tackle a chat experience \nlike never before."
                                 "                                                                                "
                                 " \nWelcome to CONVO SPHERE, where conversation evolves, and connections flourish.")
        information.config(state="disabled")
    #contact page
    def con():
        global root3,mes
        try:
            root2.destroy()
        except:
            pass
        root3 = Tk()
        root3.title("CONVO SPHERE screen")
        root3.geometry("740x440")
        root3.maxsize(740, 440)
        root3.minsize(740, 440)
        root3["background"] = "#121212"
        labela = Label(root3, text="", font=("arial", 15, "bold"), padx=5,
                       pady=5,
                       bg="#121212",
                       fg="white")
        labela.place(x=235, y=80)
        labelT = Label(root3, text="SEND AN EMAIL ", bg="yellow", fg="black", font="impact", padx=2, pady=2)
        labelT.place(x=50, y=35, width=645)
        home = Button(root3, text="HOME", font="impact", bg="yellow", fg="black", activeforeground="white",
                      activebackground="#121212", command=lambda: main())
        home.place(x=5, y=85, width=110)
        about = Button(root3, text="ABOUT", font="impact", bg="yellow", fg="black", activeforeground="white",
                       activebackground="#121212",command=lambda:info())
        about.place(x=5, y=135, width=109)
        contact = Button(root3, text="CONTACT", font="impact", bg="yellow", fg="black", activeforeground="white",
                         activebackground="#121212")
        contact.place(x=5, y=185, width=107)
        mes=Text(root3,width=61,height=14,font="impact")
        mes.place(x=140,y=90)
        sub=Button(root3,text="SUBMIT",font="impact",bg="yellow",fg="black",activebackground="#121212",
                   activeforeground="white",command=lambda :email())
        sub.place(x=595,y=385,width=100)
    #mail system
    def email():
        message= mes.get("1.0","end")
        sender_mail="chatappsender@gmail.com"
        receiver_mail="thechatapp007@gmail.com"
        password="euul vxrp eqxi yffv"

        server=mail.SMTP("smtp.gmail.com",587)
        server.starttls()
        log=server.login(sender_mail,password)
        print("logged into the server")
        main_mail= server.sendmail(sender_mail,receiver_mail,message)
        print("message sent!")
        L2 = Label(root3, text="THANKS FOR YOUR FEED BACK!", bg="#121212", fg="yellow", font="impact")
        L2.place(x=150, y=385)



    # MAIN PAGE OF THE PROGRAM START

    Name=EN.get()
    Pass=EP.get()
    confirmation=mg.askquestion("confirmation","Are You Sure")
    cur.execute("select * from users")
    data=cur.fetchall()
    list1=[data]
    k1 = False
    k10= False
    K11=False
    for i in list1:
        while True:
            for j in i:
                l2=list(j)
                if confirmation=="yes":
                    if Name=="" or Pass=="":
                        k10=True
                        mg.showerror("error","empty user name or password is not available")
                        break
                    elif Name ==l2[1]   and Pass ==l2[2] :
                        global user_entry,bot_entry
                        k1 =True
                        root.destroy()
                        root2=Tk()
                        root2.title("CONVO SPHERE screen")
                        root2.geometry("740x440")
                        root2.maxsize(740,440)
                        root2.minsize(740,440)
                        root2["background"]="#121212"
                        #main program start
                        #bot reply start
                        bot_entry = Text(root2, width=60, height=7, font=("impact", 12),state="disabled")
                        bot_entry.place(x=150, y=80)

                        #bot reply end
                        #user entry start
                        user_input = Label(text="START YOUR CHAT BELOW:", fg="yellow", font=("impact", 12, "italic"), bg="#121212")
                        user_input.place(x=150, y=250)
                        user_entry = Text(root2,width=60,height=7,font=("impact",12))
                        user_entry.place( x=150, y=280)
                        #user entry end
                        submit_button=Button(text="SUBMIT",font=("Impact",12),pady=2,padx=2,bg="yellow",fg="black"
                                             ,activebackground="#121212",activeforeground="white",command=lambda :gpt())
                        submit_button.place(x=5,y=300)

                        #main program end
                        labelT=Label(root2,text="CONVO SPHERE",bg="yellow",fg="black",font="impact",padx=5,pady=2)
                        labelT.place(x=50,y=35,width=645)
                        home= Button(root2,text="HOME",font="impact",bg="yellow",fg="black",activeforeground="white",
                                     activebackground="#121212")
                        home.place(x=5,y=85,width=110)
                        about = Button(root2, text="ABOUT", font="impact", bg="yellow", fg="black", activeforeground="white",
                                      activebackground="#121212",command=lambda: info())
                        about.place(x=5, y=135,width=109)
                        contact=Button(root2,text="CONTACT",font="impact", bg="yellow", fg="black", activeforeground="white",
                                      activebackground="#121212",command=lambda : con())
                        contact.place(x=5,y=185,width=107)


                elif confirmation=="no":
                    K11=True
            break
    if k1 == False and k10==False and K11 ==False:
        mg.showwarning("warning", """Incorrect user_name/Password please check again""")

        #MAIN PAGE OF THE PROGRAM END

#LOGIN PAGE GUI START
root=Tk()
root.title("CONVO SPHERE")
root.geometry("320x400")
root.maxsize(320,400)
root.minsize(320,400)
img= PhotoImage(file="logo/logo FINAL.png")
root.iconphoto(True,img)
root["background"]="#121212"

L= Label(root,text="CONVO SPHERE ",font="impact",pady=2,padx=70,bg="yellow")
L.place(x=50,y=35)
t1=Label(root,text="Your Name",font=("impact",12,"italic"),bg="#121212",fg="yellow")
t1.place(x=30,y=104)
EN=Entry(root,width=43)
EN.place(x=35,y=130)
t2=Label(root,text="Your Password",font=("impact",12,"italic"),bg="#121212",fg="yellow")
t2.place(x=30,y=180)
EP=Entry(root,width=43,show="*")
EP.place(x=35,y=207)
sb=Button(root,text="SUBMIT",padx=10,font="impact",bg="yellow",activebackground="#121212",activeforeground="white",command=check)
sb.place(x=175,y=280)
sign_up=Button(root,text="SIGN UP",padx=10,font="impact",bg="yellow",activeforeground="white",activebackground="#121212",
               command= reg)
sign_up.place(x=80,y=280)
#LOGIN PAGE GUI END




root.mainloop()