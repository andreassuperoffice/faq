---
title: "How can I see all our requests in all categories in SuperOffice Service?"
url: https://community.superoffice.com/en/support-faqs/faq/how-can-i-see-all-our-requests-in-all-categories-in-superoffice-service/
lang: en
updated: "28 Dec 2025"
---

# How can I see all our requests in all categories in SuperOffice Service?

Updated on 28 Dec 2025

How can I see all requests that are registered in all [categories](https://docs.superoffice.com/en/request/admin/category/index.html) in our SuperOffice Service?

To be able to see all requests in all categories, a SuperOffice user needs to have the following set up in SuperOffice [Settings and Maintenance](https://community.superoffice.com/en/support-faqs/faq/how-do-i-access-administration-part-settings--maintenance-in-superoffice-crm/):

1. SalesPremiumServicePremiumMarketingPremium or Service User Plan, it can be configured in the SuperOffice user card.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6465341-P72EG1u8u5dUzGnHQLuBWkDph50MzLY2wutiscg5Y88kY9OrN1dIPN6TiXxESr30-0/image-20251228112911-1.png)
2. The user needs to have a Role that has *"List all requests", "Read all requests", and "Edit all requests"* functional rights granted to it. To grant these functional rights, please follow the steps below:

   1. Note which **Role**the user has.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6465343-7jspyNHqDcTmwWcDR24jjy1y1JHTd3yX8TptlfaWmTkRQwgGycKmG4AF2fOJGbO8-0/image-20251228113117-3.png)

   2.Click on **Roles (1),** select the role (2)**that the** user had, open the tab **Functional rights (3),**and in the column**This role can**:move*"List all requests", "Read all requests", "Edit all requests" (4)*

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6465345-F4exMJnSfJkmCFCBpTF6rQX7PnXMCg6CPapdEwdyrKg5dDgAb0AILSeZjL2uON8m-0/image-20251228113439-5.png)

**Note!**It is important that the role has only 3 above underlined functional rights, related to request management, in the column ¨This role can¨. If in the column "This role can" it has: *¨List request in own categories¨, ¨Read request in own categories¨, ¨Edit request in own categories¨,*as well as, *"List all requests", "Read all requests", "Edit all requests"* then the functional rights which above override the below ones and you won´t be able to see all requests, only the ones you are Category member of.

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6465346-PPZIUb3Yxjc6POWTMs1cEHzBlF4Mmo0KUE7X93gd44CHBhKWxt6p4rYmYTLUnlXB-0/image-20251228113540-6.png)

**More information**

Docs: [Request categories](https://docs.superoffice.com/en/request/admin/category/index.html)

Docs: [Create request category](https://docs.superoffice.com/en/request/admin/category/create.html)
