# Production Asset Requirements
Project: Around The Block
Version: 1.0.0 Preview
Status: Approved Preview

## Scope

Daftar ini hanya mencatat resource yang benar-benar diperlukan oleh gameplay approved. Existing map tidak didesain ulang. NPC dapat memakai standard humanoid/NPC base dengan appearance khusus bila tidak membutuhkan custom 3D body.

## Multiplayer Production Assets

### Benteng Martello

#### Combat Ship
Type: 3D Model

**Function**  
Kapal individual yang digunakan player selama pertempuran laut.

**Visual Brief**  
Satu kapal tempur yang dapat digunakan ulang untuk seluruh player. Bentuk harus tetap mudah dibaca saat bergerak di laut.

**Required States**

- Aktif
- Hancur / Tidak Aktif

#### Colonial Cannon
Type: 3D Model

**Function**  
Meriam yang digunakan pada kapal dan area pantai.

**Visual Brief**  
Satu meriam yang dapat digunakan ulang dengan gaya peninggalan kolonial dan arah tembak yang jelas.

**Required States**

- Diam
- Respons Menembak

#### Shark Mob
Type: 3D Model

**Function**  
Bahaya bagi player yang berada di air.

**Visual Brief**  
Hiu sederhana yang tetap mudah terlihat di area perairan.

**Required States**

- Berenang
- Menyerang

#### Benteng Martello Guide
Type: NPC Appearance

**Function**  
Karakter yang memperkenalkan aktivitas melalui narasi singkat.

**Visual Brief**  
Pemandu aktivitas sejarah dengan tampilan ramah dan mudah dikenali. Gunakan dasar humanoid/NPC standar dengan tampilan yang berbeda dari karakter lainnya.

### Mari Berkebun

#### Coffee Plant Set
Type: 3D Model

**Function**  
Tanaman kopi untuk proses tanam sampai panen.

**Visual Brief**  
Kondisi tanaman harus cukup jelas untuk membedakan tahap utama pertumbuhan.

**Required States**

- Ditanam
- Tumbuh
- Siap Dipanen
- Setelah Panen bila diperlukan

#### Cinnamon Plant Set
Type: 3D Model

**Function**  
Tanaman kayu manis untuk proses rawat, panen, dan tumbuh kembali.

**Visual Brief**  
Perubahan sebelum dan sesudah panen harus mudah dibedakan.

**Required States**

- Siap Dipanen
- Setelah Panen / Tumbuh Kembali

#### Palm Oil Tree Set
Type: 3D Model

**Function**  
Pohon sawit untuk proses rawat, buah tumbuh, panen, dan tumbuh kembali.

**Visual Brief**  
Pohon sawit dengan buah yang jelas saat siap dipanen.

**Required States**

- Buah Siap Dipanen
- Setelah Panen / Tumbuh Kembali

#### Coffee Harvest Item
Type: ITEM

**Function**  
Hasil panen kopi yang dapat dijual.

**Visual Brief**  
Item kopi yang mudah dibedakan dari hasil kebun lainnya.

#### Cinnamon Harvest Item
Type: ITEM

**Function**  
Hasil panen kayu manis yang dapat dijual.

**Visual Brief**  
Item kayu manis yang langsung terbaca sebagai hasil panen.

#### Palm Fruit Harvest Item
Type: ITEM

**Function**  
Hasil buah sawit yang dapat dijual.

**Visual Brief**  
Item tandan atau buah sawit yang tetap jelas saat berada di inventaris.

#### Fertilizer Item
Type: ITEM

**Function**  
Mempercepat pertumbuhan atau pemulihan tanaman.

**Visual Brief**  
Satu item pupuk sederhana; tidak membutuhkan beberapa jenis pupuk.

#### Plantation Guide
Type: NPC Appearance

**Function**  
Karakter yang memperkenalkan aktivitas melalui narasi singkat.

**Visual Brief**  
Pemandu kebun yang terlihat hangat, antusias, dan sedikit terlalu bangga pada sawit. Gunakan dasar humanoid/NPC standar dengan tampilan yang berbeda dari karakter lainnya.

### Main Egrang

#### Egrang Rideable
Type: 3D Model

**Function**  
Egrang yang dapat dinaiki untuk bergerak dengan posisi lebih tinggi.

**Visual Brief**  
Sepasang egrang tradisional sebagai satu aset yang dapat dinaiki.

**Required States**

- Sedang Dinaiki
- Turun dari Egrang

#### Old Man
Type: NPC Appearance

**Function**  
Karakter yang memperkenalkan aktivitas melalui narasi singkat.

**Visual Brief**  
Bapak tua santai yang memperkenalkan egrang sebagai solusi untuk jalan rusak. Gunakan dasar humanoid/NPC standar dengan tampilan yang berbeda dari karakter lainnya.

### Mancing Dulu

#### Lele Catch Item
Type: ITEM

**Function**  
Salah satu hasil pancing dari empang.

**Visual Brief**  
Item ikan Lele yang mudah dikenali.

#### Tuna Catch Item
Type: ITEM

**Function**  
Salah satu hasil pancing dari empang.

**Visual Brief**  
Item ikan Tuna yang berbeda jelas dari Lele.

#### Hiu Catch Item
Type: ITEM

**Function**  
Hasil pancing langka dan absurd dari empang.

**Visual Brief**  
Item Hiu yang tetap terbaca sebagai hasil pancing dan cocok untuk inventaris.

#### Fisherman
Type: NPC Appearance

