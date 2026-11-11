---
title: "How do I obtain the backup of our SuperOffice Online database?"
url: https://community.superoffice.com/en/support-faqs/faq/how-do-i-obtain-the-backup-of-our-superoffice-online-database/
lang: en
updated: "24 Aug 2026"
---

# How do I obtain the backup of our SuperOffice Online database?

Updated on 24 Aug 2026

How do I obtain the backup of our SuperOffice Online database?

To get a backup of your database and/or documents and/or document templates, please follow the steps below:

1. Send a request to [SuperOffice Support](https://cs.superoffice.com/) asking for a backup. FAQ: [How do I register a support request within SuperOffice CRM?](https://community.superoffice.com/en/support-faqs/faq/how-do-i-register-a-support-request-from-within-superoffice-crm/)
2. SuperOffice Support will inform you when the backup is ready to be downloaded.
3. Follow the instructions in the section that is relevant to your case:

- [If you want to download both the database and the document archive, use the Download tool](https://community.superoffice.com/en/support-faqs/faq/how-do-i-obtain-the-backup-of-our-superoffice-online-database/#1)
- [If you only need to download the database, use the Operational Center](https://community.superoffice.com/en/support-faqs/faq/how-do-i-obtain-the-backup-of-our-superoffice-online-database/#2)
- [If you need more information on how to work with the .sdb file database](https://community.superoffice.com/en/support-faqs/faq/how-do-i-obtain-the-backup-of-our-superoffice-online-database/#3)

**You want to download both the database and the document archives with the Download tool**

1. Click on the following link to download the Download tool: <https://online.superoffice.com/Download/Tool>
2. Double-click the file and then click on the **Login** button.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6621756-EqLX60z5h9k4wXzpLp9xhATnNoOFs7EhE1KzjbljDIyHiFHKOIEngLYZ4Piahq6u-0/image-20260409120834-1.png)
3. This will open the login dialog in a browser. Login using your SuperOffice credentials and select the tenant. You will get a confirmation message if the login is successful.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6185017-mP3YPBb7uini8Rxs4XpascgRbjtUYZPG41xG5Coyh5aW6yYwnWs0QSL8iQfXhS2B-0/image-20250425111101-2.png)
4. Navigate back to the tool. From the drop-down list, select the backup (1), click next to **Database** (2) if you want to download it, click next to **File** (3)if you want to download it, select the location where backup and document files have to be stored (4), and click on the **Download** (5)button.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6622231-0APEXArgKDXUuydB6qDzGmCEGLaYS2Y4uH3szIMR3RYhg9LZbbAhrP6p2r2w5IuY-0/image-20260409142455-2.png)
5. The document archive will be downloaded in two files:

   •    “Files 1.zip".

   **Note!** The documents found in the “Files 1.zip” folder are not accessible via the SuperOffice CRM interface.

   •    "Files 2."

   The database backup will be downloaded in *.sdb* format. If you need more information on how to work with the .sdb file database, navigate to [this section](https://community.superoffice.com/en/support-faqs/faq/how-do-i-obtain-the-backup-of-our-superoffice-online-database/#3).
6. Click on the link behind the word **here** (1)in the pop-up dialog to access the files, and then click **Finished** (2)to close the download tool.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6622232-NUyuW3AU54chG6pzUn2sFiPOSoxdWt2H4u2meluJy84819qsQh8Ao48dA59cUQnl-0/image-20260409142613-3.png)

**If you download the database from the Operational Center**

1. Your SuperOffice administrator will have to access the <https://online.superoffice.com/OC2/> and log in with his/her SuperOffice user name and password.
2. In the Operation Center, click on the **Backup/ Restore** section.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6622305-I5O3d605fMEUFipYQs8LAmrxPw52tsNNgeKLiFF5gLwwfdZKqKPEBfE7ie3Gp8BQ-0/image-20260409144636-6.png)
3. Simply click on the database icon to download the database

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6622304-HcuXfSRjYDaoF7PfWFlYyknwJhzRI7LFDsUBKjQTKjZdq3wS5xkJn6HC26zcmZGU-0/image-20260409144548-5.png)

**How to work with the .sdb file the database**

SDB files are gzip-compressed binary database snapshots exported from a SuperOffice CRM database. To open the database, you will need to overwrite an existing database on the SQL-Server.

We recommend that you create a new database with an ODBC connection  ([Create Microsoft SQL Server | SuperOffice Docs](https://docs.superoffice.com/en/onsite/install/database/create-ms-sql-server-db.html)), which you will overwrite during the database import (e.g., SOimport):

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6631704-MspYXWKdwHctSNpejctomLWMKeK6B0ZgTP0knK3ZRNR65lITQd150rzSWJ8rmOzs-0/image-20260415145841-1.png)

You can download CRMSetup [here](https://online3.superoffice.com/Cust1990/CS/scripts/rms.fcgi/getAttachment/6626597-upc6SP1k8aZZH6CltOUjkbIXj0PhlEWw2MAfb9lMLf0wattzfrkMSLwNUzCOmYYo-0/CrmSetup.zip).

This zipped folder contains 3 files:

- CrmSetup.exe
- Options advanced import.txt
- arg-file DBimport.txt

Here we will show how to import the full database with the provided import file arg-file DBimport.txt

For more advanced imports, see Options advanced import.txt in the downloaded folder and read further about CrmSetup here: [CrmSetup and CrmTask utilities | SuperOffice Docs](https://docs.superoffice.com/en/onsite/install/database/crmsetup-and-crmtask.html)

Fill in the import file like this: Red-marked values should be replaced according to the database you wish to replace:

*import-database*

*--database-server SQL server name*

*--database-name DBname*

*--db-user dbusername*

*--db-password dbpassword*

*--table-prefix prefix*

*--source-file pathtofile.sdb*

Example. Import file arg-file DBimport.txt created. Backup file was placed on the C drive, so the path is C:\database.sdb

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6631720-iIN0xCUM7iklmAHLMUfC7QfH5AXWKQyYxffxXkfWsFYzD0BZsFYlyLpMdZATrLC1-0/image-20260415150149-2.png)

When you have an .sdb file, a CrmSetup.exe file, and the import file, you run CMD.EXE as administrator and run the command to import the database. Basically, you point out the import file:

 crmsetup --arg-file DBimport.txt

In the screenshot below, you can see that all 3 files are placed on the C: drive.

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6631721-5erOAzB0SAhQCEkhRZE9nH3ASZixRMcsXBSrcluiEf2QYI7riPdjapHyngMJ3OpA-0/image-20260415150227-3.png)

**Note!**The import-database command in CrmSetup will *kill any existing SuperOffice tables* in the target database and replace them with the data from the SDB file.

**More information**

SuperOffice CRM is based on two types of data storage: Database and Document Archives.

- Database references: [Database table listing | SuperOffice Docs](https://docs.superoffice.com/en/database/tables/index.html).

- The SO\_Arc folder contains the document archive. Files are stored in a structure based on: the User ID of the creator, the year and half-year the document was created. File names are automatically generated using the company name and template type.

- Microsoft SQL Server Database data is separated for each customer. All Databases have a 30-day “point in time” backup. This means that a Restore can be made from any specific date/time within the last 30 days. In addition, a monthly backup is taken and stored for 12 months. A yearly backup is stored for 10 years.

- All Document Archives have continuous mirroring between two physically separated data centers and have individual backups in both locations. The backup runs once a day (usually at night). Document changes are backed up and stored for 30 days. Backup of deleted files (documents) is stored for 90 days.
