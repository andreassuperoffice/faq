---
title: "Why do some e-mail replies send from SuperOffice Service and Marketing bounce?"
url: https://community.superoffice.com/en/support-faqs/faq/why-do-some-e-mail-replies-send-from-superoffice-service-and-marketing-bounce/
lang: en
updated: "27 Dec 2023"
---

# Why do some e-mail replies send from SuperOffice Service and Marketing bounce?

Updated on 27 Dec 2023

Sometimes we get bounce messages after sending e-mail replies from SuperOffice Service. Why do our replies bounce and what do the different bounce message codes mean?

There are some known reasons that cause e-mails to bounce.

**Hard and Soft bounce**

All bounces can be split into two groups - soft and hard bounces.

A soft bounce means that an e-mail reached a recipient's mail server, but due to temporary errors, the message has not been delivered. SuperOffice Online uses [Mailgun](https://docs.superoffice.com/email/mailgun/security.html) to send, receive, and track emails. Mailgun will keep trying to deliver the message which bounced softly, but eventually it will stop trying to deliver based on the receiving e-mail server provider’s feedback.

A hard bounce means that an e-mail cannot be delivered, because a recipient's e-mail address does not exist, either a mail domain name does not exist or a recipient's e-mail server has blocked delivery. Mailgun will stop attempting delivery after one hard bounce.

**Most common bounces**

Bounce messages contain a three-digit code. The first digit defines if the server has accepted a message, fulfilled a request, ran into a temporary problem, encountered an error etc. If the code starts with 4, - that indicates a temporary issue (a soft bounce), if it starts with 5 – that indicates a permanent issue (a hard bounce). the other two digits give more specific details about the problem. Below you will find the list of most common bounce codes:

500        Syntax error, the server could not recognize the command.

501        Command arguments have a syntax error.

502        Command was not implemented.

503        Bad sequence of commands.

504        A parameter of command is not implemented.

550        Recipient's mailbox name does not exist

551        The recipient is not local to the server.

552        Recipients mailbox has excited storage limits

553        Recipient's mailbox name is invalid

554        The incoming server identified your email as spam, or your IP has been blacklisted.

**Mailgun bounce codes and solutions**

The table below explains some common Mailgun bounce codes, their meanings and how they can be addressed:

|  |  |  |
| --- | --- | --- |
| **Code** | **Meaning** | **Solution** |
| 498 | There is no MX or A records for the domain which is used in your recipients email address. | Confirm that there are no typos in the recipient's email address. If there are no mistakes in the email address, try to retype and save the email address which fails. |
| 499 | It was impossible to connect to MX servers, in other words - recipient's server was inaccessible. | Try to resend an email. If this didn´t help, contact the recipient's IT. |
| 530 | Authentication is missing. | Set DKIM record, please check [this](https://docs.superoffice.com/email/mailgun/dkim/index.html) article for more information. |
| 550 (5.1.0) | Address rejected. | Confirm that the recipient's email address is correct. |
| 550   (5.1.1) | Recipient address rejected: User unknown in relay recipient table. |
| 550   (5.5.0) | No such recipient. |
| 550  (5.6.11) | Some invalid characters (bare line feed characters) were added into a message you sent. | Check [this FAQ.](https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-some-e-mail-replies-bounce-with-an-error-about-bare-line-feed-characters-in-superoffice-service/) |
| 550 (5.7.0) | Due to the receiving mail server's local policy violation email cannot be delivered. | Confirm or set up an SPF record. If this doesn’t help, contact the recipient's IT to discuss how to overcome their security policies applied to your company’s emails. |
| 550 (5.7.1) | Recipient's address rejected an email. SPF fail, particular IP should not send on behalf of the customer's mail provider. |
| 554 | Transaction has failed. It's a permanent error and the server will not try to send the message again. The incoming server thinks that your email is spam, or your IP has been blacklisted. | Make sure that Mailgun’s IP\* is whitelisted in the recipient's mail server. If this doesn’t help, contact the recipient's IT to discuss how to overcome their security policies applied to your company’s emails. |
| 602 | A message cannot be delivered to the recipient. Mailgun tried to deliver it for 8 hours. | Try to resend an e-mail again and confirm that the recipient's email address is correct. |
| 605 | A recipient previously bounced and SuperOffice will stop attempts to deliver email to previously bounced addresses. | Check [this FAQ.](https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-i-get-an-error-message-code605-errornot-delivering-to-previously-bounced-address-in-superoffice-online-service-or-marketing/) |
| 607 | A recipient´s mail server has identified your message as Spam. | Confirm or set up an SPF record. If this doesn’t help, contact the recipients IT to discuss how to overcome their security policies applied to your company’s emails. |

**More information:**

FAQ: [What to do when the newsletters get blacklisted after sending them out from SuperOffice Mailing?](https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-the-newsletters-get-blacklisted-after-sending-them-out-from-superoffice-mailing/)

FAQ: [What to do when my sent mailings bounce in SuperOffice Online or I get many bounce messages in SuperOffice Service?](https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-my-sent-mailings-bounce-in-superoffice-online-or-i-get-many-bounce-messages-in-superoffice-service/)

Article: [How to set up SPF?](https://docs.superoffice.com/email/mailgun/spf/set-up.html)

Mailgun FAQ on how to manage reputation: [Reputation](https://documentation.mailgun.com/en/latest/best_practices.html#reputation)

Docs: [Mailgun - Security and best practices](https://docs.superoffice.com/email/mailgun/security.html)
