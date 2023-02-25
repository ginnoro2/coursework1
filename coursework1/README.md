# Secure OTP login #
---------------------
A login system, that use 2 factor authentication, with multiple technologies integrated in one. 

To be installed prior to using the application.
1. Docker ( a mock server terminal )
```
sudo apt update
sudo apt install docker-engine
sudo docker pull Ubuntu:latest
sudo docker images
```
2. Webserver using Flask api-Run
```
127.0.0.1:5000
```
3. Sqlite3 ( Create Database ) 
```
python3 create_db.py
python3 insert_db.py
python3 open_db.py
```


# Difficulties #
----------------------

twilio OTP token ( by the time you use the application the OTP token might have changed, it expires in 7 days )
```
6791e11339cefe0ed229c00519ea9139
```


# Usage #
----------------------
install docker 
```
--https://docs.docker.com/desktop/install/mac-install/
```
pull docker image
```
--docker pull ubuntu:latest
```
download  from Github. 
```
git clone git@github.com:ginnoro2/coursework1.git
```
Then install requirements. 
```
pip3 install -r requirements.txt
```
Use python3 to run the program 
```
python3 frontend.py
```

