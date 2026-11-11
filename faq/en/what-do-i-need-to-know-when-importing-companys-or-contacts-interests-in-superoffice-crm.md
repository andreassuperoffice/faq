---
title: "What do I need to know when importing company's or contact's interests in SuperOffice CRM?"
url: https://community.superoffice.com/en/support-faqs/faq/what-do-i-need-to-know-when-importing-companys-or-contacts-interests-in-superoffice-crm/
lang: en
updated: "24 Jul 2025"
---

# What do I need to know when importing company's or contact's interests in SuperOffice CRM?

Updated on 24 Jul 2025

How do I import more than one interest under Company or Contact in SuperOffice CRM?

To import more than one interest in the company or contact interest tab you need to be aware about following things.

1. Make sure that your import file is structured in the way that each interest resides in separate line. Please refer to the example below:

   Company 1; Interest A
   Company 1; Interest B
   Company 1; Interest C
   Company 2; Interest A
   Company 3; Interest C

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6275507-xgo2B48wP4Y1ugHAdxBlYOk1hGfI3h1Ft5M2mAYkuRorN7HHz70qsbSlLoTRiodq-0/image-20250724145546-2.png)
2. Please be aware that It is not possible to update an existing interest, however you may select an existing or include a new interest in both company and contact interest tabs.

- If you want to add existing interest - make sure your import file have the interest name written exactly as an existing interest.
- If you want to add new interest make sure in the **Import** (1) screen you have configured Import **Settings** (2) in the way that New interest values would have **Add new item to list** (3) option selected.

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6275510-5F4TBrkWDc7tSghhi9zF1i3ZxW3NQ0xgUAakZTEDFKo9NeqsXiO4Uc5ZwhS7ym9Y-0/image-20250724150100-3.png)

**Note!**SuperOffice CRM does not have import limits. However, import can fail due to reasons not related to the SuperOffice application. Therefore, we always advise splitting big imports in chunks. E.g. start with a small number of records and see if the data and import configuration works as you want. Then increase the chunks with every import.

**More information**

Video:[How to import customer contacts](https://www.youtube.com/watch?v=dVkCfpOkNl8&t=1s&ab_channel=SuperOfficeNetwork)
