---
title: "How do I start using the new Microsoft 365 OAuth 2.0 authentication in SuperOffice CRM?"
url: https://community.superoffice.com/en/support-faqs/faq/how-do-i-start-using-the-new-microsoft-365-oauth-2.0-authentication-in-superoffice-crm/
lang: en
updated: "24 Feb 2026"
---

# How do I start using the new Microsoft 365 OAuth 2.0 authentication in SuperOffice CRM?

Updated on 24 Feb 2026

Is it possible to use QAuth 2.0 authentication to connect my Microsoft 365 account to SuperOffice Inbox, and how do I do that?

If you’re a user of SuperOffice CRM Online or SuperOffice CRM Onsite version 10.1.2 or higher (and hotfix 8.5 R17), you can use the modern authentication (OAuth 2.0) method to connect to your Microsoft 365 account in the SuperOffice Inbox.  For SuperOffice CRM Onsite 10.1.2 or higher, you can also connect your Microsoft 365 account to an IMAP mailbox in SuperOffice Service. In SuperOffice CRM Online, the Service module uses our integrated mail service.

**Note!** It is possible to use this feature as well if you’re a user of SuperOffice CRM Onsite (from version 9.2 R10 to 10.1.2). For more information, please contact your SuperOffice contact.

[**Click here to learn how to create a mailbox in SuperOffice Service with OAuth 2.0 for SuperOffice CRM Onsite.**](https://community.superoffice.com/en/support-faqs/faq/how-do-i-start-using-the-new-microsoft-365-oauth-2.0-authentication-in-superoffice-crm/#a1)

[**Click here to learn how to connect to the SuperOffice Inbox with OAuth 2.0.**](https://community.superoffice.com/en/support-faqs/faq/how-do-i-start-using-the-new-microsoft-365-oauth-2.0-authentication-in-superoffice-crm/#a2)

[**Click here when you experience the problem that your Microsoft account is not recognized as a Microsoft 365 account.**](https://community.superoffice.com/en/support-faqs/faq/how-do-i-start-using-the-new-microsoft-365-oauth-2.0-authentication-in-superoffice-crm/#a3)

**Creating a mailbox in SuperOffice Service Onsite with OAuth 2.0**

1. Navigate to Settings and Maintenance, then click on **Requests** - **E-mail**, and then on **New mailbox**.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6553042-XF6WO8FBI2HBA1ZgGhYiqEUFUzT3A7zAyaZokz6MqUkQAuzSD4hyN6axBOjEbeLH-0/image-20260224135444-1.png)
2. A pop-up will appear. Fill in the email address of your Office 365 mailbox. If SuperOffice recognizes the UPN as a Microsoft 365 email account, we redirect you to Microsoft for authentication.
3. When the authentication is completed, you can fill in the Mailbox details.

**More information:**

[Email in Service and Marketing](https://docs.superoffice.com/en/email/service/index.html)

[Set up mailboxes in Service](https://docs.superoffice.com/en/email/service/learn/create-mailbox.html)

**Note!** During the setup of a mailbox in Service, you may be presented with an Invalid client\_id error as below:

![](https://online2.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/5071888-BBzBhEhs62r9YSlZZf5ZdQIzBtffAcpWWs14ewLlFbeCEP06SR8wBKY8EKLS6sA5-0/image-20220708102705-1.png)

This is due to a security mechanism that only allows one registration per serial number. Get in touch with SuperOffice support and provide the serial number of the installation you have a problem with.

 If you see a red-marked error as below, please delete the cookies in your browser and try again. If that does not help, please check if the Firewall is blocking IMAPS on port 993.

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6553159-ETCgS8nTARyPhMDNLp7ZRW9jmom6hCmx135rJp7ifmU9J5923oib1jo1DkafEdky-0/image-20260224143313-2.png)

**Connect to the SuperOffice Inbox with OAuth 2.0**

1. To access the e-mail options, click the **Personal settings button** and click **E-mail options**.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6553175-rTqd5cjwYUyuwZgEqFI2B8OmDjklWP6wjOhIspGRJ6U0hRFmdOudPTuod57JIwt5-0/image-20260224143435-3.png)
2. Click on the **E-mail account tab** and then on the **Edit/remove button**. If you were logged in to the SuperOffice Inbox already, you should remove your account before you can make the OAuth 2.0 connection.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6553202-BtaB2B5yuXWbtTFxXzHLCwWmnTtG5UGxPPFKtWgDHHOUFZdjjcsJmh6hW2DZwEC6-0/image-20260224143522-4.png)
3. When there is no account configured in the SuperOffice Inbox, fill in your Microsoft 365 'User Principal Name' (UPN) in the field **E-mail account** and click **Next**.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6553204-5brgTw645TCdrxm5KZ78YD2JWoQw5ULqX2hEerzmstXxupBe1INkfoojf6k3A7bC-0/image-20260224143628-5.png)
4. If SuperOffice recognizes the UPN as a Microsoft 365 email account, you will be redirected to Microsoft for authentication. Authenticate your Microsoft account and complete the login.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6553270-Hl3LrdG4TMBSlGZNKsQZ3MyupisG9Yd209xEQKqrPfAT9LPdMyUhgdpueKQXNykd-0/image-20260224144443-6.png)
5. You will then be taken back to the SuperOffice Inbox. Your email account is now set up to use OAuth 2.0 authentication.

**My UPN is not recognized as a Microsoft 365 email account, but I am using Microsoft 365**

There are 2 known causes of this problem.

One possible cause is that the internal DNS is not pointing the MX Record of the domain to Microsoft. The solution is to make sure the internal DNS is pointing the MX Record of the domain to Microsoft.

Please follow the steps below to check if the setup is correct via the command prompt from your local network. You may need help from your IT administrator to perform this.

1. Open the command prompt.

2. Type "nslookup", then press **Enter**. You will see the following: **Default Server: <FQDN of your server> ...**

3. Type "set type=mx", then press **Enter**.

4. Type the domain’s name that you want to look up, then press **Enter**. The MX records of that domain will appear.

![](https://online2.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/5071891-PKrKtOqIBQEh87UfGY7do1XhApCM3SwGWF7j5Jkr6q9pOMeKXDhN8ZcjdIDtXXWC-0/image-20220708102755-2.png)

If the MX does not point to Microsoft, as in the picture above, this is the cause of the problem. Contact your IT administrator to resolve this DNS issue.

The other known cause is that the NetServer of your Onsite SuperOffice CRM installation is configured to use EasyMail instead of MailKit. This can be adjusted in the web.config. file in the Web Installation on the server.

    <Mail>
      <Component>
        <add key="Reader" value="EasyMail" />
        <add key="Sender" value="EasyMail" />
      </Component>
    </Mail>

This has to be switched to:

    <Mail>
      <Component>
        <add key="Reader" value="MailKit" />
        <add key="Sender" value="MailKit" />
      </Component>
    </Mail>
