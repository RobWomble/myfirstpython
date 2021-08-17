#!/usr/bin/env python3
## Moving files with SFTP

## import paramiko so we can talk SSH
import paramiko
import os

cont_ask = ''

def mover():
    global cont_ask
    input_add = input("enter address: ")
    input_user = input("enter username: ")
    input_pass = input("enter password: ")

    ## where to connect to
    t = paramiko.Transport(input_add, 22) ## IP and port

    ## how to connect (see other labs on using id_rsa private/public keypairs)
    t.connect(username=input_user, password=input_pass)

    ## Make an sftp connection object
    sftp = paramiko.SFTPClient.from_transport(t)

    ## iterate across the files within directory
    for x in os.listdir("/home/student/filestocopy/"): # iterate on directory contents
      if not os.path.isdir("/home/student/filestocopy/"+x): # filter everything that is NOT a directory
        sftp.put("/home/student/filestocopy/"+x, "/tmp/"+x) # move file to target location

    ## close the connection
    sftp.close() # close the connection

    cont_ask = input("type 'q' and press enter to quit, or anything else to continue")

while cont_ask != 'q':
    mover()


