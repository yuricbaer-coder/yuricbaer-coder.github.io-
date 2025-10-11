from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permite que o front-end acesse a API

@app.route('/calcular', methods=['POST'])
def calcular_gorjeta():
    data = request.json
    pagar = float(data.get('valor'))
    gorjeta = int(data.get('avaliacao'))

    if gorjeta < 1 or gorjeta > 5:
        return jsonify({'erro': 'Nota inválida. Digite entre 1 e 5.'}), 400

    if gorjeta in [1, 2]:
        valor_gorjeta = pagar * 0.05
        mensagem = 'Obrigado pelos 5% de gorjeta.'
    elif gorjeta == 3:
        valor_gorjeta = pagar * 0.10
        mensagem = 'Obrigado pelos 10% de gorjeta.'
    elif gorjeta == 4:
        valor_gorjeta = pagar * 0.15
        mensagem = 'Obrigado pelos 15% de gorjeta.'
    else:
        valor_gorjeta = pagar * 0.20
        mensagem = 'Obrigado pelos 20% de gorjeta.'

    total = pagar + valor_gorjeta

    return jsonify({
        'mensagem': mensagem,
        'total': round(total, 2)
    })

if __name__ == '__main__':
    app.run(debug=True)