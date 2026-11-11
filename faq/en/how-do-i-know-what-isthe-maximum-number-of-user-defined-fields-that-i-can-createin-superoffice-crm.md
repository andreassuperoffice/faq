---
title: "How do I know what is the maximum number of user-defined fields that I can create in SuperOffice CRM?"
url: https://community.superoffice.com/en/support-faqs/faq/how-do-i-know-what-isthe-maximum-number-of-user-defined-fields-that-i-can-createin-superoffice-crm/
lang: en
updated: "16 Apr 2025"
---

# How do I know what is the maximum number of user-defined fields that I can create in SuperOffice CRM?

Updated on 16 Apr 2025

How do I know what is the maximum number of user-defined fields that I can create in SuperOffice CRM?

SuperOffice CRM allows creating user-defined fields in [Settings and Maintenance](https://community.superoffice.com/en/support-faqs/faq/how-do-i-access-administration-part-settings--maintenance-in-superoffice-crm/), under **Fields** (1). A maximum of 119 fields are available per section (2).

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6177490-sxFPCU7jbOFEjiRUcFjsnCDLRFKoHCHSfubgQWxajPSxjaEwhHkl8uwoEPg5oQPO-0/image-20250416151637-1.png)

There is a limit of the field types that can be used per section. You may create a maximum of:

- 60 fields (of which 4 must be indexed) of types number, date, check-box and list.
- 40 fields (of which 4 must be indexed) of types short text and unlimited date.
- 9 fields (of which 4 must be indexed) of type long text.
- 10 fields (of which 4 must be indexed) of type decimal.

The fields that can be used stand for the types that are explained under the image.
![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6177512-GMMOKM6qQzaGwZyEgQL3BRlpBrASsCAQ3ommj9XPbUg2sPXKacKXwReuGm2BWbPZ-0/image-20250416155223-2.png)

- Number (1) fields use Long fields that are stored in the UDXXXsmall table in the database.
- Short text (2) fields use String[40] fields. When the number of String[40] fields finish, it will start using String[200].
- Long text (3) fields use String[200] fields that are stored UDXXXLarge table in the database.

  **Note!**If the short text fields occupied space of the long text fields it will decrease the available number of fields for the long text type fields.
- Date (4) fields use String[200] fields that are stored UDXXXLarge table in the database.
- Unlimited date (5) fields use String[40] fields.
- Checkbox (6) fields use String[200] fields that are stored UDXXXLarge table in the database.
- Drop-down (7) fields use String[200] fields that are stored UDXXXLarge table in the database.
- Decimal (8) fields use a double type of fields.

In total there are 60 Long, 40 String[40], 10 Double and 9 String[200].

**Note!** If you do not index (1) (make it searchable in the free-text search) any field, you will have 56 Long type fields to use. In other words, you lose the space of 4 fields. The same rule applies to String[40] (36), Decimal (6) and String[200] (5) type fields.

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6177514-EPOlULiJIejdWX82CMIqubqfjOwsqQg7DirQ5rjKxerN6AzzZc55PjC6FjF06gp8-0/image-20250416155344-4.png)

**More information:**

Video**:**[How to add a user-defined field to SuperOffice](https://www.youtube.com/watch?v=SpeZVxpxeMM&list=PL9fefjwA0X290ZZ8bMUHWh_d6s3Y2P0Jr&index=16&ab_channel=SuperOfficeNetwork)

FAQ: [Why I cannot change a type of an already created user define field?](https://community.superoffice.com/en/support-faqs/faq/how-do-i-change-a-type-of-a-user-defined-field-which-i-created-before/)
