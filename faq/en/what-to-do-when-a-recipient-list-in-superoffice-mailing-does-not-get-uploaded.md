---
title: "What to do when a recipient list in SuperOffice Mailing does not get uploaded?"
url: https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-a-recipient-list-in-superoffice-mailing-does-not-get-uploaded/
lang: en
updated: "26 Mar 2026"
---

# What to do when a recipient list in SuperOffice Mailing does not get uploaded?

Updated on 26 Mar 2026

I want to include my recipient list, but it does not get loaded; recipients do not get uploaded, I just see the message: "Please wait, the recipient list is being updated...," or I get an empty list. Why does it happen, and how do I fix it?

There are some known reasons when this situation might occur. The sections underneath explain them. Please click on the relevant section to find the solution:

- [When your recipients do not have e-marketing consent](https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-a-recipient-list-in-superoffice-mailing-does-not-get-uploaded/#1)
- [When your recipients are companies, not people](https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-a-recipient-list-in-superoffice-mailing-does-not-get-uploaded/#2)
- [When*the eJScheduler* service is stopped (only SuperOffice CRM Onsite)](https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-a-recipient-list-in-superoffice-mailing-does-not-get-uploaded/#3)
- [When the *Registry* table has wrong values in the database (only SuperOffice CRM Onsite)](https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-a-recipient-list-in-superoffice-mailing-does-not-get-uploaded/#4)
- [When the *ejournalCrontab* file has wrong values (only SuperOffice CRM Onsite](https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-a-recipient-list-in-superoffice-mailing-does-not-get-uploaded/#5))

​

**When your recipients do not have e-marketing consent**

If in the Mailing setup you have selected the **Type (1)**that does not have consent from the recipients, then the recipient list will be empty.

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6607375-oK4zzEaYq3bcfeDU1tB8KA9x6EaY1Ust0FFGFI6ixjQD9JitM3UYR3U7N7n7l1AA-0/image-20260326211842-1.png)

To be able to send communication to the contact that you store in your CRM, you must have the consent. Please read [this FAQ](https://community.superoffice.com/en/support-faqs/faq/how-do-i-change-what-type-of-mailings-my-contacts-receive-from-my-company/) to learn how you can change it. Also, it is possible to ignore consent when you select the option **Override consent and subscription (2)** in the Recipients step.

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6607376-RUNZIkJP0XaC2BPBYKMOOnUm0CLXxTyHBXt7f9R26pQcHUtySHMxEcCJUdIAbdZz-0/image-20260326212035-2.png)

​

**When your recipients are companies, not people**

If you want to include companies as recipients, then you should select **Include companies (3)**. If a company has no email address, the mailing will instead be sent to all related contacts in the recipient list.

If you want to send the mailing only to companies in the recipient list (and not related to contacts), then select **Prefer company (4)**. Each company will only receive one mailing. Contacts that do not belong to a company will still receive the mailing. The Prefer company option is only available if you selected Include companies above.

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6607378-7fNlBf2mbc9QzDSfSILM8euCJDe4Xi28k3fATK9NdGpwtYozDBBixd3BqeDqUC0S-0/image-20260326213444-4.png)

​

**When the eJScheduler service is stopped (only SuperOffice CRM Onsite)**

The *ejtermsetup.exe*application starts the *ejScheduler* service, which is responsible for periodically running the applications *ejournalcron.exe* and *importmail.exe.*These applications, in turn, will perform various automatic tasks. One of these tasks is the recipient list generation.

When *ejScheduler* is stopped, you can experience the described situation. To start the service, please follow the steps below:

1. In the global search field, on the server where SuperOffice Service is installed, type in Services and open the Service application.

   ![](https://online2.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/4409685-Eho7hAmEqPnA0aA5sgcNt4YQGkHTsbQrDAwP84tuS3T89dXhic2Qrm3rKMTtsT98-0/image.png)
2. In the list of services, find the one that is called **ejScheduler**(1). If the status is empty and you see the option that allows you to start (2) a service, click on it.

   ![](https://online2.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/4409686-YYwJ67zpEaywedFeesLiDbYI8KOSgJM8I2cYlEldKRIYAxwaHlI5USx82KB74T66-0/image.png)

​

**When the *Registry* table has wrong values in the database (only SuperOffice CRM Onsite)**

When the value of the *Registry* table entry *DBI executable (reg\_id=131)* is empty or points to an invalid SuperOffice installation path, the recipient list generation task won't work.

**Note!** SuperOffice recommends performing a backup before making any changes directly in the database. [This FAQ](https://community.superoffice.com/en/support-faqs/faq/how-do-i-make-a-backup-of-the-superoffice-crm-database/) explains how to do it.

​

**When the *ejournalCrontab* file has wrong values (only SuperOffice CRM Onsite)**

When a path to the *ejournalCron.exe* file is incorrect or if the domain is not the same as your SuperOffice CRM installation, the recipient list generation task won't work. Please make sure these values are the same as those of your installation. To find the file, please follow the steps below:

1. Navigate to the SuperOffice Service installation folder on the server where SuperOffice is installed.
2. In the installation root folder, find and open the ***ejCrontab***(1) file.
3. In the file, you'll find two tasks for importing and sending an email. Make sure that the path (2) to the executable and the domain next to it are responding to your installation information.

![](https://online2.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/4413272-dOP0ocnaMQM2OEsDeqzp6fp7llFoN65fpNYJiZYFJg8xGd6SDPIeL86ZTxLgkb2d-0/image.png)

**More information**

FAQ: [How do I delete or change a finished Mailing?](https://community.superoffice.com/en/support-faqs/faq/why-cant-i-delete-or-mark-a-sent-mailing-as-completed-in-superoffice/)
