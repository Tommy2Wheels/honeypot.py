
Objective: Honeypot Implementation: Set up a basic honeypot using Python to attract potential attackers and log their activities for analysis.
--------------------------------------------------------------------------------------------------------------------
Create the File Manually via SSH

SSH into your VPS:

Start your Terminal or Command Prompt

  SSH root@your_VPS_IP

Once logged in, use a text editor (like nano or vim) to create and paste your code:
  nano honeypot2.py
    Paste the contents of thehoneypot2.py file.
    Save and exit (Ctrl+O, Enter, then Ctrl+X for nano).

Run the honeypot:
  python3 honeypot2.py

To see the log run:
  tail -f honeypot.log
  
---------------------------------------------------------------------------------------------------------------------

Additional information necessary:

  You will have to edit the code to your specific host that you want to implement this honeypot on. For the project, I have left my VPS IP address so my professor can grade this project. Additonally you will have to change the port number as well or add a range of ports. 
