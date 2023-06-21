class CallCenter:
    def __init__(self):
        self.queue = []

    def enqueue_call(self, customer):
        self.queue.append(customer)
        print(f"Incoming call from {customer}. Added to the queue.")

    def handle_calls(self, num_csrs):
        csrs = [f"representatives{i}" for i in range(1, num_csrs + 1)]

        while self.queue:
            if csrs:
                csr = csrs.pop(0)
                customer = self.queue.pop(0)
                print(f"{csr} is assisting {customer}.")
            else:
                print("All representatives are currently busy. Please wait.")

call_center = CallCenter()

# Enqueue incoming calls
call_center.enqueue_call("Customer1")
call_center.enqueue_call("Customer2")
call_center.enqueue_call("Customer3")

# Handle calls with 2 available CSRs
call_center.handle_calls(2)
