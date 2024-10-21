import Main

def ticket_status_change():
    # changes status from open to close
    completion_input = input('Select the ticket to mark the service ticket as complete:\nInput complete ticket, for example "ticket1" ')
    if completion_input in Main.service_tickets:
        try:
            print(f'{completion_input} has been marked "complete". Returning to main menu.\n')    
            Main.service_tickets[completion_input]['status'] = 'complete'
                 
        except TypeError:
            print('No open ticket to close.')

    else:
        print('Invalid selection. Returning to Main Menu')