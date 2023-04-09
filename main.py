import pytesseract#테서렉트 및 opencv
import cv2 

from googletrans import Translator#구글 번역
translator=Translator()

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'#테서렉트 경로 지정

img_path = 'test2.jpg'
img = cv2.imread(img_path)
rgb_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)#opencv를 사용하여 이미지 색상 변경

usingLang = ['','']
usingLang[0], usingLang[1] = input('사용할 언어를 입력하세요. \n오차를 줄이기 위하여 2개의 언어를 사용하여야 합니다. (kor, eng, jpn) : ').split()


ocrResult = pytesseract.image_to_string(rgb_image, lang=usingLang[0]+"+"+usingLang[1])#테서렉트로 이미지 내 문자 추출

print('\n'+usingLang[0],usingLang[1],"언어를 이미지에서 추출한 결과입니다.")
print('------------------추출 결과---------------------\n')
print(ocrResult.replace('\n',' '))

for i in range(0,2):
    if(usingLang[i]=='kor'):
        usingLang[i]='ko'
    elif(usingLang[i]=='eng'):
        usingLang[i]='en'
    elif(usingLang[i]=='jpn'):
        usingLang[i]='ja'

print('\n------------------번역 결과---------------------\n')

print(translator.translate(ocrResult.replace('\n',' '),src=translator.detect(ocrResult).lang,dest='ko').text)#(번역할 str, 번역할 str의 언어, 번역할 언어).번역 결과만
print('\n--------------------------------------------')