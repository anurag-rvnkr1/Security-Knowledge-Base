# 09-HTML-CSS-JavaScript-Security.md

# Part 1 — Introduction to HTML, CSS, JavaScript, Browser Rendering, DOM, and Client-Side Security Fundamentals

> **"Every web page is built using HTML, CSS, and JavaScript. Understanding how browsers interpret these technologies is essential for identifying client-side vulnerabilities such as XSS, DOM manipulation flaws, insecure JavaScript, and UI-based attacks."**

---

# Learning Objectives

After completing this part, you will understand:

- HTML Fundamentals
- CSS Fundamentals
- JavaScript Fundamentals
- Browser Rendering
- DOM (Document Object Model)
- HTML Elements
- CSS Styling
- JavaScript Execution
- Client-side vs Server-side
- Why Frontend Security Matters
- Enterprise Frontend Architecture

---

# Introduction

Every modern website consists of three core technologies:

```
           Web Page

        ┌───────────────┐

        │     HTML      │

        │   Structure   │

        ├───────────────┤

        │      CSS      │

        │ Presentation  │

        ├───────────────┤

        │ JavaScript    │

        │  Behaviour    │

        └───────────────┘
```

Together they create interactive web applications.

---

# HTML

HTML stands for:

```
HyperText

↓

Markup

↓

Language
```

HTML defines the **structure** of a webpage.

---

# HTML Responsibilities

HTML describes:

- Headings
- Paragraphs
- Images
- Links
- Forms
- Tables
- Videos
- Buttons
- Inputs

Think of HTML as the **skeleton** of a webpage.

---

# HTML Example

```
Page

│

├── Heading

├── Paragraph

├── Image

├── Button

└── Form
```

Without HTML, browsers have no structure to display.

---

# CSS

CSS stands for:

```
Cascading

↓

Style

↓

Sheets
```

CSS controls the appearance of HTML.

---

# CSS Responsibilities

CSS defines:

- Colors
- Fonts
- Layout
- Position
- Animation
- Spacing
- Responsive design
- Visual effects

Think of CSS as the **skin and clothing** of a webpage.

---

# CSS Example

Without CSS:

```
Simple Text
```

With CSS:

```
Styled Text

Buttons

Cards

Navigation

Responsive Layout
```

---

# JavaScript

JavaScript provides interactivity.

Examples:

- Form validation
- Dynamic updates
- API requests
- Animations
- Interactive menus
- Notifications
- Authentication logic
- Real-time updates

Think of JavaScript as the **brain and muscles** of the webpage.

---

# HTML + CSS + JavaScript Together

```
HTML

↓

Page Structure

+

CSS

↓

Visual Design

+

JavaScript

↓

Interactivity

=

Modern Website
```

---

# Browser Rendering Process

When visiting a website:

```
Browser

↓

Download HTML

↓

Parse HTML

↓

Build DOM

↓

Download CSS

↓

Build CSSOM

↓

Execute JavaScript

↓

Render Page
```

Each stage influences how the page is displayed.

---

# What is the DOM?

DOM stands for:

```
Document

↓

Object

↓

Model
```

The DOM is an in-memory representation of the webpage created by the browser.

---

# DOM Tree

Example page:

```
HTML

↓

HEAD

↓

BODY

├── H1

├── P

├── FORM

│

├── INPUT

└── BUTTON
```

Every HTML element becomes a DOM node.

---

# Why DOM Matters

JavaScript does **not** directly modify HTML files.

Instead:

```
JavaScript

↓

DOM

↓

Browser

↓

Updated Page
```

The browser updates the visible page based on DOM changes.

---

# Browser Parsing

The browser reads HTML from top to bottom.

```
HTML

↓

Parser

↓

DOM

↓

Rendering
```

Malformed HTML may lead to unexpected rendering behavior.

---

# HTML Elements

Common HTML elements include:

| Element | Purpose |
|----------|----------|
| `<html>` | Root document |
| `<head>` | Metadata |
| `<title>` | Page title |
| `<body>` | Visible content |
| `<div>` | Generic container |
| `<span>` | Inline container |
| `<form>` | User input |
| `<input>` | Input field |
| `<button>` | Clickable button |
| `<img>` | Image |

---

# HTML Attributes

Elements often contain attributes.

Examples:

- id
- class
- src
- href
- alt
- value
- placeholder
- type
- disabled

Attributes provide additional information and behavior.

