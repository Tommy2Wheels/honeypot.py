Option 1: Create the File Manually via SSH

SSH into your VPS:
  SSH root@your_VPS_IP

Once logged in, use a text editor (like nano or vim) to create and paste your code:
  nano honeypot2.py
    Paste the contents of your honeypot2.py file.
    Save and exit (Ctrl+O, Enter, then Ctrl+X for nano).

Run the honeypot:
  python3 honeypot2.py

To see the log run:
  tail -f honeypot.log
  
