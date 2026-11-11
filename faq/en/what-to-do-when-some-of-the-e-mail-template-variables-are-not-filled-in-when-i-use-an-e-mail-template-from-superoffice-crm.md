---
title: "What to do when some of the e-mail template variables are not filled in when I use an e-mail template from SuperOffice CRM?"
url: https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-some-of-the-e-mail-template-variables-are-not-filled-in-when-i-use-an-e-mail-template-from-superoffice-crm/
lang: en
updated: "19 Mar 2026"
---

# What to do when some of the e-mail template variables are not filled in when I use an e-mail template from SuperOffice CRM?

Updated on 19 Mar 2026

I create a new e-mail from SuperOffice CRM using an e-mail template with the variables. Some of the variables are not filled in. Why does it happen, and how do I fix it?

Sometimes, template variables can be enclosed in other HTML tags, making them unrecognizable to the SuperOffice parser. After making a new e-mail template or editing an existing one, the corrupted variable might appear. In this situation, instead of the data from SuperOffice CRM that has to be parceled, the template will pass a variable itself. This is illustrated in the example below.

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6593706-UOnkQntdcTDABGzcBsM6nKbJy7XAZaQPpAMNWkZSXXkZd41eYHGewjSyF060Jnnd-0/image-20260319081636-1.png)

To fix a template, you'll have to clean the failing variables manually. Please follow the steps below to do it:

1. Open your e-mail template as a text file (Notepad).
2. The whole HTML of the message will appear. All the variables in the file should appear two times. The first one looks perfectly fine (marked in green).

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6593707-lDUzzLOYPpkcoIScZFKt6tiGnRRSUZeEzm3cMePnhRonJCWJtuc1k8kxC2fPOiWK-0/image-20260319082501-2.png)
3. Press **CTRL+F.**This option will help you to find the other variable in the file.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6593708-KWdIrkLdRn9NCleaTHklFCpEDknhnlbqzJL61mtcuXef72hNGxBONly88hUEQtkD-0/image-20260319082634-3.png)

   You will find the variable that will be surrounded by extra signs (marked in orange).

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6593712-njib0btyPW3Zspu5OUuGDDAptZZIjKbaTuEwdpUcqe342GWxY2NrrxTWPKzMaieh-0/image-20260319085114-5.png)
4. Remove it so the variable would be surrounded only by brackets {} (example in green).

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6593713-fAaiOpk0gPszCX6N8Dt13kUD7tXCTYSztJeJQQx01tACb8sjE7zO9a3yI5kWOfBy-0/image-20260319085305-6.png)
5. Save the file and upload it to [Settings and Maintenance](https://community.superoffice.com/en/support-faqs/faq/how-do-i-access-administration-part-settings--maintenance-in-superoffice-crm/).
6. Test it to make sure that all variables are visible.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6593723-2WC5eCf1ixQgA3Dola0uSGrr9HCN8MtL7aAeWcHAxEpwORyZ8Ma9CjNB3C7E98up-0/image-20260319090218-7.png)

**More information**

FAQ: [How do I create and use e-mail templates in SuperOffice CRM?](https://community.superoffice.com/en/support-faqs/faq/how-do-i-create-and-use-e-mail-templates-in-superoffice-crm/)
