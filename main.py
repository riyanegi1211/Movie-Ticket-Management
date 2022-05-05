import PySimpleGUI as sg
import pandas as pd
import sys
from datetime import datetime

df_row_num = 0
column_names = ['Movie Name', 'Show Time', 'Rate of Tickets', 'Customer Name', 'Number of Tickets', 'Amount',
                'Donation']
df = pd.DataFrame(columns=column_names)

# Global Variable
Movie_name = "No Info"
Show_time = "No Info"
Rate_ticket = "No Info"
Av_tickets = 0


def message(mes):  # Showing Message
    sg.theme('DarkAmber')
    # Add a touch of color
    # All the stuff inside your window.
    layout = [[sg.Text(mes, key="Message")],
              [sg.Button('OK')]]
    # Create the Window
    window = sg.Window('Message', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'OK':
            window.close()
            return


def Balance(bal):  # Returning Balance Amount
    global df_row_num, df
    sg.theme('DarkAmber')
    # Add a touch of color
    # All the stuff inside your window.
    layout = [[sg.Text(f'Balance Amount : {bal}')],
              [sg.Button('Return Change'), sg.Button('Donate')]]

    # Create the Window
    window = sg.Window('Get Change', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:  # if user closes window
            window.close()
            menu()
        if event == 'Return Change':
            window.close()
            message("Change Returned \nTHANK YOU")
            df.loc[df_row_num, 'Donation'] = 0
            df_row_num = df_row_num + 1
            menu()
        if event == 'Donate':
            window.close()
            message("Change Donated \nTHANK YOU")
            df.loc[df_row_num, 'Donation'] = bal
            df_row_num = df_row_num + 1
            menu()


def Money(ticket):  # Calculating Total Amount
    global Av_tickets, df_row_num, df
    sg.theme('DarkAmber')
    # Add a touch of color
    Av_tickets = Av_tickets - ticket
    Amount = ticket * Rate_ticket
    # All the stuff inside your window
    layout = [[sg.Text(f'Total Amount : {Amount}')],
              [sg.Text('Enter Money : '), sg.InputText()],
              [sg.Text(size=(23, 1), key='wrong')],
              [sg.Button('Continue'), sg.Button('Cancel')]]

    # Create the Window
    window = sg.Window('Payment', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        df.loc[df_row_num, 'Amount'] = Amount
        val = int(values[0])
        if (val >= Amount):
            if event == 'Cancel' or event == sg.WIN_CLOSED:  # if user closes window or clicks cancel
                window.close()
                menu()
            if event == 'Continue':
                window.close()
                Balance(val - Amount)
        else:
            if event == 'Cancel' or event == sg.WIN_CLOSED:  # if user closes window or clicks cancel
                window.close()
                menu()
            window['wrong'].update("Please Enter more money")


def new():  # Manager's Entry portal
    global Movie_name, Rate_ticket, Show_time, df, Av_tickets
    sg.theme('DarkAmber')
    # Add a touch of color
    # All the stuff inside your window.
    layout = [[sg.Text('Movie Name : '), sg.InputText()],
              [sg.Text('Show Time : '), sg.InputText()],
              [sg.Text('Rate of Ticket : '), sg.InputText()],
              [sg.Text('Total number of tickets : '), sg.InputText()],
              [sg.Button('Save'), sg.Button('Cancel'), sg.Button('Shut Down')]]

    # Create the Window
    window = sg.Window('Manager', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == 'Cancel' or event == sg.WIN_CLOSED:  # if user closes window or clicks cancel
            window.close()
            menu()
        if event == 'Shut Down':
            folder_time = datetime.now().strftime("%Y-%m-%d_%I-%M-%S_%p")
            df.to_excel("Movie_Data" + folder_time + ".xlsx")
            window.close()
            message("Shutting Down")
            sys.exit()
        if event == 'Save':
            window.close()
            Movie_name = values[0]
            Show_time = values[1]
            Rate_ticket = int(values[2])
            Av_tickets = int(values[3])
            menu()


def pay(movie, show, rate):  # Customer's Payment Portal
    global Av_tickets, Movie_name, Rate_ticket, Show_time
    global df, df_row_num
    sg.theme('DarkAmber')
    # Add a touch of color
    # All the stuff inside your window.
    layout = [[sg.Text(f'Movie name : {Movie_name}')],
              [sg.Text(f'Show time : {Show_time}')],
              [sg.Text(f'Rate of ticket : Rs. {Rate_ticket}')],
              [sg.Text('Name : '), sg.InputText()],
              [sg.Text('Number of Tickets : '), sg.InputText()],
              [sg.Text(f'Seat\'s Available : {Av_tickets}')],
              [sg.Text(size=(28, 1), key='wrong')],
              [sg.Button('Buy'), sg.Button('Cancel')]]

    # Create the Window
    window = sg.Window('Customer', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        tik = int(values[1])
        if Av_tickets == 0:
            if event == 'Cancel' or event == sg.WIN_CLOSED:  # if user closes window or clicks cancel
                window.close()
                menu()
            window.close()
            folder_time = datetime.now().strftime("%Y-%m-%d_%I-%M-%S_%p")
            df.to_excel("Movie_Data" + folder_time + ".xlsx")
            message("Sold Out \nShutting Down")
            sys.exit()
        df = df.append({'Movie Name': Movie_name, 'Show Time': Show_time, 'Rate of Tickets': Rate_ticket,
                        'Customer Name': values[0], 'Number of Tickets': tik}, ignore_index=True)
        if tik <= Av_tickets and Av_tickets != 0:
            print(movie)
            if event == 'Cancel' or event == sg.WIN_CLOSED:  # if user closes window or clicks cancel
                window.close()
                menu()
            if event == 'Buy':
                window.close()
                Money(tik)
        else:
            if event == 'Cancel' or event == sg.WIN_CLOSED:  # if user closes window or clicks cancel
                window.close()
                menu()
            window['wrong'].update("Please request fewer tickets")


def login(passkey, username):  # Login as manager
    sg.theme('DarkAmber')
    # Add a touch of color
    # All the stuff inside your window.
    layout = [[sg.Text('Username : '), sg.InputText()],
              [sg.Text('Password : '), sg.InputText()],
              [sg.Text(size=(26, 1), key='wrong')],
              [sg.Button('Login'), sg.Button('Cancel')]]

    # Create the Window
    window = sg.Window('Login', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == 'Cancel' or event == sg.WIN_CLOSED:  # if user closes window or clicks cancel
            window.close()
            menu()
        if passkey == values[1] and username == values[0]:
            window.close()
            new()
        else:
            window['wrong'].update("Wrong Username or Password")


def menu():  # Main Menu
    global Movie_name, Rate_ticket, Show_time
    sg.theme('DarkAmber')
    # Add a touch of color
    # All the stuff inside your window.
    layout = [[sg.Button('Manager'), sg.Button('Customer')]]

    # Create the Window
    window = sg.Window('Choice', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == 'Manager':
            window.close()
            login('1207', 'Riya')
        if event == 'Customer':
            window.close()
            pay(Movie_name, Show_time, Rate_ticket)


if __name__ == "__main__":
    menu()