---

# CSS Selectors

CSS targets HTML elements using selectors.

Common selector types:

- Element selector
- Class selector
- ID selector
- Attribute selector
- Descendant selector
- Child selector

Selectors determine which elements receive styling.

---

# CSS Cascade

When multiple rules apply:

```
Multiple Rules

↓

Priority

↓

Winning Rule

↓

Displayed Style
```

Understanding precedence helps avoid unexpected styling.

---

# JavaScript Execution

JavaScript executes inside the browser.

```
Browser

↓

JavaScript Engine

↓

DOM Access

↓

User Interaction
```

Modern browsers execute JavaScript using optimized engines.

---

# JavaScript Can

JavaScript can:

- Modify HTML
- Modify CSS
- Read forms
- Send HTTP requests
- Store data
- Display notifications
- Process user input
- Update the page without reloading

---

# Client-Side vs Server-Side

```
Browser

↓

HTML

↓

CSS

↓

JavaScript

(Client Side)

──────────────

Server

↓

Application Logic

↓

Database

(Server Side)
```

The client focuses on presentation and interaction, while the server performs trusted business logic and data processing.

---

# Why Client-Side Security Matters

Browsers execute code received from web servers.

If malicious code reaches the browser:

```
Malicious Script

↓

Browser Executes

↓

User Data

↓

Potential Compromise
```

Many web attacks target client-side execution.

---

# Browser Trust Model

A browser assumes that:

```
Website

↓

Delivered Code

↓

Execute
```

Security mechanisms such as the Same-Origin Policy (SOP), Content Security Policy (CSP), sandboxing, and permission controls help reduce risks, but unsafe application code can still introduce vulnerabilities.

---

# Enterprise Frontend Architecture

```
Browser

↓

HTML

↓

CSS

↓

JavaScript

↓

REST API

↓

Application Server

↓

Database
```

The frontend communicates with backend services through APIs.

---

# Frontend Security Goals

A secure frontend should:

- Protect user data
- Prevent unauthorized script execution
- Validate user input
- Use HTTPS
- Handle errors safely
- Minimize exposed information
- Communicate securely with APIs

---

# Common Client-Side Risks (Overview)

Common categories include:

- Cross-Site Scripting (XSS)
- DOM-based vulnerabilities
- Clickjacking
- Insecure JavaScript
- Sensitive data exposure
- Third-party script compromise
- Client-side storage misuse

Each topic will be covered in later chapters.

---

# Real Enterprise Example

An online banking portal loads:

```
Browser

↓

HTML

↓

CSS

↓

JavaScript

↓

Authentication API

↓

Account Dashboard
```

The browser:

- Builds the DOM
- Applies CSS
- Executes JavaScript
- Requests account data from secure backend APIs
- Displays personalized information

The security of each layer contributes to the overall security of the application.

---

# Hands-on Lab (Conceptual)

Using your browser:

1. Open any website.
2. Launch Developer Tools.
3. Inspect the HTML structure.
4. Explore the DOM tree.
5. View applied CSS rules.
6. Observe JavaScript files loaded by the page.
7. Refresh the page and monitor the Network panel to see HTML, CSS, and JavaScript being downloaded.

---

# Interview Questions

1. What are the roles of HTML, CSS, and JavaScript?
2. What is the DOM?
3. How does a browser render a webpage?
4. What is the difference between client-side and server-side processing?
5. Why is JavaScript important in modern web applications?
6. What is the CSS cascade?
7. What are HTML attributes?
8. Why is frontend security important?
9. Can JavaScript modify HTML after a page loads?
10. What security mechanisms help protect browser execution?

---

# Best Practices

- Separate structure, presentation, and behavior.
- Use semantic HTML where appropriate.
- Keep JavaScript modular and maintainable.
- Load resources securely over HTTPS.
- Minimize unnecessary client-side logic for sensitive operations.
- Validate data on both the client and the server.
- Regularly review third-party scripts and dependencies.

---

# Common Mistakes

- Assuming client-side validation alone provides security.
- Exposing sensitive information in HTML or JavaScript.
- Embedding secrets or API keys in frontend code.
- Overloading pages with unnecessary JavaScript.
- Ignoring browser security features and headers.
- Trusting all data received from the browser.

---

# Key Takeaways

