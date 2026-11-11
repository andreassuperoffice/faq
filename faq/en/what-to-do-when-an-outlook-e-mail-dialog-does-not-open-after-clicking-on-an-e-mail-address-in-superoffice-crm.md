---
title: "What to do when an Outlook e-mail dialog does not open after clicking on an e-mail address in SuperOffice CRM?"
url: https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-an-outlook-e-mail-dialog-does-not-open-after-clicking-on-an-e-mail-address-in-superoffice-crm/
lang: en
updated: "26 May 2025"
---

# What to do when an Outlook e-mail dialog does not open after clicking on an e-mail address in SuperOffice CRM?

Updated on 26 May 2025

I want to send a new e-mail using the Outlook application and clicking on the e-mail address in SuperOffice. Now when I click on any e-mail address (1) I get a pop-up that I need to log on to an e-mail server. When I right-click on a contact and choose the Send an e-mail (2) option it is greyed out. Why does it happen and how do I fix it?

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6219723-sZIqJNm4GR30d5HeGsJ6pYNcFXMMo6eI4xdQtZLi3yDegGMIzZ7hlor0wYRr3uLA-0/image-20250526152310-2.png)

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6219725-BnZeZT2wtsZrmQz4fX9XeSwMA07n5nes3a0t44wmX4KQ9QwmLPj72wc4cbzaWUIt-0/image-20250526152338-3.png)

There are four known situations when the problem occurs:

- [When SuperOffice WebTools are not installed or connected](https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-an-outlook-e-mail-dialog-does-not-open-after-clicking-on-an-e-mail-address-in-superoffice-crm/#1.1)
- [When the Outlook desktop app is installed and SuperOffice MailLink tries to use it](https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-an-outlook-e-mail-dialog-does-not-open-after-clicking-on-an-e-mail-address-in-superoffice-crm/#1)
- [When the Windows registry’s reference to SuperOffice.Mail.ProtocolHandler.exe file is corrupted](https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-an-outlook-e-mail-dialog-does-not-open-after-clicking-on-an-e-mail-address-in-superoffice-crm/#2)
- [When there is a mismatch between MS Office Bitness value in the Windows registry and version, installed on the computer](https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-an-outlook-e-mail-dialog-does-not-open-after-clicking-on-an-e-mail-address-in-superoffice-crm/#3)
- [When an antivirus program on a computer has a script- blocking setting enabled](https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-an-outlook-e-mail-dialog-does-not-open-after-clicking-on-an-e-mail-address-in-superoffice-crm/#4)

​

**When SuperOffice WebTools are not installed or connected**

In this situation you need to install or reconfigure SuperOffice WebTools. Please check these FAQs for the instructions on how to do it:

FAQ: [How do I download and install WebTools for SuperOffice CRM?](https://community.superoffice.com/en/support-faqs/faq/how-do-i-download-and-install-webtools-for-superoffice-crm/)

FAQ: [What to do when e-mails and documents from SuperOffice CRM stopped opening with Microsoft Office programs?](https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-e-mails-and-documents-from-superoffice-crm-stopped-opening-with-microsoft-office-programs/)

​

**When the Outlook desktop app is installed and SuperOffice MailLink tries to use it**

In this situation you are able to archive e-mails from Outlook, but when you try to create a new e-mail by clicking on a contact's e-mail address or use the E-mail button on the Toolbar -– the dialog does not get populated, you see only “*Performing tasks..*.” notification in the right corner of the screen. Please read [this FAQ](https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-i-get-an-error-superoffice-mail-link-was-unable-to-connect-to-the-outlook-process-when-i-try-to-create-a-new-email-or-open-an-outlook-by-pressing-the-inbox-button-in-superoffice-crm/) for further details on troubleshooting and fix.

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6219761-NUL5h9GdpE1Jh6QIFZ3tSumYwOfLDL5Mc2nKu3tB3YunSpwB3KU4nnQg9xsk0KbI-0/image-20250526154552-4.png)

​

**When the Windows registry’s reference to *SuperOffice.Mail.ProtocolHandler.exe* file is corrupted**

In this situation we suggest to:

1. Make sure that *SuperOffice.Mail.ProtocolHandler.exe* exists in the installation folder.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6210316-CZc0fiZFeEOpAUA2komXLTW615mTgGayGQ3RJoPUfPMTMtGOK8DtACIl4Mmpspcp-0/image-20250519123024-4.png)
2. Check if the path to the *SuperOffice.Mail.ProtocolHandler.exe* file in Windows Registry is correct and not corrupted.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6219944-4OZG7ijzJwDbXCNrjGILm8fPinDpgmqfujKuQlG4Zh4F7h1LNRwwRdzkFbBwkx1W-0/image-20250526162732-5.png)

​

**When there is a mismatch between MS Office Bitness value in the Windows registry and version, installed on the computer**

In this situation we suggest to read [this FAQ](https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-i-get-an-error-creating-an-instance-of-the-com-component-with-clsid...-when-opening-an-e-mail-from-superoffice-crm) to learn how to troubleshoot it.

​

**When an antivirus program on a computer has a script-blocking setting enabled**

If your antivirus blocks scripts, it will prevent SuperOffice Outlook MailLink to creates a new 'Outlook.application object'.

To make sure if this is the problem in your case, you can get a script to run a test (please [contact SuperOffice Support](https://cs.superoffice.com/) to get it). If you get a success message, the script blocking is not enabled. If you get another message, this indicates that script blocking could be a problem. In this case, we suggest:

1. Make sure Script-blocking registry does not exist in the Outlook Application root in the Windows registry. If it exists, please delete it.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6219946-Ip7rQs7ER4f4BfoqkfSP7qqckzc15Cwdlkr05Da9qBWFUYslNxLdluY4yO0HhAh6-0/image-20250526163106-6.png)
2. Check if files *ScrBlock.dll* and *scrauth.dll* exist on your computer. You can disable them by renaming files.
