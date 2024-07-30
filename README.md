# Azure-Data-Engineering-Project

### Use Case Architecture
![image](https://github.com/user-attachments/assets/984a6339-15aa-414e-9ee4-19fa2ffe525d)

### Login to Azure Account using protal.azure.com
### Create Required Resources in Azure Infrastructure
1. Create a Resource Group for the Services
![image](https://github.com/user-attachments/assets/d22f1989-1a10-42ae-8f88-a0a4c15bd377)
2. Create Azure DataLake Gen2 Account
![image](https://github.com/user-attachments/assets/92c523aa-636d-4f11-bd45-71cd86aaa7e4)

-select below option to create DataLake Gen2 account in storage account and create 

![image](https://github.com/user-attachments/assets/3e2dbb7c-24da-4204-9ca7-9ac9afc9a0c7)
![image](https://github.com/user-attachments/assets/e6438cd9-d759-48b5-897a-b47602cc9071)

4. Create Azure DataFactory Resource
![image](https://github.com/user-attachments/assets/44b90a6d-a0fa-4e22-959e-14ef3ea1fade)
![image](https://github.com/user-attachments/assets/e14f2dd3-e73b-46d0-bde9-9e45de338931)

5. Create Azure Synapse Analytics Resource
![image](https://github.com/user-attachments/assets/bc5438ca-f5ed-4ff6-9245-6d342037dc93)
![image](https://github.com/user-attachments/assets/54bc7a91-591a-4862-a57c-99b4d03c79c2)

-By default Serverless SQL pool will be assigned to synapse with SQL Server Admin
-It will take a while to deploy all the required resouces for the instance

![image](https://github.com/user-attachments/assets/f3e378b0-ad01-4b1d-a1e1-fdaff56bf43e)

7. Create Azure Databricks Resource for data transformation/pre-processing
- Select Standard Pricing Tier for this project
![image](https://github.com/user-attachments/assets/c03811c0-56e7-4272-af25-dabcad28f340)
![image](https://github.com/user-attachments/assets/99904dbd-e6ce-41ec-816b-2812dca56c4e)

7. Create Key Vault to implement secured shared secrets and principal
![image](https://github.com/user-attachments/assets/1eee97f8-2c02-4881-bdb3-0440aec686a2)
![image](https://github.com/user-attachments/assets/30c061be-9373-413a-ab32-623f17dc89f4)

#### Inside Resource group all the services are stored
![image](https://github.com/user-attachments/assets/22c3dbe8-eea6-4204-8c15-dd1b0fc8bf7d)

## Create the Data Source
### Download the Lightweight version of AdvantureWorks Operational Database using below link:
https://github.com/Microsoft/sql-server-samples/releases/download/adventureworks/AdventureWorksLT2022.bak

### Restore the .bak file to the SQL Server Database
1. Create Database into the server using 'create database AdvantureWorksDB2020L' this query
2. Save the file in backup folder of the SQL server for database restore. Sample path is 
- C:\Program Files\Microsoft SQL Server\MSSQL16.RHUGVEDSQLSERVER\MSSQL\Backup
![image](https://github.com/user-attachments/assets/0234a7a8-dbf9-4a44-b945-6cf7be6c11ab)

![image](https://github.com/user-attachments/assets/60b5b108-f7e9-45e4-860b-64c4b037cfda)

- Do not forget to choose the below options before restore
![image](https://github.com/user-attachments/assets/3eb841cd-e073-4f58-b23a-1b0eff523d65)

![image](https://github.com/user-attachments/assets/1b792d0b-219f-447f-b8b7-807f66e7ae47)



