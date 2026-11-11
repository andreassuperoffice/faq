---
title: "How do I import products (price list) to SuperOffice CRM?"
url: https://community.superoffice.com/en/support-faqs/faq/how-do-i-import-products-price-list-to-superoffice-crm/
lang: en
updated: "24 Jul 2025"
---

# How do I import products (price list) to SuperOffice CRM?

Updated on 24 Jul 2025

How do I import products (price list) to SuperOffice CRM?

To import your products to SuperOffice CRM, simply follow the steps below:

1. Log in to [Settings and Maintenance](https://community.superoffice.com/en/support-faqs/faq/how-do-i-access-administration-part-settings--maintenance-in-superoffice-crm/).
2. Click on the **Import (1)** button in the navigator, then select **Products** (2), select an existing Price list from the **Import to price list (3)** drop-down menu, and click on the **Excel (4)** button.

   **Note!**If you want to create a new price list, please check [this article](https://docs.superoffice.com/en/sale/admin/quote/price-list-and-products.html#add-a-price-list), which explains how to do it.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6275563-3Eh3IhQzTbdiL7yIANbKBbe9Hty6wWMxDhqkdXCcQ6xo7KNDKYQyEc18iGE9roW4-0/image-20250724152222-1.png)
3. **Upload file** and upload an Excel file with the list of your products.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6275566-g9a2jNZdXeseMGGs9UL7bFgdWZAccGWx98PpTc98gn6Esad7GDRqukjoUXO5WyHR-0/image-20250724152304-2.png)

   **Note!**
   - The file should be prepared beforehand. While preparing import files take into consideration which field will be used for the duplicate match because this field must be unique.
   - Add the columns **Code, Name, List Price** - these are the mandatory fields.
   - As products from the file will be imported to one specific price list, therefore you don´t need a column for the **Price list name**.
4. Map the import file columns to SuperOffice CRM fields. Make sure that required fields are mapped otherwise, you won't be able to import the products.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6275579-4iHL7p1qNKGezC9KzzYILbONbFMz6opaDQAr49tQQd4uyOqoiH2frIYpXyhPjCEl-0/image-20250724152937-3.png)

   **Note!** If the Excel spreadsheet has a title row at the top, this will also be displayed in the list. You can remove this when you preview the data in the next step.
5. [Configure the import settings (products)](https://docs.superoffice.com/en/admin/import/learn/configure-import-settings.html) if necessary and click **Next.**
6. You will get a preview of your import, click **Import** if the import is correct.

**Note!**SuperOffice recommends you back up the SuperOffice database before you import large amounts of data. [This FAQ](https://community.superoffice.com/en/support-faqs/faq/how-do-i-obtain-the-backup-of-our-superoffice-online-database/) explains how to do it.

**More information:**

Docs: [Import products from Excel](https://docs.superoffice.com/en/admin/import/learn/import-products-from-excel.html)

Video: [How to import products into SuperOffice Quote](https://www.youtube.com/watch?v=xOTB6j2zzNo&ab_channel=SuperOfficeNetwork)
