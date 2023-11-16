-- creates the user with all privileges
CREATE USER
IF NOT EXIXTS 'user_0d-1'@'localhost'
	IDENTIFIED BY 'user_0d_1_pwd';
	GRANT ALL PRIVILEGES
	ON *.*
	TO 'user_0d_1'@'localhoest';
