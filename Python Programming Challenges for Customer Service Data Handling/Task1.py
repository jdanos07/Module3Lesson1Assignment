# Task 1: Customer Service Ticket Tracker Demonstrate your ability to use 
# nested collections and loops by creating a system to track customer service tickets.

# Problem Statement: Develop a program that:

# Tracks customer service tickets, each with a unique ID, customer name, 
# issue description, and status (open/closed).
# Implement functions to:
# Open a new service ticket.
# Update the status of an existing ticket.
# Display all tickets or filter by status.
# Initialize with some sample tickets and include functionality for additional ticket entry.
# Example ticket structure:

# service_tickets = {
#     "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
#     "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
# }

service_tickets = {}


def service_ticket_submission():
        # a menu and guide for creating service tickets
    print('Welcome to the Service Ticket Submission and tracking system\n')
    print('Main Menu:\n 1. Submit a Ticket\n 2. Display Current tickets\n 3. Change Ticket\'s Status\n 4. Exit')
    
    while True:    
        try:
            menu_selection = input('Please select a menu item to proceed: ')

        except ValueError:
            print('Input just the number for the menu action you would like to select.\n For example: To start a ticket input "1"')

        else:
            if menu_selection == '1':
                new_service()
            elif menu_selection == '2':
                ticket_display()
            elif menu_selection == '3':
                ticket_status_change()
            elif menu_selection == '4':
                exit_strategy()
                break

def new_service():
    # information gathering and submission of new ticket
    if len(service_tickets) >= 5:
        print('Service ticket que is full. Max 5 active tickets.')
    ticket_creation = input("Is a service ticket required? Yes/No ").lower()
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
        for key, value in service_tickets.items():
            if not value: 
                ticket_id = key
                break
        else:
            ticket_id = f'ticket{len(service_tickets)+ 1}'
        service_tickets[ticket_id] = new_ticket

        print(f'Your Serivce ticket for: \n{new_ticket}\nhas been created & submitted.')
        print(service_tickets)
    
    else:
        print('\nReturning to Main Menu.\n')
   
        

def ticket_status_change():
    # changes status from open to close
    completion_input = input('Select the ticket to mark the service ticket as complete:\nInput complete ticket, for example "ticket1" ')
    if completion_input in service_tickets:
        try:    
            service_tickets[completion_input]['status'] = 'closed'
            
        except TypeError:
            print('No open ticket to close.')
        

def ticket_display():
    for key, ticket in service_tickets.items():
            if ticket != '':   
                print(f'{key}: {ticket}')


def exit_strategy():
    exit = input('Are you sure you want to quit? Yes/No? ').lower()
    if exit == 'yes':
        print('\nThese are the current service tickets open or completed:\n')
        for key, ticket in service_tickets.items():
            if ticket != '':   
                print(f'{key}: {ticket}')
    else:
        print('Return to main menu.') 

service_ticket_submission()