import sys
import logging

def error_message_detail(error,error_detail:sys):#Ye ek function hai jo error ke baare mein extra info nikalta hai
    _,_,exc_tb=error_detail.exc_info()#kaunsi line me error ayyi h 
    file_name=exc_tb.tb_frame.f_code.co_filename#kis python file me error ayyi h 
    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
        #ek formatted string banegi jisme: File k naam,Line Number,Error message  sab ek line me a jata h 
        file_name,exc_tb.tb_lineno,str(error)
    )
    return error_message
    

class CustomException(Exception):#ye ek custom class h jo python ki exception class ko extend krti h 
    def __init__(self,error_message,error_detail:sys):
        #Yahaan constructor ke andar pehle base class ka constructor call kiya gaya
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
        #Is line mein upar likha function call karke proper error message assign kiya jata hai.
    def __str__(self):
        return self.error_message
    

# if __name__=="__main__":
#     try:
#         a=1/0
#     except Exception as e:
#         logging.info("Divide by Zero")
#         raise CustomException(e,sys)