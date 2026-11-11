---
title: "How do I change a file  in the document template that is already created in SuperOffice CRM?"
url: https://community.superoffice.com/en/support-faqs/faq/how-do-i-change-a-file--in-the-document-template-that-is-already-created-in-superoffice-crm/
lang: en
updated: "8 May 2025"
---

# How do I change a file  in the document template that is already created in SuperOffice CRM?

Updated on 8 May 2025

I want to change an existing document in SuperOffice CRM. We have a new version of content and it will be quicker simply to upload a new file rather than copying and pasting all the changes into the old file. How do we do it?

1. Make sure to set your **Local settings** to "**Manually uploading and downloading files**" \*
   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6198158-K3YHXebUgFo6XyzjEi54ylQTAXarYcukdbIPql6LlJdKxlNbL2t0ZpQ8QHEQipQD-0/image-20250508125748-1.png)
   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6198159-lGbbx41bnCWoF6sBcSWWSpchK8XEyo6ngAjGC7diaPciYSFhiIf2nh15cIpud5ni-0/image-20250508125837-2.png)

   **\***If you are using SuperOffice onsite, with a version older than 10.2.10, then you need to turn off WebTools on your computer and refresh the browser before going to step 2.
2. Click on **Lists** (1) in the Navigator menu, select the **Document - Template** (2) option from the drop-down list and find the template, that you want to edit (3)
   .![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6198178-TQwGi6GITcLwUmpP3F9uP0HmwIiAksIBsD6PMGYbjby4a9HkmwAUoWyDRnYtSh6A-0/image-20250508130054-3.png)
3. Double-click on the document template’s name in the list. In the **Edit list item** screen click **upload**, then **Upload file** (select the new version of the file that you want to upload) and press **Save** (3).
   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6198179-40CcSZjSz7zsupF6lYp5uI35LpT5MbMe7CwN6dhaORRbGJzWA3PkyuwSxQRp033h-0/image-20250508130303-4.png)

   **Note!**The file name itself will not change in the system, since we are saving over the old file, not creating a new. After saving and opening the template again in the list, you will still see the name of the old file, even if the content will be overwritten with the new.
   The file format/extension will change if you are uploading a file in another file format. For example, if your original file is called “file1.doc” and you replace it with “file2.docx”, after saving and reopening the template in the list, the file will be called “file1.docx”.
4. If you want to change a document translation file, click on **Languages** (1) tab, select the language (2) that you need, click **Save** (3), then **Upload file** (4) and press **Save** (5) to finish.
   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6198185-GU79gNAewNi65Ydl111AfzK5gUpO9k1caQHmWSypOIm9lHe0CwgcxtNdqBT1sLzl-0/image-20250508130547-5.png)
5. After you’ve finished changing all documents, please connect your WebTools again by changing your local settings back to "**Use SuperOffice WebTools**"

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6198186-7FweXxyQKByOmYcyLKyRIiMdIsa2cSrNz2Yps1ATglguES341l3NR1AlfweSlbsL-0/image-20250508130644-6.png)
   **\*** If you are using SuperOffice onsite, with a version older than 10.2.10, then you need to connect WebTools again on your computer described in [this FAQ](https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-e-mails-and-documents-from-superoffice-crm-stopped-opening-with-microsoft-office-programs/).

**Note!**
We do not support changing the file extension/file format for a template with translations.
If you want to change the file extension for a file with a translation, for example, changing the file type from old .doc to the newer .docx format, then you will need to follow these steps:

1. Download all the language translation files.
2. Open and resave them in the new format.
3. Delete all the language translations in SuperOffice for this template.
4. Change the file extension of the default document according to the steps in this FAQ (steps 2 and 3).
5. Create the translations again with the new files in the new format.
