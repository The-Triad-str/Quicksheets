from flask import Flask, jsonify, request
import getnotes as g
import math


def freq_to_note(freq):
  notes = ('A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#')
  note_number = 12 * math.log2(freq / 440) + 49
  return notes[int(note_number % 12) - 1] + str(int(math.log2(freq / 440)) + 4)



app = Flask(__name__)


@app.route('/returnjson', methods=['GET'])
def ReturnJSON():
    if request.method == 'GET':
        resp = g.getn()
        parseresp = {}
        # Example usage:
        print(freq_to_note(440))  # Prints "A4"
        print(freq_to_note(880))  # Prints "A5"
        for count, i in enumerate(resp):
            if i[0] != 0:
                note = str(freq_to_note(i[0]))
            else:
                note = "R"
            parseresp[str(count)] = {
                "frequency": note,
                "duration": str(i[1])
            }
        return jsonify(parseresp)


if __name__ == '__main__':
    app.run(host='172.16.176.46')
