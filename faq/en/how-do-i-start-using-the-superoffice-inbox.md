---
title: "How do I start using the SuperOffice Inbox?"
url: https://community.superoffice.com/en/support-faqs/faq/how-do-i-start-using-the-superoffice-inbox/
lang: en
updated: "8 Jan 2026"
---

# How do I start using the SuperOffice Inbox?

Updated on 8 Jan 2026

How do I start using the SuperOffice Inbox?

To start using SuperOffice Inbox for reading, sending and archiving emails directly from SuperOffice CRM, please follow the steps below:

[Step 1. Confirm that your e-mail account has met prerequisites](https://community.superoffice.com/en/support-faqs/faq/how-do-i-start-using-the-superoffice-inbox/#1)

[Step 2. Set up SuperOffice as preferred email client](https://community.superoffice.com/en/support-faqs/faq/how-do-i-start-using-the-superoffice-inbox/#2)

[Step 3. Configure SuperOffice Inbox with your email account details](https://community.superoffice.com/en/support-faqs/faq/how-do-i-start-using-the-superoffice-inbox/#3)

​

**Step 1. Confirm that your e-mail account has met prerequisites**

SuperOffice Inbox supports only the IMAP and SMTP protocols, so please make sure both are enabled for your email account. If you're using Office 365, refer to the following FAQs: [this article for IMAP](http://learn.microsoft.com/en-au/troubleshoot/exchange/user-and-shared-mailboxes/pop3-imap-owa-activesync-office-365) and [this article for SMTP](http://learn.microsoft.com/en-us/exchange/clients-and-mobile-in-exchange-online/authenticated-client-smtp-submission).

Please check [this article](https://docs.superoffice.com/en/online/system-requirements.html) for other SuperOffice requirements.

**Note!** Gmail now requires app passwords for third-party apps instead of your regular password. See [this FAQ](https://community.superoffice.com/en/support-faqs/faq/how-do-i-generate-a-googleapp-password-to-use-2-step-verification-with-superoffice-inbox/). From January 2025, IMAP will be permanently enabled for all Gmail accounts, so no action is needed regarding IMAP settings.

​

**Step 2. Set up SuperOffice as preferred email client**

When you log into SuperOffice CRM for the first time, the WebTools installation dialog appears. There you can select which email client should be the default one.

If you haven't selected that SuperOffice should be the default email client before, please follow these steps:

1. Click on ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6149227-HPZANxNnbF03KiWKirpIzMkD3yO3wnKZ6awMyFdE1NunOQmolcoRCt3sTNo0MeI0-0/image-20250327153351-1.png) and from the drop-down menu select **Local settings**.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6149228-YQkmFmgC2N88T715KjdWzOtTZijMEuhRFOE9h6PmmLdfwjOdPTbfC6ShFr5om9R6-0/image-20250327153436-2.png)
2. Make sure that *SuperOffice CRM*is selected in the **E-mail client** (1) field and then click **OK (2).**

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6149232-DxZI8UeWGEa3w7pMKEwpaSU8NaHSqgxqiIykXeXT4obWxfCWJcXECrgwDG8RzEW1-0/image-20250327153556-3.png)

​

**Step 3. Configure SuperOffice Inbox with your email account's details**

Click the **Inbox** (1) button in the navigator. Enter the login for the **e-mail address** (2) you want to configure with the SuperOffice Inbox and click **Next**(3).

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6149238-roRcoEP1dqU6CUnegSo8zPsIoqkRiK8zoXyk1YuAhgHiqMCBGc1yuziZGipmacXp-0/image-20250327153744-4.png)

You will then need to enter your **Password** (1) and click **Log in** (2).

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6149248-bURE5AyYs0lrfHnboZZW3OrAlhlsi6ITreFDa5YeQNcaWtLlb8bsDtYnk2k92stm-0/image-20250327154013-5.png)

If SuperOffice recognizes the e-mail provider, the server settings will be set up automatically and the inbox will load. If not, the more settings screen will be displayed and you must fill in the required fields.

To make sure your emails are imported to SuperOffice Inbox please fill in:

- **Incoming e-mail server:**yourIMAP server details;
- **User name**: your user name, which is most of the time your full e-mail address;
- **Password:** your e-mail account password;
- **SSL:** depending on your e-mail provider's settings it can be on or off.

To make sure you can send out emails from SuperOffice Inbox please fill in:

- **Outgoing e-mail server:**your SMTP server details;
- **User name:** your user name, which is most of the time your full e-mail address;
- **Password:**  your e-mail account password;
- **SSL:** depending on your e-mail provider's settings it can be on or off.

Then click on **Save.**

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6149267-0dtElaC1xqizGWOhoh4TxnFgH7E6PecJHDkcA4w1XI8fjE1wSeMR37syrHD974jy-0/image-20250327154409-6.png)

**Note!**

1. If you work on SuperOffice Onsite and the port has to be specified to access the e-mail server, please use a colon ":" after the email server name E.g.: "my.mail.server:80".
2. SuperOffice automatically imports to database all e-mails, which were created in the last 30 days if you work on SuperOffice Online and last 180 days if you work on SuperOffice Onsite. This can be changed in the web.config <Component> section <add key="NumberOfDaysToDownload"> line. If you work with SuperOffice Online, please [contact SuperOffice support](https://community.superoffice.com/en/support-faqs/faq/how-do-i-register-a-support-request-from-within-superoffice-crm/).

If you want to change your e-mail account, please follow the steps below:

1. Click on ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6149279-QFjr0CpM1anqnYd8cOdxDeKAJCb9FJlslch51YHNemAsxJEbu6uwDuk1P4W9syzH-0/image-20250327154847-8.png) and then choose **E-mail options.**

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6149278-y3K9YoxTgPCOBPi0kOMKh1AQI8xt7pbBt1IgFOMLfpLlpBn7wtm19tXdH9YuQw09-0/image-20250327154841-7.png)
2. Select **E-mail account** (1) tab, press **Edit/remove** (2) button and then **OK** (3)to finish.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6149281-xxWwhXKzlyqFPi29dkdiBwSWLSJqGaoqti8J3qYxgfY9ng6SGbKEk2SQKhclqHjo-0/image-20250327154924-9.png)

**More information**

FAQ: [How to set up my Office 365 email account with SuperOffice Inbox?](https://community.superoffice.com/en/support-faqs/faq/how-to-set-up-my-office-365-email-account-withsuperofficeinbox/)

Docs: [Set up SuperOffice Inbox](https://docs.superoffice.com/en/email/inbox/learn/setup.html)
