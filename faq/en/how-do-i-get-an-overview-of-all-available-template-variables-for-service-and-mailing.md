---
title: "How do I get an overview of all available template variables for Service and Mailing?"
url: https://community.superoffice.com/en/support-faqs/faq/how-do-i-get-an-overview-of-all-available-template-variables-for-service-and-mailing/
lang: en
updated: "4 Aug 2026"
---

# How do I get an overview of all available template variables for Service and Mailing?

Updated on 4 Aug 2026

How do I get an overview of all available template variables which I can to use in Service or Mailing?

You can use template variables to insert information from your SuperOffice CRM into the communication messages with customers. To get an overview of all available template variables for requests and mailings, please click on one of the links below:

- [If you want to get variables for requests](https://community.superoffice.com/en/support-faqs/faq/how-do-i-get-an-overview-of-all-available-template-variables-for-service-and-mailing/#anchor1)
- [If you want to get variables for mailings](https://community.superoffice.com/en/support-faqs/faq/how-do-i-get-an-overview-of-all-available-template-variables-for-service-and-mailing/#anchor2)

**Get a list of all available template variables you can use in reply templates in requests**

1. Click on **Main menu** (1), then **Knowledge base** (2) and **Reply templates** (3).

   ![](https://app.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6802163-2OfHQ0Nr8uFKDxE67i2srQz32aiz07tyt28KmkZJM7tQj91eOgPbgxiyyFwynT2H-0/image-20260804103129-1.png)
2. Click on the **New reply template** button in the top-right corner to create a new reply template. Please check [this article](https://docs.superoffice.com/en/request/reply-templates/learn/create.html) to learn more about creating reply templates.

   ![](https://app.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6802164-IYKezOuCWC0hybLe5g9wRHEtdnyFNLKboFXQX1TndJgEekd2Gf44prp4Xg22aSER-0/image-20260804103252-2.png)
3. To get a list of all template variables, you can either type "**%PARSER\_TREE%"**(2) in the **HTML text** (1) tab **or** click on **Template variables** (3) and choose an item **List of available template variables**(4) and save the template by clicking **OK** (5).

   ![](https://app.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6802188-lmSzxtAJ7Ii3daAi0XrQC0YWwJjbUG7mxLo7Fc4IURiIqTcAPYC3P014qijJLQH0-0/image-20260804103451-3.png)

   ![](https://app.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6802189-QK3Rxx20Z5nuONwgEqIxQt4XmOEWjew64AHbEZ80prLlmASuAJW73KMSEF67Ds7K-0/image-20260804103556-4.png)
4. Then, when you use this reply template in a request, it will bring all available template variables, which can be used, and values, which would have been filled in the template that used the template variable.

   ![](https://app.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6802216-GW83jrbP3aPAXlS8iyO6Bd8fygq1n3aJxs5GfeYL3dWJac0aB5yWGSREkyMrH0bZ-0/image-20260804104150-5.png)

   ![](https://app.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6802231-UDDoUSaGjurRXSXWCFGLLOXelIQ8jwQESNE8Qf79dn08zclbmLGufFbr2eQsqgOm-0/image-20260804104420-6.png)
5. To use template variables, simply type them within parentheses inside the reply template, and the next time you'll use this template for the reply, the information in template variables will be filled in with the information from SuperOffice CRM.

   ![](https://app.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6802232-2NcXQqsOJp6bhG3HKucMxcLMNXTx8723lLn0MWiYgxuCQENOg9QmlACokSXrEnhM-0/image-20260804104627-7.png)

**Get a list of all available template variables you can use in a message in mailings**

1. Open a mailing message, which you can use for testing and in any text paragraph type in **[[PARSER\_TREE]]** (1) and click on **Send test** (2). Include an e-mail address where you want to receive a test e-mail and click **OK**.

   ![](https://app.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6802248-N8rB7DWH1bBZi3BlKghCTe4o4qwT9lncqyD63Bj4ARnss1iXLJfDn1cALxzIW1wS-0/image-20260804105014-8.png)

   ![](https://app.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6802253-Zk9pneTKepx4I9U1tWNp5QlIc7HkmAub8HnSgfLfu72JO7qPxbySYaP6cmcX5rFo-0/image-20260804105103-9.png)
2. Then check your email. You will find a message that contains all possible template variables you can use in a mailing message. You can use data from fields on:
   - Recipient's company
   - Recipient's contact card
   - Recipient's personalized e-marketing management links
   - Some licence and maintenance information
   - The user who is set to "Our Contact" on the recipient's company card.

     |  |
     | --- |
     | ourContact.company.address  ourContact.company.url  ourContact.company.name  ourContact.direct  ourContact.cellphone  ourContact.salutation  ourContact.title  ourContact.lastname  ourContact.middlename  ourContact.firstname  ourContact.email  ourContact.name |
   - The user who is set to "Our Sales Contact" on the recipient's company card

     |  |
     | --- |
     | ourSalesContact.company.address  ourSalesContact.company.url  ourSalesContact.company.name  ourSalesContact.direct  ourSalesContact.cellphone  ourSalesContact.salutation  ourSalesContact.title  ourSalesContact.lastname  ourSalesContact.middlename  ourSalesContact.firstname  ourSalesContact.email  ourSalesContact.name |

     **Note!** With template variables, you can also include User-Defined field values in your Mailing message. To do this, enter the Prog ID of the User Defined field as a variable in your Mailing message.

     ![](https://app.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6802257-wfNDFKD9ZuPbsb8w2BHDMF8oljFF7sWuKfYSGYAximMOuFg4L4Y4Kqzj3FlrAAE9-0/image-20260804105221-10.png)

     ![](https://app.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6802260-LwUhPR2WUDhcFZlqjPZrPUBgmxqWPB2HGTHKZ8pKpWCUT04ooSSqQSKJo4m0HA7q-0/image-20260804105409-12.png)

**Note!**You can alsouse functions that retrieve specific information. You can alter a date output by changing the variable format. Below are options that you can use.

YY4 = year, 4 digits
YY2 = year, 2 digits
MM2 = month, 2 digits
MM1 = month, 1 or 2 digits
DD2 = day of month, 2 digits
DD1 = day of month, 1 or 2 digits
MONTH = Name of month. Array of names must be passed as 3rd argument.
WDAY = Name of weekday. Array of names, starting with sunday, as 4th argument.

More information about the meaning of the fields you can find in [the SDK.](https://docs.superoffice.com/database/overview.html)

HH24: Hour of day, 2 digits, 24 hour format
H24: Hour of day, 1 or 2 digits, 24 hour format.
HH12: Hour of day, 2 digits, 12 hour format.
H12: Hour of day, 1 or 2 digits, 12 hour format
MI2: Minutes. 2 digits.
SS2: Seconds. 2 digits.
AMPM: AM/PM indicator, "am" or "pm"

**More information**

Docs: [Reply template variables (Service)](https://docs.superoffice.com/en/request/reply-templates/learn/template-variables.html)
