---
title: "What to do when I cannot see which e-mail I have already archived to SuperOffice CRM from my Outlook Sent Item list?"
url: https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-i-cannot-see-which-e-mail-i-have-already-archived-to-superoffice-crm-from-my-outlook-sent-item-list/
lang: en
updated: "24 Feb 2026"
---

# What to do when I cannot see which e-mail I have already archived to SuperOffice CRM from my Outlook Sent Item list?

Updated on 24 Feb 2026

After the e-mail gets archived to SuperOffice CRM, next time when I select it, the archive button lights up with a green sign indicating that the e-mail has been archived. When I select an already archived e-mail in the Sent Items folder, the button does not light up in green. Why does it happen?

![](https://online2.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/4447263-99hJm7WPBf2sRklF2nQnSzUXlM8RoomkoWZmaor2TkjP1MrWqiznqsiymXNaPN1g-0/image.png)

This feature (the indication of e-mail that has already been archived from the Sent Items folder) is not supported by SuperOffice MailLink. Please read the explanation below.

When archiving an e-mail, the MailLink picks up the unique Message-ID that belongs to the e-mail and stores it in the ForeignKey table with the appointment ID. This ID determines if an e-mail is already archived or not. When a new e-mail is saved, the MailLink first checks the ForeignKey table to see if an e-mail with the same ID is already archived by anyone. The Sent Items folder in Outlook contains no unique Message-ID. For this reason, the reference to the item in the SuperOffice database becomes invalid, and the e-mail cannot be identified as already archived.

In some cases, [turning off Cashed Exchange-mode](http://support.office.com/en-us/article/Turn-on-Cached-Exchange-Mode-7885af08-9a60-4ec3-850a-e221c1ed0c1c) allows us to identify if e-mail in the Sent Items folder was archived already. However, this setting has an impact on Outlook performance.

**Note!**

1. Changing to a none-cached Exchange-mode will not enable duplicate detection of already archived mails (because they lack the ID).
2. Changing to a none-cached Exchange-mode will not result in existing items found in Outlook’s sent-item folder suddenly reporting this unique ID. They will remain ID-less.
3. Only new e-mails sent after changing this setting have the potential to receive a unique ID, but there are no guarantees.
