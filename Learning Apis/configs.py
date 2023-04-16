import configparser

config = configparser.ConfigParser()   #initialize the config parser

config.read('db_connection.config')    #reading configuration file
#print(config['servers']['CONNECT_DB_LOCAL'])  # reading configurations from the file




def db_connection(db_con):
    return str(config['servers'][db_con])