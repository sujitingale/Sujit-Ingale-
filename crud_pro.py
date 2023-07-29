# ------------------------------- CRUD PROJECT------------------------------

import mysql.connector as my_module

print("\n--------------------------------------------------")
print("***********  Welcome to my_company ***********")

def insert(mycon,mycur):
	try:
		print("\n--------------------------------------------------\n")
		id=int(input("Enter Employee id : "))
		name=input("Enter Employee name : ")
		salary=int(input("Enter Employee salary : "))
		query="insert into employee(id,name,salary) values(%s,%s,%s)"
		value=(id,name,salary)
		mycur.execute(query,value)
		mycon.commit()
		print("\n",mycur.rowcount," row is inserted \n")
		print("\n--------------------------------------------------")
	except my_module.Error as e:
		print(e)

def display(mycur):
	try:
		print("\n--------------------------------------------------")
		query="select * from employee"
		mycur.execute(query)
		print("|------------------------------------|")
		print("| id     |  name        |  salary ")
		print("|------------------------------------|")
		for i in mycur.fetchall() :
			print("| ",i[0],"\t |",i[1],"\t|",i[2])
			print("|------------------------------------|")
	except my_module.Error as e:
		print(e)


def update(mycon,mycur):
	try:
		print("\n--------------------------------------------------")
		id=int(input("Enter Employee id for update : "))
		name=input("Enter updated Employee name : ")
		salary=int(input("Enter updated Employee salary : "))
		query="update employee set name=%s,salary=%s where id=%s"
		value=(name,salary,id)
		mycur.execute(query,value)
		mycon.commit()
		print("\n",mycur.rowcount," row is updated \n")
	except my_module.Error as e:
		print(e)


def delete(mycon,mycur):
	try:
		print("\n--------------------------------------------------")
		id=input("Enter Employee id for delete : ")
		query="delete from employee where id="+id
		mycur.execute(query)
		mycon.commit()
		print("\n",mycur.rowcount," row is deleted \n")
		print("\n--------------------------------------------------")
	except my_module.Error as e:
		print(e)


def menu ():
	try:
		mycon=my_module.connect(host="localhost",user="root",password="",database="my_company")
		mycur=mycon.cursor()
		option="yes"
		while option=="yes":
			print("-----------------------------------------------\n\n\t OPTIONS :-")
			print("\n\t 1. INSERT \n\t 2. DISPLAY \n\t 3. UPDATE \n\t 4. DELETE \n\t 5. EXIT \n")

			ch=input("enter your choice :")
			if ch=="1" or ch=="insert" or ch=="INSERT":
				insert(mycon,mycur)
			elif ch=="2" or ch=="display" or ch=="DISPLAY":
				display(mycur)
			elif ch=="3" or ch=="update" or ch=="UPDATE":
				update(mycon,mycur)
			elif ch=="4" or ch=="delete" or ch=="DELETE":
				delete(mycon,mycur)
			else:
				print("you are Exited")
				exit()
	except my_module.Error as e:
		print(e)

menu()