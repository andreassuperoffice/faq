---
title: "How to configure system, personal and request type signatures in SuperOffice?"
url: https://community.superoffice.com/en/support-faqs/faq/how-to-configure-system-personal-and-request-type-signatures-in-superoffice/
lang: en
updated: "27 Feb 2026"
---

# How to configure system, personal and request type signatures in SuperOffice?

Updated on 27 Feb 2026

I want to make signatures for my company. How are system, personal, and request type signatures configured and applied in SuperOffice?

Signatures in SuperOffice can be configured in three different areas:

1. [System signatures (for e-mail and requests)](https://community.superoffice.com/en/support-faqs/faq/how-to-configure-system-personal-and-request-type-signatures-in-superoffice/#t1)
2. [**Personal signatures** (for e-mail and requests)](https://community.superoffice.com/en/support-faqs/faq/how-to-configure-system-personal-and-request-type-signatures-in-superoffice/#t2)
3. [**Request type signatures** (via reply templates)](https://community.superoffice.com/en/support-faqs/faq/how-to-configure-system-personal-and-request-type-signatures-in-superoffice/#t3)

How a signature is applied depends on where it is configured and whether a personal signature exists.

**System signatures**

There are two types of system signatures - **e-mail** and **request** signatures. An administrator configures system signatures, and it applies to all users who do not have a personal signature set. Please note that the option to edit system signatures is **only available to administrators**.

Please follow the steps to set the system signatures below:

1. Click on ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6549630-m8WEzgnAK4XgCwHK6SYh19D0PdiFI3e4cxcRR2GXga1hP6x69ZqE7ff8QD08gPX4-0/image-20260222040018-2.png), and then the **Edit system signature** option.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6549629-7AXaFTYPikc8uSqhYICoDHabg6D27S293eyWICmAABimUyQSU1PkFBuZQuGWRX3l-0/image-20260222035950-1.png)
2. Edit a default **e-mail signature** and click on the **Save** button.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6549631-dfQhEB3Xggra58CIE1u7Gc1Mhs0AZQ1kmld5ePqr9jZGwrRgfpGo3oZEMPG6WHXc-0/image-20260222040429-3.png)

   Such signatures are used for all users for normal e-mails (excluding requests). They are applied only if the user does not have a personal e-mail signature.

   Variables for e-mail signature must be written in **curly brackets**. You can find all the sender's variables [here](https://docs.superoffice.com/en/document/templates/variables/for-sender-contact-dialog.html), or you can add the variables by clicking on the ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6559369-DnmkH7XGr8HQJETwRuoOOMImQkzt2yB72CSn62jTrZBApAII1N9wCK26T7bNcHnn-0/image-20260227095732-1.png)icon.
3. **Request signature** is used for all users replying in requests if they don’t have a personal signature, or the request type excludes signatures.

   You can find the variables for the request signature [here](https://docs.superoffice.com/en/knowledge-base/learn/reply-templates/template-variables.html#user), or you can add the variables by clicking on the ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6559369-DnmkH7XGr8HQJETwRuoOOMImQkzt2yB72CSn62jTrZBApAII1N9wCK26T7bNcHnn-0/image-20260227095732-1.png) icon.

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6549632-taQpOWts8nFCPoGiUpga1KXDZSFMxjjhQq5jcpyAM3ubwuT467iKZz03syBsSPZD-0/image-20260222040731-4.png)

Please note that these variables will not work for automated replies sent by the system, because such replies are not linked to a user.

**Personal signature**

Each user can configure personal signatures separately for **e-mail**and **requests.** Please note that **personal signatures always override system signatures.**Please follow the steps to add a personal signature below:

