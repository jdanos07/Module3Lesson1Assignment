import Main


def ticket_display():
    for key, ticket in Main.service_tickets.items():
        if ticket:   
            print(f'{key}: {ticket}')
