class HashMap:
    def __init__(self, array_size):
        self.array_size = array_size
        self.array = [None for item in range(array_size)]

    def hash(self, key):
        key_bytes = key.encode()
        hash_code = sum(key_bytes)

    def compressor(self, hash_code):
        return hash_code % self.array_size

    def assign(self, key, value):
        array_index = self.compressor(self.hash(key))
        current_array_value = self.array[array_index]

        if current_array_value is None or current_array_value[0] == key:
            self.array[array_index] = [key, value]
            return

        # Collision!

        number_collisions = 1

        while (current_array_value[0] != key):
            new_array_index = self.compressor(self.hash(key)) + number_collisions
            current_array_value = self.array[new_array_index]

            if current_array_value is None or current_array_value[0] == key:
                self.array[new_array_index] = [key, value]
                return

            number_collisions += 1

        return

    def retrieve(self, key):
        array_index = self.compressor(self.hash(key))
        possible_return_value = self.array[array_index]

        if possible_return_value is None:
            return None

        if possible_return_value[0] == key:
            return possible_return_value[1]

        retrieval_collisions = 1

        while (possible_return_value != key):

            array_index += 1
            possible_return_value = self.array[array_index]

            if possible_return_value is None:
                return None
            if possible_return_value[0] == key:
                return possible_return_value[1]

        return