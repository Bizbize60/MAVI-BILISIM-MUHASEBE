# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 14:29:03 2023

@author: Tunahan Turgut

"""
import mysql.connector

class payments_debts:
    def __init__(self,company_name):
        self.company_name=company_name
        self.debt=input("Borç?")
        self.payment=input("ALINACAK?")
        sql="INSERT INTO MAVI (sirket, borc , alinacak) VALUES (%s, %s ,%s)"
        val=(self.company_name,self.debt,self.payment)
        mycursor.execute(sql,val)
        mydb.commit()

    def __str__(self):
        return f"Şirket Adı:{self.company_name} Tarih:{self.date} Borç:{self.debt} Alınacak:{self.payment}"

def islemler():
    while(True):
        print("1:Yeni Bir Döküman Girişi \n2:TÜM GEÇMİŞ\n3:TEK BİR ŞİRKETLE OLAN GEÇMİŞ\n4:ZATEN VAR OLAN ŞİRKET\n ")
        choice=input("Hangi İşlemi Seçmek İstersiniz?")
        if choice=="1":
            add_new_document()
        if choice=="2":
            list_all()
        if choice=="3":
            specific_company()
        if choice=="4":
            add_to_document()
def add_new_document():
    print("Çıkmak İçin  0")
    print("ŞİRKET İSMİ")
    company=input("")
    if company=="0":
        islemler()
    sql=(f"SELECT * FROM MAVI WHERE sirket='{company}'")
    mycursor.execute(sql)
    if mycursor.fetchall():
        print("BÖYLE BİR KAYIT ZATEN VAR")
        islemler()
    company=payments_debts(company)            
def list_all():
    mycursor.execute("SELECT * FROM mavi")
    result=mycursor.fetchall()
    for results in result:
        print(results)
def specific_company():   
    company=input("HANGİ ŞİRKET?")
    sql=(f"SELECT * FROM MAVI WHERE sirket='{company}'")
    mycursor.execute(sql)
    if not mycursor.fetchall():
        print("BÖYLE BİR ŞİRKET YOK")
        islemler()
        results=mycursor.fetchall()
        i=0
    for data in results:
        print(data)
        i+=1
        if i==5:
            break
    sql=(f"SELECT borc FROM MAVI WHERE sirket='{company}'")
    mycursor.execute(sql)
    results=mycursor.fetchall()
    total_borc=0
    for borc in list(results):
        liste=list(borc)
        total_borc+=liste[0]

    sql=(f"SELECT alinacak FROM MAVI WHERE sirket='{company}'")
    mycursor.execute(sql)
    results=mycursor.fetchall()
    total_alinacak=0
    for alinacak in results:
        liste=list(alinacak)
        total_alinacak+=liste[0]
    if total_alinacak>total_borc:
        print("+",total_alinacak-total_borc)
    else:
        print("-",total_borc-total_alinacak)  
def add_to_document():
    company=input("HANGİ ŞİRKET?")
    sql=f"(SELECT * FROM mavi WHERE sirket='{company}')"
    mycursor.execute(sql)

    if not mycursor.fetchall():
        print("BÖYLE BİR KAYIT YOK")
    else:
        borc=input("borc?")
        alinacak=input("alinacak?")
        sql="INSERT INTO MAVI (sirket,borc,alinacak) VALUES (%s, %s, %s)"
        val=(company,borc,alinacak)
        mycursor.execute(sql, val)
        mydb.commit()        
                        
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin123",
    database="mydatabase"
)
mycursor=mydb.cursor()
mycursor.execute("SHOW TABLES")
if ('mavi',) in mycursor:
    islemler()
else:
    mycursor.execute("CREATE TABLE MAVI (sirket VARCHAR(255),borc INT,alinacak INT,tarih DATE)")
    islemler()



                    
