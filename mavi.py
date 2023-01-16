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
        sql="INSERT INTO dokumanlar (sirket, borc , gelecek) VALUES (%s, %s ,%s)"
        val=(self.company_name,self.debt,self.payment)
        mycursor.execute(sql,val)
        mydb.commit()

    def __str__(self):
        return f"Şirket Adı:{self.company_name} Tarih:{self.date} Borç:{self.debt} Alınacak:{self.payment}"

def islemler():   
    while(True):
        print("1:Yeni Bir Döküman Girişi \n2:Borçlar Alınacaklar \n ")
        choice=input("Hangi İşlemi Seçmek İstersiniz?")
        if choice=="1":
            print("Çıkmak İçin  0")
            print("ŞİRKET İSMİ")
            company_name=input("")
            if company_name=="0":
                continue
                
            company_name=payments_debts(company_name)
        if choice=="2":
            mycursor.execute("SELECT * FROM dokumanlar")
            result=mycursor.fetchall()
            for results in result:
                print(results)

        


                        
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin123",
    database="mydatabase"
)
mycursor=mydb.cursor()
mycursor.execute("SHOW TABLES")
if ('dokumanlar',) in mycursor:
    islemler()
else:
    mycursor.execute("CREATE TABLE dokumanlar (sirket VARCHAT(255),borc INT,alinacak INT)")
    islemler()



                    
