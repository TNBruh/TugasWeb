Dalam file Model.py terdapat sebuah kelas yang membantu semua pengolahan data yang diberi nama Database. Database mengolah database MongoDB. GetCollection() dan CreateCollection() membuat objek collection yang dibutuhkan untuk menyimpan data. Hanya dibutuhkan 3 collection yang berbeda, yaitu yang akan diberi nama "Teams", "Tournaments", dan "Users".
Di dalam kelas Database, terdapat juga metode-metode untuk mengolah koleksi-koleksi tersebut;
AddUser() menambah user,
AddTeam() menambah sebuah tim,
AddTourn() menambah sebuah turnamen,
FindUser() mencari user,
FindTeam() mencari tim,
FindMembers() mencari anggota-anggota tim,
FindTourn() mencari turnamen,
FindUserTeam() mencari tim sebuah pengguna,
Remove() menghapus sebuah dokumen dari sebuah koleksi,
AddMember() menambahkan anggota ke sebuah tim,
RemoveMember() mengeluarkan sebuah anggota dari sebuah tim,
Clear() menghapus sebuah koleksi