**Function**  
Karakter yang memperkenalkan aktivitas melalui narasi singkat.

**Visual Brief**  
Pemancing santai yang terlihat lebih fokus pada kail daripada keributan sekitar. Gunakan dasar humanoid/NPC standar dengan tampilan yang berbeda dari karakter lainnya.

#### Toko Madura Stall
Type: 3D Model

**Function**  
Tempat player menjual hasil tangkapan untuk mendapatkan uang.

**Visual Brief**  
Toko kecil dekat area pemancingan yang mudah dikenali sebagai titik penjualan hasil pancing.

### Macan Lepas

#### Tiger
Type: 3D Model

**Function**  
Musuh utama pada encounter di basement.

**Visual Brief**  
Harimau yang terbaca jelas sebagai ancaman saat reveal pertama, tetapi tetap sederhana dan ringan untuk gameplay.

**Required States**

- Idle / Roam
- Run / Chase
- Attack
- Hit Reaction
- Defeat

#### Black Briefcase
Type: 3D Model

**Function**  
Properti utama Businessman sekaligus visual cue untuk imbalan transaksi.

**Visual Brief**  
Koper eksekutif hitam sederhana yang terlihat premium dan mudah terbaca saat dibawa NPC, tanpa detail berlebihan.

**Required States**

- Closed
- Open

#### Businessman
Type: NPC Appearance

**Function**  
Karakter yang menawarkan pekerjaan dan memberikan imbalan setelah completion.

**Visual Brief**  
Pria berpakaian formal rapi dengan posture percaya diri, membawa Black Briefcase, dan memberi kesan kaya serta sedikit arogan tanpa terlihat seperti villain.

### Tambang Masa Depan

#### CyberWorld Mining Resource Set
Type: 3D Model

**Function**  
Sumber daya yang ditambang dan ditukar menjadi mata uang di tiga tingkat area tambang.

**Visual Brief**  
Satu keluarga visual dengan tiga tingkat yang semakin terlihat bernilai tanpa membutuhkan nama mineral khusus.

**Required States**

- Tingkat 1
- Tingkat 2
- Tingkat 3

#### Mining Tool Upgrade Set
Type: ITEM

**Function**  
Peralatan tambang yang meningkat mengikuti progres tiga tingkat.

**Visual Brief**  
Tiga variasi peningkatan yang mudah dibedakan secara visual.

**Required States**

- Dasar
- Menengah
- Lanjutan

#### Job Recruiter
Type: NPC Appearance

**Function**  
Karakter yang memperkenalkan aktivitas melalui narasi singkat.

**Visual Brief**  
Perekrut yang ramah, meyakinkan, dan terlihat seperti sedang menawarkan peluang besar. Gunakan dasar humanoid/NPC standar dengan tampilan yang berbeda dari karakter lainnya.

### Purchasable Items

#### Flying Motorcycle
Type: 3D Model

**Function**  
Kendaraan utama yang dapat digunakan setelah semua bagian yang dibutuhkan terkumpul.

**Visual Brief**  
Motor terbang yang terbaca jelas sebagai kendaraan premium/futuristik dan tetap ringan untuk penggunaan berulang.

**Required States**

- Incomplete / Locked
- Complete / Ready
- Flying
- Out of Fuel

#### Flying Motorcycle Part Set
Type: Item Set

**Function**  
Komponen pembelian yang dibutuhkan sebelum Flying Motorcycle siap digunakan.

**Visual Brief**  
Empat bagian yang mudah dibedakan: Motorcycle Body, Engine, Flight Module, dan Fuel.

#### Dealer NPC
Type: NPC Appearance

**Function**  
Menjaga toko kendaraan dan menjelaskan sistem pembelian Flying Motorcycle.

**Visual Brief**  
NPC salesman/dealer yang rapi, percaya diri, dan cocok dengan toko kendaraan futuristik.

#### Fuel Set
Type: Item Set

**Function**  
Pilihan bahan bakar untuk menggunakan Flying Motorcycle.

**Visual Brief**  
Tiga varian yang mudah dibedakan: Pertamak, Pertali, dan Okibos. Pertamak memiliki kapasitas tertinggi; Pertali dan Okibos setara.

## Singleplayer Motion Tracking — Presentation Requirements

Motion Interaction masih berstatus **Experimental**. Resource di bawah ini adalah kebutuhan presentation/interaction yang sudah implied oleh gameplay dan perlu divalidasi saat prototype.

### Menghalau Bajak Laut

- **Fortress Health Bar** — indikator HP benteng yang mudah dibaca selama serangan kapal.
- **Cannon Aim / Fire Feedback** — arah bidikan dan hasil tembakan harus langsung terbaca.

### Menanam Pohon

- **Tool State / Active Tool Feedback** — player harus memahami tool aktif: sekop, bibit, alat penyiram, atau pupuk.
- **Sequence Success / Fail Feedback** — aksi benar/salah harus terbaca sebelum retry.

### Memancing Ikan

- **Fishing Timing Indicator** — menampilkan posisi ikan dan Green Zone saat bite terjadi.
- **Stamina Indicator** — menampilkan stamina sesi.
- **Catch / Miss Feedback** — hasil pull harus langsung terbaca.

## Asset Boundaries

- Tidak menambahkan decorative props yang tidak dibutuhkan gameplay.
- Motion gesture visuals tidak dianggap final sebelum testing venue.
- Map View screenshots berada di approved preview HTML sebagai visual reference.
