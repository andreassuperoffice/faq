---
title: "What is the maximum size of an attachment which can be uploaded in SuperOffice CRM?"
url: https://community.superoffice.com/en/support-faqs/faq/what-is-the-maximum-size-of-an-attachment-which-can-be-uploadedin-superoffice-crm/
lang: en
updated: "28 Mar 2026"
---

# What is the maximum size of an attachment which can be uploaded in SuperOffice CRM?

Updated on 28 Mar 2026

What is the maximum size of an attachment which can be uploaded in SuperOffice CRM?

SuperOffice CRM Online and Onsite have different limitations concerning the size of attachments. For more specific information, please read the sections below:

[Please click here if you use SuperOffice CRM Online](https://community.superoffice.com/en/support-faqs/faq/what-is-the-maximum-size-of-an-attachment-which-can-be-uploadedin-superoffice-crm/#1)

[Please click here if you use SuperOffice CRM Onsite](https://community.superoffice.com/en/support-faqs/faq/what-is-the-maximum-size-of-an-attachment-which-can-be-uploadedin-superoffice-crm/#2)

​

**Attachment size limits in SuperOffice CRM Online**

**Documents in SuperOffice CRM**

The maximum size of a document upload in SuperOffice CRM is 94.4 MB, and the time for a file upload is 5 min.

This means that, for example, you need about 2,5–3 Mbit/sec upload speed to be able to add/edit a 94 MB file to SuperOffice CRM Online.

**Attachments in Mailings and Service**

The maximum size of attachments in SuperOffice Mailings and Service messages in requests is 25 MB, both for incoming and outgoing messages.

One message in a request (ticket) in SuperOffice Service, for example, cannot have 3 attachments each the size of 10 MB, because the total attachment size will exceed 30 MB.

**Note!**

Newest information for attachment size limits in SuperOffice Online can also be found in Docs: [System requirements for SuperOffice CRM Online](https://docs.superoffice.com/en/online/system-requirements.html)

​

**Attachment size limits in SuperOffice CRM Onsite**

SuperOffice Web Onsite installation does not have file size limitations. However, the IIS server, where SuperOffice is installed, might have.

For example, an IIS server might only allow processes (e.g., file uploading) to run for a limited time (e.g., 60 seconds). Therefore, if your file upload takes longer than that, it will fail. Or it could be that the IIS server has a restriction on the content length. This means that, when your file exceeds a default limit (30000000 bytes - roughly 28.6 MB), the upload process will fail. To change this restriction, you can follow the steps below:

1. Select your SuperOffice site and double-click on **Request Filtering**

   ![](https://online2.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/3507369-byrTeQnH9xeol2c6DASPhxSLXXjFB6yNZteP79GSDI60hEiC3GAwAB44Kn2P6Dsp-0/image.png)
2. Click on **Edit Feature Settings** and in the **Maximum allowed content length** field set another limit to attachment sizes, then click **OK** to finish.

   ![](https://online2.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/3507374-JKy2ydGkQlrrprruFExsjhEejj2KgCMjwUB7y3tfcRlo5tlqHqIid09iSJksfPcd-0/image.png)
