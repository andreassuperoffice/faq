---
title: "What should I consider when our company domain name changes?"
url: https://community.superoffice.com/en/support-faqs/faq/what-should-i-consider-when-our-company-domain-name-changes/
lang: en
updated: "31 Mar 2026"
---

# What should I consider when our company domain name changes?

Updated on 31 Mar 2026

Our company will change its domain name. This means that our email addresses will change. What effects will this have on the usage of SuperOffice CRM Online?

This change will affect several parts of SuperOffice CRM Online, depending on which modules you are using.

Click on the links below to see what has to be changed when:

[**You are using an identity provider (IDP) to log in to SuperOffice CRM Online**](https://community.superoffice.com/en/support-faqs/faq/what-should-i-consider-when-our-company-domain-name-changes/#a1)

[**You are using a SuperOffice password to log in to SuperOffice CRM Online**](https://community.superoffice.com/en/support-faqs/faq/what-should-i-consider-when-our-company-domain-name-changes/#a2)

[You are sending out and receiving e-mails from SuperOffice Service and eMarketing](https://community.superoffice.com/en/support-faqs/faq/what-should-i-consider-when-our-company-domain-name-changes/#a3)

[You are using the SuperOffice for Outlook to archive e-mails from Office 365](https://community.superoffice.com/en/support-faqs/faq/what-should-i-consider-when-our-company-domain-name-changes/#a4)

[You are using the SuperOffice WebTools](https://community.superoffice.com/en/support-faqs/faq/what-should-i-consider-when-our-company-domain-name-changes/#a5)

[You are using your own SMTP server to send out e-mails from SuperOffice CRM](https://community.superoffice.com/en/support-faqs/faq/what-should-i-consider-when-our-company-domain-name-changes/#a6)

[**You are using Synchronizer for SuperOffice**](https://community.superoffice.com/en/support-faqs/faq/what-should-i-consider-when-our-company-domain-name-changes/#a7)

**You’re using an IDP to log into SuperOffice CRM Online**

When using Azure/Office 365 or G Suite as identity provider to log in to SuperOffice CRM, your new domain name has to be connected to your SuperOffice CRM environment.

To connect your SuperOffice CRM environment with your new domain name, please register a support request via **Help (1) - Contact** **support (2)** in SuperOffice CRM. Our support team will change this for you.

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6202150-BjhJiOsmoJHlSgLFBhYldZ3YYq8tjJ02sGQXdadACyhyUpBHe7TBWRjfLxzdaaqX-0/image-20250513093607-1.png)

**You are using a SuperOffice password to login to SuperOffice CRM Online**

In this scenario it is enough to change the e-mail addresses on the user cards in the SuperOffice admin. You can do this in the Administrator module under **Users (1)** and then change the e-mail address in the **User name** **(2)** and **e-mail address (3)** field.

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6223508-ADPiOgN5Z8qWay1YT0NGyYfKWY3kSSRdXyltAAfbWoO9WHwn1PaJeKat3bX8Nn3l-0/image-20250529091541-1.png)

You can also change the e-mail addresses on the Contact and Company cards by using the **Bulk Update** feature. Make a selection of all contact persons whose e-mail addresses you want to change with the new domain name, and use the **Replace e-mail addresses with** action in Bulk Update:

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6223510-QYnN91DdHs91NemCY8CFdM7fjXzxk4fS1nbfwNHxx7pT5j2XrmKJ50y3L2ZQUNuf-0/image-20250529092113-2.png)

**You’re sending out and receiving e-mails from SuperOffice Service and eMarketing**

To prevent being marked as SPAM, your IT administrator has to set up an SPF record for SuperOffice CRM Online for your new domain.

Additional information: [How to set up SPF record](https://docs.superoffice.com/en/email/mailgun/spf/set-up.html)

To import e-mails as requests to SuperOffice Service, a new forwarding rule has to be set up for your new mailboxes. This rule will then automatically forward e-mails from your new service mailboxes to the forwarding address(es) of your SuperOffice CRM installation. You can find these forwarding addresses in **Settings and maintenance (1)** under **Requests (2)** and then **E-mail (3)**:

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6223512-7Gf9uddQ7IdiTPeHoE0nS5tuAxkMZdM1LTna3PXXaf88B2ofYrRHwmbj2SwRjq8m-0/image-20250529092902-3.png)

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6223514-Sr8YotrHx6X3SYypNQNgmWfMFIGqjmBMFRYRTF32bLKLX96563982eNewbGgl5Nf-0/image-20250529093057-4.png)

Under **Mailboxes (4)**, you can see the **Forwarding address (5)** for each of your mailboxes.

To show your new domain name as the sender of e-mails, you should change the e-mail addresses in each mailbox. Double click on each mailbox line to open the settings of that mailbox and change the e-mail address:

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6223515-3S4FHW0zt8j1FT7TxrYQM9nNCKxDwEM7rzu33sDOJoJ0iz7cnLJcp5ZiWdlXEFaO-0/image-20250529093252-5.png)

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6223516-lq9ZA8F51G28RrL84yqRdR4ETHsw6CjWyzi4wQ32jDbSfbpHi8hsDPCe7Z9uoehP-0/image-20250529093516-6.png)

Next, go to **Preferences (1)**, then **Global preferences (2)**, and change the **Default From address (3)**.

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6223519-cHDxBb8Hr5Y5Sf3tCEP6tzktUzJuXu2h0zF6aFzttTRiIOpYZtDmBTg3KED71BuX-0/image-20250529093807-7.png)

**You are using the SuperOffice for Outlook to archive e-mails from Office 365.**

When the main e-mail address of your Office 365 account changes, you may have to log in again to the SuperOffice for Outlook application. If you see the following pop-up when opening SuperOffice for Outlook, click on **We run SuperOffice Online or Onsite** (depending on the installation you use) to log in to this application with your new e-mail address.

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6223520-o56f5l6JX1cxAebFa8BCSZXX5hfnFTnHZpNqKkwHQOrSUPcwduhi65tqQ6Ygu6AX-0/image-20250529094007-8.png)

**You are using the SuperOffice WebTools to open documents in the installed version of Office**

You will have to log in again to the SuperOffice WebTools with your new login name. You can do this by following the steps in [this article](https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-e-mails-and-documents-from-superoffice-crm-stopped-opening-with-microsoft-office-programs/#2) after your login name (username) to SuperOffice CRM has been changed to your new e-mail address.

**You are using your own SMTP server to send out e-mails from SuperOffice**

If you are using your own SMTP server to send out e-mails from SuperOffice Service and eMarketing, after the change of the domain your SMTP address will change too.

This means that your new SMTP address must be updated in SuperOffice CRM Online as well. Our support team can help you with this. Please register a support request via **Help (1) - Contact support (2)** in SuperOffice CRM and our support team will be glad to assist you.

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6202150-BjhJiOsmoJHlSgLFBhYldZ3YYq8tjJ02sGQXdadACyhyUpBHe7TBWRjfLxzdaaqX-0/image-20250513093607-1.png)

**You are using Synchronizer for SuperOffice**

To be able to carry on working without any interruptions after the domain name change, the users have to be relinked for the Synchronizer. Click [here](https://help.infobridge.com/docs/synchronizer/how-to-deal-with-a-companyname-change/) to find the instructions on how to do this.
