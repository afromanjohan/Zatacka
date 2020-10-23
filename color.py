colors = [((0, 0, 0), "Black"), ((255, 255, 255), "White"), ((255, 0, 0), "Red"), ((0, 255, 255), "Cyan"), ((255, 255, 0), "Yellow"),
              ((255, 0, 255), "Pink"), ((0, 128, 0), "Green"), ((0, 0, 255), "Blue"), ((255, 165, 0), "Orange")]

def colorTransformer(color):
    color = color.capitalize()
    for col in colors:
        if col[1] == color:
            return col[0]