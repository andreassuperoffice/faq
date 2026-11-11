---
title: "What to do when I get an error message \"Code:605 Error:Not delivering to previously bounced address\" in SuperOffice Online Service or Marketing?"
url: https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-i-get-an-error-message-code605-errornot-delivering-to-previously-bounced-address-in-superoffice-online-service-or-marketing/
lang: en
updated: "8 May 2025"
---

# What to do when I get an error message "Code:605 Error:Not delivering to previously bounced address" in SuperOffice Online Service or Marketing?

Updated on 8 May 2025

I am getting a bounce message in my request or mailing statistics after sending a reply to some specific contacts:

*Code: 605
Error: "Not delivering to previously bounced address"
Notification:
headers: [["X-Mailgun-Sid", "WyIyMTVlNiIsICJoYXJyeS5zdW5kZWxpbkBoYW5keW9ubGluZS5uZXQiLCAiZmExZDY2Il0="].....*

Why does it happen and how do I fix it?

Most of the customers that use SuperOffice Online solution use out-of-the-box service for sending out e-mails. This service is provided by SuperOffice partner Mailgun.

When some of your recipient e-mail addresses have bounced previously - they are collected in a suppression list. All subsequent e-mail delivery attempts are ignored to protect SuperOffice CRM Online's sending reputation. Bounced e-mail addresses are collected automatically when Mailgun detects events of delivery failures due to permanent recipient's mailbox errors, such as a non-existent mailbox.

However, if you are sure that the recipient's e-mail address is available now there is a way to remove these e-mails from the suppression list. Please forward the e-mail addresses that creates bounce messages to [SuperOffice support](http://cs.superoffice.com) and request to get them removed from the suppression list.

**Note!**

- Soft bounces and other failures (such as ESP rejects an email because it thinks it is spam) are not added to the list.
- If you use your own domain email address we recommend to set up SPF record. Check the articles below for more information:

[How to avoid being categorized as spam when sending Mailings from SuperOffice Online?](https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-my-sent-mailings-bounce-in-superoffice-online-or-i-get-many-bounce-messages-in-superoffice-service/)

[What is SPF and how do I configure and set it up with Google Account?](https://docs.superoffice.com/email/mailgun/spf/set-up.html)

**More information:**

Docs: [Mailgun - Security and best practices](https://docs.superoffice.com/email/mailgun/security.html)

Article: [SMTP errors and reply codes](http://www.serversmtp.com/en/smtp-error)
