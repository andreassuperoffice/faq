---
title: "What to do when I cannot delete a company record in SuperOffice CRM?"
url: https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-i-cannot-delete-a-company-record-in-superoffice-crm/
lang: en
updated: "28 Dec 2025"
---

# What to do when I cannot delete a company record in SuperOffice CRM?

Updated on 28 Dec 2025

I want to delete a company card in SuperOffice CRM. I click on the Task button, then I try to click on the Delete option, but it is inactive (grayed out). Why does it happen, and how do I fix it?

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6465333-OnAAo6aMNbox66wcjDHzgYPbm9xHwa9lp43zLP8T3mgGtQ46tnEsLPWS8xYu0KMr-0/image-20251228104535-1.png)

There are several known situations when this can occur:

- [When a user does not have the rights to delete a company](https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-i-cannot-delete-a-company-record-in-superoffice-crm/#1)
- [When a user wants to delete the main company card](https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-i-cannot-delete-a-company-record-in-superoffice-crm/#2)
- [When a user wants to delete a company card that is linked in ERP connector](https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-i-cannot-delete-a-company-record-in-superoffice-crm/#3)

**When a user does not have the data rights to delete a company**

When a SuperOffice user cannot delete a company, often the user role that the user has is not permitted to delete records. To confirm or change that, please follow the steps below:

1. Log in to [Settings and Maintenance](https://community.superoffice.com/en/support-faqs/faq/how-do-i-access-administration-part-settings--maintenance-in-superoffice-crm/).
2. Check which **Role** that the user cannot delete from the company.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6465334-mMRpqrUSHcM2csJaFKqtbAgrzZZM83O0pH7jCfqXB1duULyyIR3PS7L2H4t2WGf7-0/image-20251228104806-2.png)
3. Navigate to **Roles (1)**, select the role of the user (2), click on the **Data rights** **(3)** tab, and confirm that in the Company line, the **Delete** (4) option is selected.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6465335-4aUJtxwBCNMYLPwmswS2usoXTFeuxrmFhUKCBniGXjSWu3a6fn5Skb3No2P0xcio-0/image-20251228105012-3.png)

**When a user wants to delete the main company card**

When a SuperOffice user cannot delete the company, it could be that this company is the main (your) company card. Simply hover over the grayed-out delete option. If the tool-tip says that "*This company owns associates and cannot be deleted,*" that means it is the main company card, and you do not want to delete it.

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6465336-RPxScSHA09lWadOWf0qAI3QH1JRrai9j0jk2QmZ2KW5ww93UFulJFe7uQYyZiSP0-0/image-20251228110249-1.png)

**When a user wants to delete a company card that is linked in ERP connector**

When a SuperOffice user cannot delete a company, it could be that this company is linked to the ERP system. This is possible by using one of the ERP link apps that we offer in the [SuperOffice App Store](https://appstore.superoffice.com/). To be able to delete the company, you should first remove the ERP link. Then the option to delete will become active.

**More information:**

FAQ: [How to remove a large number of company records from SuperOffice?](https://community.superoffice.com/en/support-faqs/faq/how-do-i-remove-companies-and-contacts-from-superoffice-crm/)

FAQ: [How can I restore companies and contacts deleted from SuperOffice?](https://community.superoffice.com/en/support-faqs/faq/how-can-i-restore-companies-contacts-or-requests-deleted-from-superoffice/)
