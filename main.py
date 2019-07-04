from O365 import Account

#### Connexion API Office Rest 365 ####
def AccountO365_Connexion():
    credentials = ('client_id', 'client_secret')

    account = Account(credentials)
    m = account.new_message()
    m.to.add('to_example@example.com')
    m.subject = 'Testing!'
    m.body = "Coucou on dirait que ça marche."
    m.send()

#### Get File ---- Write ----> Storage ####

#### OCR ####

#### Interpret order -----> Customer{}, Articles{} ####

#### Cosmos DB ####

#### EDI transformation ####

#### Order assistance interface (Web app) ####

#### Export to Order Systeme ####

## COUCOU ca marche ###

if __name__ == '__main__':
    pass