- HTML provides the structure of a webpage, CSS controls its presentation, and JavaScript enables interactivity.
- Browsers parse HTML, build the DOM, apply CSS, execute JavaScript, and render the page.
- The DOM is the interface through which JavaScript modifies web content.
- Client-side code improves user experience but should never be treated as a trusted security boundary.
- Understanding frontend technologies is essential before studying vulnerabilities such as XSS, DOM-based attacks, and insecure client-side logic.

# 09-HTML-CSS-JavaScript-Security.md

# Part 2 — HTML Forms, CSS Security, JavaScript Execution, DOM Manipulation, Events, Browser APIs, and Client-Side Attack Surface

> **"Every interactive webpage relies on forms, JavaScript events, DOM manipulation, and browser APIs. Understanding how these components work is essential before learning advanced client-side attacks such as XSS, DOM-based vulnerabilities, and clickjacking."**

---

# Learning Objectives

After completing this part, you will understand:

- HTML Forms
- Form Elements
- HTML5 Input Types
- Client-side Validation
- CSS Rendering
- CSS Selectors
- CSS Inheritance
- JavaScript Execution Flow
- JavaScript Events
- DOM Manipulation
- Browser APIs
- Client-side Attack Surface

---

# HTML Forms

Forms allow users to submit information to web applications.

```
User

↓

HTML Form

↓

Browser

↓

HTTP Request

↓

Web Server
```

Forms are one of the primary interaction points between users and applications.

---

# Common Form Elements

```
Form

│

├── Text Box

├── Password Field

├── Checkbox

├── Radio Button

├── Dropdown

├── Text Area

├── File Upload

└── Submit Button
```

---

# Typical Form Workflow

```
User Input

↓

Browser Validation

↓

Submit

↓

Server Validation

↓

Database

↓

Response
```

Both client-side and server-side validation are important.

---

# HTML5 Input Types

Modern HTML supports specialized input types.

| Input Type | Purpose |
|------------|----------|
| text | General text |
| password | Hidden password input |
| email | Email addresses |
| number | Numeric values |
| date | Calendar selection |
| tel | Telephone numbers |
| url | Website URLs |
| search | Search queries |
| file | File uploads |

These types improve usability and enable basic browser validation.

---

# Client-Side Validation

Browsers can validate user input before submission.

```
User

↓

Input Validation

↓

Valid?

↓

Yes

↓

Submit

────────────

No

↓

Display Error
```

---

# Important Security Principle

Client-side validation improves usability but **must never be considered a security control**.

```
Browser Validation

↓

Can Be Bypassed

↓

Server Validation Required
```

Attackers can modify or completely bypass client-side validation.

---

# HTML5 Validation Examples

Browsers may validate:

- Required fields
- Email format
- Minimum length
- Maximum length
- Numeric ranges
- Date formats

These checks help users but do not replace backend validation.

---

# CSS Rendering

After HTML parsing:

```
HTML

↓

DOM

+

CSS

↓

CSSOM

↓

Render Tree

↓

Page Displayed
```

CSS determines how the page appears.

---

# CSS Inheritance

Some properties automatically inherit.

```
BODY

↓

FONT

↓

DIV

↓

PARAGRAPH
```

Inherited properties reduce repetitive styling.

---

# CSS Specificity

Multiple rules may match the same element.

```
Element Rule

↓

Class Rule

↓

ID Rule

↓

Winning Rule Applied
```

More specific selectors generally take precedence.

---

# CSS Box Model

Every HTML element is treated as a box.

```
+-----------------------+

      Margin

+-------------------+

      Border

+---------------+

     Padding

+-----------+

   Content

+-----------+
```

Understanding the box model is important for layout and UI analysis.

---

# CSS Positioning

Common positioning modes:

- Static
- Relative
- Absolute
- Fixed
- Sticky

These influence where elements appear on the page.

---

# Responsive Design

Modern websites adapt to different screen sizes.

```
Desktop

↓

Tablet

↓

Mobile
```

Responsive layouts improve usability across devices.

---

# JavaScript Execution

JavaScript executes after the browser loads or encounters scripts.

```
HTML

↓

JavaScript Engine

↓

Execution

↓

DOM Updates
```

Execution timing affects page behavior and performance.

---

# JavaScript Lifecycle

```
Page Loads

↓

Parse HTML

↓

Execute Scripts

↓

Register Events

↓

User Interaction

↓

DOM Updates
```

---

# Variables

JavaScript stores information in variables.

Examples of stored data:

