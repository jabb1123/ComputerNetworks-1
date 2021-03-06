CODE = {'A': '.-', 'B': '-...', 'C': '-.-.',
      'D': '-..', 'E': '.', 'F': '..-.',
      'G': '--.', 'H': '....', 'I': '..',
      'J': '.---', 'K': '-.-', 'L': '.-..',
      'M': '--', 'N': '-.', 'O': '---',
      'P': '.--.', 'Q': '--.-', 'R': '.-.',
      'S': '...', 'T': '-', 'U': '..-',
      'V': '...-', 'W': '.--', 'X': '-..-',
      'Y': '-.--', 'Z': '--..',
      '0': '-----', '1': '.----', '2': '..---',
      '3': '...--', '4': '....-', '5': '.....',
      '6': '-....', '7': '--...', '8': '---..',
      '9': '----.', 'a': '.-.-', '+': '.-.-.',
      '.': '.-.-.-'
}

UNCODE = {'.-': 'A', '-...':'B', '-.-.':'C',
      '-..': 'D', '.': 'E', '..-.': 'F',
      '--.': 'G', '....': 'H', '..': 'I',
      '.---': 'J', '-.-': 'K', '.-..': 'L',
      '--': 'M', '-.': 'N', '---': 'O',
      '.--.': 'P', '--.-': 'Q', '.-.': 'R',
      '...': 'S', '-': 'T', '..-': 'U',
      '...-': 'V', '.--': 'W', '-..-': 'X',
      '-.--': 'Y', '--..': 'Z',
      '-----': '0', '.----': '1', '..---': '2',
      '...--': '3', '....-': '4', '.....': '5',
      '-....': '6', '--...': '7', '---..': '8',
      '----.': '9', '.-.-': 'a', '.-.-.': '+',
      '.-.-.-': '.'
}

morseBin = {
  '.': '10',
  '-': '1110'
}

binMorse = {
  '1' : '.',
  '111' : '-',
  '10' : '.',
  '1110' : '-'
}
