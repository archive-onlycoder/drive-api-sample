# service account

# import the required libraries
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds",
         'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file",
         "https://www.googleapis.com/auth/drive"]



# Create a function getFileList with 
# parameter N which is the length of 
# the list of files.
def getFileList(N):
    creds=ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
  
    # Variable creds will store the user access token.
    # If no valid token found, we will create one.
    
    # Connect to the API service
    drive = build('drive', 'v3', credentials=creds)
  
    # request a list of first N files or 
    # folders with name and id from the API.
    files = drive.files()
    
    # data=files.get(fields='*').execute()
    result = files.list(pageSize=N, fields="files(id, name)").execute()
    # print(data)
    # return the result dictionary containing 
    # the information about the files

    f = open("data.json", "w")
    import json
    f.write(json.dumps(result))
    f.close()

    
  
  
    
# # Get list of first 5 files or 
# # folders from our Google Drive Storage
result_dict = getFileList(100)
  
  
  
# # Extract the list from the dictionary
# file_list = result_dict.get('files')
  
  
  
# # Print every file's name
# for file in file_list:
#     print(file['name'])