---
title: "What to do when I get an error „Failed to save document“ when archiving an e-mail to SuperOffice CRM?"
url: https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-i-get-an-error-failed-to-save-document-when-archiving-an-e-mail-to-superoffice-crm/
lang: en
updated: "28 May 2025"
---

# What to do when I get an error „Failed to save document“ when archiving an e-mail to SuperOffice CRM?

Updated on 28 May 2025

I am archiving an email from Outlook to SuperOffice CRM and I get an error message:

*Failed to save document*

Why does it happen and how do I fix it?

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6222115-8MquALucOpYrTwFI2iNfdO1ME8x0tgs4QBbcR648MmzHEWs9p1X6oQhoK0KdR4FK-0/image-20250528102429-1.png)

There are 6 known situations when this error can occur:

- [When a user does not have Data rights to create documents](https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-i-get-an-error-failed-to-save-document-when-archiving-an-e-mail-to-superoffice-crm/#1)
- [When a user does not have access to the template which is used when archiving](https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-i-get-an-error-failed-to-save-document-when-archiving-an-e-mail-to-superoffice-crm/#2)
- [(Onsite Only) When an impersonate user in SuperOffice CRM product configuration does not have edit rights to document archive](https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-i-get-an-error-failed-to-save-document-when-archiving-an-e-mail-to-superoffice-crm/#3)
- [(Onsite only) When the SuperOffice configuration has restrictions on archived file size](https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-i-get-an-error-failed-to-save-document-when-archiving-an-e-mail-to-superoffice-crm/#4)
- [When the terminal server configuration allows opening virtual desktop on the different machine](https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-i-get-an-error-failed-to-save-document-when-archiving-an-e-mail-to-superoffice-crm/#5)
- [When the SuperOffice Mail Link version is old](https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-i-get-an-error-failed-to-save-document-when-archiving-an-e-mail-to-superoffice-crm/#6)

**A user does not have Data rights to create documents**

Itmight be that a user who tries to archive an email does not have sufficient data rights to create documents in SuperOffice CRM.

Please follow the steps below to see if that is the case:

1. Log in to [Settings and maintenance.](https://community.superoffice.com/en/support-faqs/faq/how-do-i-access-administration-part-settings--maintenance-in-superoffice-crm/)
2. Click on **Roles** (1), and select the role(2) that the user has.
3. Make sure that in the **Document** line in **My own** column create, update or delete is selected.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6222122-niuLYXOxwfieA1Xt84FKR4p5uEheBFoEpJrWUXdcUmtnBDu4hgx3AHDiZxpSMBkR-0/image-20250528102945-2.png)

**A user does not have access to the template which is used when archiving**

Please follow the steps below to see if this is the case:

1. Log in to [Settings and maintenance.](https://community.superoffice.com/en/support-faqs/faq/how-do-i-access-administration-part-settings--maintenance-in-superoffice-crm/)

2. Click on the **Lists**(1) item, then choose the**Email template** (2) from the drop-down menu and select the that is used for archiving (3). Make sure that the user group (4) of the user who gets an error is selected (has access).

​![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6222123-n4SFqRjWmcZiF7FxA5eWWPe4T1RT3JSjqF0crsrhxl1i1g6Rq7dCMxCqgkrEaxIx-0/image-20250528103233-3.png)

**Note!** The template that is used to archive e-mails is selected in the archiving dialog in Type field.

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6222129-KAnen1ijmG6DWC78qJnlcAjCmPqU5R0BGm6PIPDjD3ExDOqGThHPLQs231qbTF3I-0/image-20250528103440-4.png)

**(Onsite only) An impersonate user in SuperOffice CRM product configuration does not have edit rights to document archive**

Please follow the steps below to see if this is the case:

1. Open the SuperOffice web (or NetServer if it is installed separately) product configuration app, which can be found in the SuperOffice server.
2. Navigate to the chapter called **Document archive (1)** and confirm that **Impersonate User details are filled it.**
3. If the details are filled in click on the **Validate (2)**button. That should generate a notification of successful user authentication (3).

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6222130-zHJTHeWEYZaZ49ekzTrDMR1xbWQxZrmRxYYRH30Wx6pkD5wdJcDC9gFSiaAMke6U-0/image-20250528103533-5.png)

**(Onsite only) The SuperOffice configuration has restrictions on archived file size**

All SuperOffice installations have a limit for the archived attachment size. It can be changed in the SuperOffice configuration file. Please follow the steps below to do it:

1. Find and open the *SuperOffice.config* file. Please read [this article](https://docs.superoffice.com/en/onsite/install/win-client/superoffice-config.html) to learn where to find it.
2. Go to the section *<Documents>* and change the value in this section:

*<!-- Size of internal buffer in KB -->*

*<add key="BufferSize" value="**3000**">*

**The terminal server configuration allows opening virtual desktop on the different machine**

In Terminal Server environment it is possible to have situation when a user logs in from the different physical/virtual machines. SuperOffice Mail Link component is using some encrypted keys that are generated with information about the machine (where the program is being executed on).

Please follow the steps below to fix the problem:

1. Please find the *default.site* and *netserver.config* files in SuperOffice Mail Link installation.
2. Rename these files with the extension *\_old.*
3. Reconfigure Mail Link manually for this user, please follow instructions on [this FAQ](https://community.superoffice.com/en/support-faqs/faq/how-do-i-configure-superoffice-maillink-for-outlook-manually/).
4. If issue was solved you can delete the old files, because new ones should be created.

**The SuperOffice Mail Link version is old**

If in the SuperOffice Mail Link log file you can detect the error message pointing to *SuperOfficeMailLink.Streams* folder, your SuperOffice Mail Link has a known bug.

There are two known solutions in this situation:

1. Upgrade the SuperOffice to the latest version, check [this FAQ](https://community.superoffice.com/en/support-faqs/faq/how-do-i-upgrade-superoffice-crm-to-the-latest-version/) for more information about this.
2. Upgrade Web Tools (Mail link) to the version without the bug. To get an installer, please [contact SuperOffice support](https://community.superoffice.com/en/support-faqs/faq/how-do-i-register-a-support-request-from-within-superoffice-crm/).

If you get this error message while you are using SuperOffice CRM in Travel mode there is a chance that you SuperOffice Mail Link experience another known bug.

Upgrade the SuperOffice to the latest version, please check [this FAQ](https://community.superoffice.com/en/support-faqs/faq/how-do-i-upgrade-superoffice-crm-to-the-latest-version/) for more information about this.

**More information**

FAQ:[What to do when I get an error "Failed to communicate with server" from SuperOffice Mail Link?](https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-i-get-an-error-failed-to-communicate-with-server-from-superoffice-mail-link/)
