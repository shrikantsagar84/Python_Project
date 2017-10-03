import requests
import multiprocessing
import time
import csv

# creating function for sending mail
def send_email():
    mailgun_server = "https://api.mailgun.net/v3/sandbox93c30d36457345cba9c23ff550bdc119.mailgun.org/messages"      # mailgun server address
    mailgun_api = "key-f07df2afcde2522bf3ccb8a4b32cee6a"        # mailgun api
    email_list = ["shrikantsagar19@gmail.com", "shrikantsagar84@yahoo.com"]     # emails list
    for email in email_list:
        requests.post(
            mailgun_server,
            auth=("api", mailgun_api),
            data={"from": "Shrikant Sagar <shrikant@samples.mailgun.org>",
                  "to": email,
                  "subject": "Sending email by mailgun",
                  "text": "Hello Dear, I hope you are well."})      # sending email using the requests.post method
print(send_email())

def write_to_csv():
    email_contents = {'from': ["Shrikant Sagar <shrikant@samples.mailgun.org>"],        # dictionary
             'to': ["shrikantsagar19@gmail.com"],
             'subject': "Sending email by mailgun",
             'text': "Hello Dear, I hope you are well."}
    with open("email_contents_csv.csv", 'w') as csv_file:       # writing dictionary to csv file
        writer = csv.writer(csv_file)
        for data in email_contents.items():
            writer.writerow(data)
print(write_to_csv())

def parallel_email_send():
    emails_list = [["ss1@ymail.com", "ss2@ymail.com"], ["ss3@ymail.com", "ss4@ymail.com"]]
    for emails in range(len(emails_list)):      # sending email parallel to users using the multiprocessing
        pool = multiprocessing.Pool()           # creating pool object
        em = emails_list[emails]
        response = pool.map(send_email(), em)   # mapping of emails 
        t1 = time.time()                        # time taken to send emails
        pool.close()                            # closing
        pool.join()                             #joining                
        print("Time taken to send Emails: ", time.time()-t1)
print(parallel_email_send())


    
    



        
