---
title: "What to do when I get an error \"Installation failed\" while installing SuperOffice WebTools or MailLink applications?"
url: https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-i-get-an-error-installation-failed-while-installing-superoffice-webtools-or-maillink-applications/
lang: en
updated: "5 Jun 2025"
---

# What to do when I get an error "Installation failed" while installing SuperOffice WebTools or MailLink applications?

Updated on 5 Jun 2025

I am installing SuperOffice WebTools and/or MailLink application, but the installation fails with the error: *Installation failed*. Why does it happen and how do I fix it?

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6213142-LKExxNA3tDHxZbrxLhy2tZArwt3010uUH8YdI3OfoS6L6zuQisgPzakqZSxuIRNb-0/image-20250520170312-6.png)

There could be several reasons why the installation fails. First of all, you want to get a more detailed error message and then depending on the error, fix the cause. To get a more detailed error message follow the steps below:

1. Start SuperOffice WebTools or MailLink installation again.
2. In the installation dialog click on the **Customize** button.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6213136-eGdLMLFgZOyUzzrNubKH8DPb5GwHg7WD96B057mhdicTorpBCb0x4QmfWYFtO5lM-0/image-20250520165803-2.png)
3. In the new dialog select **Advanced installation** and click **Install**.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6213138-kaZ5CetURhEENDl5gFRm8NTXDkL205RPQPx8nrydTOCbazK7UjhWpcS2yXYMG6WO-0/image-20250520165945-4.png)
4. Click **Next** and **Install**in the installation wizard until the installation finishes or you get an error message.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6213139-SocFhT1OkW3aLwbsyCSfWxwlkXlz05DmXIaRCAxKw3i0zpLxX0W3w2Gi4pzgN0KA-0/image-20250520170010-5.png)

Below find described most common situations and/or error messages:

- You get an error "*Installation Failed*" when you try to upgrade your WebTools after your SuperOffice installation has recently been upgraded/migrated (e.g. to 8.3 from 8.2 or similar).

  In this case, you need to uninstall WebTools and run the installer again.
- You get en error "*Installation Failed*" when a windows user that tries to install the SuperOffice application does not have *Write* permissions either in *Program Files* or *AppData* folders.

  In this case, make sure that the user has *Write* permissions on the folders that have been mentioned above.
- You get an error *1603 “Fatal Error During Installation”* when short file name creation is disabled on the target machine.

  In this case, make sure that the value *“NtfsDisable8dot3NameCreation”* is equal to 0, which indicates that short file name creation is enabled.

  ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6213143-xlsqkpIUL4Pil3Y98SmTqX9Ajxuf2zoqWABr86ldXLNt2Z8jskfb1mhcYIGye8XW-0/image-20250520170615-7.png)

  ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6213145-lmTTnKZ62m5j8LQ1eEtgATe7lpUNAybFfrbFlsWcFhZQs0F3ry23wsqTcbPuDq0s-0/image-20250520170659-9.png)

**More information:**

Technical Documentation: [Compatibility reports](https://docs.superoffice.com/en/onsite/compatibility/index.html)

FAQ: [What to do when I get an error "Installation failed" while installing SuperOffice Windows application?](https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-i-get-an-error-installation-failed-while-installing-superoffice-windows-application/)
