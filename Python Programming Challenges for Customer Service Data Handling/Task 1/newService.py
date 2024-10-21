import Main


def new_service():
    # information gathering and submission of new ticket
    ticket_creation = input("Is a new service ticket required? Yes/No ").lower()

    if ticket_creation == 'yes':
        customer_name = input('Name: ')
        issue = input('Brief description of the issue: ')
        status_open = 'open'
    
        new_ticket ={
            'customer': customer_name,
            'issue': issue,
            'status': status_open
        }
     
        ticket_id = None
        for key, value in Main.service_tickets.items():
            if not value: 
                ticket_id = key
                break
        else:
            ticket_id = f'ticket{len(Main.service_tickets)+1}'
        Main.service_tickets[ticket_id] = new_ticket
        
        print(f'Your Serivce ticket has been created & submitted.')
        

        