1. Click on ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6549630-m8WEzgnAK4XgCwHK6SYh19D0PdiFI3e4cxcRR2GXga1hP6x69ZqE7ff8QD08gPX4-0/image-20260222040018-2.png), and then the **Edit personal signature** option.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6549636-B2nSAIl3R2RcgLW3hp6ojNwsir1bDA6jmTMjpfwnLeNaBHCOi1Oi2gq1bOy9ZGer-0/image-20260222041127-8.png)
2. Personal **e-mail signature** will be used **for normal e-mail templates**(this means that it will not be used for meeting invitations, privacy confirmations, quote confirmations, and order confirmations). If a personal e-mail signature exists, it is used. If not, the system e-mail signature is used instead.

   Variables for e-mail signature must be written in **curly brackets**. You can find all the sender's variables [here](https://docs.superoffice.com/en/document/templates/variables/for-sender-contact-dialog.html), or you can add the variables by clicking on the ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6559369-DnmkH7XGr8HQJETwRuoOOMImQkzt2yB72CSn62jTrZBApAII1N9wCK26T7bNcHnn-0/image-20260227095732-1.png)icon.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6549634-PpimejQIuaifqqkr1ZLe2oWWeGyMBMSMkaJiBNZqkb4Mzznh1gq31alrbRIRlCni-0/image-20260222040955-6.png)

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6549639-eKemz4cMOMBZLXp6HGNDEABxKcOE9s5SuHaH2FPD8rnmMyy3xY3uZkqfRLgEreI3-0/image-20260222043741-11.png)
3. Personal **request signature** is used when replying to requests. If a personal request signature exists, it is used. If not, the system request signature is used instead.

   You can find the variables for the request signature [here](https://docs.superoffice.com/en/knowledge-base/learn/reply-templates/template-variables.html#user), or you can add the variables by clicking on the ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6559369-DnmkH7XGr8HQJETwRuoOOMImQkzt2yB72CSn62jTrZBApAII1N9wCK26T7bNcHnn-0/image-20260227095732-1.png) icon.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6559427-d9UN1qjXEyRUE6I9GFQ0TBogYYkYQ822L4W3sQjbFZFp6AyUbdsdxpsAWzurLo9M-0/image-20260227101411-2.png)

**Request type signatures**

Request type signatures are configured separately using **Reply Templates** in SuperOffice Service.

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6549641-ax1wKP8hO17DuxuEFyDuYG13MkZpxjQb6InW0CW5ktSwng1lYlrZa5zbTKGqkRWQ-0/image-20260222044209-13.png)

If a request type is configured to **exclude signatures**:

- No personal signature will be used.
- No system signature will be used.

Instead, the signature must be included directly in the selected Reply Template.

To configure a request type signature, please follow the steps below:

1. Create or edit a Reply Template in the Knowledge Base (KB). You can find more information on how to create a reply template [here](https://docs.superoffice.com/en/knowledge-base/learn/reply-templates/create.html).
2. Optionally, you can create folders for signatures for better organization (for example, per team or for signature management).
3. If needed, set a default language for the reply template (for example, English).
4. **Requirements:**

- The signature must be written in HTML.
- Service variables can be used. You can find all the service variables [here](https://docs.superoffice.com/en/knowledge-base/learn/reply-templates/template-variables.html#user). You can also use the **List all variables** to see available variables. An example: Hello [[user.firstname]].

  ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6559887-yi4ARkNrIDFF5bqCaJJbfOKN8O0YLdML6qiQtj3h2oz85CgmX55BlwcJquHgsbMp-0/image-20260227115748-3.png)

When changing the request type, the signature follows the customer’s preferred language defined **in the contact card**.

This is how changing the request type changes the signature.

**Request type: call**

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6549642-niHK5l1s1BklEAIDFEjseni1rugEdSBP6Hj7pcJByUDLFTigaQMeM3TGP7Kyoe1C-0/image-20260222045730-14.png)

**Request type: request**

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6549643-CBxPdM0Atslq73ID76ER4ZQort5zKh5XIudqydKfUt6YF6AtW0noSP5KJkleJzAc-0/image-20260222045804-15.png)

**More information**

Docs: [Edit signatures](https://docs.superoffice.com/en/learn/getting-started/edit-email-signature.html)