- User input
- API responses
- Configuration values
- Session state
- Temporary calculations

Variables are fundamental to application logic.

---

# Functions

Functions perform reusable operations.

```
Event

↓

Function

↓

Process

↓

Result
```

Functions help organize application code.

---

# Conditional Logic

Applications make decisions based on conditions.

```
Condition

↓

True?

↓

Yes

↓

Action A

────────────

No

↓

Action B
```

---

# Loops

Loops repeat operations.

```
Start

↓

Condition

↓

Execute

↓

Repeat

↓

Stop
```

Loops are commonly used when processing collections of data.

---

# JavaScript Events

Events represent user or browser actions.

Examples:

- Click
- Double-click
- Keyboard input
- Mouse movement
- Form submission
- Page load
- Window resize

---

# Event Flow

```
User Action

↓

Browser

↓

Event

↓

JavaScript

↓

DOM Update
```

---

# Common Browser Events

| Event | Trigger |
|--------|----------|
| click | Mouse click |
| submit | Form submission |
| change | Input value changes |
| input | User typing |
| load | Page finishes loading |
| keydown | Key pressed |
| mouseover | Cursor enters element |
| resize | Window size changes |

---

# Event Listeners

JavaScript can wait for specific events.

```
Browser

↓

Event Listener

↓

Event Occurs

↓

Execute Function
```

This enables interactive applications.

---

# DOM Manipulation

JavaScript can modify the DOM dynamically.

```
JavaScript

↓

DOM

↓

Updated HTML

↓

Browser Display
```

---

# Common DOM Operations

Applications commonly:

- Read elements
- Create elements
- Remove elements
- Update text
- Change attributes
- Modify styles
- Rearrange content

---

# Dynamic Web Pages

Instead of reloading:

```
User Click

↓

JavaScript

↓

DOM Updated

↓

Visible Change
```

Modern Single Page Applications (SPAs) rely heavily on this approach.

---

# Browser APIs

Browsers provide built-in APIs that JavaScript can use.

Examples:

- Fetch API
- Storage API
- Clipboard API
- Notification API
- Geolocation API
- History API
- WebSocket API

---

# Fetch API

JavaScript can request data from servers.

```
JavaScript

↓

Fetch Request

↓

Server

↓

JSON Response

↓

DOM Updated
```

This enables asynchronous web applications.

---

# Storage APIs

Browsers provide several storage mechanisms.

```
Browser

│

├── Cookies

├── Local Storage

├── Session Storage

└── IndexedDB
```

Each storage option has different security and persistence characteristics.

---

# History API

The History API allows applications to change URLs without reloading pages.

```
User Navigation

↓

History API

↓

URL Updated

↓

No Full Reload
```

This is commonly used in Single Page Applications.

---

# Notification API

Applications can display browser notifications.

```
Application

↓

Permission Request

↓

User Grants

↓

Notification Displayed
```

Notifications require explicit user consent.

---

# Geolocation API

Applications may request location information.

```
Application

↓

Permission

↓

Location Data

↓

Application Logic
```

Access is controlled by browser permissions.

---

# Client-Side Attack Surface

Everything executing inside the browser contributes to the client-side attack surface.

```
Browser

│

├── HTML

├── CSS

├── JavaScript

├── DOM

├── Browser APIs

├── Forms

├── Third-Party Libraries

└── External Resources
```

Each component should be considered during security reviews.

---

# Third-Party JavaScript

Many applications load external libraries.

```
Application

↓

Third-Party Script

↓

Browser Executes
```

Risks include:

- Supply chain compromise
- Malicious updates
- Data leakage
- Privacy concerns

Organizations should carefully review and monitor third-party dependencies.

---

# Enterprise Frontend Architecture

```
Browser

↓

HTML

↓

CSS

↓

JavaScript

↓

REST API

↓

Authentication Service

↓

Application Server

↓

Database
```

JavaScript coordinates communication between the user interface and backend services.

---

# Real Enterprise Example

An online shopping application works as follows:

```
User

↓

Search Product

↓

JavaScript

↓

Fetch API

↓

Product API

↓

JSON

↓

DOM Updated

↓

Products Displayed
```

No full page refresh is required, improving responsiveness.

---

# Hands-on Lab (Conceptual)

Using your browser's Developer Tools:

1. Inspect an HTML form.
2. Identify different input types.
3. Observe client-side validation behavior.
4. Monitor network requests during form submission.
5. Watch DOM changes after interacting with the page.
6. Inspect loaded JavaScript files and browser storage.

