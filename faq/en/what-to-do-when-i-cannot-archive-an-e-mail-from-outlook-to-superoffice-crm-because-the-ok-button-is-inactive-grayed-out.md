---
title: "What to do when I cannot archive an e-mail from Outlook to SuperOffice CRM, because the OK button is inactive (grayed out)?"
url: https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-i-cannot-archive-an-e-mail-from-outlook-to-superoffice-crm-because-the-ok-button-is-inactive-grayed-out/
lang: en
updated: "28 Nov 2025"
---

# What to do when I cannot archive an e-mail from Outlook to SuperOffice CRM, because the OK button is inactive (grayed out)?

Updated on 28 Nov 2025

I want to archive an e-mail from my Outlook to SuperOffice CRM. I selected the e-mail, clicked on the archive button in the Outlook Ribbon, selected a company in the archiving dialog, but the e-mail button is inactive (grayed out). Why does it happen, and how do I fix it?

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6421984-xzZWRyjd9bkpMRKuiHx39bTaXsEA2ZXW7rYT8XX5ZZBYBackmG9OJW5PGayDeA5f-0/image-20251128131025-2.png)

The **OK** button in the archiving dialog becomes inactive (grayed out) when the **Company** or the **Type** fields are not filled in. Fill in these fields to make the **OK** button active.

If the **Type** field appears to be empty, as in the screenshot below, it means that your SuperOffice user account does not have access to the e-mail templates that are used to archive.

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6421979-IOU8xOANb0AEFCl7HoKEe4jonLSAyjJ5DrkXtMDSy4ao2OXLmFpWZjHtMFnls1h2-0/image-20251128131003-1.png)

Let your SuperOffice Administrator follow the steps below to make sure that your user account has access to the e-mail templates:

1. In [Settings and Maintenance](https://community.superoffice.com/en/support-faqs/faq/how-do-i-access-administration-part-settings--maintenance-in-superoffice-crm/), click on **Lists (1)**, choose an **Email template (2**) from the drop-down list, click on the **User groups** (3) tab, and in the list select the user **group (4)**, which the user belongs to. In the right-side column, make sure that this user group has access to the e-mail template and tick next to **Inc. E-mail** (5) or the template that is used to archive incoming e-mails in your organization.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6421991-el9uWy5nwkMJMnHazcdKp5067mIOLTxw56pgeHj2PBGHdi8UP2Enuc64n8YsGRnG-0/image-20251128131337-3.png)

   **Note!** If you used to see more templates in the **Type** field before, make sure that other templates are visible in your account's user group. Also, check MailLink settings, **Archive Option** (1) section, and make sure that the box next to **Show all templates** (2) is ticked.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6421992-RkTBlFiwzi50rxT46kyRCI8HzA5oAXL07XIwyqDc0hMw7pIZLzbjgQO0Yc2gR081-0/image-20251128131508-4.png)

**More information**

FAQ: [How do I create and use e-mail templates in SuperOffice CRM?](https://community.superoffice.com/en/support-faqs/faq/how-do-i-create-and-use-e-mail-templates-in-superoffice-crm/)

Docs: [Archive emails to SuperOffice](https://docs.superoffice.com/integrations/mail-link/archive.html)
