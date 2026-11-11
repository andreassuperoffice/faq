---
title: "What to do when more than one request is created for one incoming e-mail in SuperOffice Service?"
url: https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-more-than-one-request-is-created-for-one-incoming-e-mail-in-superoffice-service/
lang: en
updated: "28 Dec 2025"
---

# What to do when more than one request is created for one incoming e-mail in SuperOffice Service?

Updated on 28 Dec 2025

What to do when more than one request is created for one incoming e-mail in SuperOffice Service?

There are two known situations when more than one request is created for one incoming e-mail:

- [When the system creates more than one request from one e-mail](https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-more-than-one-request-is-created-for-one-incoming-e-mail-in-superoffice-service/#2)
- [When the system imports more than one e-mail from the Inbox](https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-more-than-one-request-is-created-for-one-incoming-e-mail-in-superoffice-service/#1)

**When the system creates more than one request from one e-mail**

There are two common causes of duplicate requests for an online customer.

1. **Delivering the e-mail from MailGun to SuperOffice.**

   a) This is most often observed by looking at the creation timestamps of requests. A new request appears first, and duplicates may appear a few minutes or hours later. This can happen for all or almost all incoming requests, with a similar pattern of timestamps for each. Please [reach out to support](https://community.superoffice.com/en/support-faqs/faq/how-do-i-register-a-support-request-from-within-superoffice-crm/) for help troubleshooting this further.
2. **The process of creating the request gets interrupted, and the system starts overcreating the request. The most common steps that can cause this are:**

a) **Failing custom setup of the inbox filter**

You can find filters here:

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6465413-Q0TWzR9ctlNqk4nZyHjKKpuJPkOyiI6JNqbuGxpu2kRU09z7OlTbOYfAbWCapaWa-0/image-20251228201546-3.png)

Check if there is a filter that applies to the inbox the e-mail came to. Try to change the filter so it is not linked to this inbox, and see if the issue continues.

b) **Failing a custom script, which is in charge of e-mail import.**

If you are aware that your solution uses a script during the import process, please reach out to the responsible consultant who set it up. If you are unsure, [reach out to support](https://community.superoffice.com/en/support-faqs/faq/how-do-i-register-a-support-request-from-within-superoffice-crm/).

c) **Autoreplies with broken IF statements.**

This occurs when the standard auto-reply template has been edited, such as by removing some text. To confirm if this applies to your case, please follow the steps below:

1. Check which template is used for auto-reply by navigating to **Settings and maintenance** - **Requests** (1) - **System templates** (2), then go down to the **Customers** (3) and check which template is set up in the **Reply template for auto-reply** (4).

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6465411-Ai4ad9UPA8UKkJA285uunFWUEwhBL7GSq5oJgEnWYHcG8oM4PaDhJQemzPzdCeo1-0/image-20251228200555-1.png)

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6465412-acLl92DeWThLSJJ8d3FYAWWCSCoolOgRPypmxER454G5uWlZuFnc5fElnqBFCJW8-0/image-20251228200832-2.png)

It is also possible that another auto-reply template is set up for the particular inbox. To check it, navigate to **Requests** (1), then **E-mail** (2), and in the **Reply template for reply to contact field** (3), you'll see which template is used for the incoming e-mail to this particular mailbox.

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6465415-PcSI039WgK7QQKWuzsX2URUObSngOrkgEaUe4frQaft5BJdjuzqS046gxBuQc94T-0/image-20251228201922-5.png)

2. Open a relevant template by clicking on **Main menu** (1) -  **Knowledge Base** (2) and choosing **Reply templates** (3) from the drop-down list.

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6465416-xY5qw6YX4PTQ76zCKME90827UNYiKJE5sP7nZGtYg5EF8lgfFj3mG4Eje9woBdkt-0/image-20251228202246-6.png)

3. From the list of all the templates, please open the template that you identified in the first step.

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6465417-HFWzUNO8pibtjP6PXebCYN0DzZeKDW3ss6GD7aaOZrWgkCLGSowKwRLEnL7K9pus-0/image-20251228202406-7.png)

4. Make sure that the IF part is not removed without removing the ENDIF part in the reply template. In other words, confirm that there is no "—[[ENDIF]]-- " tag, which does not have "—[[IF:]]-- " before. Please also check the reply template **HTML text** (1)in **Source** (2) viewer mode. Sometimes, tags **IF** and **ENDIF** (3) are not visible in plain text.

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6465418-4agepqi3fqgPSPCiRMH5TfrmfRUmynQqj9TbdexnnnNPjmRby9qySL9eqepnhMjf-0/image-20251228202953-8.png)

**When the system imports more than one e-mail from the Inbox (Onsite only)**

There can be several reasons why SuperOffice Service imports more than one e-mail from the inbox:

1. When e-mail duplicates exist in the mail server, and SuperOffice Service is importing everything that it finds in the inbox. In this case, please make sure that the inbox in the mail server has only one e-mail.
2. If there is only one e-mail message in the mail server (inbox), check how many e-mails are being imported from the mail server to the SuperOffice Service installation. To do this, go to the **inbox**folder that can be found in the SuperOffice Service installation folder on the server.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6465421-WcoG9r6gtg9rtoyCiF37OCkWclm6F2ykKW8S7D0d3eFqpttkUp3e2ytprsqC89h3-0/image-20251228204332-9.png)

The files in the Inbox folder can be opened with the Notepad program. By opening them, you can see how many duplicate e-mails were imported at that particular moment. Duplicates can be created when the SuperOffice server loses connection with the mail server during the import process. In these situations, all the import procedures (including deleting e-mails from the original mailbox after importing into Service) can not be performed successfully. As a result, the same e-mail is being imported as many times as it takes to perform the import successfully and delete it from the mailbox.