---

# Interview Questions

1. What is an HTML form?
2. Why is server-side validation mandatory?
3. Explain the CSS Box Model.
4. What is CSS specificity?
5. What are JavaScript events?
6. What is DOM manipulation?
7. What is the Fetch API?
8. Name some Browser APIs.
9. Why are third-party JavaScript libraries a security concern?
10. What contributes to the client-side attack surface?

---

# Best Practices

- Validate input on both the client and server.
- Use semantic HTML and accessible form controls.
- Keep JavaScript modular and avoid unnecessary global variables.
- Request browser permissions only when needed.
- Review and minimize third-party JavaScript dependencies.
- Monitor browser storage and avoid storing sensitive information insecurely.
- Test responsive layouts across multiple devices.

---

# Common Mistakes

- Trusting client-side validation for security.
- Loading unnecessary third-party libraries.
- Exposing sensitive information in browser storage.
- Ignoring browser permission requests and their implications.
- Creating overly complex DOM structures that reduce maintainability.
- Failing to sanitize data before displaying it in the browser.

---

# Key Takeaways

- HTML forms are the primary interface for collecting user input.
- Client-side validation improves user experience but must always be backed by server-side validation.
- CSS controls presentation through selectors, inheritance, specificity, and the box model.
- JavaScript enables interactivity through events, DOM manipulation, and browser APIs.
- Browser APIs and third-party scripts expand application capabilities but also increase the client-side attack surface.

# 09-HTML-CSS-JavaScript-Security.md

# Part 3 — JavaScript Security, Browser Storage Security, Same-Origin Policy, CORS, Client-Side Security Controls, and Common Vulnerabilities

> **"Most client-side attacks do not exploit the browser itself—they exploit insecure JavaScript, improper trust assumptions, unsafe storage, and weak communication between the browser and web applications."**

---

# Learning Objectives

After completing this part, you will understand:

- JavaScript Security
- Client-Side Trust Model
- Browser Storage Security
- Cookies
- Local Storage
- Session Storage
- IndexedDB Security
- Same-Origin Policy (SOP)
- Cross-Origin Resource Sharing (CORS)
- Browser Security Controls
- Common Client-Side Vulnerabilities
- Secure JavaScript Practices

---

# JavaScript Security

JavaScript executes with the permissions granted to the webpage.

```
Website

↓

JavaScript

↓

Browser

↓

DOM

↓

User Interaction
```

If malicious JavaScript executes, it may interact with resources that the webpage is permitted to access.

---

# JavaScript Trust Model

The browser downloads JavaScript from the server.

```
Server

↓

JavaScript

↓

Browser

↓

Execute
```

Because browsers execute delivered scripts, applications must ensure only trusted and authorized scripts are served.

---

# Why Client-Side Code Cannot Be Trusted

Everything delivered to the browser is visible to users.

```
HTML

↓

CSS

↓

JavaScript

↓

Developer Tools

↓

User Can Inspect
```

Therefore:

- Client-side validation can be bypassed.
- JavaScript can be modified locally.
- Requests can be replayed or altered.
- Hidden fields should not be considered secure.

---

# Security Principle

Never assume the browser is a trusted environment.

```
Browser

↓

User Controlled

↓

Validate Again

↓

Server
```

Sensitive decisions must always be enforced on the server.

---

# Client-Side vs Server-Side Security

| Client Side | Server Side |
|-------------|-------------|
| Improves usability | Enforces security |
| Can be modified | Controlled by server |
| Visible to users | Hidden from users |
| Executes in browser | Executes on server |
| Never trust completely | Source of authoritative decisions |

---

# Browser Storage

Modern browsers provide multiple storage mechanisms.

```
Browser

│

├── Cookies

├── Local Storage

├── Session Storage

└── IndexedDB
```

Each mechanism has different security characteristics.

---

# Cookies

Cookies are small pieces of data stored by the browser.

```
Server

↓

Set Cookie

↓

Browser Stores

↓

Future Requests

↓

Cookie Sent
```

Cookies are commonly used for:

- Sessions
- Authentication
- User preferences
- Tracking

---

# Secure Cookie Attributes

Important cookie security attributes include:

