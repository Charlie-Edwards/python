import pytesseract, PIL.Image, cv2
from pytesseract import Output
import os, sys, getpass

conf = r"--psm 4 --oem 3"

def extract_text():
    output = pytesseract.image_to_string(PIL.Image.open("vjuNp.jpg"), config=conf)
    print(output)

def letter_boxes():
    img = cv2.imread("vjuNp.jpg")
    height, width, _ = img.shape

    boxes = pytesseract.image_to_boxes(img, config=conf)
    print(boxes)

    for box in boxes.splitlines():
        box = box.split(" ")
        img = cv2.rectangle(
            img,
            (int(box[1]), height - int(box[2])), # pt1
            (int(box[3]), height - int(box[4])), # pt2
            (255, 255, 0),                       # bgr
            1                                    # thickness
        )

    cv2.imshow("img", img)
    cv2.waitKey(0)

def word_boxes():
    img = cv2.imread("vjuNp.jpg")
    height, width, _ = img.shape

    confidence_threshold = int(input("Confidence threshold (%): ")) or 80

    data = pytesseract.image_to_data(img, config=conf, output_type=Output.DICT)

    amount_boxes = len(data['text'])
    for i in range(amount_boxes):
        if float(data['conf'][i]) > confidence_threshold:
            (x, y, width, height) = data['left'][i], data['top'][i], data['width'][i], data['height'][i]
            img = cv2.rectangle(
                img,
                (x, y),
                (x + width, y + height),
                (255, 255, 0),
                1
            )
            img = cv2.putText(img, data['text'][i], (x, y + height + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 1, cv2.LINE_AA)

    cv2.imshow("img", img)
    cv2.waitKey(0)

def main():
    os.system('cls' if sys.platform == 'win32' else 'clear')
    print("[1] Text Extraction:")
    print("[2] Rectangle Plotting (per letter):")
    print("[3] Rectangle Plotting (per word with annotations and confidence filter):")
    selection = input(f"\n{getpass.getuser()}: ")

    if selection == "1":
        extract_text()
    elif selection == "2":
        letter_boxes()
    elif selection == "3":
        word_boxes()
    else:
        main()

main()
