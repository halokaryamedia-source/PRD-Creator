# Production Asset Requirements
Project: Around The Block
Version: 1.0.0 Preview
Status: Approved Preview

## Scope
Only gameplay-required resources are included. Existing map layout is not redesigned. NPC characters may use standard humanoid/NPC bases with unique appearances unless a custom model is explicitly required.

## Multiplayer Assets

### Benteng Martello

#### Combat Ship
Type: 3D Model
**Function:** Kapal individual untuk pertempuran laut.
**Visual Brief:** Reusable combat ship yang tetap mudah dibaca saat bergerak di laut.
**Required States:** Active; Destroyed / Disabled.

#### Colonial Cannon
Type: 3D Model
**Function:** Meriam untuk kapal dan area pantai.
**Visual Brief:** Reusable cannon bergaya peninggalan kolonial dengan arah tembak jelas.
**Required States:** Idle; Firing Response.

#### Shark Mob
Type: 3D Model
**Function:** Bahaya bagi player di air.
**Visual Brief:** Hiu sederhana yang mudah terlihat di perairan.
**Required States:** Swim; Attack.

#### Benteng Martello Guide
Type: NPC Appearance
**Function:** Memperkenalkan aktivitas.
**Visual Brief:** Pemandu sejarah yang ramah dan mudah dikenali.

### Mari Berkebun

#### Coffee Plant Set
Type: 3D Model
**Function:** Tanaman kopi dari tanam sampai panen.
**Required States:** Planted; Growing; Ready to Harvest; Post-Harvest bila diperlukan.

#### Cinnamon Plant Set
Type: 3D Model
**Function:** Kayu manis untuk maintain, harvest, dan regrowth.
**Required States:** Ready to Harvest; Post-Harvest / Regrowth.

#### Palm Oil Tree Set
Type: 3D Model
**Function:** Sawit untuk fruit growth, harvest, dan regrowth.
**Required States:** Fruit Ready; Post-Harvest / Regrowth.

#### Coffee Harvest Item
Type: ITEM
**Function:** Hasil kopi yang dapat dijual.

#### Cinnamon Harvest Item
Type: ITEM
**Function:** Hasil kayu manis yang dapat dijual.

#### Palm Fruit Harvest Item
Type: ITEM
**Function:** Hasil buah sawit yang dapat dijual.

#### Fertilizer Item
Type: ITEM
**Function:** Mempercepat pertumbuhan/pemulihan tanaman.

#### Plantation Guide
Type: NPC Appearance
**Function:** Memperkenalkan aktivitas berkebun.
**Visual Brief:** Hangat, antusias, sedikit terlalu bangga pada sawit.

### Main Egrang

#### Egrang Rideable
Type: 3D Model
**Function:** Rideable traditional toy untuk movement lebih tinggi.
**Required States:** Mounted; Dismounted.

#### Old Man
Type: NPC Appearance
**Function:** Memperkenalkan egrang sebagai solusi jalan rusak.

### Mancing Dulu

#### Lele Catch Item
Type: ITEM
**Function:** Hasil pancing Lele.

#### Tuna Catch Item
Type: ITEM
**Function:** Hasil pancing Tuna.

#### Hiu Catch Item
Type: ITEM
**Function:** Rare/absurd fishing result.

#### Fisherman
Type: NPC Appearance
**Function:** Memperkenalkan dan menemani aktivitas memancing.

#### Toko Madura Stall
Type: 3D Model
**Function:** Tempat player menjual hasil tangkapan untuk mendapatkan uang.
**Visual Brief:** Toko kecil dekat area pemancingan yang mudah dikenali sebagai titik penjualan.

### Macan Lepas

#### Tiger
Type: 3D Model
**Function:** Musuh utama pada encounter di basement.
**Required States:** Idle / Roam; Run / Chase; Attack; Hit Reaction; Defeat.

#### Black Briefcase
Type: 3D Model
**Function:** Properti Businessman dan visual cue untuk imbalan transaksi.
**Required States:** Closed; Open.

#### Businessman
Type: NPC Appearance
**Function:** Menawarkan pekerjaan dan memberikan imbalan setelah completion.
**Visual Brief:** Pria formal rapi, percaya diri, kaya, sedikit arogan, membawa Black Briefcase.

### Tambang Masa Depan

#### CyberWorld Mining Resource Set
Type: 3D Model
**Function:** Resource/deposit yang ditambang dan ditukar menjadi Shared Currency.
**Required States:** Tier 1; Tier 2; Tier 3.
**Visual Brief:** Satu keluarga visual dengan tier lebih tinggi terlihat lebih bernilai tanpa mengarang nama mineral/lore.

#### Mining Tool Upgrade Set
Type: ITEM
**Function:** Equipment yang meningkat mengikuti progression tiga tingkat.
**Required States:** Basic; Improved; Advanced.

#### Job Recruiter
Type: NPC Appearance
**Function:** Memperkenalkan tawaran kerja dan progression tambang.

## Purchasable Items Assets

#### Flying Motorcycle
Type: 3D Model
**Function:** Kendaraan utama yang dapat digunakan setelah semua bagian terkumpul.
**Required States:** Incomplete / Locked; Complete / Ready; Flying; Out of Fuel.

#### Flying Motorcycle Part Set
Type: Item Set
**Function:** Komponen yang dibeli bertahap sebelum motor siap digunakan.
**Required Parts:** Motorcycle Body; Engine; Flight Module; Fuel.

#### Dealer NPC
Type: NPC Appearance
**Function:** Menjaga dealer dan menjelaskan sistem pembelian motor per bagian.

#### Fuel Set
Type: Item Set
**Function:** Fuel untuk menggunakan Flying Motorcycle.
**Variants:** Pertamak; Pertali; Okibos.
**Gameplay Balance:** Pertamak > Pertali = Okibos.
**Player Text:** Pertamak = “100% ASLI DIJAMIN.”; Pertali = “Bensin Sejuta Umat”; Okibos = “Energi Masa Depan”.

## Singleplayer Motion Tracking — Presentation Requirements

Motion Interaction remains **Experimental** until venue testing.

### Menghalau Bajak Laut
- Fortress Health Bar.
- Cannon Aim / Fire feedback.
- Ship path / attack-point readability.

### Menanam Pohon
- Active tool feedback for sekop, bibit, alat penyiram, pupuk.
- Sequence success/fail feedback.

### Memancing Ikan
- Fishing Timing Indicator with Green Zone.
- Stamina Indicator.
- Catch / Miss feedback.

## Boundaries
- Do not add unsupported decorative assets.
- Motion-control presentation remains provisional until venue testing.
- Nine approved Map View references belong to the approved preview package and source record.
