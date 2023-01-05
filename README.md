# HomeWorkBot
 A simple telegram bot that tells you the homework of a specified day.
 !WARNING! - The user interaction is in Romanian language.


 General work info:

 The homework is taken from a live-sheet in Google Docs and is imported via pandas package in a csv sheet.
 The main extracted dataframe is split in smaller dataframes for each day of the week.

 
 Main part of the telegram bot:

 Here in `dayIndex` is saved the index of the current day of the week.
 After that the bot is logged and initialized. It is assigned a token and a dispatcher.
 The buttons for the days of the week are created and assigned to the keyboard.
 
 The welcome text is handled with all the basic information and commands
 The message to display the keyboard with the choice of the day is handled
 The `next_day` command is handled
 Last part ment to display the homework of the specified day

 Execution of the bot

 similar Discord bot - (In development at the moment)
