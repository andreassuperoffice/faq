---
title: "What to do when I get an error '34255555555' is not a valid value for this property. Valid values are from Int32.MinValue through Int32.MaxValues' after clicking on the Archive E-mail button in SuperOffice Outlook Ribbon?"
url: https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-i-get-an-error34255555555-is-not-a-valid-value-for-this-property.-valid-values-are-from-int32.minvalue-through-int32.maxvalues-after-clicking-on-the-archive-e-mail-button-in-superoffice-outlook-ribbon/
lang: en
updated: "12 Jun 2025"
---

# What to do when I get an error '34255555555' is not a valid value for this property. Valid values are from Int32.MinValue through Int32.MaxValues' after clicking on the Archive E-mail button in SuperOffice Outlook Ribbon?

Updated on 12 Jun 2025

After clicking on the **Archive E-mail** button in SuperOffice Outlook Ribbon I get an error:

*'34255555555' is not a valid value for this property. Valid values are from Int32.MinValue through Int32.MaxValues.*

Why does it happen and how do I fix it?

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6237387-NzqnmtYo9YYB70F5DEpPBormnrzEUDw75gf2GMChu1gXWhZmDpu99fFlydODreuA-0/image-20250612143657-1.png)

The error occurs when the archiving dialog coordination key or keys have an invalid value in Windows Registry. To fix it, please follow the steps below:

1. In the search box type in *regedit*and open Registry Editor program.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6147299-aHzH1OQksFdpHSLNYxoJmQ99METrmXcFmSoYcOdmMdwnuzDOEInniMI2Nx6800LH-0/image-20250326172509-1.png)
2. Navigate to *Computer\HKEY\_CURRENT\_USER\Software\SuperOffice\MailLink\*and check all the keys under **MailLink**. One of them has a number from the error message as a value. In this example, the **ArchiveAsDocument** key, **WindowsHeight** has a value, which is out of the range.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6237440-DUqULs6uNY1BtRhRgax6zF2yDca3uP7Leq2OA672u5gAmfo2B2MChoK6ymeIu0C5-0/image-20250612144104-2.png)
3. To fix it, double-click on the wrong value and change it to *-1* (default) and click **OK** to save it.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6237443-dNmEk1sRXlljCpdcrGrPUhMg6t52UeXPuLssF6Y1Y64jExwCrCtsKWwb3xlwdJDi-0/image-20250612144147-3.png)

**More information**

FAQ: [What can I do when I run into the problems with archiving e-mails from Outlook to SuperOffice CRM?](https://community.superoffice.com/en/support-faqs/faq/what-can-i-do-when-i-run-into-the-problems-with-archiving-e-mails-from-outlook-to-superoffice-crm/)
