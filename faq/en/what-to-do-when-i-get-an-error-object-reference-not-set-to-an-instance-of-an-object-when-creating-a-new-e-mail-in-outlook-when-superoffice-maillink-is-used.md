---
title: "What to do when I get an error \"Object reference not set to an instance of an object\" when creating a new e-mail in Outlook when SuperOffice MailLink is used?"
url: https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-i-get-an-error-object-reference-not-set-to-an-instance-of-an-object-when-creating-a-new-e-mail-in-outlook-when-superoffice-maillink-is-used/
lang: en
updated: "8 Apr 2025"
---

# What to do when I get an error "Object reference not set to an instance of an object" when creating a new e-mail in Outlook when SuperOffice MailLink is used?

Updated on 8 Apr 2025

I am using MailLink and while clicking on the E-mail button in the toolbar, right-clicking on a contact record or clicking on an e-mail address I get an error:

*Object reference not set to an instance of an object*

The [MailLink log file](https://docs.superoffice.com/en/email/mail-link/debug.html) has an error:

*SuperOffice.Mail.ProtocolHandler.exe: MailProtocolHandler: Error handling Mail Link Web-request! - Error: Object reference not set to an instance of an object*

Why does it happen and how do I fix it?

This error indicates a problem with the Operating System settings or with the Microsoft Office application library. To fix it, please try the following:

1. Make sure that Microsoft Outlook is the default program on your PC to open emails with.

2. Make sure that the .eml file type is set to open with Microsoft Outlook.

If that did not help, the problem can be with the Microsoft Office application library.

3. Try to use the *Repair* function in Microsoft Office. Read a Microsoft article [Repair an Office application](https://support.microsoft.com/en-us/office/repair-an-office-application-7821d4b6-7c1d-4205-aa0e-a6b40c5bb88b?ui=en-us&rs=en-us&ad=us) to learn more about it.

4. If Office repair did not help, please try to reinstall the Microsoft Office application.

If this did not help to solve your problem, please contact SuperOffice support by raising a support request from inside SuperOffice via Help -> Support.

**More information**

FAQ: [What can I do when I run into the problems with archiving e-mails from Outlook to SuperOffice CRM?](https://community.superoffice.com/en/support-faqs/faq/what-can-i-do-when-i-run-into-the-problems-with-archiving-e-mails-from-outlook-to-superoffice-crm/)

FAQ: [What can I do when I run into the problems with SuperOffice WebTools?](https://community.superoffice.com/en/support-faqs/faq/what-can-i-do-when-i-run-into-the-problems-with-superoffice-webtools/)
