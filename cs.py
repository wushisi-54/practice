import easyocr
reader = easyocr.Reader(['ch_sim','en'], gpu =True )
result = reader.readtext('cs.png', detail= 0)
print(result)