---
title: "What to do when I get an error \"Unable to cast COM object....\" when opening an e-mail from SuperOffice CRM?"
url: https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-i-get-an-error-unable-to-cast-com-object....-when-opening-an-e-mail-from-superoffice-crm/
lang: en
updated: "19 Mar 2026"
---

# What to do when I get an error "Unable to cast COM object...." when opening an e-mail from SuperOffice CRM?

Updated on 19 Mar 2026

I get an error after trying to open an e-mail from SuperOffice or clicking on the E-mail button. The error message is:

*Unable to cast COM object of type 'Microsoft.Office.Interop.Outlook.ApplicationClass' to interface type 'Microsoft.Office.Interop.Outlook\_Application'. This operation failed because the QueryInterface call on the COM component for the Interface with IIF '{00063001-0000-0000-C000-000000000046}' failed due to the following error: Error loading type library/DLL. (Exception from HRESULT: 0x80029C4A (TYPE\_E\_CANTLOADLIBRARY)).*

The error in the MailLink log file:

*SuperOffice.Mail.ProtocolHandler.exe: MailProtocolHandler: Error handling Mail Link Web-request! - Error: Unable to cast COM object of type 'Microsoft.Office.Interop.Outlook.ApplicationClass' to interface type 'Microsoft.Office.Interop.Outlook.\_Application'. This operation failed because the QueryInterface call on the COM component for the interface with IID '{00063001-0000-0000-C000-000000000046}' failed due to the following error: Error loading type library/DLL. (Exception from HRESULT: 0x80029C4A (TYPE\_E\_CANTLOADLIBRARY)).*

Why does it happen, and how do I fix it?

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6593703-ELf3tcHx4JXRff7cLbshLnnhteoDCnz2KWPaRMOGON2AakrI96dpN0zj0FEqNQA7-0/image-20260319080804-1.png)

This error indicates a problem with the Microsoft Office library. To fix it, please try the following steps:

1. Try to use the *Repair* function in Microsoft Office. Please read the Microsoft article [Repair an Office application](https://support.microsoft.com/en-us/office/repair-an-office-application-7821d4b6-7c1d-4205-aa0e-a6b40c5bb88b) to learn more about it.
2. If Office repair did not help, please try to reinstall the Microsoft Office application.

**More information**

FAQ: [What can I do when I run into the problems with archiving e-mails from Outlook to SuperOffice CRM?](https://community.superoffice.com/en/support-faqs/faq/what-can-i-do-when-i-run-into-the-problems-with-archiving-e-mails-from-outlook-to-superoffice-crm/)

FAQ: [What can I do when I run into the problems with SuperOffice WebTools?](https://community.superoffice.com/en/support-faqs/faq/what-can-i-do-when-i-run-into-the-problems-with-superoffice-webtools/)
