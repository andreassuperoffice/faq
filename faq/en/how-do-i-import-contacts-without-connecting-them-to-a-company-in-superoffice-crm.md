---
title: "How do I import contacts without connecting them to a company in SuperOffice CRM?"
url: https://community.superoffice.com/en/support-faqs/faq/how-do-i-import-contacts-without-connecting-them-to-a-company-in-superoffice-crm/
lang: en
updated: "23 Jun 2025"
---

# How do I import contacts without connecting them to a company in SuperOffice CRM?

Updated on 23 Jun 2025

I want to import an excel file of contacts who do not belong to any company. How do I do it?

**Note!**

1. SuperOffice user, that is performing contact import, has to have a role, that has [data right](https://docs.superoffice.com/en/admin/user-management/learn/role/set-data-rights-for-role.html) setup, which allows to create and/or update contacts. Please check [this FAQ](https://community.superoffice.com/en/support-faqs/faq/how-do-i-configure-what-information-the-users-of-our-company-can-access-in-superoffice-crm/) for more information.
2. To import contacts without a company connection into SuperOffice CRM, you need to set up the **Mandatory company on contact** preference to **No**. Please check [this FAQ](https://community.superoffice.com/en/support-faqs/faq/how-do-i-create-contacts-without-a-company-connection/) for more information.
3. Import cannot be undone, that's why we recommend creating a database backup before making any large data updates. If SuperOffice is installed onsite, please refer to [this FAQ](https://community.superoffice.com/en/support-faqs/faq/how-do-i-make-a-backup-of-the-superoffice-crm-database/) that explains how to do it. If you use SuperOffice Online, please contact [Support](https://community.superoffice.com/en/support-faqs/faq/how-do-i-register-a-support-request-from-within-superoffice-crm/).

To import contacts without connecting them to a company, please follow the steps below:

1. Prepare an import file that contains new contacts. Please check [this article](https://docs.superoffice.com/en/admin/import/learn/create-import-file.html) for the tips regarding the preparation of the import file.
2. In the [Settings and Maintenance](https://community.superoffice.com/en/support-faqs/faq/how-do-i-access-administration-part-settings--maintenance-in-superoffice-crm/), choose **Import** (1) in the Navigator menu on the left, then select **Company/contact**(2) and click on the **Excel** (3) icon.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6247097-g5UJdMqHn6teptezW2i0J4kgBQBfY07Wm3Bl1d8eXSLq3XWTeK2YeoXXbhP0TWoz-0/image-20250623110911-1.png)
3. In the next step, upload your Excel file in the Upload file dialog.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6247098-dtiPAy1SHBmn5DI4Jc8Iqm81OerEcsH6B8KTIZKYf1DdIiPsMlIFc9DAq2o6Kb1N-0/image-20250623111505-2.png)
4. Select the SuperOffice fields for the columns of your import file. You do not need to do this for the columns you do not want to import.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6247115-eXU30WHR485F3CCsMGaR0AeMdMKo2b5jf5jbBCZfeDhUaNGC81bIn5eegCqw4Ik5-0/image-20250623112825-4.png)
5. Click on **Configure import settings** (1) and in the **Import settings** dialog, next to **If no company name** select *Import contacts without company* (2) option. Make other adjustments if needed and click **Save** (3).

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6247120-9PbBZh8sr79SlBtGUrnHOt97e4ESZ15uazScLsNM1sD56tj10adYPsx19uPKUIfQ-0/image-20250623113019-5.png)
6. When you are happy with the set-up, click **Next**.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6247121-H3dONYZYESfwFbwgZjq6E6A4sN80oDzEZaB7k6E3pTdWYyCnyuCIYQXsnqfsnXZu-0/image-20250623113055-6.png)
7. In the next step you will see a preview of import, check whether everything is correct and click on the **Import** button to finish the import.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6247128-T7PRkdthwwkbu0WtsMfo4j6ezEnMHiLWEzq6EcR9lMnRZkgmCisdSlA1hlcpu7Y2-0/image-20250623113135-7.png)
8. The import result screen will appear. Click on **Go to selection of new companies/contacts** to open a selection of imported contacts.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6247161-2wl49gLLE8I35l6uJLI6De0z8H9oBYsMB1mEDJf4hon5Rf6z2S88pL88I7aYiORf-0/image-20250623113809-8.png)
9. If you need to make adjustments to the imported contacts, you can easily do it from a selection using the [Bulk update](https://docs.superoffice.com/en/learn/basics/bulk-update.html) feature.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6247164-jKqHinRUjNsSWK7Cp1tYNKJUHss3uS8MGrtG1gy0iA98pJYMUnZROnAULFn9YOMa-0/image-20250623113958-9.png)

**More information**

**FAQ:** [Why is the “Number” field not allocated automatically during the import of companies/contacts?](https://community.superoffice.com/en/support-faqs/faq/what-do-i-do-when-the-values-of-contact-or-company-number-field-is-not-allocated-automatically-during-the-import/)