| Attribute | Purpose |
|------------|----------|
| Secure | Sent only over HTTPS |
| HttpOnly | Not accessible to JavaScript |
| SameSite | Controls cross-site sending |
| Path | Restricts URL scope |
| Domain | Restricts host scope |
| Expires / Max-Age | Defines lifetime |

---

# HttpOnly

```
JavaScript

↓

Read Cookie?

↓

No
```

HttpOnly helps protect cookies from being read through client-side JavaScript, reducing the impact of certain attacks such as XSS on session cookies.

---

# Secure Attribute

```
HTTP

↓

Cookie Sent?

↓

No

────────────

HTTPS

↓

Cookie Sent
```

This helps prevent cookies from being transmitted over unencrypted connections.

---

# SameSite Attribute

SameSite limits when browsers send cookies with cross-site requests.

Common values:

- Strict
- Lax
- None (must also use `Secure` in modern browsers)

This attribute is an important defense against Cross-Site Request Forgery (CSRF).

---

# Local Storage

Local Storage stores persistent data.

```
Browser

↓

Local Storage

↓

Data Persists

↓

Browser Restart
```

Characteristics:

- Large capacity
- Persistent
- Accessible through JavaScript

---

# Session Storage

Session Storage is temporary.

```
Browser Tab

↓

Session Storage

↓

Tab Closed

↓

Data Removed
```

Data is isolated to the browser tab or window.

---

# Local Storage vs Session Storage

| Local Storage | Session Storage |
|---------------|-----------------|
| Persistent | Temporary |
| Shared within same origin | Isolated per tab/session |
| Larger storage | Temporary storage |
| Accessible by JavaScript | Accessible by JavaScript |

---

# IndexedDB

IndexedDB provides structured browser storage.

```
Browser

↓

IndexedDB

↓

Large Structured Data

↓

Offline Applications
```

Common uses include:

- Offline web applications
- Large datasets
- Progressive Web Apps (PWAs)

---

# Storage Security

Sensitive information should be handled carefully.

Examples of data requiring protection:

- Authentication tokens
- Personal information
- Financial information
- Health records

Choosing an appropriate storage mechanism depends on the application's security requirements.

---

# Storage Risks

Improper storage can lead to:

- Data exposure
- Privacy issues
- Token theft
- Persistent compromise after an attack

Client-side storage should not contain information that would cause significant harm if exposed.

---

# Same-Origin Policy (SOP)

The Same-Origin Policy is a core browser security mechanism.

```
Website A

↓

Cannot Freely Access

↓

Website B
```

SOP helps isolate websites from one another.

---

# What is an Origin?

An origin consists of:

```
Protocol

+

Host

+

Port
```

Example:

```
https://example.com:443
```

All three components determine the origin.

---

# Same-Origin Examples

| URL 1 | URL 2 | Same Origin? |
|--------|--------|--------------|
| https://example.com | https://example.com | Yes |
| https://example.com | http://example.com | No |
| https://example.com | https://api.example.com | No |
| https://example.com | https://example.com:8443 | No |

---

# Why SOP Exists

Without SOP:

```
Malicious Site

↓

Read Banking Website

↓

Sensitive Data Stolen
```

SOP prevents arbitrary cross-origin access in browsers.

---

# What SOP Restricts

SOP restricts many cross-origin interactions involving:

- DOM access
- Cookies
- Storage
- JavaScript objects
- Certain network responses

This isolation is fundamental to browser security.

---

# Cross-Origin Resource Sharing (CORS)

Sometimes applications legitimately need cross-origin communication.

```
Frontend

↓

API

↓

Different Origin
```

CORS provides a controlled mechanism for this.

---

# CORS Flow

```
Browser

↓

Cross-Origin Request

↓

Server Sends CORS Headers

↓

Browser Decision

↓

Allow

OR

Block
```

The browser enforces the server's CORS policy.

---

# Simple Requests

Some requests are considered "simple" and may not require a preflight request.

Typical characteristics include:

- Standard HTTP methods
- Simple headers
- Supported content types

The browser still checks the server's CORS response headers.

---

# Preflight Requests

For certain cross-origin requests:

```
Browser

↓

OPTIONS Request

↓

Server

↓

Permission?

↓

Actual Request
```

The browser verifies that the server permits the intended request before sending it.

---

# Common CORS Headers

| Header | Purpose |
|----------|----------|
| Access-Control-Allow-Origin | Allowed origins |
| Access-Control-Allow-Methods | Allowed HTTP methods |
| Access-Control-Allow-Headers | Allowed request headers |
| Access-Control-Allow-Credentials | Allows credentialed requests |
| Access-Control-Max-Age | Preflight cache duration |

