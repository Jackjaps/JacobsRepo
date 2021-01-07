#python3 
#pip install azureidentity
#pip install azure 

from azure.storage.blob import BlobServiceClient
from azure.storage.blob import ContainerClient
from azure.storage.blob import BlobClient
connection_string = "DefaultEndpointsProtocol=https;AccountName=pent001;AccountKey=TKjgBOqvXI79F3lCbD8C0w7DKkHYEtIKSBnqkAr4PGgqEclRwP+w8yBpBWDMCiOXOCtNdp7Pv7fdsKBQv+balQ==;EndpointSuffix=core.windows.net"

def listBlobs (connection,containerName):
    service = BlobServiceClient.from_connection_string(conn_str=connection)
    container = ContainerClient.from_connection_string(conn_str=connection, container_name=containerName)
    blob_list = container.list_blobs()
    for blob in blob_list:
        print(blob.name + '\n')

def uploadBlob(filenamepath,fileName,connection,containerName):
    blob = BlobClient.from_connection_string(conn_str=connection, container_name=containerName, blob_name=fileName)
    with open(filenamepath+fileName, "rb") as data:
        blob.upload_blob(data)
    print("File loaded")

#Storage Account: pent001
#Container: prueba
#Keyaccess: TKjgBOqvXI79F3lCbD8C0w7DKkHYEtIKSBnqkAr4PGgqEclRwP+w8yBpBWDMCiOXOCtNdp7Pv7fdsKBQv+balQ==

def main():
    print("List of blobs on the azure account")
    listBlobs(connection_string,"prueba")
    #uploadBlob("./","exampleFile.txt",connection_string,"prueba")

if __name__ == "__main__":
    main()
