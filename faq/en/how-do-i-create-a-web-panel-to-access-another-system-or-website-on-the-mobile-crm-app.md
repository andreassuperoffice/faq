---
title: "How do I create a web panel to access another system or website on the Mobile CRM app?"
url: https://community.superoffice.com/en/support-faqs/faq/how-do-i-create-a-web-panel-to-access-another-system-or-website-on-the-mobile-crm-app/
lang: en
updated: "25 Feb 2026"
---

# How do I create a web panel to access another system or website on the Mobile CRM app?

Updated on 25 Feb 2026

I would like to see all publicly accessible information about the company's stored in CRM in a separate tab on my Mobile CRM app. How can I set it up?

You can easily create a web panel displaying any website accessible on the internet. In addition, you can adjust the website URL so that it will automatically fill in the known data of the company from Mobile CRM data.

In this example, we will show you how to create a web panel, which would automatically show information about the company from the D&B Hoovers – the world's largest commercial database: <https://www.hoovers.com>

Please follow the steps below:

1. Tap on the **Menu**button in the middle of the screen and choose the item **Settings** from the menu.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6556225-IjTwfpEPC6JK07Kj0nQbTtlZiNzUgxCy1HHIi1pHuateoKuj3dde1aAqzCyctMoN-0/image-20260225164544-1.png)
2. In the **Settings**, tap on the **Web panels and links** option.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6556226-ZrmBWMI4M37wdZ1i10ewErLdqIJnpJLoFBCDWEMds6eO598wlyMrA7bpi21maEnO-0/image-20260225164640-2.png)
3. Tap the **Add** button.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6556251-Q7lAtciiBBBpGEo1y7lIoo6HkpahkONNIj73pRBFf9yQLgRYY6C2JJNb6z7LtZDS-0/image-20260225164928-3.png)
4. In the **Name (1)** field, fill in the name of the web panel. In the **URL** (2) – insert the link to a website you want to display. In this example, we want the web panel to display the information about the company in Hoovers website, which is why we are creating a URL with the company’s name variable as a search parameter in the URL. *http://www.hoovers.com/company-information/company-search.html?term=<name>*

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6556260-ZEnMQlB6DSUSDG9TsqHWD9hJfLZdHecXyxxYDSEy740yfeIFkaGDtK36ZpP4NMZ7-0/image-20260225165033-4.png)

   Since we want to open a website in the web panel, the **Task type** (3) should stay *WWW tab,* and as **Location** (4),we choose the *Company* screen. Tap on the **Save** (5)button to store the settings.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6556261-pgXwi1Y69R3yO8Ub81oT1KFotnwUOFw6QyCbLJEXj2Z7hFQHM9Oll3SAKK4JM94S-0/image-20260225165144-5.png)
5. Navigate to the company record and scroll down to the bottom of all available information - there you will see the Webpanels tab and the web panel you just created.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6556269-Bjjlu0IYuZ13ltFoMJa3ligo8i6X9Bh2oQSGF4pY2g80PqMwwTy131zLLmPCOWBg-0/image-20260225165308-6.png)

   **Note!** The app uses icons and the rank of Web Panels that are created using [Settings and Maintenance](https://community.superoffice.com/en/support-faqs/faq/how-do-i-access-administration-part-settings--maintenance-in-superoffice-crm/) and published for mobile devices. The web panels set up in Settings and maintenance appear by default in front of the ones set up on the app. Please check [this FAQ](https://community.superoffice.com/en/support-faqs/faq/how-do-i-create-a-new-web-panel-in-superoffice-crm/) to learn how to create a web panel in SuperOffice CRM.

**More information**

FAQ: [How do I add a new web panel in SuperOffice?](https://community.superoffice.com/en/support-faqs/faq/how-do-i-create-a-new-web-panel-in-superoffice-crm/)
