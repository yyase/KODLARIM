import re

with open("transkript.txt", "r", encoding="utf-8") as f:
    text = f.read()

# tüm zaman ifadelerini tek seferde sil
clean_text = re.sub(r'\b\d+\s*dakika\s*\d*\s*saniye|\b\d+\s*dakika|\b\d+\s*saniye|\b\d+:\s*', '', text)

with open("temiz_transkript.txt", "w", encoding="utf-8") as f:
    f.write(clean_text)

print("Tüm zaman kodları temizlendi.")

