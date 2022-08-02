import psycopg2
con=None
curr=None
try:
    con=psycopg2.connect(
        host="localhost",
        database="Tool_Rental",
        user="postgres",
        password="saad",
        port=5432
    )
    curr=con.cursor()
    
except Exception as error:
    print(error)
def deleteRowofTable(name,id):
        if name=='costumer':
            try:
                curr.execute(f"delete from costumer where costumer_id={id}")
            except Exception as error:
                print(error)
                return
        elif name=='Tools':
            try:
                curr.execute(f"delete from Tools where Tools_id={id}")
            except Exception as error:
                print(error)
                return
        print("Delete SUCCESSFUl")
        con.commit()
        

def Displayrentalsbycostumer():
    curr.execute("select rentals.rental_id from costumer inner join rentals on costumer.costumer_id=costumer_id_costumers ;")
    rows= curr.fetchall()
    
    for row in rows:
        lst=query_rentals("*",f"rental_id={row[0]}")
        print(lst)

def DisplayToolByJob(job):
    curr.execute(f"select Tools_jobs.tool_id_tools from Jobs inner join Tools_jobs on Jobs.job_id=Tools_jobs.job_id_jobs and jobs.job_name='{job}' ")
    rows=curr.fetchall()
    for row in rows:
        print(get_tool_name(row[0]))
def get_rental_days(id):
    curr.execute(f"select Rental_duration from Tools where Tools_id={id};")
    Rental_duration=curr.fetchone()
    return Rental_duration[0]
def query_customers(seletion,condition=None):
    rows=None
    
    if condition is None:
        curr.execute(f"select {seletion} from Costumer;")
    else:
        curr.execute(f"select {seletion} from Costumer where {condition};")
    rows=curr.fetchall()
    
    return rows

def query_tools(seletion,condition=None):
    rows=None
    
    if condition is None:
        curr.execute(f"select {seletion} from tools;")
    else:
        curr.execute(f"select {seletion} from tools where {condition};")
    rows=curr.fetchall()
    
    return rows
def query_rentals(seletion,condition=None):
    rows=None
    
    if condition is None:
        curr.execute(f"select {seletion} from Rentals;")
    else:
        curr.execute(f"select {seletion} from Rentals where {condition};")
    rows=curr.fetchall()
    
    return rows




def  get_tool_id(name):
    curr.execute(f"select Tools_id from Tools where title={name};")
    id=curr.fetchone()
    return id

def get_tool_name(id):
    curr.execute(f"select title from Tools where Tool_id={id};")
    toolname=curr.fetchone()
    return toolname[0]

def get_customer_id(name):
    curr.execute(f"select Costumer_id from Costumer where fname={name};")
    id=curr.fetchone()
    return id

def get_customer_name(id):
    curr.execute(f"select fname from Costumer where Costumer_id={id};")
    name=curr.fetchone()
    return name[0]
def display_query_menu():
      print("option 1 is selected\n")
      print("1. Display all customers\n")
      print("2. Display all tools (optionally by job)")
      print("3. Display all rentals (optionally by customer)")
      innerinput=input("Enter your option please\n")
      if innerinput=='1':
        allCostomerDisplay()
      elif innerinput=='2':
        curr.execute('select * from jobs;')
        jobs=curr.fetchall()
        for job in jobs:
            print(job[1]+" use these tools")
            DisplayToolByJob(job[1])
      elif innerinput=='3':
        Displayrentalsbycostumer()
        
        
def allCostomerDisplay():
    curr.execute("select * from Costumer;")
    rows=curr.fetchall()
    for row in rows:
        print(f"id:{row[0]}")
        print(f"fname:{row[1]}")
        print(f"Lname:{row[2]}")
        print(f"postal_code:{row[3]}")
        print(f"phonenumber:{row[4]}")
        print(f"Membership_date:{row[5]}")
        print("\n\n")
def display_main_menu():
    userinput=0
    
    while userinput!="x":
        print("1. Queries (sub-menu)")
        print("2. Insert tool rental")
        print("3. Delete tool rental")
        print("x. Exit")
        userinput=input("Enter your option please\n")
        if userinput=='1':
            display_query_menu()
          

        elif userinput=='2':
            
            print("option 2 is selected\n")
            customerInsert()

        elif userinput=='3':
            print("option 3 is selected\n")
            name=input('please enter name table row you need to delete\n')
            id=input('please enter row id\n')
            deleteRowofTable(name,id)
        elif userinput=='x':
            print("EXIT\n")
            break
def customerInsert():
        Fname=input("please enter your first name\n")
        Lname=input("please enter your last name\n")
        pcode=input("please enter your postal code\n")
        pnumber=input("please enter your Phone number code\n")
        Mdate=input("please enter your Membership_date in yyyy-mm-dd format\n")
        try:
            curr.execute(f'''insert into Costumer(Fname,Lname,postal_code,phonenumber,Membership_date)
                    values('{Fname}','{Lname}',{pcode},{pnumber},'{Mdate}');''')
        except Exception as error:
            print("insertion failed error is:")
            print(error)
        print("successful insertion")
        con.commit()
            
       
display_main_menu()
# print(query_customers("*"))
# DisplayToolByJob("electrical")
# print(get_customer_name(1))
# print(get_tool_name(1))
if curr is not None:
    curr.close()
if con is not None:
    con.close()
