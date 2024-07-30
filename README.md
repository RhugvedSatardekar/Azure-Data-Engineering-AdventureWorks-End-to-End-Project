## Usecase Architecture
![image](https://github.com/user-attachments/assets/984a6339-15aa-414e-9ee4-19fa2ffe525d)

## Login to Azure Account using [protal.azure.com](https://portal.azure.com/)

## Create Required Resources in Azure Infrastructure

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

6. Create Azure Databricks Resource for data transformation/pre-processing
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

## Establish the Connection between On-Premise SQL Server and Azure Cloud Infrastructure

1. Create a new user with password in 'SQL Server > Security > Logins' 
![image](https://github.com/user-attachments/assets/d7653b9b-88cb-4ada-94b1-779c7d2d8786)

2. Provide the Membership access to the user
![image](https://github.com/user-attachments/assets/82363961-23cd-46b5-b587-be05693b36d2)

3. Open Key Vault and Create secrets for username and password created for SQL Server in previous step <br/>
3.1 First of all Add the Role Based Access Control (RBAC) to the key vault
![image](https://github.com/user-attachments/assets/02071387-7487-4686-846e-6f9e7bcec2cd)
![image](https://github.com/user-attachments/assets/a7162116-25fd-4834-905b-8221ac8cc2a6)
![image](https://github.com/user-attachments/assets/daf0893a-0451-427c-8e82-76a6e52fb0df)
3.2 Then Review and Assign the role
![image](https://github.com/user-attachments/assets/5b5f6bd4-784f-49bc-9431-f4f7a65acaf5)
3.3 Add the username and password as seperate secrets
![image](https://github.com/user-attachments/assets/50f6d76e-96c0-495c-ae9d-f5205909cbc2)
3.4 Using these secrets all the services can access the On-Premise SQL server Database

## Data Ingestion
1. Launch the Azure Data Factory Portal from Azure Data Factory Resource <br/>
2. 
