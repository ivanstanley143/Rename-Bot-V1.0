import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "16795822")

API_HASH = os.environ.get("API_HASH", "791cc620cf2344a0fbf20b258fa679d2")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "5204820983:AAH9uNHFa8jbRYgLsDqjhstgIXNAl_9odnI") 

FORCE_SUB = os.environ.get("FORCE_SUB", "ZKP_AVENUES") 

DB_NAME = os.environ.get("DB_NAME","Cluster0")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://jamiedornankoyyodan:jamiedornankoyyodan@cluster0.ioz6q.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://graph.org/Rename-Bot-01-15")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '561339410').split()]

PORT = os.environ.get("PORT", "8080")
