class PostOffice:
    def __init__(self, users):
        self.users = set(users)
        self.inboxes = {user: [] for user in users}
        self.counter = 0

    def send_message(self, sender, recipient, title, body, urgent=False):
        if recipient not in self.inboxes:
            raise KeyError(f"No such user: {recipient}")
        self.counter += 1
        message = {
            "id": self.counter,
            "from": sender,
            "to": recipient,
            "title": title,
            "body": body,
            "unread": True,
        }
        if urgent:
            self.inboxes[recipient].insert(0, message)
        else:
            self.inboxes[recipient].append(message)
        return self.counter

    def read_inbox(self, recipient, n=None):
        inbox = self.inboxes.get(recipient, [])
        for msg in inbox:
            msg["unread"] = False
        return inbox if n is None else inbox[:n]

    def search_inbox(self, recipient, text):
        return [
            msg for msg in self.inboxes.get(recipient, [])
            if text.lower() in msg["title"].lower() or text.lower() in msg["body"].lower()
        ]

    @property
    def boxes(self):  # for compatibility with the test
        return self.inboxes
