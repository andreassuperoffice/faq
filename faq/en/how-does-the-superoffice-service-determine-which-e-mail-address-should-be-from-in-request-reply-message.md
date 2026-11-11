---
title: "How does the SuperOffice Service determine which e-mail address should be \"From\" in request reply message?"
url: https://community.superoffice.com/en/support-faqs/faq/how-does-the-superoffice-service-determine-which-e-mail-address-should-be-from-in-request-reply-message/
lang: en
updated: "12 Aug 2025"
---

# How does the SuperOffice Service determine which e-mail address should be "From" in request reply message?

Updated on 12 Aug 2025

We use SuperOffice Service to answer our customers’ inquiries, and in different situations, replies get different “From” e-mail addresses. How is the sender’s address determined in SuperOffice Service?

SuperOffice assigns the "From" e-mail address at the moment when the request is created in Service. The system uses a few rules to determine which e-mail should be set as the "From" address for all the communication, which will eventually be sent for the request.

1. If the request is created automatically by importing an e-mail from the mailbox, the "From" address will be the address of the mailbox from which the e-mail was imported.
2. If the requests have been created in the category, which is associated with a mailbox, then the "From" address will be the one, which is associated with the category.

**Note!**

• If the category has several mailboxes connected to it, it's not defined which one will be used as the "From" address.

• A "From" address is not going to be changed if, after being created, the request is transferred to another category.

1. If the request is created in a category that does not have an associated mailbox, the "From" address will be the one configured in **Settings and Maintenance** → **Preferences** → **Global preferences** → **Default from address**.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6287800-R3lnQnxC25CAY9KXI0ynan3rGfUl5j1nzaylIeLCBs7Ind0bE4bq6dqOrhRfMQaf-0/image-20250812134041-1.png)

**More information**

Forum: [Change from email address when replying to a customer](https://community.superoffice.com/en/technical/forums/api-forums/service-crmscript/change-from-email-address-when-replying-to-a-customer/)
