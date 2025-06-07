def calculate_parity_bits(data_bits):
    m = len(data_bits)
    r = 0
    while (2 ** r) < (m + r + 1):
        r += 1
    return r

def insert_parity_bits(data_bits):
    r = calculate_parity_bits(data_bits)
    total_length = len(data_bits) + r
    hamming_code = []
    j = 0
    for i in range(1, total_length + 1):
        if (i & (i - 1)) == 0:
            hamming_code.append(0)
        else:
            hamming_code.append(int(data_bits[j]))
            j += 1
    return hamming_code

def calculate_hamming_code(data_str):
    data_bits = list(map(int, data_str))
    hamming_code = insert_parity_bits(data_bits)
    n = len(hamming_code)
    for i in range(len(hamming_code)):
        if (i + 1) & (i) == 0:
            parity_pos = i + 1
            parity = 0
            for j in range(1, n + 1):
                if j & parity_pos:
                    parity ^= hamming_code[j - 1]
            hamming_code[i] = parity
    return hamming_code
def detect_and_correct_error(received_code):
    n = len(received_code)
    r = calculate_parity_bits(received_code)
    syndrome = 0
    for i in range(r):
        parity_pos = 2 ** i
        parity = 0
        for j in range(1, n + 1):
            if j & parity_pos:
                parity ^= received_code[j - 1]
        if parity:
            syndrome += parity_pos

    if syndrome != 0 and syndrome <= len(received_code):
        received_code[syndrome - 1] ^= 1
    return received_code, syndrome
