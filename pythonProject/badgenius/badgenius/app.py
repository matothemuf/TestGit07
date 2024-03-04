import random
import base64

# Function to generate a random string of responses (A, B, C, D)
def generate_random_responses(length=40):
    # Define the possible response options: A, B, C, D
    options = ['A', 'B', 'C', 'D']
    # Generate a random string of responses with the specified length
    random_responses = ''.join(random.choice(options) for _ in range(length))
    return random_responses

# Function to encode responses into a base64 string
def encode_responses(responses):
    # Define a mapping for encoding each response option to a 2-bit binary representation
    encoding_dict = {'A': '00', 'B': '01', 'C': '10', 'D': '11'}

    # Group responses into pairs for efficient encoding
    response_pairs = [responses[i:i+2] for i in range(0, len(responses), 2)]

    # Convert response pairs to binary and then to bytes
    binary_representation = ''.join([encoding_dict[response[0]] + encoding_dict[response[1]] for response in response_pairs])
    encoded_bytes = int(binary_representation, 2).to_bytes(len(binary_representation) // 8, byteorder='big')

    # Limit the base64 encoded string to 20 characters
    encoded_string = base64.b64encode(encoded_bytes).decode('utf-8')[:20]

    return encoded_string

# Function to decode a base64-encoded string back into the original responses
def decode_responses(encoded_string, response_length=40):
    # Define a mapping for decoding each 2-bit binary to the original response option
    decoding_dict = {'00': 'A', '01': 'B', '10': 'C', '11': 'D'}

    # Pad the encoded string to ensure correct decoding
    encoded_string = encoded_string.ljust(20, '=')

    # Decode the base64 string to bytes
    decoded_bytes = base64.b64decode(encoded_string)

    # Obtain binary representation and map it back to the original responses
    expected_binary_length = response_length * 2
    binary_representation = format(int.from_bytes(decoded_bytes, 'big'), '0' + str(expected_binary_length) + 'b')
    decoded_responses = ''.join(decoding_dict[binary_representation[i:i+2]] for i in range(0, len(binary_representation), 2))

    return decoded_responses

# Main part of the program
random_responses = generate_random_responses()
print(f"Random Responses: {random_responses}")

encoded_string = encode_responses(random_responses)
print(f"Encoded String: {encoded_string}")

decoded_responses = decode_responses(encoded_string, len(random_responses))
print(f"Decoded Responses: {decoded_responses}")