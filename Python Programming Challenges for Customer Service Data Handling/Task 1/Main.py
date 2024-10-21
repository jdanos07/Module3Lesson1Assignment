service_tickets = {
    'ticket1': {'customer': 'Jordan', 'issue': 'Can\'t log in. Incorrect username.', 'status': 'open'}, 
    'ticket2': {'customer': 'Wylie', 'issue': 'The system won\'t load', 'status': 'open'}
    }



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
                import newService
                newService.new_service()
            elif menu_selection == '2':
                import ticketDisplay
                ticketDisplay.ticket_display()
            elif menu_selection == '3':
                import ticketStatuschange
                ticketStatuschange.ticket_status_change()
            elif menu_selection == '4':
                import exitStrategy
                exitStrategy.exit_strategy()
                break
            else:
                print('Select from the menu options provided.')
      
    
service_ticket_submission()