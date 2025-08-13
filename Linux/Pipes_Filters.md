# Pipelines and Filters

Pipelines allow us to string the simple commands together to make more complex commands.

Commands pass their **standard output (stdout)** to the next commands **standard input (stdin)**.  The final command will then print to the screen unless the output is redirected.

The Linux philosophy for commands is;

> Commands do one thing and do it well

## Filter commands

Filter commands are those which accept input from **stdin**.  These can be identified by typing in the command without any arguments, and they will generally wait for you to type something in from the keyboard.