---

# Browser Security Controls

Modern browsers implement multiple protections.

```
Browser

│

├── Same-Origin Policy

├── CORS

├── CSP

├── Sandbox

├── Permissions

├── Mixed Content Protection

└── Certificate Validation
```

These controls work together to reduce client-side risk.

---

# Content Security Policy (CSP)

CSP restricts which resources may load.

```
Browser

↓

Script Request

↓

Allowed by CSP?

↓

Yes

↓

Execute

──────────────

No

↓

Blocked
```

A strong CSP can significantly reduce the impact of certain script injection attacks.

---

# Mixed Content Protection

A secure page should avoid loading insecure resources.

```
HTTPS Page

↓

HTTP Script

↓

Blocked
```

Mixed content protection helps maintain transport security.

---

# Third-Party Scripts

Applications frequently depend on external JavaScript.

```
Website

↓

Third-Party Script

↓

Browser Executes
```

Potential risks include:

- Supply-chain attacks
- Unexpected updates
- Privacy concerns
- Compromised dependencies

---

# Common Client-Side Vulnerabilities (Overview)

Examples include:

- Cross-Site Scripting (XSS)
- DOM-Based XSS
- Clickjacking
- Insecure Browser Storage
- Sensitive Data Exposure
- Misconfigured CORS
- Dependency Vulnerabilities

Each vulnerability will be explored in dedicated chapters.

---

# Secure JavaScript Practices

Recommended practices:

- Treat browser input as untrusted.
- Validate all data on the server.
- Avoid exposing sensitive information.
- Use secure browser APIs.
- Review third-party dependencies.
- Apply the principle of least privilege.

---

# Enterprise Architecture

```
Browser

↓

JavaScript

↓

Same-Origin Policy

↓

HTTPS

↓

API Gateway

↓

Application Server

↓

Database
```

Multiple browser and server controls protect communication.

---

# Real Enterprise Example

A healthcare portal stores a user's session in a secure cookie.

```
Browser

↓

HTTPS

↓

Secure + HttpOnly Cookie

↓

Authenticated API

↓

Medical Records
```

The application also:

- Uses CSP
- Enables HSTS
- Restricts cross-origin requests with CORS
- Performs server-side authorization for every request

Together these controls help protect sensitive patient information.

---

# Hands-on Lab (Conceptual)

Using your browser:

1. Open Developer Tools.
2. Inspect browser cookies.
3. View Local Storage and Session Storage.
4. Identify which cookies use `Secure`, `HttpOnly`, and `SameSite`.
5. Observe CORS headers for API requests in the Network panel.
6. Compare resources loaded from the same origin and different origins.

---

# Interview Questions

1. Why can't client-side JavaScript be trusted?
2. What is the Same-Origin Policy?
3. What defines an origin?
4. Compare Local Storage and Session Storage.
5. What are the benefits of HttpOnly cookies?
6. What does the Secure cookie attribute do?
7. What is CORS?
8. What is a CORS preflight request?
9. Why are third-party JavaScript libraries a security concern?
10. Name common browser security mechanisms.

---

# Best Practices

- Never trust client-side validation alone.
- Store sensitive session information using appropriate server-managed mechanisms.
- Enable Secure, HttpOnly, and appropriate SameSite cookie attributes.
- Configure CORS using the principle of least privilege.
- Use HTTPS throughout the application.
- Apply a strong Content Security Policy.
- Regularly review third-party JavaScript dependencies.

---

# Common Mistakes

- Storing highly sensitive information in insecure client-side storage.
- Using overly permissive CORS configurations.
- Assuming hidden form fields are secure.
- Disabling browser security features during production.
- Exposing unnecessary information through JavaScript.
- Loading untrusted third-party scripts without review.

---

# Key Takeaways

- Browser-side code executes in an environment controlled by the user and should never be fully trusted.
- Cookies, Local Storage, Session Storage, and IndexedDB each have different security properties and use cases.
- The Same-Origin Policy isolates websites from one another, while CORS enables controlled cross-origin communication.
- Modern browsers provide multiple built-in security mechanisms, including CSP, mixed content protection, and certificate validation.
- Secure client-side development requires careful handling of storage, communication, dependencies, and trust boundaries.

```text id="jid720"
**Next:** Part 4
```