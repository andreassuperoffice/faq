---
title: "What to do when I get an error \"You need to select an item first\" when archiving an e-mail from Outlook to SuperOffice CRM?"
url: https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-i-get-an-error-you-need-to-select-an-item-first-when-archiving-an-e-mail-from-outlook-to-superoffice-crm/
lang: en
updated: "12 Jun 2025"
---

# What to do when I get an error "You need to select an item first" when archiving an e-mail from Outlook to SuperOffice CRM?

Updated on 12 Jun 2025

When I am archiving an email I get a notification:

*"You need to select an item first".*

In the [MailLink log file](https://docs.superoffice.com/en/email/mail-link/debug.html) I see one of these errors:

*Error: Unable to cast COM object of type 'Microsoft.Office.Interop.Outlook.ExplorerClass' to interface type 'Microsoft.Office.Interop.Outlook.\_Explorer'. This operation failed because the QueryInterface call on the COM component for the interface with IID '{00063003-0000-0000-C000-000000000046}' failed due to the following error: Interfaz no compatible (Exception from HRESULT: 0x80004002 (E\_NOINTERFACE))*

*Internal error. Unable to cast COM object of type 'Microsoft.Office.Interop.Outlook.ApplicationClass' to interface type 'Microsoft.Office.Interop.Outlook.\_Application'. This operation failed because the QueryInterface call on the COM component for the interface with IID '{00063001-0000-0000-C000-000000000046}' failed due to the following error: Library not registered. (Exception from HRESULT: 0x8002801D (TYPE\_E\_LIBNOTREGISTERED)).*

Why does it happen and how do I fix it?

The error can occur when:

- SuperOffice MailLink detects old registry key values from the old Outlook installations in the Windows Registry.
- Different versions of different MS Office programs are running on the same computer. For example MS project 2013 while other Office programs are 2016.

There are three known ways how to solve the problem:

1. [Correct Windows registry](https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-i-get-an-error-you-need-to-select-an-item-first-when-archiving-an-e-mail-from-outlook-to-superoffice-crm/#1)
2. [Run Microsoft Office repair](https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-i-get-an-error-you-need-to-select-an-item-first-when-archiving-an-e-mail-from-outlook-to-superoffice-crm/#2)
3. [Reinstall Microsoft Office](https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-i-get-an-error-you-need-to-select-an-item-first-when-archiving-an-e-mail-from-outlook-to-superoffice-crm/#3)

**Correct Windows registry**

To solve the problem delete registry values, which point to old Outlook installations. To do it please follow the steps below:

Step 1. Fix the Interface keys

1. In the Windows Registry Editor navigate to:

   *HKEY\_CLASSES\_ROOT\Interface\{00063001-0000-0000-C000-000000000046}\TypeLib*

   **Note!**If your computer is 32 bit you will find the registry key for the interface in a different location: *HKEY\_CLASSES\_ROOT\Wow6432Node\Interface\*
2. Find a '**(Default)**' entry with the value *'{00062FFF-0000-0000-C000-000000000046}'*
3. Make sure that '**Version**' entry matches the value of the Outlook version that is **currently** installed. If not include the correct version and delete incorrect.

Step 2. Fix the TypeLib keys

1. In Windows Registry Editor and navigate to:

   *HKEY\_CLASSES\_ROOT\TypeLib\{00062FFF-0000-0000-C000-000000000046}*

   **Note!**If your computer is 32 bit you will find the registry key for the interface in a different location: *HKEY\_CLASSES\_ROOT\Wow6432Node\TypeLib\*

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6237207-09HDBnYL3MBDM5NbX7SywBwyoUYWHEYWACUhB1QGxhzZO6pmsWPROWElxN9LZMLu-0/image-20250612134822-1.png)
2. Make sure that the '**Version**' entry matches the value of the Outlook version that is **currently** installed. If not include the correct version and delete incorrect.

   **Note!** Do not delete the entry for the version that was configured in first step.

These are the Outlook versions:

- Outlook 2000 - 9.0
- Outlook 2002 - 9.1
- Outlook 2003 - 9.2
- Outlook 2007 - 9.3
- Outlook 2010 - 9.4
- Outlook 2013 - 9.5
- Outlook 2016 - 9.6

**Note!** Incorrectly editing a registry can permanently damage your computer or server (if you work on Citrix/Terminal Server), so do not delete or adjust any key if you don't know specifically why you do it. We recommend to back up Windows registry before making any change. You can find instructions how to do it in [this article](https://neosmart.net/wiki/backup-restore-registry/).

**Run Microsoft Office repair**

Please check this Microsoft [support article](https://support.microsoft.com/en-us/office/repair-an-office-application-7821d4b6-7c1d-4205-aa0e-a6b40c5bb88b?ui=en-us&rs=en-us&ad=us) to get instructions how to do it.

**Reinstall Microsoft Office**

Please check this Microsoft [support article](https://support.microsoft.com/en-us/office/repair-an-office-application-7821d4b6-7c1d-4205-aa0e-a6b40c5bb88b?ui=en-us&rs=en-us&ad=us) to get instructions how to do it.

**More information**

Forum: [MailLink error/message 'You need to select an item first'](https://community.superoffice.com/en/technical/forums/product-forums/crm-windows-application/maillink-errormessage-you-need-to-select-an-item-first/)
