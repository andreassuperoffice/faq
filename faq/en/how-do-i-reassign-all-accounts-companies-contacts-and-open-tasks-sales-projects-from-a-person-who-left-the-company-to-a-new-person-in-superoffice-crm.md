---
title: "How do I reassign all accounts (companies, contacts) and open tasks, sales, projects from a person who left the company to a new person in SuperOffice CRM?"
url: https://community.superoffice.com/en/support-faqs/faq/how-do-i-reassign-all-accounts-companies-contacts-and-open-tasks-sales-projects-from-a-person-who-left-the-company-to-a-new-person-in-superoffice-crm/
lang: en
updated: "6 May 2025"
---

# How do I reassign all accounts (companies, contacts) and open tasks, sales, projects from a person who left the company to a new person in SuperOffice CRM?

Updated on 6 May 2025

One of our employees left the company, and I need to reassign all contacts that belong to this person to a new person. Also, I need to reassign all open tasks, sales, projects, and remove the old user from SuperOffice and give this licence to the new SuperOffice user. How do I do it?

The smooth transfer of work from one to another user in SuperOffice CRM requires multiple steps to follow. The procedure described in this FAQ is a suggestion, but not the only way how to perform it.

To begin with please make sure you have these requirements in place:

1. Please do not delete the user of the person who left the company before reassigning records in SuperOffice.
2. Please make sure the new person has a SuperOffice user created already. Please check [this FAQ](https://community.superoffice.com/en/support-faqs/faq/how-do-i-create-a-new-user-in-superoffice-crm2/) for more information.
3. Your SuperOffice user has administrative rights with functional rights to Allow bulk update. Please check [this FAQ](https://community.superoffice.com/en/support-faqs/faq/how-do-i-configure-what-information-the-users-of-our-company-can-access-in-superoffice-crm/) for more information.
4. We always recommend creating a database backup before making any large data updates. If SuperOffice is installed onsite, please check [this FAQ](https://community.superoffice.com/en/support-faqs/faq/how-do-i-make-a-backup-of-the-superoffice-crm-database/) that explains how to do it. If you use SuperOffice Online, backups are created automatically. However, we strongly recommend that you order a backup before making any changes, as this requires contacting SuperOffice support. You should also be ready to act quickly if any data needs to be restored. Please check [this FAQ](https://community.superoffice.com/en/support-faqs/faq/how-do-i-obtain-the-backup-of-our-superoffice-online-database/) that explains how to do it.

To transfer all accounts (companies and with contacts) and open work (tasks, follow-ups, sales, projects), please follow the steps below:

1. [Make selections of records in SuperOffice CRM that you want to reassign.](https://community.superoffice.com/en/support-faqs/faq/how-do-i-reassign-all-accounts-companies-contacts-and-open-tasks-sales-projects-from-a-person-who-left-the-company-to-a-new-person-in-superoffice-crm/#1)
2. [Change ownership of these records from the old to the new user.](https://community.superoffice.com/en/support-faqs/faq/how-do-i-reassign-all-accounts-companies-contacts-and-open-tasks-sales-projects-from-a-person-who-left-the-company-to-a-new-person-in-superoffice-crm/#2)
3. [Retire the old user and reassign the user licence to the new user.](https://community.superoffice.com/en/support-faqs/faq/how-do-i-reassign-all-accounts-companies-contacts-and-open-tasks-sales-projects-from-a-person-who-left-the-company-to-a-new-person-in-superoffice-crm/#3)

**1. Make selections of records in SuperOffice CRM that you want to reassign**

To retain the original lists of records which ownership was changed we suggest making [static selections](https://docs.superoffice.com/en/search-options/selection/learn/create.html). Then make a different selection for different types of records that you want to reassign to the new user:

1. Click on Find (1) and one by one make searches of Companies (2), Contacts (3), Follow-ups (4), Sales (5), Projects (6)

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6194024-IXYnAoHT8WWgIXyi2IIPGGB5J5AmWxGXPRpEsgw1EcKA52Mqc0dfD7LqErNrnJhW-0/image-20250506090805-1.png)
2. Different entities in SuperOffice CRM have different fields, which determine the ownership. Therefore, be aware that you should use different fields as criteria for search.
   1. When you search for Companies use the field **Our contact** to determine which companies belong to the user.

      ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6194194-ujxYYHXRSQ1ubynOlo9kAhOezD5ZbAitwm74xkUNSpAI6i4mH59IoiUJbQyum43d-0/image-20250506102638-3.png)
   2. When you search for Contacts use the field **Our contact** to determine which contacts belong to the user.

      ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6194195-3ouZEPibYJ67QD7Q3LcouTtyPqICrnYyASFUmgK8cJwi2IlOASqTNQrgel2jHJN6-0/image-20250506102744-4.png)
   3. When you search for Follow-ups use the field **Owner** to determine which follow-ups belong to the user.

      ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6194202-lotKlplZc96Ffd9uLjOHPsLlfpTxffoMi7uoJU1ccHLi3TJ5R4A2B8DppHcBQwn4-0/image-20250506102851-5.png)
   4. When you search for Sales use the field **Owner** to determine which sales belong to the user.

      ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6194203-U8blw4681oFr4ktnhNNCzBYnFnscFmCm20j7T1xH0M8MjGKit2KxXW7bJYywwalB-0/image-20250506102929-6.png)
   5. When you search for Projects use the field **Responsible**to determine which sales belong to the user.

      ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6194204-dMMDPTuP7woU9Ubpk0L5wNgCSp8yG8kauGe2OusdNFIuSe8OY06ZhEDmM1cf1bGd-0/image-20250506103020-7.png)
3. Then save these searches as static selections. Click on **Save** (1)as selection and choose **Static selection** (2). Repeat it for searches of Companies, Contacts, Follow-ups, Sales, Projects one by one.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6194223-CJwqJP9FyfaPXl9CHZobqSfn5uKDEZi2HplP0lWiQOANgLyESRhUjGEpfTt5t6x1-0/image-20250506103302-8.png)

**2. Change ownership of these records from the old to the new user**

Below is explained how to change ownership of the company records in SuperOffice. Please follow the same steps to change ownership of other entities.

1. Open the selection and click on **Task button (1)** and **Bulk update (2).**

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6194235-IUlwQ2jasEj320Gx7sEHcrNYHUoZOTQgCCtERB92SUpoiSsNkmKYp6M6P8TtqcK1-0/image-20250506103833-11.png)
2. Select **Our contact (1)** field, select a user that you want to assign companies to and click **Update (2).**

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6194234-aoKen1o516pGTOX6SBGLyG7tFZDxNAwZ7Jdob8KlxRfgGPsXk1BJLo1pans4SPks-0/image-20250506103754-10.png)
3. Click **Yes**to confirm an update.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6194233-dpQrkFWeMG4lXOJdfc9cM1WXIUiPJ0poJU42bb4doycHWehUyApf4d9JES1x1YtB-0/image-20250506103629-9.png)
4. Repeat it to change ownership of other entities.

**3. Retire the old user and reassign the user license to the new user**

After all companies, contacts, sales, follow-up`s and projects are reassigned to a new user you can either take away the login right for the user (recommended way) or delete the user. Please check [this FAQ](https://community.superoffice.com/en/support-faqs/faq/how-do-i-set-a-user-as-a-former-employee-in-superoffice-crm/) to see in detail how to do it.
