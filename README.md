# TP1DPBO2024C1

## Janji

Saya Sabila Rosad NIM 2106000 mengerjakan TP 1
dalam mata kuliah Desain Pemrograman Berorientasi Objek
untuk keberkahanNya maka saya tidak melakukan
kecurangan seperti yang telah dispesifikasikan
Aamiin.

## Desain Program

![image](https://cdn.discordapp.com/attachments/957671708058325032/1215331161035776140/image.png?ex=65fc5c58&is=65e9e758&hm=a247eaf6f0f4b78d3b36682f88b0bdb3d0d3d4e551492da9caef85e6ab3301f2&) <br>
Alasan desain program : <br>

a. kelas Character merupakan Parent class <br>
b. kelas Player merupakan Child class dari Character dengan penambahan atribut berupa "Level". kelas ini merupakan karakter yang dimainkan oleh pemain. <br>
c. kelas NPC merupakan Child class dari Character dengan penambahan atribut berupa "tipe". kelas ini merupakan karakter yang ada di dalam game aka bot aka tidak dimainkan oleh pemain. <br>
d. kelas Friend merupakan Child class dari NPC. kelas ini merupakan NPC yang bersifat baik <br>
e. kelas Enemy merupakan Child class dari NPC. kelas ini merupakan NPC yang bersifat jahat <br>

A. Class Character

- Atribut :
  - name : nama dari karakter
  - gender : jenis kelamin dari karakter
  - atk : jumlah besar atk dari karakter
  - hp : jumlah hp dari karakter
  - role : role dari karakter
  - item : item yang dibawa oleh karakter
- Methods :
  - set() : menetapkan value
  - get() : mendapatkan value
  - attacking()
  - skill()
  - upgrade()

B. Class Player

- Atribut :
  - level : level dari karakter
- Methods :
  - set() : menetapkan value
  - get() : mendapatkan value
  - mission()
  - add_item()

C. Class NPC

- Atribut :
  - tipe : tipe dari karakter
- Methods :
  - set() : menetapkan value
  - get() : mendapatkan value

D. Class Friend

- Methods :
  - give_mission()
  - sell_item()
  - buy_item()

E. Class Enemy

- Methods :
  - talking()
  - reward()

## Dokumentasi dan Alur Program

Untuk dokumentasi menggunakan screenshot yang sudah tersedia di folder Screenshot<br>
Lalu untuk alur program : <br>

1. Compile file sesuai bahasa
2. Run programnya
3. Ketika program berhasil dijalankan, maka akan menampilkan output:
   - data player beserta atributnya
   - data npc yang jahat dan yang baik
   - interaksi karakter
