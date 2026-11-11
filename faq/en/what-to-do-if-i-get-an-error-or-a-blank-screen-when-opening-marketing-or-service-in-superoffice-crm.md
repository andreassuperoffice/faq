---
title: "What to do if I get an error or a blank screen when opening Marketing or Service in SuperOffice CRM?"
url: https://community.superoffice.com/en/support-faqs/faq/what-to-do-if-i-get-an-error-or-a-blank-screen-when-opening-marketing-or-service-in-superoffice-crm/
lang: en
updated: "26 May 2025"
---

# What to do if I get an error or a blank screen when opening Marketing or Service in SuperOffice CRM?

Updated on 26 May 2025

When I try to open Marketing or Service I get an error:

*A Netserver exception occured: Service call failed with exception User.SaveUser [SR\_INVALID\_USERNAME] [SR\_ADMIN\_USER\_NAME\_ALREADY\_EXIST]*

Why does it happening, and how do I fix it?

![](https://cs.superoffice.com/scripts/customer.fcgi/getAttachment/2662770-cpkKqP41pq7EFDmFAJFRIOt6mQdWZP0ZmthrJ3JmmwrGzgW0dGpwqNJckL98cZ50-0/Fontenay%20eMarketing%20Error%2020150506%200857.jpg)

or blank screen:

![](https://online2.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/3271721-x2YHSMGUtWaalkNUE6Q2Z06ATOkSdsb9eYa9XPsoqrGrO2PGd9Mntqy3h4xCye12-0/image.png)

There are two known situations when this error happens:

- [When the Service config file has incorrect values](https://community.superoffice.com/en/support-faqs/faq/what-to-do-if-i-get-an-error-or-a-blank-screen-when-opening-marketing-or-service-in-superoffice-crm/#1)
- [When System user was not created with ID = 1 during the installation](https://community.superoffice.com/en/support-faqs/faq/what-to-do-if-i-get-an-error-or-a-blank-screen-when-opening-marketing-or-service-in-superoffice-crm/#2)

**When [Service config](https://docs.superoffice.com/en/service/config/index.html) file has incorrect values**

The solution is to correct the values in the Config file. Check this [article](https://docs.superoffice.com/en/service/config/index.html) to learn more.

**When the System user was not created with ID = 1 during the installation.**

When you run *eJtermsetup.exe* to install Service a System user should be created in the *eJuser* table with record id = 1. When you enabled **Service/Complete** license for a user before running*eJtermsetup.exe* the user gets a record id = 1 (not system user) and this causes the described problem. To confirm please run the query: *select \* from crm7.ejuser*

This is how the results in the database should look like:

![](https://cs.superoffice.com/scripts/customer.fcgi/getAttachment/2870401-FnudGj48rCnUKFiln8dOxcL4XWm3PfwrbB7zLf2sZidDJoIGADkL09kSj7d3idxK-0/image.png)

This is the example of a mistake:

![](https://cs.superoffice.com/scripts/customer.fcgi/getAttachment/2870402-0O4Xy0PNKEUp4UnDbcY5eUn2EoqOmkJT2ikzUclBCK3sahLn0JPozTJgQZUNLiqb-0/2017-01-20_11-35-38.png)

**Note!** The fix needs to be applied directly to the database. Contact your IT responsible or [SuperOffice Consultant](https://www.superoffice.com/company/contact/) for this task.

The solution is to fix an ID order in the *eJuser* table. Please follow the steps below to do it:

1. Open **Settings & Maintenance** and disable the **Service/Complete** license for the user which has ID = 1
2. In the **Associate** table in the database, update the eJuserID to 0 on the user record, which has ID = 1 in the test.
3. Run this query:

   *update crm7.EJUSER set loginname = '(System)', username='(System)', firstname='', lastname='', access\_level=16762879, status=127, signature=NULL, notify\_mask=0, email\_mask=0, sms\_mask=0, language='en', dictionary='en', flags=0, last\_category=-1, login\_attempts=0, new\_gui=1,  picture\_id=-1, num\_expanded\_messages=3 where id = 1*
4. Then open **Settings & Maintenance** again and you can change back the user plan to the user which had ID 1 in the database before.
