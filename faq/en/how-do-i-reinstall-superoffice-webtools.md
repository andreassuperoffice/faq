---
title: "How do I reinstall SuperOffice WebTools?"
url: https://community.superoffice.com/en/support-faqs/faq/how-do-i-reinstall-superoffice-webtools/
lang: en
updated: "24 Jul 2026"
---

# How do I reinstall SuperOffice WebTools?

Updated on 24 Jul 2026

I have been recommended to reinstall SuperOffice WebTools. How do I do it?

Before you start, check which part of SuperOffice WebTools you need to reinstall.

Use this FAQ if documents from SuperOffice CRM do not open, edit, or save correctly. This FAQ explains how to reinstall the SuperOffice WebTools component used for document handling on Windows and Mac.

Please be aware and only uninstall the program you intend to reinstall. Do not uninstall MailLink as part of this process unless this has been specifically recommended by your IT department or SuperOffice Support.

Please follow the steps below to reinstall SuperOffice WebTools:

- If you use SuperOffice WebTools on the Windows operating system, please follow the instructions in [this section](https://community.superoffice.com/en/support-faqs/faq/how-do-i-reinstall-superoffice-webtools/#1)
- If you use SuperOffice WebTools on the Mac operating system, please follow the instructions in [this section](https://community.superoffice.com/en/support-faqs/faq/how-do-i-reinstall-superoffice-webtools/#2)

​

**Reinstall SuperOffice WebTools on the Windows operating system**

1. Close your SuperOffice CRM.
2. You need to uninstall the existing components related to **WebTools**. To do this, open the list of installed applications on your computer. You can access it in two ways - through **Apps & Features** or **Programs and Features**. Check [this article](https://support.microsoft.com/en-us/help/4028054/windows-10-repair-or-remove-programs) for further instructions on how to find both **Apps & Features** and **Programs and Features**.

   In this guide, we’ll use **Programs and Features**.
3. In the list of programs, find **SuperOffice Web Extensions**(1), select it, and click on the **Uninstall**(2) button.

   ![](https://app.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6793198-nKfa2IPtB2d9kq65mOTI7nKA878J6keoekLbrhZosTdULREi6j6qneKku6q0Sagd-0/image-20260724072025-5.png)
4. To make sure that all WebTools settings are reset after reinstall, delete the **TrayApp** (2) folder in **AppData Roaming** (1) and the **SuperOffice 7 Web Extensions** (4) folder in **AppData Local** folder (3).

   ![](https://app.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6793197-snQrqpdAKSOw47TA6ESoJLhKui1K79P0mpf22e5XkIzjjzZNNHD1x61pU8Er5weW-0/image-20260724072011-4.png)

   ![](https://app.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6793196-D42HlODife4w9UtwUUMRqKsfdd838SI1mRbDyIXb4QqIgqJAIG4Kl1Tw7tfaix3F-0/image-20260724071952-3.png)
5. Please follow [this FAQ](https://community.superoffice.com/en/support-faqs/faq/how-do-i-download-and-install-webtools-for-superoffice-crm/) to install WebTools.

**Note!**

This FAQ explains how to reinstall SuperOffice Web Extensions.

In rare cases, Windows users may be asked to reinstall MailLink. This should only be done if it has been specifically recommended by your IT department or SuperOffice Support.

If you need to reinstall MailLink, you should delete SuperOffice MailLink from the Programs and Features and also the MailLink folder from the AppData Roaming folder. Then youcan download and install it separately from the [SuperOffice Download Service](https://downloadservice.superoffice.com/).

For more information, read the FAQ: [Why is MailLink not installed when I download WebTools?](https://community.superoffice.com/en/support-faqs/faq/why-is-maillink-not-installed-when-i-download-webtools/)

​

**Reinstall SuperOffice WebTools on the Mac operating system**

1. Close your SuperOffice CRM and WebTools applications. To close WebTools, right-click on the SuperOffice icon in the tray and click **Quit**.

   ![](https://app.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6793195-WCIPOdHP5E9jmbpIRneNE7SZRb9LOO07TZOZtAo3RarGKq07ecyrLgYmcp5EM4DH-0/image-20260724071934-2.png)
2. Open Finder and select Applications
3. Find all the files with the **SuperOffice WebTools** name. Right-click on them and click**Move to Bin****.**

   ![](https://app.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6793194-n13rKFNJUrWOBp0KGHgulRFp7cFqDfLMzm1hdfxxgsZGeyLxyKw64hcnyOD9tMBO-0/image-20260724071843-1.png)
4. Please follow [this FAQ](https://community.superoffice.com/en/support-faqs/faq/how-do-i-download-and-install-webtools-for-superoffice-crm/) to install WebTools.

**Note!** ​If you have been recommended to install the latest version of WebTools, download it from the [SuperOffice Download Service](https://downloadservice.superoffice.com/) page.

**More information**

FAQ:[What to do when I get an error "Installation failed" while installing SuperOffice WebTools or MailLink applications?](https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-i-get-an-error-installation-failed-while-installing-superoffice-webtools-or-maillink-applications/)
