from flask import Flask, render_template, request, jsonify
from hamming import calculate_hamming_code, detect_and_correct_error

app = Flask(__name__)

# Bellek simülasyonu
data_memory = []
address_counter = 0
@app.route('/')
def index():
    global data_memory, address_counter
    data_memory = []
    address_counter = 0
    return render_template('index.html')


@app.route('/encode', methods=['POST'])
def encode():
    global address_counter
    data = request.json.get('data')
    if not data or any(c not in '01' for c in data):
        return jsonify({'error': 'Geçersiz veri. Sadece 0 ve 1 içermeli.'}), 400

    hamming = calculate_hamming_code(data)
    address = address_counter
    address_counter += 1
    data_memory.append({'address': address, 'data': hamming})
    return jsonify({'address': address, 'hamming': hamming})

@app.route('/memory')
def memory():
    return jsonify(data_memory)

@app.route('/error', methods=['POST'])
def apply_error():
    index = int(request.json.get('address'))
    bit_pos = int(request.json.get('bit_pos')) - 1

    if index < 0 or index >= len(data_memory):
        return jsonify({'error': 'Geçersiz adres'}), 400

    data = data_memory[index]['data'][:]
    if bit_pos < 0 or bit_pos >= len(data):
        return jsonify({'error': 'Geçersiz bit pozisyonu'}), 400

    data[bit_pos] ^= 1
    data_memory[index]['data'] = data
    if not isinstance(data[bit_pos], int):
        return jsonify({'error': 'Veri formatı geçersiz (int değil)'}), 400

    return jsonify({'corrupted': data})

@app.route('/correct', methods=['POST'])
def correct():
    index = int(request.json.get('address'))
    if index < 0 or index >= len(data_memory):
        return jsonify({'error': 'Geçersiz adres'}), 400

    corrupted = data_memory[index]['data'][:]
    corrected, syndrome = detect_and_correct_error(corrupted)
    return jsonify({'corrected': corrected, 'syndrome': syndrome})

if __name__ == '__main__':
    app.run(debug=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

