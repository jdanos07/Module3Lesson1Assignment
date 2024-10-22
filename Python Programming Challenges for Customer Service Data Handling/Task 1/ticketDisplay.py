def ticket_display(service_tickets):
    for key, ticket in service_tickets.items():
        if ticket:   
            print(f'{key}: {ticket}')
