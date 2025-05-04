import os
import csv

output_file = "csv_head.txt"

with open(output_file, "w", encoding="utf-8") as out_f:
    for filename in os.listdir("."):
        if filename.endswith(".csv") and os.path.isfile(filename):
            print(f"读取文件: {filename}")
            out_f.write(f"[{filename}]:\n")
            try:
                with open(filename, "r", encoding="utf-8", errors="ignore") as csv_file:
                    reader = csv.reader(csv_file)
                    header = next(reader, None)
                    if header:
                        out_f.write(",".join(header) + "\n")
                        for i, row in enumerate(reader):
                            out_f.write(",".join(row) + "\n")
                            if i == 4:
                                break
                    else:
                        out_f.write("(空文件或无法读取表头)\n")
            except Exception as e:
                out_f.write(f"(读取失败: {e})\n")
            out_f.write("\n")
