#Logger ka use hota hai code execution ke during important events ko record karne ke liye — jaise ki errors,
#  warnings, info messages, etc. Ye information file ya console mein store ki ja sakti hai.
#Ye logging files aapko later help karengi bugs trace karne mein, model training steps dekhne mein,
#  ya production errors track karne mein.


import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"#🕓 Current date-time ke base par ek unique file name ban raha hai
logs_path=os.path.join(os.getcwd(),"logs")#📁 Ye path set karta hai:
#Current working directory → logs folder → uske andar new log file
os.makedirs(logs_path,exist_ok=True)
#📂 Agar logs/ folder pehli baar ban raha ho toh create kar do.
#exist_ok=True ensures ke agar folder already ho toh error na aaye.

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)# Ye batata hai:filename: kaha log save honge format: har log message ka format kya hoga (Time, line no, module name, level, message) level: kya type ke logs capture karne hain (INFO or above)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
#Ye batata hai:filename: kaha log save honge format: har log message ka format kya hoga (Time, line no, module name, level, message) level: kya type ke logs capture karne hain (INFO or above)


if __name__=="__main__":
    logging.info("Logging has started")