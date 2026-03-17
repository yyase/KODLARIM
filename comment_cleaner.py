input_file = "yorumlar.txt"
output_file = "temiz_yorumlar.txt"

with open(input_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

clean_comments = []

for line in lines:
    line = line.strip()

    if line.startswith("@"):
        continue
    if "Show Comment" in line:
        continue
    if line == "":
        continue

    clean_comments.append(line)

with open(output_file, "w", encoding="utf-8") as f:
    for comment in clean_comments:
        f.write(comment + "\n")

print("Yorumlar temizlendi.")
