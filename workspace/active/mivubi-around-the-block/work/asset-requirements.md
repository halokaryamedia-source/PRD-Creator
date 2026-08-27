# Production Asset Requirements
Project: MIVUBI – Around The Block
Version: 1.0.0

## Scope Note

Dokumen ini hanya mencatat resource yang benar-benar dibutuhkan oleh gameplay yang sudah disetujui. Layout map dianggap sudah tersedia. NPC narator dapat menggunakan standard humanoid/NPC base; current scope tidak membutuhkan custom 3D NPC model selama skin/appearance yang sesuai dapat disediakan melalui sistem yang sudah ada.

## Required Model Summary

1. Combat Ship
2. Colonial Cannon
3. Shark Mob
4. Coffee Plant Set
5. Cinnamon Plant Set
6. Palm Oil Tree Set
7. Egrang Rideable
8. Tiger
9. CyberWorld Mining Resource Set

## Required Item Summary

1. Coffee Harvest Item
2. Cinnamon Harvest Item
3. Palm Fruit Harvest Item
4. Fertilizer Item
5. Lele Catch Item
6. Tuna Catch Item
7. Hiu Catch Item
8. Mining Tool Upgrade Set

## Benteng Martello

### Gameplay Moment — Naval Combat

### 3D Models

#### Combat Ship
Flow: Benteng Martello — Naval Combat
Moment: Player Starts the Match
Type: MODEL
Function: Kapal individual yang digunakan player selama fase naval PvP.
Visual Brief: Satu reusable combat ship yang dapat dipakai untuk semua participant. Model harus mendukung posisi player dan penggunaan meriam selama pertempuran; visible damage/destruction state dapat menjadi bagian dari model bila dibutuhkan oleh implementasi.

#### Colonial Cannon
Flow: Benteng Martello — Naval Combat / Shore Combat
Moment: Ship and Shore Combat
Type: MODEL
Function: Meriam yang digunakan untuk menembak kapal lawan dari kapal maupun pinggir pantai.
Visual Brief: Reusable cannon model dengan bentuk peninggalan era kolonial yang dapat digunakan pada kapal dan pantai. Harus memiliki arah tembak yang terbaca dan state/animation firing bila mechanic memerlukannya.

#### Shark Mob
Flow: Benteng Martello — Water Hazard
Moment: Player Enters the Water
Type: MODEL
Function: Environmental hazard yang menyerang player yang terlalu lama berada di perairan.
Visual Brief: Shark mob yang dapat berenang mengelilingi pulau dan memiliki animation dasar untuk swim dan attack.

## Perkebunan

### Gameplay Moment — Growing and Harvesting Crops

### 3D Models

#### Coffee Plant Set
Flow: Perkebunan — Kopi
Moment: Planting, Growing, and Harvesting
Type: MODEL
Function: Tanaman kopi yang menunjukkan progression dari ditanam sampai siap dipanen.
Visual Brief: Coffee plant dengan visual state yang cukup untuk membedakan planted/growing/ready-to-harvest dan state setelah panen bila diperlukan.

#### Cinnamon Plant Set
Flow: Perkebunan — Kayu Manis
Moment: Maintaining and Harvesting
Type: MODEL
Function: Tanaman/pohon kayu manis yang dapat dipanen lalu kembali melalui regrowth.
Visual Brief: Cinnamon plant/tree dengan readable harvest-ready dan post-harvest/regrowth state.

#### Palm Oil Tree Set
Flow: Perkebunan — Sawit
Moment: Fruit Growth and Harvest
Type: MODEL
Function: Pohon sawit yang menghasilkan buah untuk dipanen berulang.
Visual Brief: Palm oil tree dengan visible fruit-ready state dan post-harvest/regrowth state. Satire sawit tidak membutuhkan visual exaggeration tambahan.

### Items

#### Coffee Harvest Item
Flow: Perkebunan — Kopi
Moment: After Harvest
Type: ITEM
Function: Hasil panen kopi yang dapat dijual.
Visual Brief: Item panen kopi yang mudah dibedakan dari dua komoditas lain.

