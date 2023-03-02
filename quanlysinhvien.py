students = []

def dtb(diemToan, diemLy, diemHoa):
    return(diemToan + diemLy + diemHoa) / 3

def tangDanGPA(students):
    for i in range(0, len(students)):
        for j in range(i + 1, len(students)):
            if(students[i]["DTB"] > students[j]["DTB"]):
                temp = students[i]
                students[i] = students[j]
                students[j] = temp
def luuFile(students):
    file = open("D:\data.txt","w",encoding='utf-8')
    for i in range(len(students)):
        file.write("{0};{1}\n".format(students[i]["Ho_va_ten"], students[i]["DTB"]))
    file.close()

for i in range(2):
    
    student = {}

    maSV = int(i)
    hoVaTen = input("Nhap ten cua sinh vien thu {}: ".format(i + 1))
    diemToan = float(input("Nhap diem toan cua sinh vien thu {}: ".format(i + 1)))
    diemLy = float(input("Nhap diem ly cua sinh vien thu {}: ".format(i + 1)))
    diemHoa = float(input("Nhap diem hoa cua sinh vien thu {}: ".format(i + 1)))

    student["Ma_sinh_vien"] = maSV
    student["Ho_va_ten"] = hoVaTen
    student["Diem_toan"] = diemToan
    student["Diem_ly"] = diemLy
    student["Diem_hoa"] = diemHoa
    student["DTB"] = dtb(diemToan, diemLy, diemHoa)

    students.append(student) 

tangDanGPA(students)
luuFile(students)

    