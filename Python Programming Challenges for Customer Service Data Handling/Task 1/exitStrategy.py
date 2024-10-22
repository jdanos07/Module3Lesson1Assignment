import Main

def exit_strategy(service_tickets):
    shutdown = input('Are you sure you want to quit? Yes/No? ').lower()
    if shutdown == 'yes':    
        print('\nThese are the current service tickets open or completed:\n')
        import ticketDisplay
        ticketDisplay.ticket_display(service_tickets)

    else:
        print('Returing to Main Menu')
        Main.service_ticket_submission()

