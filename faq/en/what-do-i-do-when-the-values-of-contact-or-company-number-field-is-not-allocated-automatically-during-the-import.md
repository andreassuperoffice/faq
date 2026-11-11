---
title: "What do I do when the values of contact or company “Number” field is not allocated automatically during the import?"
url: https://community.superoffice.com/en/support-faqs/faq/what-do-i-do-when-the-values-of-contact-or-company-number-field-is-not-allocated-automatically-during-the-import/
lang: en
updated: "15 May 2026"
---

# What do I do when the values of contact or company “Number” field is not allocated automatically during the import?

Updated on 15 May 2026

I have made an import of companies and noticed that the **Number** fields on the imported records in SuperOffice are empty. It is a mandatory field in our system so now whenever I edit an imported record, I cannot save it without filling in the number field. Why company/contact number wasn't allocated automatically and how do I fill information to the number field automatically?

SuperOffice CRM does not allocate thenumber field values automatically during the import of new companies or contacts, even if this field is mandatory in your system. This is an expected system behavior; however, a wish has [been](https://community.superoffice.com/en/product-releases/bugs-wishes/product-issue/?bid=8686&azure=1)registered in our system to improve this feature.

If you are importing new contacts and/or companies, and a number is a mandatory value in your system, you want to include these values in your import file and import them together with all the other information.

If you have already imported companies/contacts without including values in your import file, you can include the number values in your current files and repeat the import. Please follow the steps below to do it.

1. Log in to [Settings and Maintenance.](https://community.superoffice.com/en/support-faqs/faq/how-do-i-access-administration-part-settings--maintenance-in-superoffice-crm/)
2. Click on the **Options (1)**and then on the tab **Number allocation (2)**. On the screen, locate the type of record you are importing. Next to it, you'll see the value, which should be used for the next record, which is created in the system. Make a note of it.

   ![](https://app.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6684062-DCmQZQyPJhFBk8bBr1lwKeOTox9A5kB6tRTpuOC7nU5BoBAu1t9SD9xCfEfNlAwf-0/image-20260515150150-1.png)
3. Edit your Import file by including the number column. Fill in the values, which should start with the number you have noted before.
4. Repeat the Import. In the **Import settings**, select the *Merge - update empty fields*option in the **Action** field. This will make sure that the number field of the companies or contacts is filled in with the values you included in your file.

   ![](https://app.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6684080-4WoEPKUa6wGDKRBDco5n8dAhdFpdP5zPTT5uDGtDhUrRdy5nFdSRSRnFJMQaQYzE-0/image-20260515150305-2.png)
5. Go back to the **Number allocation** tab, double-click on the company or contact number, and in the Next number field fill in the number, which should be allocated to the new records. This number should be 1 bigger than the last number in your import file.

   ![](https://app.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6684097-jprwwCSDIGjmjK3LX6T7nscMzNjgWEHyOwOzCqmWn0tNc8bTGUspbWfFeomdx6aS-0/image-20260515150506-3.png)

**Note!**

1. We recommend taking a backup before making any changes directly in the database. [This FAQ](https://community.superoffice.com/en/support-faqs/faq/how-do-i-make-a-backup-of-the-superoffice-crm-database/) explains how to do it.
2. Make sure that no new companies/contacts are being created when you are performing an import, as this can impact the number sequence.
3. If you are not sure about the process, we advise you to employ SuperOffice consultants. The consultant service involves a fee. Please get in touch with your SuperOffice contact person if you would like to get more information about this service.
4. If you want to change the configuration so that the number field would not be mandatory on the records card, please select the **Allow blank** (1) option in the counter dialog.

   ![](https://app.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6684098-7HCIDxQ1cIjGQsKAQiqJf8BISDsFARX944yzn6POm0iLpemI48UEfEDRkiiLHKZu-0/image-20260515150604-4.png)

**More information**

Forum: [Provisional Solution to: Company and contact number field not updated during import](https://community.superoffice.com/en/technical/forums/product-forums/crm-web-application/provisional-solution-to-company-and-contact-number-field-not-updated-during-import/)

Wish: [Import and Number allocation problem](https://community.superoffice.com/en/product-releases/bugs-wishes/product-issue/?bid=8686&azure=1)
