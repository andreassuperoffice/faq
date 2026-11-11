---
title: "What to do when some of my Mailing recipients' bounces come directly to my mailbox?"
url: https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-some-of-my-mailing-recipients-bounces-come-directly-to-my-mailbox/
lang: en
updated: "21 Aug 2025"
---

# What to do when some of my Mailing recipients' bounces come directly to my mailbox?

Updated on 21 Aug 2025

I sent out a Mailing and some of the bounce messages came back directly to my mailbox, while the recipient in the Mailing list has the status **Sent**. Why does it happen?

When SuperOffice CRM receives a bounce reply from your recipient's mail server, it assigns status **Bounced** to this recipient in your mailing.

If your mailing recipient has a **Sent**status in the list and you have received a bounce message directly to your mailbox, it is because:

- Your e-mail address is used in the mailing **From** the field.

  ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6298301-Ka5tklAyeq3W6CTA1ketwuNtQeYa0jrJcCcCiPywfK5RgZ38UspXZKyh5B5noIrj-0/image-20250821145201-1.png)
- The bounce message code has not been recognized as a bounce by SuperOffice CRM.
- Recipient’s server uses an unrecognized method to notify SuperOffice CRM that a mailing has bounced.

  ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6298309-co9ITRn2nMU8us8jaTagKdsdGRNhdMjJWlk9xFH12NcZ4Sh4esyb1faSSsYOY7F4-0/image-20250821145403-2.png)

**More information**

Docs: [Work with the recipient list after the mailing](https://docs.superoffice.com/en/marketing/recipients/learn/look-at-recipient-list.html)

Docs: [Manage bounces](https://docs.superoffice.com/en/marketing/recipients/learn/manage-bounces.html)
