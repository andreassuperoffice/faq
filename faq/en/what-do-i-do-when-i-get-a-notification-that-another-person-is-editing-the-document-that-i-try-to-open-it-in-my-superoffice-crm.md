---
title: "What do I do when I get a notification that another person is editing the document that I try to open it in my SuperOffice CRM?"
url: https://community.superoffice.com/en/support-faqs/faq/what-do-i-do-when-i-get-a-notification-that-another-person-is-editing-the-document-that-i-try-to-open-it-in-my-superoffice-crm/
lang: en
updated: "5 Jan 2026"
---

# What do I do when I get a notification that another person is editing the document that I try to open it in my SuperOffice CRM?

Updated on 5 Jan 2026

I want to edit a document in SuperOffice CRM, but after I double-click on it, I get a notification that says:

*“This document is currently being edited by …. You will not be able to edit the document and save your changes. Do you want to open it in Read mode?”*

However, my colleague, who is mentioned in the notification, is not editing a document.

Why does it happen, and how do I fix it?

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6469651-O32okgFwilLt1LA8AwqdybUsAh4iUsqnwPoSpeapq228YHfIxj7in6n7wNRy1ioA-0/image-20260105192943-3.png)

This situation may occur when the computer shuts down before the document is saved or when WebTools are not correctly configured. When a user opens a document, it will be checked out of the system for other users to prevent multiple persons from editing the same document at the same time and overwriting each other's changes. When a user does not have the WebTools configured, the document will not be checked in after the user closes it. The changes the user made are not saved back into SuperOffice, and other users will not be able to open the document.

To prevent this from happening in the future, please make sure that all documents are saved (screenshot 1) and closed (screenshot 2) before you turn off the computer or SuperOffice CRM. Also, check if the user who last opened the document has the WebTools correctly configured. See this FAQ to learn how to configure the WebTools correctly: [What to do when e-mails and documents from SuperOffice CRM stopped opening with Microsoft Office programs?](https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-e-mails-and-documents-from-superoffice-crm-stopped-opening-with-microsoft-office-programs/)

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6144819-Fc3eqbB2BoyMCRx00e1Mjp2xaEpKX0DX4w5ut2X4UyLg1COh5X9mMcZOkkGeMUWP-0/image-20250325150447-2.png)

*Screenshot 1*

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6144821-58CSZktmuGsjYqzOASe8Bzsm90PBxpLeYSicw7N1jjNwDU7jU5dqcyIU531N2ElJ-0/image-20250325150532-3.png)

*Screenshot 2*

There are two possible ways to open the document, even though this issue has occurred:

1. [Opening, saving, and closing the document on another computer.](https://community.superoffice.com/en/support-faqs/faq/what-do-i-do-when-i-get-a-notification-that-another-person-is-editing-the-document-that-i-try-to-open-it-in-my-superoffice-crm/#1)
2. [Reverting the document to the last saved version.](https://community.superoffice.com/en/support-faqs/faq/what-do-i-do-when-i-get-a-notification-that-another-person-is-editing-the-document-that-i-try-to-open-it-in-my-superoffice-crm/#2)

**Opening, saving, and closing the document on another computer**

First of all, ask your colleague to reopen and close the document that you are trying to edit. This will ensure that the document is checked in (saved to) SuperOffice CRM, and other users will be able to open and work with it.

If this doesn’t help, please ask your colleague to follow the steps below:

1. Click on the Windows Tray and find the SuperOffice application. Right-click on the SuperOffice WebTools icon and click on **Tasks**.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6144822-prCrGFXnbSKFj85EZimwY2050ho5nkpcC5dRpQh23yKfgtcGF1JbutJciTbnKqGm-0/image-20250325150726-4.png)
2. If a user does not work with other documents in SuperOffice CRM, only the **Check Alarm** task should be visible. If there are more tasks in the list, select them and, by clicking the **Delete** button, delete them from the list.

   ![](https://online2.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/4393206-UQXn2HoKN4qdNothxoXkKqUcEfFEwQBwhR53FLWl0PjBuu8UtllQN2BfrH1HsCu8-0/image.png)

**Reverting the document to the last saved version**

**Note!** If you use this option, the last corrections of the document will be lost; therefore, we advise you to start by trying the first option.

To open the last saved version of the document, please follow the steps below:

1. In the **Activities** section tab, select the document and right-click on it. Click on the **Document** option in the drop-down menu that appears.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6144837-zSQXYBo6SgJw4hUuQBJ38yjiUdCrbbKbx1iODiBOITjFOK7Gjbp1xgotIQUxRcue-0/image-20250325151006-5.png)
2. Once the document screen opens, click on the **Task** button in the bottom-left corner and click on **Revert to saved version** in the menu that appears.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6469658-x4g1UAIUUkoI8GWoXqQmLTgIqsQFeqMoXEkcy6PuPpz8zjxAtSed5jRThqGeyX9x-0/image-20260105195130-1.png)

   Now you should be able to use the document again.

To ensure that documents are being checked-in (saved) properly, please make sure that everybody in the company has installed and configured [SuperOffice WebTools](https://community.superoffice.com/en/support-faqs/faq/how-do-i-download-and-install-web-tools-for-superoffice-crm/).

Also, in the WebTools Preference screen, you can select a **Suggest check-in when editing is complete** option, which will remind you to check in the documents.

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6144850-SIeLA93eaJa8NhYnR7aH0ubZGIeamjXzM34w7iPbgtILSkRsIqGYBQjbLB2cWndL-0/image-20250325151320-7.png)

**Note!** If you "unlocked" the document while your colleague was editing it and then saved a new version of the document before your colleague had a chance to save his change the different type of notification will pop up. It says: "*Another user has changed the file since you downloaded it*".

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6145013-JpI43q4t1q0bCkqIH7D0Unnydut0g9BAPUTUxPP21GLHmxquQTt7uceMtZrgccjX-0/image-20250325161637-8.png)

In this situation, your colleague can either click on:

- **Discard your changes.**This means that all the changes that he or she made will be discarded, and the document will have changes made by you.
- **Save changes anyway.**This means that all the changes that you made will be discarded, and the document will have changes made by your colleague.

**More information:**

Docs: [Check in/out documents](https://docs.superoffice.com/en/document/learn/lock.html)
