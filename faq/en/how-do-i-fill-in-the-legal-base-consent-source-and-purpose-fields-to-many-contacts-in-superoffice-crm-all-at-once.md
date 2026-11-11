---
title: "How do I fill in the “Legal base”, “Consent source” and \"Purpose\" fields to many contacts in SuperOffice CRM all at once?"
url: https://community.superoffice.com/en/support-faqs/faq/how-do-i-fill-in-the-legal-base-consent-source-and-purpose-fields-to-many-contacts-in-superoffice-crm-all-at-once/
lang: en
updated: "12 Jan 2026"
---

# How do I fill in the “Legal base”, “Consent source” and "Purpose" fields to many contacts in SuperOffice CRM all at once?

Updated on 12 Jan 2026

All the contact information that we store in our SuperOffice database is relevant and collected in accordance with the GDPR rules and our own business regulations. Thus, I want to update the Legal basis, Consent source, and Purpose fields for our contacts in SuperOffice CRM all at once. How do I do it?

If you import or store a lot of data in your SuperOffice CRM, you can use the bulk update feature to help you get this data GDPR-ready. Please follow the steps below to fill in the privacy data for many contacts at once:

1. Click on the**Find (1)**button and in the Find screen, click on **Find Contact (2)**to start your search.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6479439-gGxQISoGcHar1jj9bmsq51Bhhtgkhnm1KOmRnrGuZMmC06d8rkmNnyEis9pjotRY-0/image-20260112174234-1.png)
2. In the Criteria tab chose the field that you want to use for identifying the contacts that need to get updated. In this example, let's find all contacts that were registered this year. To do this, select the field **Registered date (1)** and choose **Year (2)**. When you are happy with your search setup, click on **Find (3)**to get a list of these contacts.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6479450-g43Xq0TbuWLNsdEXgnaaw29jzYnWoH3ewfPj5T2DWrPnQPZZqaLQgWw1xmBgU939-0/image-20260112175139-2.png)
3. Click on the **Save as selection (1)** button at the bottom of the list, then click on the option **Dynamic (or Static) selection (2)** and click **Save (3)**.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6479458-IFrhn6HOhe24bBSxwUIJSSYca6hCq1RMTbUxNSXaa4MkdJgCGt8z1y8tht0tZhQ8-0/image-20260112175323-3.png)
4. Fill in the name (1) of the selection, choose a **Category (2)** from the drop-down list, and click **Save (3)**.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6479462-5YMH7gqlGpm3aFB8pJom1sPaagT44OYCYirCDgNPHU9KueBryFN42orbW7aMwcmo-0/image-20260112175529-4.png)
5. At the top of the screen, click on the **Task (1)**button and then choose **Bulk update (2)** in the Manage section.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6479466-qgqiAiiS4CP1fjuyN32zW4sf0nMnPIZmoj3QsnO21wsCI9uosCW5GeU8fexAWSgO-0/image-20260112181331-5.png)
6. Click on the **Contact tab (1)** and click **+Add (2)** to include a new field. Then, from the drop-down select the **Legal Basis (3),**choose an action, **Add/Update (4).**Click there where it says **Click here to add legal base for purpose** and set up preferred values in the fields (5), then click on the **Update (6)**button to initiate the change.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6479483-mcncLqRXyoLARY4J3jIurmPQZjarfWImegoNYs3w29JgZ1ggIS14LYFalrPPKnAY-0/image-20260112182536-6.png)
7. Click **Yes**to make the update.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6479484-Wn4iwHue7LRojDqxq6Pfdrw8NswGqNX12csorbnRzylnLhHXcDIftE2sSYYnGuTt-0/image-20260112182623-7.png)

**Note!** Bulk Update cannot be undone. That's why we recommend creating a database backup before making any large data updates. If your SuperOffice CRM is installed Onsite, please refer to [this FAQ](https://community.superoffice.com/en/support-faqs/faq/how-do-i-make-a-backup-of-the-superoffice-crm-database/) that explains how to do it. If you use SuperOffice Online, you do not have to do anything extra, as backups are created automatically. When bulk updating a large number of rows at once, a timeout can occur. In that case, we recommend doing the update in smaller batches.

**More information**

Docs: [Update multiple records (bulk update)](https://docs.superoffice.com/en/learn/basics/bulk-update.html)
