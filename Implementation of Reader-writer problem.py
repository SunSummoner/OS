#Implementation of Reader-writer problem using semaphores

import threading
import time
import random



# Declaring Semaphores
mutex = threading.Semaphore()  
wrt = threading.Semaphore()  
#r_c = 0  



def reader(n):
    for h in range (n):
        # Reader function
        mutex.acquire()
        
        file = open('Kritika114.txt', 'r')
        # Opening the file
        print("READER ",h+1," IS READING THE FILE")
        '''This will print every line one by one in the file'''
        # for each in file:
        #     print (each)
        rv = file.read()
        print(rv)
        #Reading the file

        file.close()
        # Closing the file
        mutex.release()


def writer():
    # Writer function

    wrt.acquire()
    li=input("What do you want to write?")
    file = open('Kritika114.txt', 'a' )
    li = "\n" +li
    #print("WRTING WRTING IN THE FILE")
    # print(li)
    file.write(li)
    file.close()
    #Closing the file

    wrt.release()
    #Releasing th lock

#main 
for j in range(2):

    #Running the threads
    reader(4)
    writer()
    reader(4)
    reader(4)
    writer()
    reader(4)
    reader(4)
    reader(4)
    reader(4)
    writer()
    reader(4)

    

