---
title: "How do I export data from SuperOffice CRM?"
url: https://community.superoffice.com/en/support-faqs/faq/how-do-i-export-data-from-superoffice-crm/
lang: en
updated: "8 Apr 2026"
---

# How do I export data from SuperOffice CRM?

Updated on 8 Apr 2026

When I want to export data from SuperOffice CRM, which options do I have?

There are three ways you can export data from SuperOffice CRM:

- [Export from a section tab or a selection to the Excel file](https://community.superoffice.com/en/support-faqs/faq/how-do-i-export-data-from-superoffice-crm/#1)
- [Export to a file from a selection to a delimited text file](https://community.superoffice.com/en/support-faqs/faq/how-do-i-export-data-from-superoffice-crm/#2)
- [Export all CRM data to the .bak or .sdb database file](https://community.superoffice.com/en/support-faqs/faq/how-do-i-export-data-from-superoffice-crm/#3)

**Export from a section tab or a selection to the Excel file**

In SuperOffice CRM, below the Company card (main) and the Mini card, you see the **Section tab** (1). The Section tab can contain, for example, lists of contacts, project members, sales, and activities that are linked to the relevant record in the main card. When the **Export** (2) button is enabled (see the note below to learn how to do it), you will see it at the bottom left side of the Section tab. It allows exporting the data from the Section tab to an Excel file.

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6166311-r5uMCKq2ME1bOonmMRHoKTxzZrbpnnk6oDnfsbXMBAE0K0YAn2nNL69l9XKQq7qa-0/image-20250407212834-2.png)

You can export data to an Excel sheet in **Selections** (1). Simply click on the **Task** (2) button to find the **Export to Excel** (3) option.

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6166312-GJlOlUzogKkfLN9rsOYwpwt7qe3cTmhxWI6ng0wTrQtnZ5SOTLmqeAWHGlGtudNc-0/image-20250407213028-3.png)

**Note!** If you are missing any data in the exported file, it’s because the column with this data was not set up in the Section tab before the export. You can configure columns by clicking on the **Settings wheel** and then selecting relevant columns.

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6166313-ojEcyrC8d3hFJ5HP5MrbCopKsgPszkFj8nAkggnrzyyjdJMdmWrF2bkGHynF2A5s-0/image-20250407213140-4.png)

**Export to a file from a selection to a delimited text file**

When you need to perform regular, predefined data export jobs, exporting data to a file is a great help. You can predefine the export file format in the template and reuse it. You can create as many templates as you want, for companies, contacts, activities, sales, etc.

Please follow the steps below to learn how to export data to a delimited text file:

1. Create an SXF template using Excel. Fill in SuperOffice variables in the first row fields using <> brackets. E.g, for company phone number use <cpho>. You can add as many variables as you want. Save the file as a tab-delimited txt file. After saving the file, change the extension to .sxf file format. [Click here](https://docs.superoffice.com/en/document/templates/learn/template-variables.html) to get a list of all SuperOffice variables.

2. Upload the template in Settings & Maintenance in the Document Template List. The template needs to be stored in the SO Archive.

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6166317-jNYJBr8JlxlX15s1SNFGJmiAJJxuUooZ43Y77zHSeOpzioH2uFJ9LsTSiN29oyKY-0/image-20250407214330-8.png)

3. Open your selection (1), click on the **Task** (2) button, and then choose the **Export to file** (3) option.

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6166314-eskWO7wywZti6BXHjZ315rn1Y5fqa1H7OeqEcgKo6sJcwwgC5uCprmAKq0ISe3Qt-0/image-20250407213612-5.png)

4. Select the export file from the drop-down list and click **Create**to export data.

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6166316-kSbsPpWMDaA7eNmKwL6grthFoCslzlgwwDWleOyFTzkXwwQYyBeO1zRt0nrybw4P-0/image-20250407214034-7.png)

5. A .txt file will be downloaded, which you can load in Excel when desired.

**Export all CRM data to the .bak or .sdb database file**

When you need to export all data from your SuperOffice CRM,  you can do it by creating a database backup.

- If you use SuperOffice Online, please follow [this FAQ.](https://community.superoffice.com/en/support-faqs/faq/how-do-i-obtain-the-backup-of-our-superoffice-online-database/)
- If you use SuperOffice Onsite, please follow [this FAQ.](https://community.superoffice.com/en/support-faqs/faq/how-do-i-make-a-backup-of-the-superoffice-crm-database/)

**Note!**

1. To be able to export data to an Excel or to a text file, a SuperOffice user must be assigned a role with a functional right ¨Can export data to file¨. In the [Settings and Maintenance](https://community.superoffice.com/en/support-faqs/faq/how-do-i-access-administration-part-settings--maintenance-in-superoffice-crm/), click on **Roles** (1), in the role list select the role your SuperOffice user has (2), click on the **Functional rights** (3) tab, and make sure that the functional right **Can export selections to file** (4) is in the right side column

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6166320-uzBsxjLblH1fHoIwduyxXzpJfydub4M2ziDn01IpGxIsJlFLxAzkIiFN4eJh4crb-0/image-20250407215349-11.png)
2. To be able to see the **Export** button in the Section tabs, the SuperOffice CRM user must have a preference enabling it. It can be enabled in the personal or system preferences. In [Settings and Maintenance](https://community.superoffice.com/en/support-faqs/faq/how-do-i-access-administration-part-settings--maintenance-in-superoffice-crm/), click on **Preferences** (1), in the drop-down list select **Functions** (2), and in the list of preferences select **Show Export button in the section tabs** (3), click on the **+Add** (4) button, and set up a preference for user, group, or whole system (5). Then save the preference by clicking on the **Save** (6)button.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6166319-2Kn4wcEmLa8Gj9eJ6qgrMjLlnWIyS7RqgwyRYuUNxMErSUemn1mWSnJR6Zz1YNfb-0/image-20250407215146-10.png)

**More information**

Blog: [Exporting data from SuperOffice as XML using SQL](https://community.superoffice.com/en/technical/blogs/archive/exporting-data-from-superoffice-as-xml-using-sql/)

SuperOffice App Store: [DataBridge for SuperOffice](https://online.superoffice.com/appstore/infobridge-software-b-v-/databridge-for-superoffice)
