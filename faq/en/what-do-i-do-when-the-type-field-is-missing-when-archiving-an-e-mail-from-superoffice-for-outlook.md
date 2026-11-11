---
title: "What do I do when the Type field is missing when archiving an e-mail from SuperOffice for Outlook?"
url: https://community.superoffice.com/en/support-faqs/faq/what-do-i-do-when-the-type-field-is-missing-when-archiving-an-e-mail-from-superoffice-for-outlook/
lang: en
updated: "2 Jun 2025"
---

# What do I do when the Type field is missing when archiving an e-mail from SuperOffice for Outlook?

Updated on 2 Jun 2025

When working in Outlook and using the SuperOffice for Outlook add-in to archive e-mails, users might experience two scenarios:

- When sending a **new e-mail**, a warning appears: “*Please select a type before proceeding. E-mail archiving cannot continue without setting the type.*”

  ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6224836-Kc3zgKBeqj7yglkf7C7K2O49jHCtg50Id1N4WIcqikbDJgMqbrcbNt7IAHH5nQuN-0/image-20250531183259-1.png)
- When trying to archive a received e-mail, there is no warning, the **Type** field is not visible, and the **Save** button is inactive, preventing the e-mail from being archived.

  ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6224838-9oUg5zu6tzSnU5zoiEHLH6j2WYaYNtZlqBZUKxKwxiFqw7316hm5XLcR0zHbQurw-0/image-20250531183559-3.png)

**Why does this happen, and how can it be fixed?**

This problem arises because the user's current settings do not grant them access to any defined **e-mail types** within SuperOffice CRM.

An **administrator** must activate and ensure accessibility of e-mail types for the affected user's groups. To resolve this, please follow these steps:

1. Open **Settings and Maintenance**.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6224847-O2KNcUFu3cSrPmcf7NgAhPnWhEIZhZhzBgy4tAMhwXkJtwem7nKE1fHIQ30lXusZ-0/image-20250531183907-12.png)
2. Go to **Users (1)** – **find the user** experiencing the issue **(2)** and check which **user groups they belong to (3)**.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6224848-nG1zjkGf95eqB2JerCimfqJYfl014cIpebyrii04eZehy0ewWM4QX9E05NH0upiJ-0/image-20250531183945-13.png)
3. Then navigate to **Lists (1)** and choose **E-mail – template (2)** list.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6224849-OgUYqBldgDggqhAqWdae91AyaSQRn0xJ8dBZnNEORfqZyCsmkQSn1DSi0oqgEYpa-0/image-20250531184305-14.png)
4. Enable and configure group access for the e-mail types.

   Ensure that the checkbox **Use grouping and filtering by user group for this list (1)** is enabled.
   - If it is enabled:
     Go to **User groups (2)** and confirm that at least **one of the user’s groups (3)** is selected for at least one **active e-mail type (4)**.

     ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6224851-qDCgcII1z59GzL8LKAmG51J4Jc4mCDkru6draYZ6EqRiuKbxhsArPSseIuLNmcUq-0/image-20250531184724-16.png)
   - If it is not enabled:
     Enable **Use grouping and filtering by user group for this list** in both:

     - Document List

       ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6224853-cPlWsIDmp1TJ0b2FZAjSUrP3cBqLKh8fWtIfC140aXAPkqAugUHdg6KPjYLd5q2r-0/image-20250531184933-18.png)
     - E-mail template List

       ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6224854-00HpFwR2SABb7UkDpjmrTmdlohlIlDoS0A5iZ7uATaDzhQJj2w7Id3m7QPz7441n-0/image-20250531185010-19.png)

       This ensures grouping logic is applied consistently across templates.
5. Navigate back to **E-mail – template** list and verify that at least one of the user’s groups is selected in at least one active e-mail type.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6224855-oLOR8wmR2jcxPzkLjZ0Tyl9RgGdTSdTx0pPKHo303Y0r3EBPNYPrfIzR7u0mP5YC-0/image-20250531185443-20.png)

**Note!** Some email types are dedicated to specific processes — for example, meeting invites or the quote process. These emails will not be visible in SuperOffice for Outlook.

**More information**

FAQ: [How do I get and start using SuperOffice for Outlook Add-in?](https://community.superoffice.com/en/support-faqs/faq/how-do-i-get-and-start-using-superoffice-for-outlook-add-in/)

FAQ: [How do I use SuperOffice with the new Outlook?](https://community.superoffice.com/en/support-faqs/faq/how-do-i-use-superoffice-with-the-new-outlook/)

FAQ: [What are the different types of Quote document templates and when are they used in SuperOffice CRM?](https://community.superoffice.com/en/support-faqs/faq/what-are-the-different-types-of-quote-document-templates-and-when-are-they-used-in-superoffice-crm/)
