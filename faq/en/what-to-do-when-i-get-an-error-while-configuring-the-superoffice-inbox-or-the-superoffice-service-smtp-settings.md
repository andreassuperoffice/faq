---
title: "What to do when I get an error while configuring the SuperOffice Inbox or the SuperOffice Service SMTP settings?"
url: https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-i-get-an-error-while-configuring-the-superoffice-inbox-or-the-superoffice-service-smtp-settings/
lang: en
updated: "25 Mar 2026"
---

# What to do when I get an error while configuring the SuperOffice Inbox or the SuperOffice Service SMTP settings?

Updated on 25 Mar 2026

What do I do when I get an error:

"*The remote certificate is invalid according to the validation procedure."*

while configuring the SuperOffice Inbox, or an error:

"*Error: The SMTP server returned the following error message: SmtpCurl error: Peer certificate can not be authenticated with given CA certificates.**SSL certificate problem: unable to get local issuer certificate.*"

while configuring the SuperOffice Service SMTP settings?

This error comes up when a self-signed certificate is used. SuperOffice Online and from SuperOffice 8.1 Onsite self-signed certificate is not supported. To be able to configure the SuperOffice Inbox, please use a third-party signed certificate or disable the cURL e-mail library. Please check [this article for more information](https://docs.superoffice.com/en/online/mail-services/curl/index.html).

**More information**

SuperOffice Community forum:[Inbox: remote certificate is invalid](https://community.superoffice.com/en/technical/forums/api-forums/service-crmscript/mailkit----remote-certificate-is-invalid-according-to-the-validation-procedure/)

Article: [Self-signed certificate](https://www.keyfactor.com/blog/self-signed-certificate-risks/)
