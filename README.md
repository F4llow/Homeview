# Homeview
Homeview VTHacks Project

to run:
fill in the api key and url in propelauth.py and proxy/proxy.mjs

have 2 terminals open. 
```tmux ls``` 
```tmux attach -t [session_number]```
start the proxy by navigating to proxy/
then ```npm install```
then node ```proxy.mjs```
this starts the authentication proxy on port 8000 and you can only access the complete app after authenticating here

in the second terminal, ```run streamlit run app.py```
this then starts the application on port 8501.
this page can only be accessed after authenticating on port 8000


Devpost: ```https://devpost.com/software/homeview```
