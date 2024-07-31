# Usecase Architecture
![image](https://github.com/user-attachments/assets/984a6339-15aa-414e-9ee4-19fa2ffe525d)

# Part 1: Environment Setup
## Login to Azure Account using [protal.azure.com](https://portal.azure.com/)

## Create Required Resources in Azure Infrastructure

1. Create a Resource Group for the Services
![image](https://github.com/user-attachments/assets/d22f1989-1a10-42ae-8f88-a0a4c15bd377)
2. Create Azure DataLake Gen2 Account (ADLGen2)
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
- Select Premium Pricing Tier for this project
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

3. Open Key Vault and Create secrets for username and password created for SQL Server in previous step 
3.1 First of all Add the Role Based Access Control (RBAC) to the key vault
![image](https://github.com/user-attachments/assets/02071387-7487-4686-846e-6f9e7bcec2cd)
![image](https://github.com/user-attachments/assets/a7162116-25fd-4834-905b-8221ac8cc2a6)
![image](https://github.com/user-attachments/assets/daf0893a-0451-427c-8e82-76a6e52fb0df)
3.2 Then Review and Assign the role
![image](https://github.com/user-attachments/assets/5b5f6bd4-784f-49bc-9431-f4f7a65acaf5)
3.3 Add the username and password as seperate secrets
![image](https://github.com/user-attachments/assets/50f6d76e-96c0-495c-ae9d-f5205909cbc2)
3.4 Using these secrets all the services can access the On-Premise SQL server Database

# Part 2: **Data Ingestion using Azure Data Factory (ADF)**
1. Launch the Azure Data Factory Portal from Azure Data Factory Resource 
2. Configure Git Version Control System for project integration 
![image](https://github.com/user-attachments/assets/d21a3782-2a41-4b58-a81b-24b4131d337d)

3. Establish Relation between Data Factory and SQL Server using Self Host Intergration Runtime. 
3.1 Integration Runtime is the compute infrastructure in Azure Data Factory helps to perform integrationn oprations using ETL pipelines. 
![image](https://github.com/user-attachments/assets/ec9d2fbd-9554-4791-9b81-137425ae30af)

![image](https://github.com/user-attachments/assets/3e2389be-3fe7-4211-8f7a-9e29f78fd7d7)

![image](https://github.com/user-attachments/assets/69a17431-2fff-4bc5-ade9-f157f52bc3de)

![image](https://github.com/user-attachments/assets/2996f967-aaf1-4b64-8c5d-6a7db5332332)

3.2 Choose Option 1: Express setup
![image](https://github.com/user-attachments/assets/8ccc78f4-9355-40b8-9b0a-3dd21dea0384)

3.3 It will download a .exe file to set-up self hosted integration runtime.  Run the file
3.4 It will take 3-5 mins to download and setup the integration runtime on the system and will be available in Azure Data Factory
![image](https://github.com/user-attachments/assets/11c66538-6664-495d-86f2-8b3e0968dd30)
3.5 Search for Microsoft integration runtime on the system and run the application
![image](https://github.com/user-attachments/assets/6d04ca9c-4fbe-4e58-ac48-208cace49444)

4. Create ETL Pipeline 
4.1 We are going to load Address table from 'AdvantureWorksDB2020L' database
4.2 Create the Pipeline and add the Copy Data Activity 
![image](https://github.com/user-attachments/assets/e0e76f47-50a9-432f-be0e-49f5f0a8b047)
4.3 Add the SQL server as Source Dataset
![image](https://github.com/user-attachments/assets/8b5d73ed-7c11-4fb6-b005-b5120a5aca59)
4.4 Set the Property and now we need to add the Linked Service to connect to the databse
![image](https://github.com/user-attachments/assets/7f5e52b2-bf9d-4361-bcf3-dbd5690a1208)
![image](https://github.com/user-attachments/assets/ec129970-e230-46ad-9428-9d4cb871e9cc)
![image](https://github.com/user-attachments/assets/1b696385-3234-4efa-b9d7-4a8d78c9ddfe)
4.5 Now hwre we get the error because the data factory has no rights to access the keyvault secrets.
Hence, we need to create an access policy for the Azure Data Factory instance(principle)
![image](https://github.com/user-attachments/assets/76594c08-7ad9-480f-b341-9476ae48ca8d)
4.6 Adding Access Policy to the Key vault secrets 
![image](https://github.com/user-attachments/assets/849bb2fc-fb5f-48cc-bfc2-2b471bf97a97)

![image](https://github.com/user-attachments/assets/6060b38d-7888-4dcb-a1ae-bf181057d0df)
4.6.1 now the Azure Data Factory has the secret data permission
![image](https://github.com/user-attachments/assets/fd2a7ba9-0b38-4afe-bbdc-3a441fe040e8)
4.6.2 Now we get the secret name after adding access policy
![image](https://github.com/user-attachments/assets/5f94efca-4b79-445d-81a9-adc7cb7a553e)

4.7 The connection with the On-Premise Database through Self-Hosted Integration Runtime is successful! 
![image](https://github.com/user-attachments/assets/4709cb37-1448-4d55-bc05-9ac457d5e952)

4.8 Now we get all the tables from 'AdvantureWorksDB2020L' Database

![image](https://github.com/user-attachments/assets/ee55d97b-02e9-47ab-bdcb-38855e96b612)
4.9 We can preview data from the source through linked service
![image](https://github.com/user-attachments/assets/04fca38a-fd37-4927-a97e-2bc9c1b6ce38)

4.10 Now we need to establish a linked service with the Sink dataset that is Datalake Gen2 Storage account in this project

![image](https://github.com/user-attachments/assets/d007b533-c1c4-438e-b752-ebee018899fa)

4.11 Create Parquet format dataset which is a Semi-structured data storage format. It stores the data in columner format giving the fast data retrival as compared to Structured formats
(CSV, Excel, relational database tables) 

![image](https://github.com/user-attachments/assets/93cbbcc0-998b-43f2-9854-f01b50338379)

4.12 Setup the linked service this time connection via 'AutoResolvedIntegrationRuntime' reason being, we need Self-Hosted integration runtime only for the On-Premise Data Sources(SQL Server, MySQL, PostgreSQL, etc)
and for cloud-based Azure services we can use its own 'AutoResolvedIntegrationRuntime'.
![image](https://github.com/user-attachments/assets/4e844975-4612-4cb2-bc4a-f623c1bbd54f)

4.13 Create a Bronze container for dataset in ADLGen2
![image](https://github.com/user-attachments/assets/132ad703-3155-4227-b912-6dc64e254e10)

![image](https://github.com/user-attachments/assets/1fc30980-6986-402c-8735-19b71e155bbc)

Important: 
The bronze, silver, and gold container approach in data lakes is a way to organize data in layers based on their level of processing:
Bronze
Contains raw, unprocessed data that can be a combination of streaming and batch transactions. This data is stored after data extraction.
Silver
Contains validated, enriched data that has been cleaned and conformed. This data is stored after data transformation and cleaning.
Gold
Contains highly refined and aggregated data that is ready to use for analytics, machine learning, and production applications. This data is stored after data science and analysis.

4.14 We can map the Source Columns with the Destination desired columns or create our own mapping
![image](https://github.com/user-attachments/assets/282645fa-18e7-47da-b616-83a0fb50a08f)

4.15 Save the Pipeline, Validate,Publish, and Trigger to execute the ETL Pipeline
![image](https://github.com/user-attachments/assets/db90d248-cda7-4f53-940d-b47e38ce2273)

![image](https://github.com/user-attachments/assets/c507bea6-74a0-4168-b0ec-8c885a1c0291)

![image](https://github.com/user-attachments/assets/8ef7d6c8-f92b-496f-a447-85965951c93e)

- Note: Due to the Self-Hosted Integration Runtime, it is possible to hit with error while debugging stating,'JRE not found', in this case please install JRE from
https://www.java.com/en/download/manual.jsp this link and set destination folder as 'C:\Program Files\Java'. After installation set up the System Environment Variable Path for Java
'JAVA_HOME' with the 'C:\Program Files\Java\jre1.8.0_421\bin' and rerun the pipline, it will succeed. More information can be found here https://learn.microsoft.com/en-gb/azure/data-factory/connector-troubleshoot-guide#error-code-jrenotfound

4.16 The Data Ingestion is successful in ADLGen2 Bronze Container
![image](https://github.com/user-attachments/assets/e877727a-8c3f-4c4d-ba57-bb1a3f056d41)

4.17 Ingest all the tables from On-Premise database to ADLgen2 using ADF Pipeline
![image](https://github.com/user-attachments/assets/43b6013e-01ee-4c7a-966b-72e5678151cd)
4.17.1 Create new pipeline and add the linked service to On-Premise DB
![image](https://github.com/user-attachments/assets/1fa64d05-5e60-487d-a3aa-e22b3f3c1fa8)

![image](https://github.com/user-attachments/assets/cc127f3d-6466-4316-b687-ef957fb06a09)

![image](https://github.com/user-attachments/assets/5c6a4d67-0d4b-440a-96de-ed2d43c12b78)

4.17.2 Do not select any table and click OK
![image](https://github.com/user-attachments/assets/15c34c77-401b-4843-9bdc-5c83f7cc3f8f)

4.17.3 Select the Query Option, Deselect First Row Only and preview the data. All the tables from DB are visible
![image](https://github.com/user-attachments/assets/8e572f30-749a-4795-bdd8-958b88e069f7)
4.17.4 Upon Debugging the Pipeline we will be able to see the all the Tables in JSON format 
![image](https://github.com/user-attachments/assets/e87c1bc5-d604-4006-a462-2a72d6e5d87e)
4.17.5 Using forEach Activity we will be reading the all the table data from JSON file
![image](https://github.com/user-attachments/assets/5a80f5a3-00e7-43b3-9720-cb0ccec09b4e)

4.17.6 Create a Copy Data Activity inside ForEach

![image](https://github.com/user-attachments/assets/fc7e132c-e143-454e-b42f-8fd8e4ce8fa1)
4.17.7 Create a new Source Dataset and use the same Linked Servive created in earlier steps
![image](https://github.com/user-attachments/assets/a83d94a6-eeda-4a7d-a21b-a0bcc223ffb0)
4.17.8 Create a new Sink Dataset for Bronze Container of ADLGen2 
![image](https://github.com/user-attachments/assets/050a169a-883f-4509-8d91-3865d26b2916)
4.17.9 Extract the schema name and table name from outer lookup activity output JSON object list
![image](https://github.com/user-attachments/assets/1b63c3fa-eb04-4a47-821e-c1fe74354a75)

4.17.10 Create a parameter to dynamically update the FolderName to have a directory as follows:
'SalesLT/Customer/Customer.parquet'

![image](https://github.com/user-attachments/assets/6cef1e49-17f2-4ebb-9b33-909b92c77743)

![image](https://github.com/user-attachments/assets/c4441b60-b7ed-4553-a766-d6ecd76ed36f)

![image](https://github.com/user-attachments/assets/240ec284-e938-4b3c-9ace-cdb9eb7c13ae)

![image](https://github.com/user-attachments/assets/4c5b4e57-b514-46be-bc53-8efb6c920709)

![image](https://github.com/user-attachments/assets/3bba5c32-bdb4-404b-a456-f412c749875d)

4.17.11 Click on publish. After Publish, Add Trigger to execute the pipeline

![image](https://github.com/user-attachments/assets/cb032b32-ebd9-4f72-af3b-f4f4f9b36d04)

4.17.12 After Successful Execution, we can check the Bronze Container of ADLGen2 

![image](https://github.com/user-attachments/assets/d019a48d-daf7-49ea-9a1f-65c57da83075)

![image](https://github.com/user-attachments/assets/bbedeb15-7eb4-463f-a34f-c6fa7973f38c)


![image](https://github.com/user-attachments/assets/e84c931a-0796-4606-9763-aa12a27f67fc)


![image](https://github.com/user-attachments/assets/aa4fdb96-bea5-4f4c-bd11-3fb9a9743407)

# Part 3: Data Transformation using Azure Databricks

## Launch the Databricks Workspace from Azure Databricks Resource we have created earlier

1. Add the Databricks to the Github repository for the project integration
![image](https://github.com/user-attachments/assets/56c63abf-082d-4ec1-8ac1-5a0c526e613b)

2. Create a Databricks Cluster (also knonw as Spark Cluster)
![image](https://github.com/user-attachments/assets/6fee526f-7036-427a-8305-2872d2266591)

![image](https://github.com/user-attachments/assets/1ff36c0e-8707-4b5c-b7f4-3e5b4f87b612)

Note: For Azure Data Lake Storage credential passthrough, we need Premium account of DataBricks to be created through Azure 

3. Mounting the ADLGen2 storage account to Databricks file system(DBFS) so that we can access the files inside Datalake as the local files of Databricks for data transformation.
3.1 Create a notebook inside the Databricks git workspace and execute as below
![image](https://github.com/user-attachments/assets/3ef837b8-6809-46df-b606-5f3633a2b473)
3.2 We can see all the folders inside SalesLT 
![image](https://github.com/user-attachments/assets/8ffa8a56-708d-4a7d-9404-b2eb1bfc759a)
3.3 Similary create silver and gold containers in ADLGen2 and mount it to DBFS
![image](https://github.com/user-attachments/assets/08a951ed-edd2-4816-b471-38f2508f7946)
Important: Once we mount the containers, we do not require to mount it again to DBFS, we can directly use the source link of container to access.

More information can be found here: https://learn.microsoft.com/en-us/azure/databricks/archive/credential-passthrough/adls-passthrough#--access-azure-data-lake-storage-directly-using-credential-passthrough


### Level 1 Transformation: bronze to silver

#### Converting Date Columns from DateTime to Date Format

4. Now we will use the `/mnt/bronze/` mount point to access all the parquet files storing database table records and load them to the `/mnt/silver/` mount point for data transformation.

4.1. After transformation, we store the data in 'delta' format in the silver container. The delta format is native to Databricks and is hosted by the 'Delta Lakehouse Architecture,' which combines the advantages of data lakes and data warehouses. Some key benefits include versioning of tables and handling schema changes. Delta format is recommended by Databricks. More info can be found [here](https://learn.microsoft.com/en-us/azure/databricks/delta/).

- The PySpark code in Databricks for data transformation is available [here on GitHub](https://github.com/RhugvedSatardekar/Azure-Data-Engineering-Project/tree/main/Databricks%20-%20Data%20Transformation).

- After executing the code files, the datetime columns from all the tables has been transformed to date
![image](https://github.com/user-attachments/assets/a3fe588f-1aa2-44d4-b844-cef9487d4613)

- We can source control our code files for collaboration to github
![image](https://github.com/user-attachments/assets/77478932-c1e4-4410-85b0-0538367ddc2c)

- The directory structure for all the delta files is shown below:

![Directory Structure](https://github.com/user-attachments/assets/5c09390a-201f-4d1a-a6b4-f8a43539a0e1)

![image](https://github.com/user-attachments/assets/7be1725e-65cf-452d-bd03-57fa0b3be366)

![image](https://github.com/user-attachments/assets/981342e8-234e-44d3-ae8f-d45f13008eff)

![image](https://github.com/user-attachments/assets/034bcaf3-22ed-4263-86d7-1f8a888915b8)


4.2 Instructions for Transformation

1. **Access Parquet Files**: Use the `/mnt/bronze/` mount point to access the parquet files.
2. **Transformation Logic**: Apply the transformation logic to convert all DateTime columns to Date format using PySpark in Databricks.
3. **Store Transformed Data**: Save the transformed data in 'delta' format in the silver container using the `/mnt/silver/` mount point.
4. **Delta Lakehouse Architecture**: Leverage the Delta Lakehouse Architecture for its benefits, including version control and schema handling.

### Additional Resources

For more detailed information on Delta Lakehouse Architecture and its benefits, refer to the [Microsoft Documentation](https://learn.microsoft.com/en-us/azure/databricks/delta/).

### Level 2 Transformation: silver to gold 

5. In gold layer/container lies our data warehouse where the data is stored in the form of Fact-Dimention table modeling

5.1 Changed the Column names from format 'FirstName' to 'First_Name' using pyspark and loading it to the gold contaier to store in the form of Fact-Dimention schema
![image](https://github.com/user-attachments/assets/e9f4454d-e3c2-4412-bedf-5fa36838bc55)

![image](https://github.com/user-attachments/assets/e66d6452-373e-4f21-9846-00ded6d363bc)

![image](https://github.com/user-attachments/assets/2da4287a-f8dd-48b0-867f-91a5662b4d24)

5.2 Lets push the files to the main branch of github repo for source control.

![image](https://github.com/user-attachments/assets/3d28aea0-c70d-4285-83ad-e6b5d9e94211)

5.3 The python code files are available [here on github](https://github.com/RhugvedSatardekar/Azure-Data-Engineering-Project/tree/main/Databricks%20-%20Data%20Transformation)



