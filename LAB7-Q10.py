''' Write a python script to display students’ details who have email id on same host (i.e. gmail.com, yahoo.com, rediffmail.com etc ) '''
def email_host(host):
    return [D1[enrolment] for enrolment, email in D6.items() if host in email]
host = input("Enter email host (e.g., gmail.com): ")
print(email_host(host))
