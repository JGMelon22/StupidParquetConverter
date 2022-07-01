import PySimpleGUI as sg
import os
from pathlib import Path
import pandas as pd

# Window content
layout = [[sg.Text("Hit OK to generate a CSV of the parquet files")],
          [sg.Text(size=(40, 1), key='-OUTPUT-')],
          [sg.Button('Ok'), sg.Button('Sair')]]

# Generate the window (form)
window = sg.Window('Tela Principal', layout)

# Display and interact with the window using an event loop

while True:
    event, values = window.read()

    # Dynamic directory
    current_directory = os.getcwd()

    data_dir = Path(current_directory + '/data/')
    full_df = pd.concat(
        pd.read_parquet(parquet_file)
        for parquet_file in data_dir.glob('*.parquet')
    )
    full_df.to_csv('Converted.csv')

    # Generate a .csv file with the .parquet files merged
    # Success message when generating the .csv
    window['-OUTPUT-'].update("CSV generated successfully!")

    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break

# Close window
window.close()
