#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 00:07:19 2017

@author: tizianomartinhernando
"""
import MySQLdb, os
 
def agregar(server,user,passwd,bd):
    db = MySQLdb.connect(server,user,passwd,bd)
    cursor = db.cursor()
    name = input('[+]Nombre: ')
    telefono = input('[+]Telefono: ')
    mail= input('[+]E-Mail: ')
    cursor.execute("insert into contactos (nombre,telefono,mail) values ('%s','%s','%s')"%(name,telefono,mail))
    print ('Datos agregados correctamente...')
    cursor.fetchall()
    cursor.close()
    input("> Press Enter...")
    run()
def ver (server,user,passwd,bd):
    try:
        db = MySQLdb.connect(server,user,passwd,bd)
        ztux = db.cursor()
        ztux.execute("select * from %s "%(bd))
        a = ztux.fetchall()
        for i in a: #Se crea una lista en la variable i
           if i=='':
               print ("No hay contactos...")
           else:
               print ('[+]Nombre:'),i[0],('\n[+]Telefono:'),i[1],('\n[+]E-Mail:'),i[2],("\n----------") #Mostramos La lista
        ztux.close()
        input("> Press Enter...")
        run()
    except:
        print ('[*]Error al conectar a la base de Datos...\n')
        run()
     
def buscar(server,user,passwd,bd):
    try:
        db = MySQLdb.connect(server,user,passwd,bd)
        buscar = input('[+]Nombre del contacto: ')
        ztux = db.cursor()
        ztux.execute("select * from %s where nombre='%s'"%(bd,buscar))
        a = ztux.fetchall()
        for i in a:
            print ('[+]Nombre:'),i[0],('\n[+]Telefono:'),i[1],('\n[+]E-Mail:'),i[2]
        ztux.close()
        input("> Press Enter...")
        run()
    except:
        print ('[*]Error al conectar a la base de Datos...\n')
        run()
         
def editar(server,user,passwd,bd):
    try:
        db = MySQLdb.connect(server,user,passwd,bd)
        print ('[1]Nombre\n[2]Telefono\n[3]E-mail\n[+]Regresar')
        opc =input('Que desas editar: ')
        if opc=='1':
            editar = input('[+]Nombre del contacto a editar: ')
            cambiar = input('[+]Escribe el nuevo nombre del contacto: ')
            ztux = db.cursor()
            ztux.execute("update %s set nombre='%s' where nombre='%s'"%(bd,cambiar,editar))
            ztux.close()
            print ('Contacto Actualizado...')
            input("> Press Enter...")
            run()
        elif opc=='2':
            editar = input('[+]Nombre del contacto a editar: ')
            cambiar = input('[+]Escribe el nuevo numero del contacto: ')
            ztux = db.cursor()
            ztux.execute("update %s set telefono='%s' where nombre='%s'"%(bd,cambiar,editar))
            ztux.close()
            print ('Contacto Actualizado...')
            input("> Press Enter...")
            run()
        elif opc=='3':
            editar = input('[+]Nombre del contacto a editar: ')
            cambiar = input('[+]Escribe el nuevo e-mail del contacto: ')
            ztux = db.cursor()
            ztux.execute("update %s set mail='%s' where nombre='%s'"%(bd,cambiar,editar))
            ztux.close()
            print ('Contacto Actualizado...')
            input("> Press Enter...")
            run()
        elif opc=='+':
            run()
        else:
            print ('Opcion Incorrecta...')
            run()
             
    except:
        print ('[*]Error al conectar a la base de Datos...\n')
        input("> Press Enter...")
        run()
 
def borrar(server,user,passwd,bd):
    try:
        db = MySQLdb.connect(server,user,passwd,bd)
        borrar = input('[+]Nombre del contacto: ')
        ztux = db.cursor()
        ztux.execute("delete from %s where nombre='%s'"%(bd,borrar))
        ztux.close()
        print ('[+]Contacto borrado con exito...')
        input("> Press Enter...")
        run()
    except:
        print ('[*]Error al conectar a la base de Datos...\n')      
  
def run():
    os.system('clear') #Cambiar "clear" por "cls" si Usas Windows
    print( '-------------------------')
    print ('    Agenda by [Z]tuX     ')
    print ('http://ztux.blogspot.com/')
    print ('   ztux.ztux@gmail.com   ')
    print ('-------------------------')
    print ('''[1] Agregar contacto 
[2] Ver contactos    
[3] Buscar Contacto  
[4] Editar Contacto  
[5] Borrar contacto  
[0] Salir            
''' )#CONFIGURAR AQUI#
    server='localhost' #Servidor MySQL
    user='root'        #Usuario MySQL
    passwd='chucho'    #Passwd MySQL
    bd='contactos'     #Base de Datos
    #################
    opc = input('> ')
    if opc =='1':
        agregar(server,user,passwd,bd)
    elif opc =='2':
        ver(server,user,passwd,bd)
    elif opc =='3':
        buscar(server,user,passwd,bd)
    elif opc=='4':
        editar(server,user,passwd,bd)
    elif opc=='5':
        borrar(server,user,passwd,bd)
    elif opc=='0':
        return 0
    else:
        print ('[*]Opcion Incorrecta...')
        run()
run()
