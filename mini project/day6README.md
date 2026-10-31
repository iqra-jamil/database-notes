Day 6


Database design for AI applications
Plan how your application's information should be stored.
-     Design a users table.
-     Design a conversations table.
-     Design a messages table.
-     Decide how messages link to conversations.
-     Design a documents table.
-     Understand document metadata, such as filename, upload date, file type, and document ID.
-    Understand why related information often belongs in separate tables.
  
  Deliverable: Draw a simple database design for an LLM chat app that also accepts document uploads.

## why tables are separate. Users, conversations, messages, and documents represent different types of data, linked through IDs to avoid unnecessary duplication.

Think of your AI chatbot database.

Why do we need 4 separate tables?

1. Users: Stores user information. Each user has a unique `user_id`.

2. Conversations: Stores chat session details. Each conversation has a `conversation_id` and `user_id`.

3. Messages: Stores individual messages. Each message has a `message_id` and `conversation_id`.

4. Documents: Stores uploaded document details. Each document has a `document_id` and `user_id`.

Why not put everything in one table?

Imagine storing a user's name repeatedly for every message and every document. This creates unnecessary duplication.

Separate tables help you:

- Avoid repeating the same information.
- Update user information in one place.
- Connect related records through foreign keys.
- Manage each type of data independently.

Your main concept to understand:

One user can have multiple conversations. One conversation can have multiple messages. One user can upload multiple documents.

This is called relational database design.