# Summary
This is an app that allows users to sign up and login to their account. This stores all their
written articles(blogs) and then gives them a link where they can share their post, so the access
would be server/account_name/blog_title. On the publisher side that articles would be add/edit/delete.
We can add a premium version that allows the player to increase the number of text they can add.
(i.e 1,500 words for free and 3,000 words for paid).

## Features
- Authentication
- CRUD Database
- Reader/Publisher Interaction
- Payment System
- Free and Pro Version

## Folder Structure
- Static
    -- Styles.css
    -- Script.js
- Template
    -- Layout.html
    -- Authentication
        --- Login
        --- Forgotten Password
        --- Register
    -- Reader
        --- Read_Post
    -- Publisher
        --- Post_List
        --- Edit_Post
    -- Index.html
- Auth.py
- App.py
- User.py
- Payment.py
