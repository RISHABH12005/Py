''' Write a python script to display students’ details whose mobile service provider is same
( first two bits 94: BSNL, 98: Airtel, 89:Idea, 77:Reliance, 97:Idea, 99:Vodafone, 79:Docomo) '''
def provider(provider):
    return [D1[enrolment] for enrolment, mobile in D3.items() if mobile.startswith(provider)]
provider = input("Enter provider code (e.g., 98 for Airtel): ")
print(provider(provider))