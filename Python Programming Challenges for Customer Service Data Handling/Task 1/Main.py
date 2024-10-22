service_tickets = {
    'ticket1': {'customer': 'Jordan', 'issue': 'Can\'t log in. Incorrect username.', 'status': 'open'}, 
    'ticket2': {'customer': 'Wylie', 'issue': 'The system won\'t load', 'status': 'open'}
    }
import newService
import ticketDisplay
import ticketStatuschange
import exitStrategy

def service_ticket_submission():
    print('Welcome to the Service Ticket Submission and Tracking system\n')

    while True:    
        try:
            print('Main Menu:\n 1. Submit a Ticket\n 2. Display Current tickets\n 3. Change Ticket\'s Status\n 4. Exit')
            menu_selection = input('\nPlease select a menu item to proceed: ')

        except ValueError:
            print('Input just the number for the menu action you would like to select.\n For example: To start a ticket input "1"')

        else:
            if menu_selection == '1':
                
                newService.new_service(service_tickets)
            elif menu_selection == '2':
                
                ticketDisplay.ticket_display(service_tickets)
            elif menu_selection == '3':
                
                ticketStatuschange.ticket_status_change(service_tickets)
            elif menu_selection == '4':
                
                exitStrategy.exit_strategy(service_tickets)
                break
            else:
                print('Select from the menu options provided.')
      
    
service_ticket_submission()