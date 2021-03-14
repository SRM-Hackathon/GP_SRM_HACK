import logging

logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S' , filename='app.log', filemode='a+')

logging.info("this is an error")
def return_log_config():    
    return logging

