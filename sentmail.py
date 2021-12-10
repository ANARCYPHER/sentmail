#! py
######################################
#Sent Mail from SMTB                 #
#                                    #
#                                    #
######################################

import smtplib

server = smtplib.SMTB('smtb.gmail.com', 587)

server.login('mymail@gmail.com', 'justfordemo')

server.sendmail('mymail@gmail.com', connect@connect', 'mail sent from Python')
print('Mail sent')