---
title: "How do I configure SuperOffice Service that the customer gets an automatic notification when his request has been forwarded to a supplier?"
url: https://community.superoffice.com/en/support-faqs/faq/how-do-i-configure-superoffice-service-that-the-customer-gets-an-automatic-notification-when-his-request-has-been-forwarded-to-a-supplier/
lang: en
updated: "20 Aug 2025"
---

# How do I configure SuperOffice Service that the customer gets an automatic notification when his request has been forwarded to a supplier?

Updated on 20 Aug 2025

We want to automate the process when after forwarding a customer request to our supplier we inform the customer about it and set the status of a customer request to “Waiting for Supplier”. How can we do this?

To automate the process, you can create a new button in the Request screen using SuperOffice [Macros](http://docs.superoffice.com/en/automation/crmscript/learn/macro-script.html). This feature requires a **subscription to [Development Tools](https://docs.superoffice.com/en/admin/license/expander-services/tool-box.html)** (formerly Expander Services). Once enabled, you can set it up in your system by following the steps below:

[Step 1. Create a new request status](https://community.superoffice.com/en/support-faqs/faq/how-do-i-configure-superoffice-service-that-the-customer-gets-an-automatic-notification-when-his-request-has-been-forwarded-to-a-supplier/#1)

[Step 2. Create a new reply template](https://community.superoffice.com/en/support-faqs/faq/how-do-i-configure-superoffice-service-that-the-customer-gets-an-automatic-notification-when-his-request-has-been-forwarded-to-a-supplier/#2)

[Step 3. Create a macro that will automate the process](https://community.superoffice.com/en/support-faqs/faq/how-do-i-configure-superoffice-service-that-the-customer-gets-an-automatic-notification-when-his-request-has-been-forwarded-to-a-supplier/#3)

[Step 4. Create a button in Screen designer](https://community.superoffice.com/en/support-faqs/faq/how-do-i-configure-superoffice-service-that-the-customer-gets-an-automatic-notification-when-his-request-has-been-forwarded-to-a-supplier/#4)

​

**Step 1. Create a new request status**

Read this [Docs article](https://docs.superoffice.com/en/request/admin/status/create.html) to learn how to create a new status in SuperOffice Service step by step. You can call the new status "Waiting for supplier".

​

**Step 2. Create a new reply template**

Read this [Docs article](https://docs.superoffice.com/en/knowledge-base/learn/reply-templates/create.html) to learn how to create a new reply template step by step. This reply template will be sent to your customer after their requests are forwarded to the supplier.

​

**Step 3. Create a macro**

1. Go to the [SuperOffice Administration module](https://community.superoffice.com/en/support-faqs/faq/how-do-i-access-administration-part-settings--maintenance-in-superoffice-crm/), click on **CRMScript** (1), choose the tab **Macros and Scripts** (2), and click the button **New macro** (3).

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6297015-llq4I6o1p90cawZpF8JlQYq7zsJoFeB56CEgjdf6o0Ps9P3fQ3ENAp5Q7EC7BehI-0/image-20250820154951-1.png)
2. Enter the **Name** (1)for the macro, select the **Folder** (2)where this Macro should be stored, and click on the **Actions**(3)tab.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6297017-bhetMGBeC3ntOO330akBnGrgBNTcU3GfRB53IZY04T4mREpPfOO8jFGPpnS47T4j-0/image-20250820155033-3.png)
3. Choose to **Load a request** in the list of action types**.**

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6297065-05hzOrZ0MdxdilDxT7ZX1SbcPOeRGpa9Pqwur532ly85X3k57r5wB4O45cUkaBeT-0/image-20250820161328-4.png)
4. Click on ![](https://online2.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/4428657-zJ2hCTN1YJMUdyg8djln8kI889o76ZIJBWSmMFiS7hKgLUFPEO8dfBfpOKr2A028-0/image.png)and choose **Request ID** (1).Then click**New Action** (2) to add a new action.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6297086-8eqB9hCISQ0Dj0tc0DMcA7cxhT7Bwla4ub9ogHFsgUyUs8abl9Yus3Kg7qCOPLuA-0/image-20250820161351-5.png)
5. Choose to **Load a contact**in the list of action types**.**

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6297087-snG3hnykW8Y9fbwOPWKAmZkrJEdylGXxzriNY5nWZZ5QzJI7IQyaGCBt6D0HmQsi-0/image-20250820161415-6.png)
6. Click on ![](https://online2.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/4428657-zJ2hCTN1YJMUdyg8djln8kI889o76ZIJBWSmMFiS7hKgLUFPEO8dfBfpOKr2A028-0/image.png)and choose **Load request,**then **Customer ID** (1)**.** Then click**New Action** (2) to add a new action.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6297088-x377SgnTUgLGCXirCudg1Iqir32J3wMPPig1B350L7a3z4msHyqbHDC3yDeOa7FY-0/image-20250820161440-7.png)
7. Choose to **Load a reply template for merging**in the list of action types**.**

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6297089-GzjXpJFee8h6qTxeM7jypPaY6zO3GOigACCZAdOTyPuGCubTppyzN38YX9ZtIqrk-0/image-20250820161500-8.png)
8. Select the **Reply template** (1) that was created in step 2. In the Contact field, choose to **Load a contact/ID** (2) and click**on New action** (3).

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6297094-3qK4TPBxKN9WXTUl2qjdcCXw9jzuQZ8Tps6nsPAzoY4tXmEYjNIMROzgNkeydEfe-0/image-20250820161651-10.png)
9. Choose to **Send an e-mail or SMS**in the list of action types**.**

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6297096-guMG7FfntzH1bkbJtpxbgaoFl0gyaTeFAXe5AHyfFfzeGuEJfuhpz04Z8Gp52N8r-0/image-20250820161741-11.png)
10. In the **Subject** (1) field, write a short subject for the customer. In the **From** (2)field, write an e-mail address that the information should be sent from, in the field **To** (3)**,**choose to **Load a customer contact/E-mail address,** in the field **HTML message** (4),choose the **HTML text**, and click**on New action** (5).

    ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6297326-69aUSZ8u3FrkCs5P4yZQFdbpYpdhGCr5M9Ip9f8pFLd0anX2860htb1iF9gAOn18-0/image-20250820173101-1.png)
11. Choose to **Change a request**in the list of action types**.**

    ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6297153-Rk05Wb22FUfzXJuhAUUukUEjorZIKX7nFUgQjFcz0OLXeoDsHOMXK7jzBdq5kuGq-0/image-20250820162601-13.png)
12. In the **Status**field, choose **Waiting for supplier** (1)and click **OK** (2).

    ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6297154-c9dAjd0L6yEciwSty6UgUFG4n5AfwKIuW8zh1FpCQaMf51cucZBxqHolEzwlFUKZ-0/image-20250820162622-14.png)

