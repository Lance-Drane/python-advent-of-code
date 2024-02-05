import sys
from collections import defaultdict, deque

instructions: list[list[str, str, str]] = [line.split() for line in sys.stdin.readlines()]


class Program:
    def __init__(self, pid: int):
        self.registers = defaultdict(int, {'p': pid})
        self.curr = 0
        self.msg_q = deque()
        self.next_receive: str | None = None
        self.sent_count = 0

    def get_next_value(self, val: str) -> int:
        return int(val) if not val[0].isalpha() else self.registers[val]

    def register_message_endpoint(self, callback):
        """
        allow for one program to send a message to another program
        """
        self.message_endpoint_other = callback

    def message_endpoint(self, value: int):
        """
        called from the other program when it sends a value, just add the value to the message queue
        for now.
        """
        self.msg_q.append(value)

    def register_execute(self, callback):
        """
        allow for one program to tell the other program to start executing its instructions
        """
        self.execute_other = callback

    def execute(self):
        """
        start executing instructions. call the other program's execution function by
        "self.execute_other()"
        """
        if not self.msg_q:
            # deadlock
            return
        if self.next_receive:
            self.registers[self.next_receive] = self.msg_q.popleft()
            if not self.msg_q:
                # deadlock
                return
            self.next_receive = None
        self.execute_instructions()

    def execute_instructions(self):
        """
        this is the main loop. normally called from "execute", but the initial back-and-forth
        needs to start from here.
        """
        while self.curr < len(instructions):
            instruct = instructions[self.curr]

            if instruct[0] == 'snd':
                self.curr += 1
                self.message_endpoint_other(self.get_next_value(instruct[1]))
                self.sent_count += 1
            elif instruct[0] == 'set':
                self.registers[instruct[1]] = self.get_next_value(instruct[2])
                self.curr += 1
            elif instruct[0] == 'add':
                self.registers[instruct[1]] += self.get_next_value(instruct[2])
                self.curr += 1
            elif instruct[0] == 'mul':
                self.registers[instruct[1]] *= self.get_next_value(instruct[2])
                self.curr += 1
            elif instruct[0] == 'mod':
                self.registers[instruct[1]] %= self.get_next_value(instruct[2])
                self.curr += 1
            elif instruct[0] == 'rcv':
                self.curr += 1
                if self.msg_q:
                    self.registers[instruct[1]] = self.msg_q.popleft()
                else:
                    self.next_receive = instruct[1]
                    break
            # jgz
            elif self.get_next_value(instruct[1]) > 0:
                self.curr += self.get_next_value(instruct[2])
            else:
                self.curr += 1

        self.execute_other()


program_0 = Program(0)
program_1 = Program(1)

program_0.register_execute(program_1.execute)
program_1.register_execute(program_0.execute)
program_0.register_message_endpoint(program_1.message_endpoint)
program_1.register_message_endpoint(program_0.message_endpoint)

program_0.execute_instructions()

print(program_1.sent_count)
