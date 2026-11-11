---
title: "What to do when I cannot open a document in SuperOffice CRM?"
url: https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-i-cannot-open-a-document-in-superoffice-crm/
lang: en
updated: "31 Mar 2026"
---

# What to do when I cannot open a document in SuperOffice CRM?

Updated on 31 Mar 2026

When I try to open a document I get an error *Path does not exist.*Why does it happen and how do I fix it?

Several known situations that may cause problems with opening documents in SuperOffice CRM.

Common scenarios when **everybody** in the company has issues with opening documents:

- [No one can open any document in the SuperOffice Windows client.](https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-i-cannot-open-a-document-in-superoffice-crm/#1)
- [No one can open any document in the SuperOffice Web client.](https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-i-cannot-open-a-document-in-superoffice-crm/#2)
- [No one can open one particular document.](https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-i-cannot-open-a-document-in-superoffice-crm/#3)

Common scenarios when **one** user has issues with opening documents:

- [A user cannot open any document in the SuperOffice Windows client.](https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-i-cannot-open-a-document-in-superoffice-crm/#4)
- [A user cannot open some or one document while in Travel mode.](https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-i-cannot-open-a-document-in-superoffice-crm/#5)

**No one can open any document in the SuperOffice Windows client**

Most probably, the cause of the problem is lost access or the absence of reading and writing rights to the SO Arc folder. To solve the issue:

1. Make sure that the computer is connected to the server where the SO Arc folder is located.
2. Make sure that everybody has read and write access rights on the SO Arc folder.

**No one can open any document in the SuperOffice Web client**

Another possible cause of the problem is an expired or changed password of an impersonated user in the SuperOffice product configuration. To solve the issue:

1. Open the SuperOffice web (or NetServer if it is installed separately) product configuration app, which can be found in the SuperOffice server.
2. Navigate to the section called **AD integration (1)** and click on the **Validate (2)**button. That should generate a notification of successful user authentication (3).

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6611153-F0P9eXZz1rel9Z1wcRkPHNgpeSE9TmrKhr9HJJguwzeDx6CCjN2UJMeKAae7Iqd0-0/image-20260331102856-1.png)

**No one can open one particular document**

Possible causes of this problem are as follows: (a) this document has been deleted from the SO Arc folder, or (b) the user who created the document has been deleted.

In both cases, to restore a lost document, you will need to have a backup of the database and/or the SO Arc folder. One of the SuperOffice consultants can help you with this task.

**Note!**A consultant´s services are available at a fee. Please contact your account manager if you would like to get more information about this service.

**A user cannot open any document in the SuperOffice Windows client**

A possible reason for this problem is that the computer does not have access to the SO Arc folder, or the read/write rights to the SO Arc folder are not activated.

To solve the issue, paste the SO Arc patch into the File Explorer. The SO Arc path can be found in the SuperOffice Client's folder, *SuperOffice.ini* file.

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6611159-zloyFqLr4WOjWtH7dA9KRxsfwW1uXAFe0n9r945RTPL97jgqyPKjqjt8cxT1uw52-0/image-20260331103346-3.png)

It should open the **SO Arc folder** on your SuperOffice server.

**A user cannot open any document while in Travel mode**

In Travel mode, SuperOffice works on a local database. Documents must be transferred to the So Local folder (SO\_LOCAL, or local SO Arc) during a local update. If a document is not available locally, it cannot be opened offline.

**More information**

FAQ: [What to do when e-mails and documents from SuperOffice CRM stopped opening with Microsoft Office programs?](https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-e-mails-and-documents-from-superoffice-crm-stopped-opening-with-microsoft-office-programs/)
