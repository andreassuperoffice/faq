---
title: "What to do when I get an error \"Installation failed\" while installing SuperOffice Windows application?"
url: https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-i-get-an-error-installation-failed-while-installing-superoffice-windows-application/
lang: en
updated: "19 Mar 2026"
---

# What to do when I get an error "Installation failed" while installing SuperOffice Windows application?

Updated on 19 Mar 2026

I am trying to install the SuperOffice Windows application, but the installation fails. Why does it happen, and how do I fix it?

![](https://online2.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/3229050-kwN9OC8dmzogf7OUwHqBh3BtoxLZIpWekCIWcjEFf5MNsMsJ8ZGG3nYLwQkLFJZq-0/image.png)

Installation can fail due to various reasons. First of all, you want to get a more detailed error message and then, depending on the error, fix the cause.

To get a more detailed error message, follow the steps below:

1. Start the SuperOffice Windows application installation again.
2. In the installation dialog, click on the **Customize**button.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6593691-SjR3yb9jufPSPGLPnXY92RqhbALtH68GdPOeRjhGGDagPY4H7KI5omSgPKQpKLyb-0/image-20260319073914-1.png)
3. In the new dialog, select **Advanced installation** and click **Install**.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6593692-epNXqpEWEgYy1IbhZa9oILzcWdIBna7kBlxmtp9iZR4wgrqY5whayjpoyBIf5t9E-0/image-20260319074013-2.png)
4. Click **Next**and**Install**in the installation wizard until the installation finishes or you get an error message.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6593693-M2YZ7q9O7WrTkM2h0HZFhMNx11ecB08hoxdsEHEkzY5YfNHZ0pmGDsRNCD1zzrFc-0/image-20260319074231-3.png)

Below are described the most common situations and/or error messages:

- You get an error "*Installation Failed*" when a Windows user who tries to install the SuperOffice application does not have write permissions in either the *Program Files* or *AppData* folders.

  In this case, make sure that the user has Write permissions in these locations.
- You get an error "*Installation Failed*" when one or more prerequisites are not present, or SuperOffice fails to install them. For example: *Error: The installation of Microsoft .Net Framework has failed. Setup will now exit.*

  ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6593694-dDeZC7WJFn34QQMjBdj5YEQCIdAKGL4aU59H0PosyPsbmjR1iCt8c4lmGIGtWcd3-0/image-20260319074437-4.png)

  In this case, make sure that the computer has all prerequisites installed. [This article](https://docs.superoffice.com/onsite/requirements/web-client.html) covers all the requirements for the SuperOffice Windows client.
- You get an error "*Installation Failed*" when the *.mst* file is not accessible or is corrupted.

  ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6593695-nu9oH3qRspGnHwPhXrlr0EqrlcZU2nz9AZD6Lyq0xHO8aq1RO9Y16MOSKoc7Xl0H-0/image-20260319074531-5.png)

  In this case, make sure that the *.mst* file is present and not corrupted.
- You get an error *"Error applying transforms. Verify that the specified transform paths are valid."* when the Windows Registry has a TRANSFORMSSECURE key missing.

  In this case, make sure that TRANSFORMSSECURE = dword:00000000 is present in the Windows Registry.

  HKEY\_LOCAL\_MACHINE\SOFTWARE\Policies\Microsoft\windows\Installer  add the dword value: "TRANSFORMSSECURE"=dword:00000000

  ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6593700-l4HbgeY5qjlfOOxGZ45MmmYwUjgbJfm2RjPZsxwDbexF5k0O1cuJRTu5lNdyEypE-0/image-20260319074909-6.png)

  **Note!** You might need to create all keys manually if they are not present yet.

**More information**

Technical Documentation: [Compatibility reports SuperOffice](https://docs.superoffice.com/onsite/compatibility/index.html)

FAQ: [What to do when I get an error "Installation failed" while installing SuperOffice Web Tools or Mail Link applications?](https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-i-get-an-error-installation-failed-while-installing-superoffice-webtools-or-maillink-applications/)
