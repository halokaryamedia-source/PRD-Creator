# Production Asset Requirements
Project: MIVUBI – Around The Block
Version: 1.0.0

## Scope Note

Dokumen ini hanya mencatat resource yang benar-benar dibutuhkan oleh gameplay yang sudah disetujui. Layout map dianggap sudah tersedia. NPC narator menggunakan standard humanoid/NPC base dengan appearance/skin yang sesuai; current scope tidak membutuhkan custom 3D NPC model. Tidak ada decorative prop, standalone particle, atau standalone non-dialogue audio yang ditambahkan tanpa kebutuhan gameplay.

## Required Model Summary

1. Combat Ship
2. Colonial Cannon
3. Shark Mob
4. Coffee Plant Set
5. Cinnamon Plant Set
6. Palm Oil Tree Set
7. Egrang Rideable
8. Tiger
9. CyberWorld Mining Resource Set — 3 progression tiers

## Required Item Summary

1. Coffee Harvest Item
2. Cinnamon Harvest Item
3. Palm Fruit Harvest Item
4. Fertilizer Item
5. Lele Catch Item
6. Tuna Catch Item
7. Hiu Catch Item
8. Bakso Treat Item
9. Mining Tool Upgrade Set — 3 progression tiers

## Benteng Martello

### Naval and Shore Combat

#### Combat Ship
Type: MODEL

**Function**  
Kapal individual yang digunakan player selama Naval Combat.

**Visual Brief**  
Satu reusable combat ship untuk seluruh participant. Wajib memiliki state aktif dan state destroyed/disabled yang terbaca jelas ketika kapal sudah tidak dapat digunakan lagi. Model tidak perlu variasi dekoratif per-player.

#### Colonial Cannon
Type: MODEL

**Function**  
Meriam yang digunakan pada kapal dan pinggir pantai untuk menembak kapal lawan.

**Visual Brief**  
Satu reusable cannon bergaya peninggalan era kolonial. Wajib memiliki arah tembak yang mudah dibaca serta firing response sederhana; tidak membutuhkan mekanisme visual tambahan di luar kebutuhan tembak.

#### Shark Mob
Type: MODEL

**Function**  
Environmental hazard bagi player yang berada terlalu lama di air.

**Visual Brief**  
Shark mob yang dapat berenang mengelilingi area perairan dan memiliki animation dasar swim serta attack.

## Perkebunan

### Growing and Harvesting

#### Coffee Plant Set
Type: MODEL

**Function**  
Tanaman kopi untuk loop Plant → Maintain → Grow → Harvest.

**Visual Brief**  
Coffee plant dengan state yang cukup untuk membedakan planted/growing/ready-to-harvest dan state setelah panen bila dibutuhkan.

#### Cinnamon Plant Set
Type: MODEL

**Function**  
Tanaman/pohon kayu manis untuk loop Maintain → Harvest → Regrowth.

**Visual Brief**  
Cinnamon plant/tree dengan harvest-ready dan post-harvest/regrowth state yang terbaca.

#### Palm Oil Tree Set
Type: MODEL

**Function**  
Pohon sawit untuk loop Maintain → Fruit Growth → Harvest → Regrowth.

**Visual Brief**  
Palm oil tree dengan fruit-ready dan post-harvest/regrowth state. Satire sawit tetap berada pada narasi dan tidak membutuhkan visual exaggeration khusus.

#### Coffee Harvest Item
Type: ITEM

**Function**  
Hasil panen kopi yang dapat dijual.

**Visual Brief**  
Item hasil kopi yang mudah dibedakan dari komoditas lain.

#### Cinnamon Harvest Item
Type: ITEM

**Function**  
Hasil panen kayu manis yang dapat dijual.

**Visual Brief**  
Item kayu manis yang mewakili hasil harvest.

#### Palm Fruit Harvest Item
Type: ITEM

**Function**  
Hasil buah sawit yang dapat dijual.

**Visual Brief**  
Item tandan/buah sawit yang mewakili hasil harvest.

#### Fertilizer Item
Type: ITEM

**Function**  
Item untuk mempercepat growth atau recovery tanaman.

**Visual Brief**  
Satu simple fertilizer item. Tidak diperlukan beberapa jenis pupuk.

## Egrang

### Traditional Mobility Activity

#### Egrang Rideable
Type: MODEL

**Function**  
Rideable traditional toy yang membuat player bergerak pada posisi lebih tinggi.

**Visual Brief**  
Sepasang egrang tradisional sebagai satu rideable gameplay asset. Harus mendukung mounted movement dan dismount tanpa balance meter, falling simulation, atau animation system yang kompleks.

## Mancing di Empang

### Custom Fishing Results

#### Lele Catch Item
Type: ITEM

**Function**  
Custom fishing result dari empang.

**Visual Brief**  
Item ikan Lele yang langsung terbaca sebagai hasil tangkapan.

#### Tuna Catch Item
Type: ITEM

**Function**  
Custom fishing result dari empang.

**Visual Brief**  
Item ikan Tuna yang dapat dibedakan dari Lele.

#### Hiu Catch Item
Type: ITEM

**Function**  
Rare/absurd fishing result dari empang.

**Visual Brief**  
Item Hiu yang tetap terbaca sebagai hasil pancing dan disederhanakan agar cocok sebagai inventory item.

## Harimau Lepas

### Basement Encounter

#### Tiger
Type: MODEL

**Function**  
PvE enemy utama yang roaming, mengejar, dan menyerang player di basement.

**Visual Brief**  
Tiger mob dengan animation dasar idle/roam, run/chase, attack, hit reaction, dan defeat. Tidak membutuhkan multi-phase boss state.

#### Bakso Treat Item
Type: ITEM

**Function**  
Payoff sederhana untuk janji Zookeeper setelah player berhasil menangani harimau.

**Visual Brief**  
Satu item Bakso yang dapat diberikan setelah completion. Tidak memerlukan sistem makanan/quest tambahan di luar pemberian item.

## CyberWorld Mining

### Three-Tier Mining Progression

#### CyberWorld Mining Resource Set
Type: MODEL

**Function**  
Resource/deposit yang ditambang dan ditukar menjadi currency sepanjang tiga tingkat pulau.

**Visual Brief**  
Satu set dengan tiga progression tiers yang terbaca sebagai Tier 1, Tier 2, dan Tier 3. Tier lebih tinggi harus terlihat lebih bernilai tanpa mengarang nama mineral, lore, atau resource family baru.

#### Mining Tool Upgrade Set
Type: ITEM

**Function**  
Mining equipment yang meningkat sejalan dengan progression tiga pulau.

**Visual Brief**  
Tiga progression variants: basic, improved, dan advanced secara fungsi/visual. Penamaan final tidak perlu dipaksakan sebagai nama in-game sampai ada approval tambahan. Tidak ada crafting system baru.

## NPC Appearance Boundary

Enam narrator menggunakan standard humanoid/NPC base dengan appearance berbeda:

- Benteng Martello Guide
- Plantation Guide
- Old Man
- Fisherman
- Zookeeper
- Job Recruiter

Appearance/skin diperlukan untuk membedakan karakter, tetapi tidak dihitung sebagai custom 3D model dalam current model scope.

## Audio Boundary

Semua spoken narrative dimiliki oleh `work/voice-production.md`. Tidak ada standalone non-dialogue AUDIO atau PARTICLE resource yang diwajibkan oleh current approved scope.