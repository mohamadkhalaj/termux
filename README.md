## termux
With this app you can save all SMS, Call Logs, Contacts, and clipboard on your PC.
## How to use
1. Install termux latest & termux api v 0.31 on your andoid phone
2. Clone this repo on your phone, make virtualenv, install all requirements (or use venv dir in project), migrate and run it, then grant all permissions to termux api
3. Do all this on your PC but run with a web server like NGINX (use wsgi)
4. Open your Django running port on your router(forward to your PC), to receive data from your phone
5. On your phone goto localhost:8000/register and create a user(this user will be save to your PC app to)
6. After that, all SMS, Call Logs, Contacts, and clipboard will be saved in PC app database and you can see it in admin page.

## TODO
-auto update data
-date format fixing
