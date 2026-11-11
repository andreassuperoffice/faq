---
title: "How do I create a new web panel in SuperOffice CRM?"
url: https://community.superoffice.com/en/support-faqs/faq/how-do-i-create-a-new-web-panel-in-superoffice-crm/
lang: en
updated: "3 Jan 2026"
---

# How do I create a new web panel in SuperOffice CRM?

Updated on 3 Jan 2026

How do I create a new web panel in SuperOffice CRM?

To create a new web panel in SuperOffice CRM, please follow the steps below:

1. Log in to [Settings and Maintenance](https://community.superoffice.com/en/support-faqs/faq/how-do-i-access-administration-part-settings--maintenance-in-superoffice-crm/).
2. Click on **Lists (1)**, select the **GUI - Web panel (2)** from the selection list, and click on the **+Add (3)**button**.**

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6359506-txxotRHrmNCL46A51zlHurs9FjhNOLGmXID9G8xlKyZjdrQqeylKeYLe68eduKH7-0/image-20251009203335-1.png)
3. Enter the required name of the item in the **Name (1)**field. This name is displayed when you add the URL address in SuperOffice CRM.

   **Note!** This is a mandatory field and must therefore be filled in.

   In the **URL(2)**field, specify the URL address. This might be an Internet page or a server-based HTML file.

   **Note!** If SuperOffice CRM is installed on an HTTPS site, web panels using HTTP URLs will not work. You must use HTTPS URLs. In the **Window name (3)** field, specify the required name of the browser window in which the URL address is to be opened. The window name, as it will finally appear, is displayed below.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6359538-TYlLKNILboW7drTcShDjanmMXZsqLZDUT9uXHmky3TisEJnZ1wEeFjHU6UI1nrrX-0/image-20251009210827-8.png)
4. In the **Visible in** the list box, choose where the URL address will be accessible in SuperOffice CRM.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6359540-jDQpzJgfLihApu6nxbZ8Ej01iH8ySiZYQ9UyPzZIaElpQjiZknAC93TDM2G0udiX-0/image-20251009210914-10.png)
   - **Side panel**: select this option to make the URL address available on the side panels in the SuperOffice CRM.

     ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6359547-Ay6OtLE5EemiQBp0j7YqsYiTUNNHUU3DL7gkEuLiJmu7GQ9pFSISwZZwUS5M28uK-0/image-20251009211813-17.png)
   - **Toolbar**: legacy option. Online customers may see this setting, but enabling it will not display the URL on the toolbar.
   - **Navigator button**: select this option to make the URL accessible as a button in the navigator in SuperOffice CRM.

     ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6359542-OYQGI211DpjQd7EikPT3sk6kcfpoHH5T19WMs33HY9dw4HKskSAdUjamXTWtwsT6-0/image-20251009211125-12.png)
   - **Panel**: select [an option in this list](https://docs.superoffice.com/en/admin/lists/learn/web-panel-add-item.html#options) to make the URL accessible as a panel/tab in SuperOffice CRM. An example from a sales card:

     ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6359548-oUrn5LzfS9MEB8u0hoSwzoljKySDOndCBtj9qP2Le583wT26Sn56l2ZHIrqcIg0P-0/image-20251009212850-1.png)
   - **Dialog**: select an [option in this list](https://docs.superoffice.com/en/admin/lists/learn/web-panel-add-item.html#options) to make the URL address accessible in a dialog. An example from a dialog for follow-ups:

     ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6359549-iIFZ1xh9dgW5Yp60mTqOqHca7W70NPxG8zwsLgTNJ5RCJFwMN7tU9FwU3oNCLZkI-0/image-20251009213208-2.png)
   - **Menu**: select an [option in this list](https://docs.superoffice.com/en/admin/lists/learn/web-panel-add-item.html#options) to make the URL accessible on one of the menus in SuperOffice CRM.

     ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6359550-jYcGODlQDHI9nYOhw85sPZl7pf03RllUsnYXay8rsSarLBUlwmcs1teJnyQ7PefG-0/image-20251009213445-3.png)
5. In the **URL encoding** list box, you can select whether the URL should be ANSI or Unicode (or no format).

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6359543-eNRwwaIs2S3EPeboFTuuo8y5ScEbKIRBBFkrfq6m0f4X4l6zTnjZeP6cF4pELCet-0/image-20251009211151-13.png)
6. Under **Available on,**choose where you want the URL address to be available. You can select several of these options simultaneously.
   - **SuperOffice CRM for Web**: when you are using the Web version of SuperOffice CRM.
   - **Mobile CRM**: when you are using the mobile version of SuperOffice CRM.

     ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6359544-bsIjzgn4DJXKM41T5ptwZamIfJwFBINUsmQ5jyUErxYhYACldkGTiRs7kTFPGhZC-0/image-20251009211218-14.png)
7. Extra settings:

   **Always reload** content on tab navigation - reloads tab content each time it’s opened to ensure the latest data is shown.
   **Do not reload** content when navigating to the main card - keeps tab content unchanged when reopened, reducing data loading if it doesn’t rely on main card data.
   **Show link** for opening in a separate window - adds a link to open the content in a new window.
8. Click the Icon list to select an **icon** (1)for the web panel. Optionally, type in a description of the item in the **Description** (2)field; it will be visible in the list of all web panels in Settings and Maintenance. And click **Save** (3)to save the changes.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6359546-E3sCykaFWGywTT4gQq20EPqWIzmS6pBX0gD5zEpot441FJu0ENg0DAbSWkXRxiao-0/image-20251009211438-16.png)

**More information**

Docs: [GUI - Web panel](https://docs.superoffice.com/en/admin/lists/learn/web-panel.html)

FAQ: [How do I create a web panel to access another system or website on the Mobile CRM app?](https://community.superoffice.com/en/support-faqs/faq/how-do-i-create-a-web-panel-to-access-another-system-or-website-on-the-mobile-crm-app/)
