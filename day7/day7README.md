Day 7

Streamlit session_state versus persistent storage
Connect everything to your actual application workflow.
-  Understand what st.session_state stores.
-  Understand how session state behaves across Streamlit reruns.
-  Understand what happens when a user refreshes, starts a new session, or the application restarts.
-  Compare session state with data saved in SQLite.
-  Decide which information belongs in session state and which belongs in a database.
-  Plan how to reload saved conversations when a user returns.
-  Review how uploaded document metadata can persist after the session ends.
  
  Deliverable: Explain how your application can restore a conversation after its in-memory state disappears.

# 1.what st.session_state stores.
st.session_state is Streamlit's way (or feature) of storing temporary data for a user's current session.
On every interaction, Streamlit reruns the script. Normal Python variables get recreated, but st.session_state preserves their values across reruns within the same session.
# 2.Understand how session state behaves across Streamlit reruns.
st.session_state preserves their values across reruns within the same session.
# 3.what happens when a user refreshes, starts a new session, or the application restarts.
There are 3 scenarios:

1. Page refresh: The Streamlit session may reset, so session_state data can be lost.

2. New session: A new user session starts with a fresh session_state. Previous session data is not automatically available.

3. Application restart: All in-memory session_state data is lost because it isn't permanently stored.

Key point: session_state is temporary storage, not permanent storage. That's why we use SQLite to save data permanently.

Streamlit session_state stores data temporarily in RAM. Its data may be lost when a user starts a new session, refreshes the page, or the application restarts.
# Compare session state with data saved in SQLite.
SQLite stores data persistently on disk. Its data remains available across page refreshes, new sessions, and application restarts, as long as the database file remains intact and accessible.

# how to Decide which information belongs in session state and which belongs in a database.
Rule to remember:

Use session_state for temporary data needed while the user interacts with the app. Use SQLite for data that must remain available after the session ends.
# how to reload saved conversations when a user returns.
For  AI chatbot, follow this workflow:
1. When a user returns, identify their user_id.
2. Query the conversations table using that user_id.
3. Display their saved conversation titles.
4. When they select a conversation, retrieve its messages from the messages table using convo_id.
5. Load those messages into st.session_state.
6. Display the restored conversation in the chat interface.
Key concept: SQLite retrieves the permanently saved data, and st.session_state holds the loaded conversation during the active session.


# how uploaded document metadata can persist after the session ends.

1. When a user uploads a document, save its metadata (filename, file type, upload date, user_id) in the SQLite documents table.
2. Store the actual document file separately on disk or in file storage.
3. When the user returns, retrieve their document metadata from SQLite using their user_id.
4. Use the saved file path or storage reference to access the actual document.
Key concept: st.session_state may lose temporary document information, but SQLite preserves document metadata after the session ends.
#  Explain how your application can restore a conversation after its in-memory state disappears.
When a user sends a message, save it in the SQLite messages table along with its conversation_id.

If st.session_state disappears:
1. Identify the returning user using their user_id.
2. Retrieve their conversations from the conversations table.
3. Let the user select a conversation.
4. Retrieve all messages belonging to that conversation using convo_id.
5. Load the retrieved messages into st.session_state.
6. Display the restored conversation in the chat interface.
Key concept: SQLite preserves the conversation permanently, while st.session_state temporarily holds the retrieved messages during the active session.