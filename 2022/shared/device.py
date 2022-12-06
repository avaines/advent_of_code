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
