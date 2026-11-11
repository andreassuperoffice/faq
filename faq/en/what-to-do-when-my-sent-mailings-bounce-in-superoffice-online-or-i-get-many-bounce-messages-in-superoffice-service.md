---
title: "What to do when my sent mailings bounce in SuperOffice Online or I get many bounce messages in SuperOffice Service?"
url: https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-my-sent-mailings-bounce-in-superoffice-online-or-i-get-many-bounce-messages-in-superoffice-service/
lang: en
updated: "13 Mar 2025"
---

# What to do when my sent mailings bounce in SuperOffice Online or I get many bounce messages in SuperOffice Service?

Updated on 13 Mar 2025

After sending out a Mailing from SuperOffice CRM Online, I have noticed that many recipients of the mailing have a status "Bounced". At the same time, I noticed a problem in SuperOffice Service. Most of the emails we send cause a bounce message, and our replies do not reach our customers.

Why is this happening and how can I resolve it?

Every CRM Online customer with access to the Marketing and Service modules receives the mailing service provided by MailGun and receives an e-mail account for SuperOffice Service in the form of "customer@domain.suocrm.XX" (.eu or .com).

Customers will often use their own email addresses to send emails (mailings or replies to cases in Service). When this is the case, the recipient's e-mail server may recognize these messages as spam, because the domain of the sender's e-mail address is different from the real domain of the e-mail address (provided by SuperOffice) that sends out the e-mail.

For example, if you use your e-mail address in the From field in SuperOffice Mailings or you use your e-mail as the Default "from address" in the SuperOffice Service setup, the recipient's e-mail server will see that the mailing or e-mail is sent from "E-mail@customer.suocrm.com" domain, but the "from" address is different, ie it contains a different domain name. This can lead to your message being identified as spam, and therefore the emails are categorized as spam.

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6127125-HJ8fK1r4i6ofe6qTaKCrZgfkIUXicZnyylE7qhnyBwirLjklSIkBYO9udexs4flD-0/image-20250313152329-1.png)

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6127126-9TF2CAietmoJrJww5uOj7KI46onZFuZeAswOqLNoGO9TNF3E6tUImfI7AOpZ8LPJ-0/image-20250313152405-2.png)

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6127127-ymjLCx4TRLPqFNjSN5bSnYhqMpnyb5H8dmyBLwZsnaMBG0od7mKwiUeGOnk8bfDi-0/image-20250313152426-3.png)

To avoid the above situation not affecting your messages, we suggest creating a so-called record that allows the SuperOffice Online MailGun service to send messages on behalf of your domain. This is done using SPF records.

You will need to create a database in the DNS for your domain "@ [yourdomain] .com" which confirms that the SuperOffice SMTP server is a trusted sender for "@ [yourdomain] .com".

The TXT record that must be added is "v=spf1 include:\_spf.online.superoffice.com ~ all".

**Note!** This should be done by your IT manager, your email server administrator, or someone who manages DNS for your domain.

**More information:**

Docs: [Set up SPF](https://docs.superoffice.com/email/mailgun/spf/set-up.html)

Google recommendations for their service, go to [About SPF records](http://support.google.com/a/answer/33786?hl=en)

FAQ: [What to do when the newsletters get blacklisted after sending them out from SuperOffice Mailing?](https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-the-newsletters-get-blacklisted-after-sending-them-out-from-superoffice-mailing/)
