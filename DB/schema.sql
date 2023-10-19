-- user: drew
CREATE USER 'drew'@'localhost' IDENTIFIED BY 'growtent';
GRANT ALL PRIVILEGES ON your_database_name.* TO 'drew'@'localhost';
FLUSH PRIVILEGES;

-- db table schema
CREATE DATABASE sensor_data;
USE sensor_data;
CREATE TABLE sensors (
  id INT NOT NULL AUTO_INCREMENT,
  sensor_id INT NOT NULL,
  temperature FLOAT NOT NULL,
  humidity FLOAT NOT NULL,
  time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
EXIT;
