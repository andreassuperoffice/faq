---
title: "What to do when I get an error \"Failed to communicate with server\" from SuperOffice MailLink?"
url: https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-i-get-an-error-failed-to-communicate-with-server-from-superoffice-maillink/
lang: en
updated: "5 Jun 2025"
---

# What to do when I get an error "Failed to communicate with server" from SuperOffice MailLink?

Updated on 5 Jun 2025

I have SuperOffice MailLink installed. When I am opening Outlook or archiving an email I get an error message:

*Failed to communicate with server*

Why does it happen and how do I fix it?

![](https://online3.superoffice.com/Cust1990/CS/scripts/rms.fcgi/getAttachment/5695509-YLgW98tsyubpL6nhsddIKELaUUFq9NH7JiEDomclGznTQBM7k5eg0Jeyp3fuFH7y-1/error%20mail-link.png)

This is a general error message and it can occur due to different reasons. To begin with please check which SuperOffice application type is configured in SuperOffice MailLink. To do it please follow the steps below:

1. Click on the arrow in the SuperOffice Ribbon in your Outlook it will open **Options**dialog.

   ![](https://online2.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/4388894-wDoUyw6l42wk0UX8QAnsxI6KPDflK9FEy9CkadyDsk5cO9t3j5d0hOlmCNB03x5m-0/image.png)
2. In **General settings (1)** check which **Preferred SuperOffice client (2)** is selected in your setup.

![](https://online2.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/4443413-8glP3z5ckpBS8qaE4Niggf4zhdbnfQxkTrcBxdDUMjWNHy7PqWp2QKw29tsW8l5i-0/image.png)

- If option **SuperOffice CRM (Web Client)** is selected click  [here](https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-i-get-an-error-failed-to-communicate-with-server-from-superoffice-maillink/#1).
- If option **SuperOffice CRM (Windows Client)** is selected click  [here](https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-i-get-an-error-failed-to-communicate-with-server-from-superoffice-maillink/#2).

**Note!** If the error comes up only when you archive e-mail as request it could be that the problem is caused by missing SOAP settings in SuperOffice Service, please check [this FAQ](https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-i-get-an-error-failed-to-communicate-with-server-when-archiving-an-e-mail-as-a-request-with-superoffice-mail-link/) to see how to fix it.

​

**SuperOffice CRM (Web Client)**

Please make a small test that will let know if it is possible to access a *TrayApp2.svc* from the computer that gets the error. To do it please copy the URL for *TrayApp2.svc (this will typically be "https://[your companies SuperOffice CRM URL]/Services/TrayApp2.svc" ) and*paste this in your browser.

- If you see [this screen](https://cs.superoffice.com/scripts/customer.fcgi/getAttachment/2231898-qpsjsj2tLbRtNqSjKkLDEE46GAdSNgKMW2gmjsTdq5aBQooGLfKiguUJhfyim0bo-0/Paste_8.png), it means you cannot access the SuperOffice server and the cause of the issue is on the server. These are the issues that we have seen before:
  - IIS is configured with multiple bindings of the same type, please check [this section](https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-i-get-an-error-failed-to-communicate-with-server-from-superoffice-maillink/#4).
  - SuperOffice WebTools / MailLink cannot resolve the domain name, please check [this section](https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-i-get-an-error-failed-to-communicate-with-server-from-superoffice-maillink/#5).
  - Some prerequisites are missing on the server, please check [this section](https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-i-get-an-error-failed-to-communicate-with-server-from-superoffice-maillink/#6).
  - IIS has problems with or is missing handler for *.svc* extensions, please check [this section](https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-i-get-an-error-failed-to-communicate-with-server-from-superoffice-maillink/#7).
- If you see [this screen](https://online2.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/3169149-frCXh4u5c6r75Ak637O4eY0HQ4elujOIfsS4sPKUbrBcNtbJck9bRWPgrekd5qZX-0/Successful%20Service%20Call.png), it means you can access the SuperOffice server and the cause of the issue is local. In this case, please follow the instructions in the first section of [this FAQ](https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-i-get-an-error-web-client-not-detected-when-i-try-to-archive-e-mail-from-outlook-to-superoffice-crm/).

​

**IIS is configured with multiple bindings of the same type​**

Windows Communication Foundation (WCF) does not allow more than one binding (of the same type) for one web site. The [Event Viewer](https://community.superoffice.com/en/support-faqs/faq/how-do-i-send-an-event-viewer-log-file-to-superoffice-support/) log on the server will display this error message:

*"Exception: System.ServiceModel.ServiceActivationException: The service '/SuperOffice/Services/TrayApp2.svc' cannot be activated due to an exception during compilation.
The exception message is: This collection already contains an address with scheme http. There can be at most one address per scheme in this collection.*"

To fix this issue please make sure that only one binding is present on the SuperOffice site in IIS, please check [this Microsoft documentation](https://learn.microsoft.com/en-us/iis/configuration/system.applicationhost/sites/site/bindings/binding) for more information about bindings.

**SuperOffice WebTools / MailLink cannot resolve the domain name**

If in the [Net Server log file](https://docs.superoffice.com/en/onsite/debug/web-client.html) you find this error message: *The remote server returned an error: (404) Not Found.* then make sure that the domain name in the WebTools / MailLink configuration URL can be reached from the computer with the problem. For testing, you can use [DNS LOOKUP](https://mxtoolbox.com/DNSLookup.aspx) online tool.

**Some prerequisites are missing on the server**

Please make sure that the SuperOffice web server meets all the requirements and has all prerequisites in place. Please check the [SuperOffice technical documentation](https://docs.superoffice.com/en/onsite/requirements/iis.html) for more information about the requirements.

​

**IIS has problems with or is missing handler for *.svc* extensions**

IIS needs a handler for .svc extensions on the SuperOffice IIS folder. If it fails or is missing then SuperOffice WebTools will show an error.

If the .svc handler is missing you need to add a **.Net Framework 4.5 Feature** called **HTTP Activation**

![](https://online2.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/4444053-jIAIDpcERrG7L4QMFpdTfgx2lu6UnrNI78I8URN2uxmnzUIRCLYuBINltsmn8qus-0/image.png)

If the .svc handler is installed, but it seems to be a cause of the error you can Revert to Parent the Handler Mappings on IIS server.

![](https://online2.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/4444056-qAdwZWzjYpDZLD09pQ6CRP33B2e6bWUOPNEaReFW0ppCqsnjUnSLCcqbSMokF7rQ-0/image.png)

**Note!** SuperOffice is not responsible for the damage these actions might cause to other applications therefore these actions should be performed by the administrator of the server.

​

**SuperOffice Windows Client**

Please make a small test that will let know if it is possible to access a SO Arc (document archive) on the SuperOffice server. Missing access could be causing the error.

Please find the SO Arc UNC in [SuperOfice.ini](https://docs.superoffice.com/en/onsite/install/win-client/superoffice-ini.html) file on your computer and then past it in the file explorer. Like the example in the screenshot below.

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6210475-gHW0bb725f7Lx10ngMfBQ0cip193RefQntPPTPO2T9DjLowRyCeN2rEd4NIEJLAJ-0/image-20250519132140-1.png)

- If you cannot access So Arc location it could mean either:
  - Your computer does not have access to SO ARC folder. In this case please make sure that your computer is configured so it can access the folder. That is the [requirement](https://docs.superoffice.com/en/onsite/requirements/iis.html) for all SuperOffice Windows application users.
  - You need to be connected to the company's network via the VPN and it could be that your VPN client is not started. In this situation, you will not have access to the SO Arc folder. Please make sure that you use SuperOffice when VPN is started.
- If you can access the So Arc folder the situation requires further investigation therefore please [contact SuperOffice support](https://community.superoffice.com/en/support-faqs/faq/how-do-i-register-a-support-request-from-within-superoffice-crm/).
