# Angular

Mor more information on build :- https://angular.io/guide/build

For deployment : https://angular.io/guide/deployment


#Note :: Need python, Lib(mysql,Flask,flask_cors,waitress )

 $ sudo apt-get update
 
 $ sudo apt-get install mysql-server
 
 $ sudo mysql_secure_installation utility
 
 $ sudo ufw allow mysql
 
 $ sudo systemctl start mysql
 
 $ sudo systemctl enable mysql
 
 $ vi /etc/mysql/mysql.conf.d/mysqld.cnf:
 	bind-address		= 0.0.0.0 ( All ip addresses. )
	
 $ sudo systemctl restart mysql
 
 $ sudo /usr/bin/mysql -u root -p
      
	mysql> CREATE USER 'demo'@'localhost' IDENTIFIED BY 'Password@1';
	
	mysql> GRANT ALL PRIVILEGES ON *.* TO 'demo'@'localhost' WITH GRANT OPTION;
	
	mysql> CREATE USER 'demo'@'IP' IDENTIFIED BY 'Password@1';
	
	mysql> GRANT ALL PRIVILEGES ON *.* TO 'demo'@'IP'  WITH GRANT OPTION;
	
	 
	 FLUSH PRIVILEGES;
	 
	 CREATE DATABASE db_name;
	 
	 create table demousers(
	 id INT NOT NULL AUTO_INCREMENT,
	 name VARCHAR(50) NOT NULL,
	 mobile VARCHAR(20) NOT NULL,
	 password VARCHAR(30) NOT NULL,
	 introduction VARCHAR(100) NOT NULL,
	 email VARCHAR(40) NOT NULL,
	 PRIMARY KEY ( id )
	 );
	 

 $ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
 
 $ sudo apt-get install nodejs
 
 $ sudo npm install --global http-server
 
 $ mkdir App
 
 $ cd App
 
 $ sudo git clone https://github.com/biswajit1987/Angular_With_Flux.git
 
 $ cd ~/App/Angular
 
 Note** Edit  main.js file 
 

       ("http://18.191.201.177:3000/users", user); # Change This IP to your server ip


 
 $ http-server
 
 Available on:
  http://127.0.0.1:8080
  http://172.31.25.851:8080

 ---------------------------
 Open new Terminal
 ---------------------------
 
 $ cd App
 
 $ mkdir server
 
 $  ls App
 
      Angular  server
	  
 $ cd server/
 
 $ mv ~/Angular/Test.py to server/
 
 ##Note** Edit UsersAPI.py file
 	HOST = '172.31.25.85' #give DB ip
	
	host="172.31.25.85" #give server ip

 
 $ python UsersAPI.py

 $ sudo chmod -R 777 App #Give full permission to App Folder
 
 #Note** :- Restart the server
 