#### Cinnamon Harvest Item
Flow: Perkebunan — Kayu Manis
Moment: After Harvest
Type: ITEM
Function: Hasil panen kayu manis yang dapat dijual.
Visual Brief: Item kayu manis yang mewakili hasil harvest.

#### Palm Fruit Harvest Item
Flow: Perkebunan — Sawit
Moment: After Harvest
Type: ITEM
Function: Hasil buah sawit yang dapat dijual.
Visual Brief: Item tandan/buah sawit yang mewakili hasil harvest.

#### Fertilizer Item
Flow: Perkebunan — Economy
Moment: Player Buys Fertilizer
Type: ITEM
Function: Item yang digunakan untuk mempercepat growth atau recovery tanaman.
Visual Brief: Simple fertilizer item yang terbaca sebagai kebutuhan perkebunan tanpa menambahkan jenis pupuk baru.

## Egrang

### Gameplay Moment — Using the Traditional Mobility Toy

### 3D Models

#### Egrang Rideable
Flow: Egrang
Moment: Player Uses the Egrang
Type: MODEL
Function: Rideable traditional toy yang membuat player bergerak pada posisi lebih tinggi.
Visual Brief: Sepasang egrang tradisional sebagai satu rideable gameplay asset. Harus mendukung mounted movement dan dismount tanpa membutuhkan balance/falling animation system.

## Mancing di Empang

### Gameplay Moment — Catching Fish

### Items

#### Lele Catch Item
Flow: Mancing di Empang
Moment: Fishing Reward
Type: ITEM
Function: Salah satu custom fishing result dari empang.
Visual Brief: Item ikan Lele yang langsung terbaca sebagai hasil tangkapan.

#### Tuna Catch Item
Flow: Mancing di Empang
Moment: Fishing Reward
Type: ITEM
Function: Salah satu custom fishing result dari empang.
Visual Brief: Item ikan Tuna yang dapat dibedakan dari Lele.

#### Hiu Catch Item
Flow: Mancing di Empang
Moment: Rare Fishing Reward
Type: ITEM
Function: Hasil tangkapan absurd/rare dari empang.
Visual Brief: Item Hiu yang tetap terbaca sebagai hasil pancing meskipun skalanya dapat disederhanakan agar cocok sebagai inventory item.

## Harimau Lepas

### Gameplay Moment — Basement Encounter

### 3D Models

#### Tiger
Flow: Harimau Lepas
Moment: Roaming, Chase, and Combat
Type: MODEL
Function: PvE enemy utama yang berkeliaran di basement lalu mengejar dan menyerang player.
Visual Brief: Tiger mob dengan animation dasar idle/roam, run/chase, attack, hit reaction, dan defeat yang dibutuhkan encounter. Tidak memerlukan multi-phase boss state.

## CyberWorld Mining

### Gameplay Moment — Mining and Career Progression

### 3D Models

#### CyberWorld Mining Resource Set
Flow: CyberWorld Mining
Moment: Mining Across the Three Islands
Type: MODEL
Function: Resource yang dapat ditambang dan ditukar menjadi currency selama progression.
Visual Brief: Satu set resource block/deposit yang dapat membedakan progression value antar-tier pulau. Exact resource names dan jumlah jenis tidak ditentukan sampai ada approval tambahan; jangan mengarang lore atau jenis mineral baru.

### Items

#### Mining Tool Upgrade Set
Flow: CyberWorld Mining
Moment: Equipment Progression
Type: ITEM
Function: Mining equipment yang dapat di-upgrade untuk mendukung progression ke resource/tier yang lebih tinggi.
Visual Brief: Mining tool dengan upgrade variants yang terbaca lebih baik dari tier sebelumnya. Exact number/form mengikuti progression yang dipakai tanpa menambahkan crafting system baru.

## Audio Boundary

Semua spoken narrative untuk keenam gameplay dimiliki oleh `work/voice-production.md`. Tidak ada standalone non-dialogue AUDIO atau PARTICLE resource yang diwajibkan oleh current approved scope.
