---
title: "What to do when I get a message \"Auto-reply not sent: Too many e-mail to:\" in SuperOffice Service?"
url: https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-i-get-a-message-auto-reply-not-sent-too-many-e-mail-to-in-superoffice-service/
lang: en
updated: "20 Mar 2026"
---

# What to do when I get a message "Auto-reply not sent: Too many e-mail to:" in SuperOffice Service?

Updated on 20 Mar 2026

What to do when I get a message "Auto-reply not sent: Too many e-mail to:" in SuperOffice Service?

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6596210-yTA39cPZBkYp0hqznp34lHNI0XrIol8xBZhZto3wXzSJjaYQdyRYz96h13Td5EQR-0/image-20260320085646-1.png)

The SuperOffice installation includes a feature that helps protect your sending reputation. It is triggered when a SuperOffice user (or a group of users) attempts to send multiple emails within a short period to a specific email address (or addresses). Then SuperOffice might prevent e-mail delivery.

The rule that prevents sending e-mails uses values stored in the mail\_block database table. In this table, the system stores email addresses and numeric values (in the field *time\_pool*). These values are reduced every time an e-mail is sent to the e-mail address, and every one-second value is increased by one. The number, which is deducted from the original value, depends on the settings in the *config* database table in the field *mb\_modifier*. When the numeric value next to the e-mail address drops below the value defined in the field *mb\_treshold*, the e-mail sending to this e-mail address is stopped. The initial value of the *time\_pool* field is set by the number in the *mb\_max\_value* field. It is the upper (initial) value for the spam-control algorithm, ensuring that a single email address does not receive too many emails.

Hence, by default, the system will allow 1 email per 10 minutes on average, with an initial buffer of 2 emails. In other words, if you send 3 emails to the same address instantly, the third one will be blocked.

The setup of this feature can be changed; there is no user interface to do it. The only way to change or disable it is to change it directly in the SuperOffice database.

- If you increase the default value of 1210 in the *mb\_max\_value* field, the buffer will increase. That means more emails may be sent before they are blocked. If the value of *mb\_modifier* decreases, more emails will be allowed per time frame.
- If the *mb\_modifier* field value is set to 0, then the rule of preventing e-mail from being sent will be disabled entirely.

**Note!**

1. Please be aware that we recommend taking a backup before making any changes directly to the database. [This FAQ](https://community.superoffice.com/en/support-faqs/faq/how-do-i-make-a-backup-of-the-superoffice-crm-database/) explains how to do it.
2. SuperOffice Online customers should contact [SuperOffice support](https://community.superoffice.com/en/support-faqs/faq/how-do-i-register-a-support-request-from-within-superoffice-crm/) if changes are needed.
