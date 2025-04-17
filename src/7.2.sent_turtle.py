class PostOffice:
    def __init__(self, users):
        self.inboxes = {user: [] for user in users}
        self.message_id_counter = 1

    def send_message(self, sender, recipient, title, body, urgent=False):
        if recipient not in self.inboxes:
            raise KeyError("Recipient does not exist")

        message = {
            "id": self.message_id_counter,
            "from": sender,
            "title": title,
            "body": body,
            "unread": True,
            "urgent": urgent,
        }

        # Insert urgent messages at the beginning
        if urgent:
            self.inboxes[recipient].insert(0, message)
        else:
            self.inboxes[recipient].append(message)

        self.message_id_counter += 1
        return message["id"]

    def read_inbox(self, user, n=None):
        inbox = self.inboxes[user]
        unread = [msg for msg in inbox if msg["unread"]]
        if n is None:
            to_return = unread
        else:
            to_return = unread[:n]

        for msg in to_return:
            msg["unread"] = False
        return to_return

    def search_inbox(self, recipient, text):
        return [
            msg for msg in self.inboxes.get(recipient, [])
            if text.lower() in msg["title"].lower() or text.lower() in msg["body"].lower()
        ]

    @property
    def boxes(self):
        return self.inboxes
