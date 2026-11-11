---
title: "How do I make a backup of the SuperOffice CRM database?"
url: https://community.superoffice.com/en/support-faqs/faq/how-do-i-make-a-backup-of-the-superoffice-crm-database/
lang: en
updated: "7 May 2025"
---

# How do I make a backup of the SuperOffice CRM database?

Updated on 7 May 2025

How do I take a backup of SuperOffice database?

There are two ways how you can take a backup of your SuperOffice database:

1. Use database management system provided backup feature. If you use SQL Server Management Studio read [here](https://msdn.microsoft.com/en-us/library/ms187510.aspx) how to do it.

2. Use SuperOffice database management tool*DBsetup.exe.*

**Important!**

1. If you are not sure how to use*DbSetup.exe* contact SuperOffice support or your IT responsible. Using it in a wrong way you can in a worst case scenario destroy the SuperOffice database.​

2. *DBsetup.exe* reads out all data from the database server that is needed to restore/move SuperOffice database. *DBSetup.exe* only takes a copy of the database. It does not take a copy of the document archive SO\_ARC.

To learn how to take a backup with *DBsetup.exe* please follow the steps below:

1. Find *DBsetup.exe* in the SuperOffice server installation folder. The first time opening *DBsetup.exe* you will get an information messages where you need to click **OK** to proceed.
2. Then in the main screen choose the **Export a database**option.
3. Enter the path/filename or click on the '...' to browse to the location on disk. The file must have the suffix ".Sdb".

   **Note!**Before SuperOffice 8.1 file extension was called .sda
4. Choose the ODBC of your database in **Source Database**. Typically SuperOffice ODBC is called "SuperOffice7", "SuperOffice8", "SuperOffice"...
5. Fill in the **User ID,  Password** and **Prefix**. If you do not have this information, please contact your companies IT responsible.
6. Click on the **Start** button to make a backup.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6196137-t4ARLyOTSWk4QmnA4GTqe2mkhTb7IOAMguDXgG21s9XmrmOGTdotqSk6gZt3X1sl-0/image-20250507114806-2.png)

**More information:**

FAQ for Online customers:[How do I get the backup of our SuperOffice Online database?](https://community.superoffice.com/en/support-faqs/faq/how-do-i-obtain-the-backup-of-our-superoffice-online-database/)