​

**Step 4. Create a button in Screen designer**

1. Go to **Screen Designer** (1) and select **Request** (2). At the bottom of the screen, click the **Edit button** (3), then choose **Elements** (4) and **drag the Button** (5) onto the request screen.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6297335-ZyaauIKfR3ukszuQRn88I49urAgh9wBhhqcBP6auGbbB4SO0ZUura3p4LiZ7R2fl-0/image-20250820173958-2.png)
2. Click the button you dragged onto the request screen (1) to open its settings. Enter a **Name** (2), then set **Action to Execute CRMScript** (3). For **CRMScript**, select the **macro** you created (4). Finally, click **Save + Publish** to apply the changes to the request screen (5).

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6297356-EGnPXmccceblHMe6bSA382sW8GfDCrh5yBPBTOjDwuIkmZ1rafm3c8DxKsGrS3Wd-0/image-20250820175114-3.png)
3. After publishing, perform a flush by removing everything after default.aspx in the URL, adding ?flush, and pressing Enter. You will find a more detailed explanation of how to perform a flush and why the changes are not immediately visible in [this FAQ](https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-changes-made-in-settings-and-maintenance-are-not-visible-in-superoffice-crm/).

**Note!**

1. Scripts, Macros, Event Handlers, and Scheduled tasks can be created for you by a SuperOffice Consultant.

2. All support questions related to Scripts and SuperOffice SDK need to be posted in the [SuperOffice Community Developer Forum.](https://community.superoffice.com/en/technical/forums/)

**More information**

Docs: [Macros and scripts](https://docs.superoffice.com/en/automation/crmscript/learn/macro-script.html)

Docs: [Create a macro - example from SuperOffice](https://docs.superoffice.com/en/automation/crmscript/learn/create-macro.html)
