class logger:
    def log(self,message):
        pass

class Databaselogger(logger):
    def  log(self,message):
        print(f"Saving'{message}' to database")

class Filelogger(logger):
    def  log(self,message):
        print(f"Writing'{message}' to File") 

class Cloudlogger(logger):
    def log(self,message):
        print(f"uploading '{message}'to Cloud") 

def save_log(logger,message):
    logger.log(message)   

db=Databaselogger()
file=Filelogger()
cloud=Cloudlogger()

save_log(db,"Database connected")
save_log(file,"File opened")
save_log(cloud,"Server started")
