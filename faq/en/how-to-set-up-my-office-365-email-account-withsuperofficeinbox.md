---
title: "How to set up my Office 365 email account with SuperOffice Inbox?"
url: https://community.superoffice.com/en/support-faqs/faq/how-to-set-up-my-office-365-email-account-withsuperofficeinbox/
lang: en
updated: "14 Jul 2025"
---

# How to set up my Office 365 email account with SuperOffice Inbox?

Updated on 14 Jul 2025

How to set up my Office 365 email account with SuperOffice Inbox?

To set up your Office 365 account with SuperOffice Inbox follow the steps below:

[Step 1. Check that all prerequisites are met](https://community.superoffice.com/en/support-faqs/faq/how-to-set-up-my-office-365-email-account-withsuperofficeinbox/#1)

[Step 2.](https://community.superoffice.com/en/support-faqs/faq/how-to-set-up-my-office-365-email-account-withsuperofficeinbox/#2) [Set up SuperOffice as a preferred email client](https://online2.superoffice.com/Cust1990/CS/scripts/blogic.fcgi?_sf=0&action=doScreenDefinition&idString=viewFaq&entryId=113742&__formKeyId=46009193#2)

[Step 3. Enter your Office 365 server and email account information to connect it with SuperOffice Inbox](https://community.superoffice.com/en/support-faqs/faq/how-to-set-up-my-office-365-email-account-withsuperofficeinbox/#3)

​

**Step 1. Check that all prerequisites are met**

SuperOffice Inbox supports only the IMAP and SMTP protocols, so please ensure both are enabled for your email account. For setup instructions, check [this article for IMAP](https://learn.microsoft.com/en-au/troubleshoot/exchange/user-and-shared-mailboxes/pop3-imap-owa-activesync-office-365) and [this one for SMTP](https://learn.microsoft.com/en-us/exchange/clients-and-mobile-in-exchange-online/authenticated-client-smtp-submission).

​

**Step 2. ​Set up SuperOffice as a preferred email client**

When you log into SuperOffice CRM for the first time, the WebTools installation dialog appears. There you can select which email client should be the default one.

If you haven't selected that SuperOffice should be the default email client before, please follow these steps:

1. Click on ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6269136-qXyhnOSYd8fyeCx0WUalX1rSahbWRTMhgzLZt1fRn3OO34iP1YQsyqYFXfidwZUG-0/image-20250714141428-2.png) and from the drop-down menu select **Local settings**.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6269135-9Trb9ZLZPhCcr4Muy9xlaZ7b2aNsYMjn5SyYIU28eQFi6Q8g8PL2ryG2Z2EEKCzQ-0/image-20250714141340-1.png)
2. Make sure that *SuperOffice CRM*is selected in the **E-mail client** (1) field and then click **OK (2).**

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6269137-3J1Jz2UHhe2LrqgrohTz0PhkEgoO6O8BTQT1JDGlOQFCA4Hqj5HnWUeEF3HlKlHK-0/image-20250714141710-3.png)

​

**Step 3. ​Enter your Office 365 server and email account information to connect it with SuperOffice Inbox**

Click the **Inbox** (1) button in the navigator. Enter the **e-mail address** (2) you want to configure with SuperOffice Inbox, then click **Next** (3). SuperOffice will then try to find your email provider.

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6269306-Cy9BdJp71g9p776NWTmBiHHCbEWzHU2Od5CPMeGoHsct7PSh5wbUEH6fYCqwEWTN-0/image-20250714160814-8.png)

If SuperOffice recognizes the email provider, the server settings will be set up automatically and the inbox will load.

If SuperOffice does not recognize the e-mail provider, you then need to enter your **Password** (1) **or** you can click on **Sign in with Microsoft** button (2).

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6269310-NdebSPAgtP2iLs8FXxG4SwcWUCmGu9d00XEzx2jFqq7wJR2JulxI8KQpTj9wogxP-0/image-20250714161106-9.png)

If your email provider isn’t recognized, try logging in using the advanced settings - especially if all required settings are already in place.

To make sure your emails are imported to SuperOffice Inbox please fill in:

- **E-mail server:**outlook.office365.com:993​;
- **User name**: your full e-mail address;
- **Password:** your Office 365 account password;
- **​SSL:** On.

To make sure you can send out emails from SuperOffice Inbox please fill in:

- **Outgoing server name:** smtp.office365.com:587;
- **User name:** your full e-mail address;
- **Password:** your Office 365 account password;
- **SSL:** On​​​​​.

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6269304-3cMaH5GDTtq5SXAyIbKLssjjgxccIJ5f25ioSiL1IlFGfPEFo5GkQjJEbmC55cSb-0/image-20250714160257-7.png)
Then click on **Save.**

**Note!**

1. SuperOffice Inbox supports OAuth 2.0 authentication. After you enter your email address and click Next, you’ll be redirected to the Microsoft login page to sign in. Depending on how your organization has configured Office 365, a Global Administrator may need to approve the SuperOffice application. This step may not be required for all users.
2. SuperOffice automatically imports to the database all e-mails, which were created in the last 60 days. This can be changed in the web.config <Component> section <add key="NumberOfDaysToDownload"> line. If you work with SuperOffice Online, please contact SuperOffice support.

If you want to change your e-mail account, please follow the steps below:

1. Click on ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6269251-6sR0pIyHohmbrAUep9MRsXeTIfXpZf4yTaWdqR14i1ywH0qnbxd21GZl8uNwcQ5G-0/image-20250714150849-5.png) and then choose **E-mail options.**

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6269252-1pP1O9SEFXSibdIAcYCEcFoHpOIRDQ4rOfmTx0RNLpTEoISP6SohAtFKHcZAOXF9-0/image-20250714150915-6.png)
2. Select the **E-mail account** (1) tab, press the **Edit/remove**(2) button, and then **OK**(3)to finish.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6269317-lyEWXElWLGU1cfZKl2FMGHJOFIZCbhUdOD8gCxhX2kRLemruwq72CjyDEDee5lMz-0/image-20250714163208-10.png)

|  |
| --- |
| Please follow [this FAQ](https://community.superoffice.com/en/support-faqs/faq/how-do-i-set-up-the-superoffice-inbox-in-superoffice-8.5-and-earlier), if you use SuperOffice Onsite 8 or any previous version. |

**More information**

FAQ: [How do I start using the SuperOffice Inbox?](https://community.superoffice.com/en/support-faqs/faq/how-do-i-start-using-the-superoffice-inbox/)

Docs: [Set up SuperOffice Inbox](https://docs.superoffice.com/en/email/inbox/learn/setup.html)
