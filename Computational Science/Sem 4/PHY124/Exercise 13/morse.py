MORSE = {
    ".": {
        "label": "E",
        "children": {
            "-": {
                "label": "A",
                "children": {
                    "-": {
                        "label": "W",
                        "children": {
                            "-": {
                                "label": "J",
                                "children": {"-": {"label": "1", "children": {}}},
                            },
                            ".": {"label": "P", "children": {}},
                        },
                    },
                    ".": {
                        "label": "R",
                        "children": {".": {"label": "L", "children": {}}},
                    },
                },
            },
            ".": {
                "label": "I",
                "children": {
                    "-": {
                        "label": "U",
                        "children": {
                            ".": {"label": "F", "children": {}},
                            "-": {
                                "label": "",
                                "children": {"-": {"label": "2", "children": {}}},
                            },
                        },
                    },
                    ".": {
                        "label": "S",
                        "children": {
                            ".": {
                                "label": "H",
                                "children": {
                                    "-": {"label": "4", "children": {}},
                                    ".": {"label": "5", "children": {}},
                                },
                            },
                            "-": {
                                "label": "V",
                                "children": {"-": {"label": "3", "children": {}}},
                            },
                        },
                    },
                },
            },
        },
    },
    "-": {
        "label": "T",
        "children": {
            ".": {
                "label": "N",
                "children": {
                    ".": {
                        "label": "D",
                        "children": {
                            ".": {
                                "label": "B",
                                "children": {".": {"label": "6", "children": {}}},
                            },
                            "-": {"label": "X", "children": {}},
                        },
                    },
                    "-": {
                        "label": "K",
                        "children": {
                            ".": {"label": "C", "children": {}},
                            "-": {"label": "Y", "children": {}},
                        },
                    },
                },
            },
            "-": {
                "label": "M",
                "children": {
                    ".": {
                        "label": "G",
                        "children": {
                            "-": {"label": "Q", "children": {}},
                            ".": {
                                "label": "Z",
                                "children": {".": {"label": "7", "children": {}}},
                            },
                        },
                    },
                    "-": {
                        "label": "O",
                        "children": {
                            ".": {
                                "label": "",
                                "children": {".": {"label": "8", "children": {}}},
                            },
                            "-": {
                                "label": "",
                                "children": {
                                    ".": {"label": "9", "children": {}},
                                    "-": {"label": "0", "children": {}},
                                },
                            },
                        },
                    },
                },
            },
        },
    },
}


def decode_morse(code, tree=MORSE):
    if not code:
        return "?"

    node = tree.get(code[0])
    if not node:
        return "?"

    for symbol in code[1:]:
        node = node.get("children", {}).get(symbol)
        if not node:
            return "?"

    return node.get("label", "?")


def decode_message(message):
    return ''.join(decode_morse(letter) for letter in message.strip().split())


morse_input = "- . -..- -"
decoded = decode_message(morse_input)
print(decoded)
