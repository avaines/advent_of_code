from re import search


class Communications_System():
    def __init__(self, input, debug=False):
        self.datastream_buffer = list(input)
        self.DEBUG = debug

    @property
    def start_of_packet_marker(self):
        return self.locate_buffered_packet_marker(buffer_len=4)

    @property
    def start_of_message_marker(self):
        return self.locate_buffered_packet_marker(buffer_len=14)


    def locate_buffered_packet_marker(self, buffer_len=0):
        potential_start_of_packet_sequence = []

        for string_reader_pointer in range(len(self.datastream_buffer)):
            potential_start_of_packet_sequence = self.datastream_buffer[string_reader_pointer : string_reader_pointer + buffer_len]

            if len(potential_start_of_packet_sequence) == buffer_len and len(potential_start_of_packet_sequence) == len(set(potential_start_of_packet_sequence)):
                # List contains all unique chars as sets cannot contain duplicates
                if self.DEBUG: print("The start of packet marker is letter number", string_reader_pointer + buffer_len, "in this case its the letter", self.datastream_buffer[string_reader_pointer + buffer_len])
                return string_reader_pointer + buffer_len

class ElfComm3000():
    def __init__(self, debug=False, inspection_cycles=[]):
        self.debug = debug
        self.cycle = 0
        self.inspection_cycles = inspection_cycles
        self.crt_width = 40
        self.crt_height = 6
        self.crt_display = [[' ']*self.crt_width for _ in range(self.crt_height)]

        self.register_x = 1
        self.signal_strength_at_inspection = []

    def execute_instruction(self, instruction):
        if instruction == "noop":
            self.clock_tick()
            if self.debug: print("NOOP, nothing to do")

        if search("addx", instruction):
            self.clock_tick()
            self.clock_tick()
            instruction_attributes = instruction.split()
            if self.debug: print("ADDX, adding", instruction_attributes[1], "to 'X' register")
            self.register_x += int(instruction_attributes[1])

    def clock_tick(self):
        self.crt_draw()
        self.cycle += 1

        if self.cycle in self.inspection_cycles:
            self.signal_strength_at_inspection.append(self.cycle * self.register_x)

    def crt_draw(self):
        if self.register_x - 1 <= self.cycle % self.crt_width <= self.register_x + 1:
            self.crt_display[self.cycle // self.crt_width][self.cycle % self.crt_width] = '#'

        # if self.debug: print(self.crt_display)

    def crt_render(self):
        # Join the row together, then join all the rows together with new lines
        return "\n".join(["".join(x) for x in self.crt_display])