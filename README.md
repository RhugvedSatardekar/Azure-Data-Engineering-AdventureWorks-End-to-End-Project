# Azure AdventureWorks Data Lake and Analytics Pipeline

# Introduction
In this project, we will utilize the AdventureWorksDB2020L SQL Server database to demonstrate a comprehensive data processing and analytics pipeline using Azure services. The pipeline will encompass data ingestion, transformation, and analysis, leveraging tools such as Azure Data Factory, Azure Data Lake Gen2, Azure Databricks, Azure Synapse Analytics, and Power BI. The project aims to showcase the seamless integration of these services to handle large-scale data efficiently, ensuring secure data management and insightful reporting.

## Project Architecture Description

![image](https://github.com/user-attachments/assets/984a6339-15aa-414e-9ee4-19fa2ffe525d)

This architecture diagram represents a data processing and analytics pipeline using various Azure services. Here's a breakdown of each component and its role in the overall architecture:

1. **On-premises SQL Server Database:**
   - The starting point of our data pipeline where raw data resides.

2. **Azure Data Factory (ADF):**
   - Responsible for orchestrating and automating data movement from the on-prem SQL Server Database to Azure Data Lake Gen2.

3. **Azure Data Lake Gen2:**
   - **Bronze Layer:**
     - Raw data ingested from the source.
   - **Silver Layer:**
     - Cleaned and transformed data ready for further analysis.
   - **Gold Layer:**
     - Final, highly curated data for advanced analytics and reporting.

4. **Azure Databricks:**
   - Provides a platform for data engineering and data science. Used for transforming raw data in the Bronze Layer to refined data in the Silver and Gold Layers using Apache Spark.

5. **Azure Synapse Analytics:**
   - An integrated analytics service that accelerates time to insight across data warehouses and big data systems. Used for querying and analyzing data stored in the Gold Layer.

6. **Power BI:**
   - A business analytics tool used to visualize data and share insights across the organization. Connects to Azure Synapse Analytics to create interactive dashboards and reports.

### Security & Governance

1. **Azure Active Directory:**
   - Provides secure authentication and authorization services, ensuring only authorized users can access the data and services.

2. **Azure Key Vault:**
   - Safeguards cryptographic keys and secrets used by cloud applications and services, enhancing security and compliance.


## Project Agenda

### [1. Environment Setup](#part-1-environment-setup)
### [2: Data Ingestion using Azure Data Factory (ADF)](#part-2-data-ingestion-using-azure-data-factory-adf)
### [3: Data Transformation using Azure Databricks](#part-3-data-transformation-using-azure-databricks)
### [4: Data Loading using Azure Synapse Analytics](#part-4-data-loading-using-azure-synapse-analytics)
### [5: Data Reporting using Power BI](#part-5-data-reporting-using-power-bi)
### [6: Security and Governance](#part-6-security-and-governance)
### [7: End to End Pipeline Testing](#part-7-end-to-end-pipeline-testing)


## Part 1: Environment Setup

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


## Part 2: Data Ingestion using Azure Data Factory (ADF)
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



## Part 3: Data Transformation using Azure Databricks

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

### Building ETL Pipeline using Azure Data Factory(ADF) to run jobs for Level 1 and Level 2 transformation in Databricks as data changes in ADLGen2 storage account 

6 Create a linked service in ADF to connect to Databricks Compute
![image](https://github.com/user-attachments/assets/78f59408-ea77-4473-bd3b-07dc52496b45)

6.1 Generate access token in Databricks to establish connection between ADF and Databricks
![image](https://github.com/user-attachments/assets/c37655c1-a41e-4253-b17b-df2f69a8fdcc)

6.2 Add the token to the key valut 
![image](https://github.com/user-attachments/assets/337c21eb-9fb0-46e9-8361-2d9e44eae4eb)

6.3 Add Access token from Key Vault to finalize generate linked service and publish the changes to access the newly created Linked Service
![image](https://github.com/user-attachments/assets/ef8f2d9d-e878-4de9-a623-85c7a3b1853a)

6.4 Add 2 notebook activities to the prior Copy All Tables to ADLGen2 Activity we created, one for bronze to silver and other for silver to bronze

![image](https://github.com/user-attachments/assets/3ae0e344-ef99-49b9-8751-e37b456b69c7)

![image](https://github.com/user-attachments/assets/3d20e153-4c52-42eb-bf47-081b9b42def3)

![image](https://github.com/user-attachments/assets/dba6e86d-d860-4d6b-ba17-3ab80edb6a8c)

6.5 Publish the changes to deploy to Data factory and git repo

6.6 Add trigger to execute the pipeline
![image](https://github.com/user-attachments/assets/3026b091-c0db-4c49-aef3-a09e455240ad)

Note: In this project, we are overwriting the data to the ADLGen2 and not implementing the incremental update. We can append the 'Delta Data' from operational databases and using databricks operations to the ADLGen2 using 'append' mode in databricks. we have four modes 'append', 'overwrite', 'ignore', and 'error' to save files on Datalakes from Databricks. 


## Part 4: Data Loading using Azure Synapse Analytics
## Part 4: Data Loading using Azure Synapse Analytics
- Synapse is built on the top of Azure Data Factory. It is a combination of both Azure Data Factory and Azure Databricks

- Version Control with Github
![image](https://github.com/user-attachments/assets/c9f662f6-e621-456a-af84-e0a475ef0d3e)

7. Create SQL Database inside 'Data' section.

1. Dedicated SQL Pool(DSP) vs Serverless SQL Pool(SSP) [difference](https://www.royalcyber.com/blogs/dedicated-sql-pool-vs-serverless-sql/)
- DSP is Azure SQL Datawarehouse having power of compute and storage. However, SSP only has compute and can connect to external source to run the queries.
- SSP It can only create the external tables, on the other hand, DSP has own storage for database tables(managed tables) and can create external tables as well along with database views.
- SSP comes with the subscription without additional charges, unlike DSP, which exhausts credits based on Datawarehouse Unit(DWH)/hour.
Note: Since the data we are dealing with is lightweight, we are going with SSP as we also have pre-processed/transformed finalized data in gold layer of ADLGen2. Hence, using the
SSP is the most optimal solution for this project.

2. When we created Synapse workspace, the connection to datalake was established automatically.
![image](https://github.com/user-attachments/assets/3b7247c0-d6cb-4892-b63a-30f02807b9ad)

3. We can see the files from gold container of ADLGen2 and can create the T-SQL query by right clicking table directory 
![image](https://github.com/user-attachments/assets/1c47967c-3365-419e-81c4-56cd03d719c3)

![image](https://github.com/user-attachments/assets/736b9953-3f9f-488d-8938-efa03a23d12f)

- The clean data after transformation is queried
![image](https://github.com/user-attachments/assets/b936a84d-1556-41de-b48f-66041f0adf7b)

4. Create Synapse pipeline to create serverless sql views dynamically in synapse for all records of gold container
4.1 We first create a stored procedure to execute the code to create the views upon pipeline trigger
![image](https://github.com/user-attachments/assets/9c150c45-1ec6-447b-a00a-97b3dcd1349d)

4.2 Create a Linked Service to connect to the serverless sql pool endpoint to store the views and it is managed by Azure SQL Database 

![image](https://github.com/user-attachments/assets/872d363b-a21c-4688-9fa8-db9fbb8ab5c2)

![image](https://github.com/user-attachments/assets/4118dfef-c237-452e-b690-fd96bf99feee)


4.3 Create a linked service to fetch records from ADLGen2 and select 'gold/SalesLT/' folder
![image](https://github.com/user-attachments/assets/3f84f1f2-4a95-4d1e-8df8-4aa51bfbb9f1)

![image](https://github.com/user-attachments/assets/8e3c366c-ae57-4788-a788-5a92e45fb679)

- Upon debugging we get the result in JSON format
![image](https://github.com/user-attachments/assets/8de5a4e0-1bec-4913-9775-c3d2841135e9)
- We need to pass names of child items to create view dynamically

4.4 Create ForEach Activity to fetch the childitems from Get Metadata activity
![image](https://github.com/user-attachments/assets/ea40c5e3-8f1d-4b3a-9d0f-42f4945526c7)

4.5 Add a stored procedure activity in Foreach loop activity to run stored procedure we created in serverless sql pool by taking ViewName as parameter having table names(@item().name) assigned to it.

![image](https://github.com/user-attachments/assets/c6730136-aca1-4c3e-9a9e-6d324f4a135b)

4.6 After publishing the Changes and triggering the pipeline, all the views from ADLGen2 gold tables are created in Synapse serverless sql pool for analysis
![image](https://github.com/user-attachments/assets/74022f37-6db5-42be-8fbd-5387c5743a0e)

![image](https://github.com/user-attachments/assets/257261f2-5742-4635-8b25-aaac205e4cf9)



## Part 5: Data Reporting using Power BI


8. Connect the Synapse Serverless sql pool with Power BI

8.1 Select Below data connector
![image](https://github.com/user-attachments/assets/7e6f237b-bf7b-4069-835b-fa84d903d06b)

8.2 Use Serverless SQL Endpoint from 'Synapse Workspace > Settings > Properties' and choose Import as Storage Mode/Data Connectivity mode as the source is lightweight and we can use DAX queries 
for data modelling along with Time Intelligence. 
![image](https://github.com/user-attachments/assets/0ba2f8e7-a09e-422b-b970-a8c9ae0c3859)

8.3 Use Micorsoft EntraID(Azure Active Directory) email to authenticate credentials for serveless sql pool access
![image](https://github.com/user-attachments/assets/9e30ab21-37dd-43e2-b69a-ed043e8cd7e2)

![image](https://github.com/user-attachments/assets/35961d53-34f2-4b75-966f-51fb6b99a778)

8.4 Load all the tables to Power BI Desktop
![image](https://github.com/user-attachments/assets/6b57c30a-4205-4859-b68d-203f4950a175)

![image](https://github.com/user-attachments/assets/20e4a72c-2685-4b3f-91db-b26cb4e19151)

8.5 Created a calculated column to classify gender from titles
![image](https://github.com/user-attachments/assets/ebca721d-c2a3-4bbb-8f80-577cf2e22cd1)

8.6 Sample Dashboard 
![image](https://github.com/user-attachments/assets/0870720f-01c8-4597-b6a0-f9071cd1e739)


## Part 6: Security and Governance


9. Creating Security Groups in Microsoft EntraID (Azure Active Directory) to access Resource Group
1. I have created a sample security group and added Owner and Users to be added to Resource Group
![image](https://github.com/user-attachments/assets/15e4fc92-adf9-45f8-8ac6-348fe0f986af)

2. Add Contributor Role Assignment to the Resource Group
![image](https://github.com/user-attachments/assets/036d206c-41e3-416c-942c-28e883a73f2e)

3. Now a Security Group has rights to access the services from Selected Resource Group
![image](https://github.com/user-attachments/assets/d34bcd8d-81ef-4c8e-8755-07a13250bbdc)


## Part 7: End to End Pipeline Testing

10. Create a scheduled Trigger to Automate the ETL Pipeline

1 . We added 2 rows to Customer Table in SQL Server Database (operational database) using below script:
```sql

USE [AdvantureWorksDB2020L]
GO

set identity_insert AdvantureWorksDB2020L.SalesLT.Customer on

-- Sample Insert Record 1
INSERT INTO [SalesLT].[Customer]
           ([CustomerID],[NameStyle]
           ,[Title]
           ,[FirstName]
           ,[MiddleName]
           ,[LastName]
           ,[Suffix]
           ,[CompanyName]
           ,[SalesPerson]
           ,[EmailAddress]
           ,[Phone]
           ,[PasswordHash]
           ,[PasswordSalt]
           ,[rowguid]
           ,[ModifiedDate])
     VALUES
           (595959,0 -- NameStyle
           ,'Mr.' -- Title
           ,'John' -- FirstName
           ,'A.' -- MiddleName
           ,'Doe' -- LastName
           ,NULL -- Suffix
           ,'Example Corp' -- CompanyName
           ,'Jane Smith' -- SalesPerson
           ,'john.doe@example.com' -- EmailAddress
           ,'555-1234' -- Phone
           ,'HASHEDPASSWORD1234567890' -- PasswordHash
           ,'SALT1234' -- PasswordSalt
           ,NEWID() -- rowguid
           ,GETDATE()) -- ModifiedDate
GO

set identity_insert AdvantureWorksDB2020L.SalesLT.Customer off

set identity_insert AdvantureWorksDB2020L.SalesLT.Customer on
-- Sample Insert Record 2
INSERT INTO [SalesLT].[Customer]
           ([CustomerID],[NameStyle]
           ,[Title]
           ,[FirstName]
           ,[MiddleName]
           ,[LastName]
           ,[Suffix]
           ,[CompanyName]
           ,[SalesPerson]
           ,[EmailAddress]
           ,[Phone]
           ,[PasswordHash]
           ,[PasswordSalt]
           ,[rowguid]
           ,[ModifiedDate])
     VALUES
           (292929,1 -- NameStyle
           ,'Ms.' -- Title
           ,'Jane' -- FirstName
           ,'B.' -- MiddleName
           ,'Smith' -- LastName
           ,'Jr.' -- Suffix
           ,'Another Corp' -- CompanyName
           ,'John Doe' -- SalesPerson
           ,'jane.smith@anothercorp.com' -- EmailAddress
           ,'555-5678' -- Phone
           ,'HASHEDPASSWORD9876543210' -- PasswordHash
           ,'SALT5678' -- PasswordSalt
           ,NEWID() -- rowguid
           ,GETDATE()) -- ModifiedDate
GO
set identity_insert AdvantureWorksDB2020L.SalesLT.Customer off
```
2. Now the new count of Customers changes from 847 to  849.
![image](https://github.com/user-attachments/assets/69a1455a-1a32-43ea-9a2d-a37a2be45899)

3. The aim is to add this delta data to ADLGen2 containers and update the Power BI report.
Hence, we add the new Scheduled Trigger for the pipeline and publish the changes to ADF workspace
![image](https://github.com/user-attachments/assets/f0a32b3a-f858-42f3-976b-c66fe1359f3f)

3. The Pipeline will trigger automatically as per schedule. In below example, I had created hourly pipeline to check and interval was set to 5. However, for real time project
we will schedule the pipeline to trigger once a day or as per the business requirement. 
![image](https://github.com/user-attachments/assets/163193d0-b23d-48cc-99bc-b6d7d930bdaf)

4. The Trigger Runs as below
![image](https://github.com/user-attachments/assets/26adcddd-e54e-497e-81c8-1f214c34e150)

5. Upon refresh the report page, the Customer count gets updated. Thus, the delta data added successfully to the ADLgen2 containers and Synapse Serverless SQL views also updated.
![image](https://github.com/user-attachments/assets/9a7acdc3-4a53-411d-b7ce-f2ffb50b518c)


# Conclusion
This comprehensive Azure AdventureWorks Data Lake and Analytics Pipeline project provides a robust architecture for handling vast amounts of data efficiently and securely. By integrating powerful Azure services like Azure Data Factory, Azure Data Lake Gen2, Azure Databricks, Azure Synapse Analytics, and Power BI, this pipeline ensures seamless data ingestion, transformation, analysis, and visualization. The inclusion of security measures such as Azure Active Directory and Azure Key Vault further strengthens the solution, ensuring data integrity and compliance. The structured agenda guides you through the step-by-step implementation, from environment setup to end-to-end pipeline testing, making it a reliable blueprint for building scalable and intelligent data solutions.
